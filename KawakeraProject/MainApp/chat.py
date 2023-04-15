import openai
import os

# OpenAIのAPIキーを取得
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAIのAPIのキーを設定
openai.api_key = OPENAI_API_KEY


# Chatを行うためのクラス作成
class Chatgpt:
    def __init__(self, system_setting, temperature=0.7):
        self.system = {"role": "system", "content": system_setting}
        self.input_list = [self.system]
        self.logs = []
        self.temperature = temperature

    def input_message(self, input_text):
        self.input_list.append({"role": "user", "content": input_text})
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.input_list,
            temperature=self.temperature,
        )
        self.logs.append(result)
        self.input_list.append(
            {"role": "assistant", "content": result.choices[0].message.content}
        )


# contextからなんの動物か推論する
def chat_inference(context):
    # Chatgptにシステム設定のためのプロンプト
    system_setting = ""
    # Chatgptクラスのインスタンス
    chatgpt = Chatgpt(system_setting)
    chatgpt.input_message(context)
    animal_name = chatgpt.input_list[-1]["content"]
    return animal_name


# 動物名から食べるものを生成
def chat_food(animal_name):
    system_setting = ""
    chatgpt = Chatgpt(system_setting)
    chatgpt.input_message(animal_name)
    food = chatgpt.input_list[-1]["content"]
    return food


# 動物名から生態地域を生成
def chat_area(animal_name):
    system_setting = ""
    chatgpt = Chatgpt(system_setting)
    chatgpt.input_message(animal_name)
    area = chatgpt.input_list[-1]["content"]
    return area


# 動物名から豆知識を生成
def chat_trivia(animal_name):
    system_setting = ""
    chatgpt = Chatgpt(system_setting)
    chatgpt.input_message(animal_name)
    trivia = chatgpt.input_list[-1]["content"]
    return trivia


# contextを受け取って動物を推論し生態と豆知識を返す関数
def chat(context):
    animal_name = chat_inference(context)
    food = chat_food(animal_name)
    area = chat_area(animal_name)
    trivia = chat_trivia(animal_name)
    return
