from typing import List, Dict
import openai


class ModelInterface:
    def chat_completion(self, messages: List[Dict]) -> str:
        pass

    def image_generation(self, prompt: str) -> str:
        pass


class OpenAIModel(ModelInterface):
    def __init__(self, api_key: str, model_engine: str, image_size: str = '512x512'):
        openai.api_key = api_key
        self.model_engine = model_engine
        self.image_size = image_size

    # def chat_completion(self, messages) -> str:
    #     response = openai.ChatCompletion.create(
    #         model=self.model_engine,
    #         messages=messages
    #     )
    #     return response
    def chat_completion(self, messages) -> str:
        try:
            response = openai.Completion.create(
                engine=self.model_engine,
                messages=messages,
            )
            return response
        except openai.error.OpenAIError as e:
            print(f"Error in chat_completion: {e}")
            return "错误了1"
        except Exception as e:
            print(f"Error in chat_completion: {e}")
            return "错误了2"

    def image_generation(self, prompt: str) -> str:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=self.image_size
        )
        image_url = response.data[0].url
        return image_url
