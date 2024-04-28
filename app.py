#import csv
import gradio as gr
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

from langchain.document_loaders import PyPDFLoader
import os

import fitz
from PIL import Image, ImageDraw, ImageFont

# Global variables
COUNT, N = 0, 0
chat_history = []
chain = ''
enable_box = gr.Textbox.update(value=None, 
                          placeholder='Upload your OpenAI API key', interactive=True)
disable_box = gr.Textbox.update(value='OpenAI API key is Set', interactive=False)

# Function to set the OpenAI API key
def set_apikey(api_key):
    os.environ['OPENAI_API_KEY'] = api_key
    return disable_box

# Function to clear chat history
def clear_history(history):
    history.clear()
    return history


# Function to enable the API key input box
def enable_api_box():
    return enable_box

# Function to add text to the chat history
def add_text(history, text):
    if not text:
        raise gr.Error('Enter text')
    history = history + [(text, '')]
    return history

# Function to process the PDF file and create a conversation chain
def process_file(file):
    if 'OPENAI_API_KEY' not in os.environ:
        raise gr.Error('Upload your OpenAI API key')

    loader = PyPDFLoader(file.name)
    documents = loader.load()

    embeddings = OpenAIEmbeddings()
    
    pdfsearch = Chroma.from_documents(documents, embeddings)

    chain = ConversationalRetrievalChain.from_llm(ChatOpenAI(temperature=0.3), 
                                   retriever=pdfsearch.as_retriever(search_kwargs={"k": 1}),
                                   return_source_documents=True)
    return chain

# Function to generate a response based on the chat history and query
def generate_response(history, query, btn):
    global COUNT, N, chat_history, chain
    
    if not btn:
        raise gr.Error(message='Upload a PDF')
    if COUNT == 0:
        chain = process_file(btn)
        COUNT += 1
    
    result = chain({"question": query, 'chat_history': chat_history}, return_only_outputs=True)
    chat_history += [(query, result["answer"])]
    N = list(result['source_documents'][0])[1][1]['page']

    for char in result['answer']:
        history[-1][-1] += char
        yield history, ''

# Function to render a specific page of a PDF file as an image
def render_file(file):
    global N, chat_history
    
    doc = fitz.open(file.name)
    page = doc[N]
    
    # Render the page as a PNG image with a resolution of 300 DPI
    pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
    image = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    
    # Get the answer from the latest chat history
    answer = chat_history[-1][1] if chat_history else ""
    
    # Create an overlay to highlight the answer
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # You can choose a different font if needed
    
   
    # Write the answer text on the image
    draw.text((10, 10), answer, fill="red", font=font)
    
    return image

# Gradio application setup
with gr.Blocks() as demo:
    # Create a Gradio block

    with gr.Column():
        with gr.Row():
            with gr.Column(scale=0.8):
                api_key = gr.Textbox(
                    placeholder='Enter OpenAI API key',
                    show_label=False,
                    interactive=True
                ).style(container=False)
            with gr.Column(scale=0.2):
                change_api_key = gr.Button('Change Key')

        with gr.Row():
            chatbot = gr.Chatbot(value=[], elem_id='chatbot').style(height=520)
            show_img = gr.Image(label='Upload PDF', tool='select').style(height=550)

    with gr.Row():
        with gr.Column(scale=0.70):
            txt = gr.Textbox(
                show_label=False,
                placeholder="Enter text and press enter"
            ).style(container=False)

        with gr.Column(scale=0.15):
            submit_btn = gr.Button('Submit')

        with gr.Column(scale=0.15):
            btn = gr.UploadButton("📁 Upload a PDF", file_types=[".pdf"]).style()
        with gr.Column(scale=0.15):
            clear_btn = gr.Button("Clear History")

    # Set up event handlers

    # Event handler for submitting the OpenAI API key
    api_key.submit(fn=set_apikey, inputs=[api_key], outputs=[api_key])

    # Event handler for changing the API key
    change_api_key.click(fn=enable_api_box, outputs=[api_key])

    # Event handler for uploading a PDF
    btn.upload(fn=render_file, inputs=[btn], outputs=[show_img])

        # Event handler for clearing chat history
    clear_btn.click(
        fn=clear_history,
        inputs=[chatbot],
        outputs=[chatbot]
    )

    # Event handler for submitting text and generating response
    submit_btn.click(
        fn=add_text,
        inputs=[chatbot, txt],
        outputs=[chatbot],
        queue=False
    ).success(
        fn=generate_response,
        inputs=[chatbot, txt, btn],
        outputs=[chatbot, txt]
    ).success(
        fn=render_file,
        inputs=[btn],
        outputs=[show_img]
    )
demo.queue()
if __name__ == "__main__":
    #demo.server_name = "0.0.0.0"  
    #demo.server_port = 8080
    demo.launch(share=True, server_name = "127.0.0.1" , server_port = 7860 )