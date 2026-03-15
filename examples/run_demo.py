import argparse

from core.loader import load_environment, list_environments
from core.agent_interface import AgentInterface
from core.sandbox import Sandbox
from core.tools import ToolRegistry, search_products
from core.evaluator import Evaluator


class DemoAgent(AgentInterface):

    def decide(self, state, tools):

        if not state["inventory"]:
            results = tools.call("search", "laptop")

            return {
                "type": "buy",
                "item": results[0]
            }

        return {
            "type": "complete"
        }


def main():

    parser = argparse.ArgumentParser(
        description="Run an agent inside Agent Evaluation Lab"
    )

    parser.add_argument(
        "--env",
        default="ecommerce",
        help="Environment name (default: ecommerce)"
    )

    parser.add_argument(
        "--list-envs",
        action="store_true",
        help="List available environments"
    )

    args = parser.parse_args()

    # List environments if requested
    if args.list_envs:
        print("Available environments:")
        for env in list_environments():
            print("-", env)
        return

    # Load environment dynamically
    env = load_environment(args.env)

    tools = ToolRegistry()
    tools.register("search", search_products)

    agent = DemoAgent("demo_agent")

    sandbox = Sandbox(agent, env, tools)

    final_state = sandbox.run()

    evaluator = Evaluator()
    result = evaluator.evaluate(final_state, sandbox.history)

    print("Final State")
    print(final_state)

    print("\nAction History")
    print(sandbox.history)

    print("\nEvaluation")
    print(result)


if __name__ == "__main__":
    main()
