import random
from utils.helpers import sleep


class Custom:
    def __init__(self, private_key: str, proxy: str) -> None:
        self.private_key = private_key
        self.proxy = proxy

    def run_module(self, use_modules: list):
        for module in use_modules:
            if not isinstance(module, list):
                module(self.private_key, self.proxy)
                sleep()
            else:
                self.run_module(module)

    def start(self, use_modules: list, random_module: bool):
        if random_module:
            random.shuffle(use_modules)
        self.run_module(use_modules)
