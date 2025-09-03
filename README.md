📧 Email Spam Detection using LSTM & Flask

A machine learning project that detects whether an email is Spam 🚨 or Ham ✅.
The project uses Natural Language Processing (NLP) techniques, an LSTM model for classification, and provides a Flask web app frontend for easy interaction.

✨ Features

Preprocesses email text (stopwords removal, punctuation removal, etc.)

Word embeddings + LSTM for sequence modeling

Handles class imbalance (ham vs spam)

Flask REST API (/predict)

User-friendly HTML frontend form

📂 Project Structure
Email_Spam_Detection_Model/
│
├── app.py                # Flask API + frontend
├── spam_model.keras      # Trained LSTM model (saved in Keras format)
├── tokenizer.pkl         # Tokenizer used for preprocessing
├── templates/
│   └── index.html        # Frontend UI
├── email.csv             # Dataset (spam/ham emails)
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

🛠️ Installation

Clone the repo:

git clone https://github.com/<your-username>/Email_Spam_Detection_Model.git
cd Email_Spam_Detection_Model


Create a virtual environment:

python -m venv venv


Activate it:

PowerShell

.\venv\Scripts\Activate.ps1


CMD

venv\Scripts\activate.bat


Install dependencies:

pip install -r requirements.txt

📊 Training the Model

If you want to retrain the model:

Open the Jupyter Notebook or Python script containing preprocessing + training steps.

Train the model using the dataset (email.csv).

Save the model and tokenizer:

model.save("spam_model.keras")
import pickle
with open("tokenizer.pkl", "wb") as handle:
    pickle.dump(tokenizer, handle)

🚀 Running the App

Start the Flask server:

python app.py


Open in browser:
👉 http://127.0.0.1:5000/

Paste email text → Click Check → Get result (Spam/Ham + confidence).

🔗 API Usage

You can also interact with the API directly.

Endpoint:

POST http://127.0.0.1:5000/predict


Body (JSON):

{
  "text": "Congratulations! You won a lottery, claim your prize."
}


Response:

{
  "text": "Congratulations! You won a lottery, claim your prize.",
  "prediction": "spam",
  "confidence": 0.98
}

🖼️ Screenshots
🔹 Web Interface

(screenshot placeholder — add later)

📌 Dependencies

Python 3.8+

Flask

TensorFlow / Keras

NumPy, Pandas, Scikit-learn

NLTK, WordCloud

Matplotlib, Seaborn

💡 Future Improvements

Deploy on Heroku / Render / AWS

Add fastText / BERT for better NLP performance

Build a React frontend for a modern UI

👨‍💻 Author

Developed by Jyotsna Koova
