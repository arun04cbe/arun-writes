from prompts.prompt import router_agent_prompt
from pydantic import BaseModel, Field
from enum import Enum
from llm import get_model_with_structured_response
from agents.req_gathering_agent import RequirementGatheringAgent
from agents.task_planning_agent import TaskPlannerAgent


class AgentType(str, Enum):

    REQUIREMENT_GATHERING_AGENT = "Requirement_Gathering_Agent"
    TASK_PLANNER_AGENT = "Task_Planner_Agent"


class RouterAgentResponse(BaseModel):
    selected_agent: AgentType | None
    comments: str = Field(
        description="Explanation of why the agent was selected or why the query cannot be handled."
    )


class RouterAgent:

    def __init__(self):
        self.prompt = router_agent_prompt
        self.req_gathering_agent = RequirementGatheringAgent()
        self.task_planner_agent = TaskPlannerAgent()

    async def route_query(self, user_query: str, conversation_history: list[dict]):

        prompt = self.prompt.format(
            user_query=user_query, conversation_history=str(conversation_history)
        )
        response = await get_model_with_structured_response(prompt, RouterAgentResponse)
        if response["parsed"]:
            selected_agent = response["parsed"].selected_agent
            comments = response["parsed"].comments

            print(f"\nSelected Agent: {selected_agent}\n")
            return selected_agent, comments
        else:
            return None, "Failed to parse model response."

    async def get_answer(self, user_query: str, conversation_history: list[dict]):
        selected_agent, comments = await self.route_query(
            user_query, conversation_history
        )
        if selected_agent:
            if selected_agent == AgentType.REQUIREMENT_GATHERING_AGENT:
                question, summary = await self.req_gathering_agent.gather_requirements(
                    user_query, conversation_history
                )
                if question:
                    return question
                if summary:
                    return summary
            elif selected_agent == AgentType.TASK_PLANNER_AGENT:
                task_plan = await self.task_planner_agent.plan_tasks(
                    user_query, conversation_history
                )
                if task_plan:
                    return task_plan
            return "Failed to route the query to an agent. " + comments
        return comments
