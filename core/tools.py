class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, name, func):
        self.tools[name] = func

    def call(self, name, *args):
        return self.tools[name](*args)


def search_products(query):

    products = {
        "laptop": ["laptop"],
        "phone": ["phone"],
        "tablet": ["tablet"]
    }

    return products.get(query, [])
