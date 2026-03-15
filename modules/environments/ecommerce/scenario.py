from core.scenario import Scenario


class EcommerceScenario(Scenario):

    def __init__(self):
        super().__init__(
            description="Buy a laptop under a simple ecommerce scenario",
            goal="purchase_laptop"
        )
