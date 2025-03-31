# reference: https://huggingface.co/pszemraj/led-large-book-summary

import torch # pip install torch
from transformers import pipeline

hf_name = 'pszemraj/led-large-book-summary'

summarizer = pipeline(
    "summarization",
    hf_name,
    device=0 if torch.cuda.is_available() else -1,
)

# ask for user input
user_text = input("Enter a passage to summarize:\n")

# loading indicator
print("\nSummarizing your text, please wait...")

# run the summarizer
result = summarizer(
    user_text,
    min_length=16,
    max_length=256,
    no_repeat_ngram_size=3,
    encoder_no_repeat_ngram_size=3,
    repetition_penalty=3.5,
    num_beams=4,
    early_stopping=True,
)

# print the result
print("\nSummary:")
print(result[0]['summary_text'])
