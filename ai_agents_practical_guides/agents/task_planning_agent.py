from prompts.prompt import task_planner_agent_prompt
from llm import get_model_response


class TaskPlannerAgent:
    def __init__(self):
        self.prompt = task_planner_agent_prompt

    async def plan_tasks(self, user_query: str, conversation_history: list[dict]):
        prompt = self.prompt.format(
            user_query=user_query, conversation_history=str(conversation_history)
        )
        response = await get_model_response(prompt)
        return response
