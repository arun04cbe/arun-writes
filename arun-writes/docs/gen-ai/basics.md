---
sidebar_position: 2
sidebar_label: Basics
sidebar_class_name: green
sidebar_key: unique-sidebar-item-key
---

# Basics on LLMs

1. LLMs (Large Language Models), are generative AI models which generates texts, images, video, audio.
2. To put it simply I can say LLMs are nothing but next-token predictors.
3. Example:- type `The cat sat on the ` in ChatGPT and observe the response,

![Cat Example GPT](../../src/images/cat_example_gpt.png)

Why does it say the `mat`, it could have generated anything, the reason being it has trained on a huge corpus of data and predicts that `mat` might be the best suited prediction for the provided input.

## What does tokens actually mean?

1. LLMs are usually trained on a huge corpus of data.
2. As humans we try to provide input to these models in text, image etc but behind the screens, the input data (text) is processed in `tokens`.
3. A token could be a word or part of a word. Each model has it's own tokenizer and is trained on a predefined finite set of tokens (called `model's vocabulary`) that the models can generate.
4. Below is the OpenAI's tokenizer example,

![Open AI Tokenizer](../../src/images/openai_tokenizer.png)

5. Earlier, LLMs were not be able to count the total `r` present in `strawberry`. The main reason is the tokenizer, where the word was split into two to three tokens.

:::tip

Watch [this](https://youtu.be/NKnZYvZA7w4?si=17DlaEg-ga1Mb45K) video to know how LLMs actually generate text.

:::

## Different Models

1. Initially, only text generation model was available. But over the time, multi-modal models came into picture.
2. Today, text generation, image generation, video generation, audio generation, real-time interactive capabilities etc. are available.

### Reasoning Models

- Unlike the chat completion models which start to generate text based on the provided input, `reasoning models` think before they answer.
- The model resembles more of how a normal person would think before they answer something. Since they have thinking time, the model takes more time to respond.
- These models are well suited for long running complex tasks.
- A few examples of reasoning models are `o1`, `o3`, `qwen-3` etc.
- Recently, `hybrid-reasoning` models came into picture where a model can be used for both `non-reasoning` and `reasoning` tasks. A few examples are `gpt-5`, `claude-opus4-5` etc.

### Embedding Models

- Embedding models are mainly used for `Retrieval Augmented Generation` use cases.
- Since the models have some limitations like `context-limit`, they might not be able to consume a huge amount of data.
- One simple solution to address the context-limit problem is `RAG`.
- Nowadays the models are released with very-high context length. But still there are problems like `lost-in-the-middle`. These are some problems addressed by RAG and embeddings are key to it.
- Embedding Models generate `vector embeddings` like a feature extraction and store these in a specialized database called `vector-database`.

:::tip

Choose embedding models for your use case from [MTEB](https://huggingface.co/spaces/mteb/leaderboard) from hugging face.

:::

### Specialized Models

- Apart from the generally available models, there are also models `fine-tuned` for specific use cases.
- `Sora2`, model specialized in video generation. `gpt-5.1-codex` - gpt-5 model which is optimized for `agentic` coding tasks.
