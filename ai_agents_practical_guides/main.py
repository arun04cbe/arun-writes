from agents.router_agent import RouterAgent
from rich.console import Console
from rich.markdown import Markdown


async def main():
    conversation_history = []
    while True:
        print("\nEnter a query (or type 'exit' to quit):")
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the application.")
            break
        router_agent = RouterAgent()

        response = await router_agent.get_answer(user_input, conversation_history)
        console = Console()
        console.print(Markdown(response))

        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "agent", "content": response})


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
