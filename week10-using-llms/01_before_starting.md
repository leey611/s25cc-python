# Before running models locally...

### Machine Learning (ML)
ML is a subset of AI where computers learn patterns from data. Similar to the process of getting better at tasks through experience. For example:

- Classifying emails as spam or not spam
- Recommending movies
- Recognizing objects, gestures, poses

Three main types of ML:
- Supervised learning: learning from labeled data
- Unsupervised learning: finding structure in unlabeled data
- Reinforcement learning: learning through trial and error with rewards

### Large Language Model (LLM)
LLM is a type of machine learning model that is trained on large amounts of data (text, sentences, languages), and can predict and generate human-like language.

How do computers take and process large amounts of human language, text, words, sentences etc? The process is called **tokenizing**. Tokenization is the process of breaking down text into smaller pieces. Go to [The Tokenizer Playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) and [Next token prediction visualization](https://alonsosilva-nexttokenprediction.hf.space/) to see it visually.

Many LLMs are based on **transformers**, a kind of machine learning architecture that understands context across long sequences of sentences.

## Using models from Hugging Face

- run `pip install -U transformers` to install transformers
- create a token at [Hugging Face](https://huggingface.co/)
- run `huggingface-cli login`
- paste your token, you won't see your token, just hit `enter`

### Gated Models
If you run some models and encounter errors, check if the model is gated. If it is gated, you might need to accept its license agreements first in order to run it. See [here](https://huggingface.co/docs/hub/en/models-gated)

## Other Resources
- [Replicate](https://replicate.com/)
- [Llama](https://www.llama.com/docs/llama-everywhere/)
- [Runway API](https://docs.dev.runwayml.com/)
- [Gemini](https://ai.google.dev/gemini-api/docs)

## Reference
- [Transformers and LLMs](https://docs.google.com/presentation/d/1uGS4w_UumzQAoq03S-sc9Nn7_hBaRNbQJf1G2SNXooU/edit?slide=id.g293f269cf46_0_7#slide=id.g293f269cf46_0_7) by Daniel Shiffman
- [LLM Explained | What is LLM](https://www.youtube.com/watch?v=67_aMPDk2zw) by codebasics
- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) by Andrej Karpathy