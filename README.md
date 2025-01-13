# BOOK QUEST 📚

**BOOK QUEST** is an AI-powered conversational tool designed to interact with PDF files. It allows users to upload PDF documents, ask questions, and receive answers while highlighting relevant content directly on the PDF pages. This project leverages OpenAI's language models, document processing libraries, and Gradio for building an interactive user interface.

---

## **Features**
- **Upload PDF Files**: Accepts PDF files as input for processing.
- **AI-Powered Q&A**: Uses OpenAI's language model to provide conversational responses based on the content of the uploaded PDF.
- **PDF Rendering**: Displays the specific page of the PDF containing the answer with highlights.
- **Interactive Chat Interface**: Users can interact with the chatbot to ask questions and receive answers in real-time.
- **OpenAI API Integration**: Requires an OpenAI API key to function.
- **Clear Chat History**: Ability to clear the chat history to start a new session.

---

## **Technologies Used**
- **Python Libraries**:
  - `gradio`: For building the web-based user interface.
  - `langchain`: For managing language model interactions and conversational retrieval.
  - `PyPDFLoader`: For loading and parsing PDF files.
  - `Chroma`: For embedding and searching document content.
  - `fitz` (PyMuPDF): For rendering PDF pages as images.
  - `Pillow`: For image manipulation and drawing.
- **OpenAI GPT**: For generating conversational responses.
- **CSS**: Custom styling for a polished user interface.

---

## **Setup Instructions**
### **1. Clone the Repository**
```bash
git clone <repository-url>
cd book-quest
```

### **2. Install Dependencies**
Make sure you have Python 3.8 or above installed. Install the required libraries using:
```bash
pip install -r requirements.txt
```

### **3. Obtain an OpenAI API Key**
Sign up for an OpenAI account and obtain an API key from [OpenAI's website](https://openai.com/).

### **4. Add CSS (Optional)**
Ensure the `gradio.css` file is placed in the project directory for a customized interface.

### **5. Launch the Application**
Run the application with:
```bash
python app.py
```

### **6. Access the Application**
The application will be accessible locally at `http://127.0.0.1:7860`. Use the `share=True` flag to make it publicly accessible.

---

## **How to Use**
1. **Enter OpenAI API Key**: Start by entering your OpenAI API key in the provided text box.
2. **Upload a PDF**: Click the `📁 Upload a PDF` button and select the desired file.
3. **Ask Questions**: Type your queries related to the content of the PDF in the input box and press `Submit`.
4. **View Answers**: The chatbot will respond with an answer based on the PDF content, and the relevant page will be displayed with highlights.
5. **Clear History**: Use the `Clear History` button to reset the chat and start a new session.

---

## **Project Structure**
```
🗂 book-quest/
🗁── app.py              # Main application file
🗁── requirements.txt    # Python dependencies
🗁── gradio.css          # Custom CSS for UI styling
🗁── logo.jpg            # Logo image for the app header
🗁── README.md           # Project documentation
```

---

## **Future Enhancements**
- **Live Text Highlighting**: Highlight specific portions of the text within the PDF page image.
- **Multiple File Support**: Enable interaction with multiple PDFs simultaneously.
- **Advanced Search Options**: Add filters like keywords, date ranges, or metadata for queries.
- **Multilingual Support**: Allow queries in multiple languages.
- **User Authentication**: Secure API key storage with user-specific settings.
- 
---

## **Contributing**
Contributions are welcome! If you have suggestions or feature requests, feel free to submit a pull request or open an issue.

---

## **Live Demo**
Check out the working project here: https://book-quest-6c2f.onrender.com/

---

## **Contributors**

- Vaishnavi Sanjay Mane
- Disha Hemant Joshi
- Purva Deepak Agine
- Durva Darshan Desai



