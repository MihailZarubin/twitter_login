import random
import json


class Utils:
    @staticmethod
    def get_settings_from_json():
        with open('../settings.json') as f:
            settings = json.load(f)
        return settings

    @staticmethod
    def get_random_width():
        return random.randint(800, 1366)

    @staticmethod
    def get_random_height():
        return random.randint(600, 768)

    @staticmethod
    def get_random_user_agent():
        chrome_version = f"{random.randint(95, 111)}.0.{random.randint(1000, 5000)}.{random.randint(100, 999)}"
        user_agents = [
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} "
            "Safari/537.36",
            f"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} "
            "Safari/537.36"
        ]
        return random.choice(user_agents)
