class AgentInterface:

    def __init__(self, name):
        self.name = name

    def decide(self, state, tools):
        """
        Agent receives environment state and available tools
        and returns an action dictionary.
        """
        raise NotImplementedError
