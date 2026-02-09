from prompts.prompt import requirement_gathering_agent_prompt
from llm import get_model_with_structured_response
from pydantic import BaseModel, Field


class RequirementGatheringAgentResponse(BaseModel):
    question: str | None = Field(
        description="The question to ask the user to gather requirements."
    )
    summary: str | None = Field(
        description="A summary of the gathered requirements if the user indicates they are done."
    )


class RequirementGatheringAgent:

    def __init__(self):
        self.prompt = requirement_gathering_agent_prompt

    async def gather_requirements(
        self, user_query: str, conversation_history: list[dict]
    ):
        prompt = self.prompt.format(
            user_query=user_query, conversation_history=str(conversation_history)
        )
        response = await get_model_with_structured_response(
            prompt, RequirementGatheringAgentResponse
        )
        if response["parsed"]:

            question = response["parsed"].question
            summary = response["parsed"].summary
            return question, summary

        else:
            return None, "Failed to parse model response."
