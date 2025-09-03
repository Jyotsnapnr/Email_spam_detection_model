from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# ==========================
# Load model and tokenizer
# ==========================
model = tf.keras.models.load_model("spam_model.keras")  # or .h5 if you saved that way

with open("tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)

MAX_LEN = 100

# ==========================
# Flask app
# ==========================
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text")  # from HTML form

    if not text:
        return render_template("index.html", prediction="⚠️ Please enter some text.")

    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding="post", truncating="post")

    prediction = model.predict(padded)[0][0]
    label = "Spam 🚨" if prediction >= 0.5 else "Ham ✅"

    return render_template("index.html", text=text, prediction=label, confidence=f"{prediction:.2f}")


if __name__ == "__main__":
    app.run(debug=True)
