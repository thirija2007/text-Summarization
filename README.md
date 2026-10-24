# Text Summarization

## Project Overview
Smart Summary AI is a text summarization web application built using Python, Streamlit, and Hugging Face Transformers. It converts lengthy articles or text into short, easy-to-understand summaries. Users can choose the summary size according to their needs and download the generated summary as a text file.

## Objectives
- To summarize lengthy text automatically.
- To save time when reading long articles.
- To provide short, medium, and long summary options.
- To allow users to download summaries for future reference.

## Features
- **Text Input:** Enter or paste an article into the application.
- **AI-Powered Summarization:** Generates summaries using a pretrained Hugging Face model.
- **Summary Size Selection:** Choose Short, Medium, or Long summaries.
- **Word Count:** Displays the original and summary word counts.
- **Download Summary:** Download the generated summary as a `.txt` file.
- **User-Friendly Interface:** Simple and interactive interface built with Streamlit.
- **Input Validation:** Requests at least 20 words before summarization.

## Technologies Used
- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- DistilBART (`sshleifer/distilbart-cnn-12-6`)

## Project Structure

```text
text-Summarization/
├── app.py
├── requirements.txt
└── README.md
```

## Setup and Execution

1. Download or clone this repository from GitHub.
2. Open the project folder in VS Code.
3. Open the terminal in VS Code.
4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL displayed in the terminal to use the application.

## How to Use
1. Open the Smart Summary AI application.
2. Enter or paste an article containing at least 20 words.
3. Select the desired summary size: Short, Medium, or Long.
4. Click **Generate Summary**.
5. View the generated summary and compare the word counts.
6. Click **Download Summary** to save the result as a text file.

## AI Model
This project uses the pretrained `sshleifer/distilbart-cnn-12-6` model from Hugging Face Transformers to generate concise summaries from longer text. An internet connection is generally required to download the model files during the initial run.

## Learning Outcomes
- Understanding text summarization using Natural Language Processing (NLP).
- Integrating pretrained AI models into Python applications.
- Building an interactive web application using Streamlit.
- Handling user input, exceptions, and downloadable outputs.

## Future Enhancements
- Support for uploading PDF and Word documents.
- Summarization of longer documents in multiple sections.
- Support for multiple languages.
- Improved user interface and summary customization.

## License
This project is intended for educational and learning purposes.
