import os
import importlib


def load_environment(name):

    base_dir = "modules/environments"

    for folder in os.listdir(base_dir):

        if folder == name:

            module_path = f"modules.environments.{folder}.scenario"

            module = importlib.import_module(module_path)

            if hasattr(module, "Environment"):
                return module.Environment()

            raise ValueError(
                f"Environment module '{name}' does not define an Environment class"
            )

    raise ValueError(f"Environment not found: {name}")
