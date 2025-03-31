from flask import Flask, render_template, request # pip install flask
import torch # pip install torch
from transformers import pipeline

app = Flask(__name__)

hf_name = 'pszemraj/led-large-book-summary'
summarizer = pipeline(
    "summarization",
    hf_name,
    device=0 if torch.cuda.is_available() else -1,
)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary_text = None

    if request.method == 'POST':
        user_input = request.form['user_text'].strip()

        if user_input:
            try:
                summary = summarizer(
                    user_input,
                    min_length=16,
                    max_length=256,
                    no_repeat_ngram_size=3,
                    encoder_no_repeat_ngram_size=3,
                    repetition_penalty=3.5,
                    num_beams=4,
                    early_stopping=True,
                )
                summary_text = summary[0]['summary_text']
            except Exception as e:
                summary_text = f"Error during summarization: {str(e)}"

    return render_template('index.html', summary=summary_text)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
