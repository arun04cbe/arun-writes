from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL_NAME = "openai/gpt-oss-120b"

model = ChatGroq(model=GROQ_MODEL_NAME, api_key=GROQ_API_KEY)


async def get_model_response(prompt):

    response = await model.ainvoke(prompt)
    return response.content


async def get_model_with_structured_response(prompt, response_model):

    model_with_structure = model.with_structured_output(
        schema=response_model, method="json_schema", include_raw=True
    )
    response = await model_with_structure.ainvoke(prompt)
    return response
