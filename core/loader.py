import importlib
import os


def load_environment(name):

    base_path = "modules/environments"

    for folder in os.listdir(base_path):

        if folder == name:
            module_path = f"modules.environments.{folder}.scenario"
            module = importlib.import_module(module_path)
            return module.EcommerceScenario()

    raise ValueError(f"Environment not found: {name}")
