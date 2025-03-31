# for mac users, this model requires macOS 14 +
# reference: https://huggingface.co/facebook/bart-large-cnn
from transformers import pipeline

# load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ask the user to input text
user_input = input("Please enter the text you'd like to summarize:\n")

# loading indicator
print("\nSummarizing your text, please wait...")

summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)

# print the output
print("\nSummary:")
print(summary[0]['summary_text'])
