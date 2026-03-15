from core.scenario import Scenario


class Environment:

    def __init__(self):

        scenario = Scenario(
            description="Buy a laptop from an ecommerce store",
            goal="purchase_laptop"
        )

        self.state = scenario.initial_state()

    def apply_action(self, action):

        if action["type"] == "buy":
            item = action["item"]
            self.state["inventory"].append(item)

        if action["type"] == "complete":
            self.state["completed"] = True

        self.state["step"] += 1

        return self.state
