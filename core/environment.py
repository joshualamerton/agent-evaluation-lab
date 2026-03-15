class Environment:

    def __init__(self, scenario):
        self.state = scenario.initial_state()

    def apply_action(self, action):

        if action["type"] == "buy":
            item = action["item"]
            self.state["inventory"].append(item)

        if action["type"] == "complete":
            self.state["completed"] = True

        self.state["step"] += 1

        return self.state
