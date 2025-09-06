import os
import requests
from json import JSONDecodeError

from .base import TimeEstimateBase


class HuggingFaceEstimate(TimeEstimateBase):

    PROMPT_FORMAT = 'Responde solo con cualquiera de estas opciones:' \
        f'[{",".join(TimeEstimateBase.OPTIONS)}].\n' \
        'Tarea: {title}.\n' \
        'Descripción tarea: {description}.\n' \
        'Haz los supuestos que tengas que hacer, pero solo responde con el ' \
        'tiempo ("1 d" por ejemplo).'

    MODEL = 'deepseek-ai/DeepSeek-V3-0324:novita'
    API_URL = "https://router.huggingface.co/v1/chat/completions"

    def __init__(self, config=None):
        super(HuggingFaceEstimate, self).__init__(config)
        self.api_key = os.getenv('HF_TOKEN')
        if not self.api_key:
            raise ValueError('Hugging Face Token not defined')

    def _estimate(self, prompt):
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "model": self.MODEL,
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(
            self.API_URL,
            headers=headers,
            json=payload
        )
        try:
            return response.json()['choices'][0]['message']['content']
        except (JSONDecodeError, IndexError, KeyError):
            return None
