import openai
import re
from Utils import Utils


class OpenAIService:

    def __init__(self):
        self.user = None
        self.api_key = Utils.get_settings_from_json()['openai_api_key']
        self.model = Utils.get_settings_from_json()['openai_api_model']

    def set_user(self, user):
        self.user = user

    def generate_twit_text(self, prompt):
        return self.get_response(prompt)

    def get_response(self, prompt, role='user'):
        try:
            openai.api_key = self.api_key
            completion = openai.ChatCompletion.create(
                model=self.model, messages=[
                    {
                        "role": role,
                        "content": prompt
                    }
                ]
            )
            res = completion.choices[0].message.content.encode('ascii', 'ignore').decode('utf-8')
            return re.sub(r'#\w+', '', res)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise e
