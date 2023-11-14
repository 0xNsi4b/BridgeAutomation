import time
import random

from user_settings.settings import sleep_min, sleep_max


def get_deadline():
    return int(time.time()) + 60 * 3


def get_percent(min_percent, max_percent):
    return random.randint(min_percent, max_percent) / 100


def sleep():
    time.sleep(random.randint(sleep_min, sleep_max))
