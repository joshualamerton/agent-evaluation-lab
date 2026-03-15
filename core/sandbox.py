class Sandbox:

    def __init__(self, agent, environment, tools):
        self.agent = agent
        self.environment = environment
        self.tools = tools
        self.history = []

    def run(self, max_steps=10):

        state = self.environment.state

        for _ in range(max_steps):

            action = self.agent.decide(state, self.tools)

            state = self.environment.apply_action(action)

            self.history.append(action)

            if state["completed"]:
                break

        return state
