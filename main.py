import ast
import concurrent.futures
import random
import traceback
from art import text2art
from termcolor import colored
import inquirer
from inquirer.themes import load_theme_from_dict as loadth

from user_settings.settings import random_wallet, max_workers
from utils.config import keys, proxies, deposit_addresses, aptos_addresses
from user_settings.functions import *
from loguru import logger
from eth_account import Account as EthereumAccount

from utils.helpers import sleep


def get_functions_from_file(file_path: str) -> list:
    with open(file_path, 'r') as file:
        source_code = file.read()
        tree = ast.parse(source_code)

        return [eval(node.name) for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]


def create_choice_dict() -> dict:
    function = get_functions_from_file('user_settings/functions.py')
    return {f'Запуск модуля {i.__name__}': i for i in function}


def get_action(choices_lst: list) -> str:
    theme = {
        "Question": {
            "brackets_color": "bright_yellow"
        },
        "List": {
            "selection_color": "bright_yellow"
        }
    }

    question = [
        inquirer.List(
            "action",
            message=colored("Выберите действие", 'light_yellow'),
            choices=choices_lst + ["Выход"]
        )
    ]
    return inquirer.prompt(question, theme=loadth(theme))['action']


def run_func(module, data):
    try:
        module(data)
    except Exception as e:
        logger.error(f"[{EthereumAccount.from_key(data[0]).address}]{e}")
        # traceback.print_exc()


def main(func: callable):

    while len(proxies) < len(keys):
        proxies.append(proxies[len(proxies) % len(proxies)])

    data = [keys, proxies]

    if func.__name__ == 'aptos_bridge':
        data.append(aptos_addresses)

    if func.__name__ == 'withdraw':
        data.append(deposit_addresses)

    acc_data = list(zip(*data))

    if random_wallet:
        random.shuffle(acc_data)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for acc in acc_data:
            executor.submit(run_func, func, acc)
            sleep()


if __name__ == '__main__':
    art = text2art(text="LayerZero     by      Alpha Rescue", font="standart")
    print(colored(art, 'light_magenta'))
    choice_dict = create_choice_dict()

    while True:
        action = get_action(list(choice_dict.keys()))
        if action in choice_dict:
            print(choice_dict[action], type(choice_dict[action]))
            main(choice_dict[action])
        elif action == 'Выход':
            exit()
        else:
            pass
