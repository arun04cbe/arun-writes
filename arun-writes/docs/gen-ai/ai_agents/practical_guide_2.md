---
sidebar_position: 2
sidebar_label: Practical Guide 2
sidebar_class_name: green
sidebar_key: unique-sidebar-item-key
---

# Prompt Optimization

(Continuation from `Practical Guide 1`)

**Do you see any problems or concerns with the provided output?**

- The good part, it has provided me a code which is correct.
- It has also provided me explanations about the code for me to understand, what is happening.
- But, is it possible to run the code in an existing python environment or in a separate sandbox environment?
- It is not possible, so does that mean `LLM` had a mistake, no it isn't.
- Now comes the real `prompt engineering`, instead of requesting model to generate in an open-ended way, try to be more `specific` on how you can use it in your downstream automation tasks.

## How do we take prompting?

1. Prompt Engineering is an iterative process. It might be hard to get what we wanted from the model in one-shot.
2. Write a prompt for your needs, run and observe the output and try to refine it.

Below is the prompt with some modifications for the code generation example. Update the prompt and observe the response again.

```python title="Updated Prompt"

prompt = """
You are AI Agent capable of generating code for the given user input.

Instructions:
1. Generate code in Python language.
2. Do not install any libraries, assume all libraries are already installed.
3. Do not provide any explanation, only provide the code.

Output Format:
1. Give the output in as a python dictionary format with the following keys
- code: The code generated for the given input.
- explanation: A brief explanation of the code.

Input: {user_input}
"""
```

:::tip[Prompt Engineering Best Practices]

1. Always try to write your prompts in `markdown` format.
2. Segregating the prompt into multiple sections, highlighting the important parts of the prompt helps in getting better responses. Below is how I have been structuring the prompts,
   1. _Role_ of the Assistant/Agent - What is the core part of expectation from AI.
   2. _Instructions/Rules_ - Steps to be followed to achieve the goal
   3. _Inputs_ - Description of the inputs provided
   4. _Output_ - Required output in desired format
   5. _Examples_ (`Few Shot Prompting`) - Provide examples for complex scenarios
3. Checkout out `prompting guides` from the model which you have chosen for your use case. Follow `openai` cookbooks and `anthropic` prompting guides.
4. Use `structured outputs` wherever possible to make sure model responses are without any parsing errors.
5. Try avoiding `Negative Prompting` (might be an older trick)

:::

I have a personal experience of going from 50% to 70% in terms of accuracy when using `gpt4.1` specific prompt when I switched from `gpt-4o`
