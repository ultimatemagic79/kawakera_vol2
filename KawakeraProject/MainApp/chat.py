import openai
import os
from .trans import deepl_translator

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
    """
    _summary_ : contextからなんの動物かを推論する関数

    Parameters
    --------------------------------
    context : string
        画像を表現するテキスト

    Returns
    --------------------------------
    output : string
        テキストから推論した動物名

    """

    # Chatgptにシステム設定のためのプロンプト
    system_setting = """\
        ####Settings###
        You are a scholar who knows animals.

        ####Situation###
        You receive a text from a user that describes an image of an animal

        ####Request###
        Please use the following format in your response
        [name]: "animal name"
        Please determine the animal most likely to be in the image based on the text you received from the user, step by step.
        Please output the name of the animal you have determined according to the format.

        Here are some examples

        Example 1
        user:a medium-sized dog breed with a short, white coat covered in black spots
        assistant: [name] Dalmatian

        Example 2
        user: a black and white dog standing on top of a grass covered field, a picture by Toyen
        assistant: [name] Shiba Inu
        """
    # Chatgptクラスのインスタンス
    chatgpt = Chatgpt(system_setting)
    chatgpt.input_message(context)
    animal_name = chatgpt.input_list[-1]["content"]
    animal_name = animal_name[8:]
    return animal_name


# 動物名から豆知識と食べ物，生態地域，豆知識を生成
def chat_knowledge(animal_name):
    system_setting = """\
        ####Settings###
        You are a scholar who knows a lot about animals. You have a wealth of knowledge about what animals eat, where they live, and trivia about them.

        ######Status###.
        You are about to be asked a question by a curious user about what animals eat, where they live, and trivia about animals.

        ######Requirement###.
        Please answer the user's questions.

        Here are some examples

        Example 1
        user: What do lions eat?
        assistant: They eat bamboo shoots and bamboo shoots as well as bamboo shoots and bamboo grass. It has been recorded that it sometimes catches and eats small animals such as insects.
        user:Where do lions live?
        assistant:Lions are found in Central Africa (excluding southern South Africa) and northwestern India.
        user: Please tell us some trivia about lions.
        assistant: Lions spend most of the day sleeping. Lions originally spend 15 to 20 hours a day sleeping or lying down to relax. The success rate of temporary hunting is 20% to 30%. Hunting is not done every day, but every few days. In zoos, fasting days are set aside in accordance with wild ecology, and food is given every few days.

        Example 2
        user: Please tell me what giant pandas eat.
        assistant: They eat large mammals such as zebras, wild boars, gnus, and antelope.
        user:Please tell us where the giant panda lives.
        assistant: Giant pandas live in the mountainous forests of Sichuan, Shaanxi, and Gansu provinces in the southwestern part of the People's Republic of China, at altitudes ranging from 1300 to 3500 meters.
        user: Please tell us some trivia about giant pandas.
        assistant: Pandas are actually carnivores, and are classified in the Carnivora family. While herbivores have long intestines that are more than 20 times their body length, pandas' intestines are about 4 times their body length. From this point of view, pandas are carnivores. Pandas spend much of the day eating, but only 20% of the bamboo and bamboo grass they eat can be digested. Their eyes are surprisingly sharp and scary. They eat all day long.
        """
    chatgpt = Chatgpt(system_setting)
    question_food = f"Tell us what {animal_name} eat."
    chatgpt.input_message(question_food)
    food = chatgpt.input_list[-1]["content"]
    question_area = f"Tell us where the {animal_name} live."
    chatgpt.input_message(question_area)
    area = chatgpt.input_list[-1]["content"]
    question_trivia = f"Tell me some trivia about {animal_name}"
    chatgpt.input_message(question_trivia)
    trivia = chatgpt.input_list[-1]["content"]
    knowledge = {
        "name": animal_name,
        "food": food,
        "area": area,
        "trivia": trivia,
    }
    knowledge = deepl_translator(knowledge)
    return knowledge


# 動物名から食べるものを生成
def chat_food(animal_name):
    system_setting = """\
        ####Settings###
        You are a scholar who knows animals.
        
        ####Situation###.
        A question from a user who is curious about animals about what the animals eat

        ####Request###.
        Please answer the user's question.
        Here are some examples

        Example 1
        user: Tell us where the lion live.
        assistant: Eats large mammals such as zebras, wild boars, gnus, antelopes, etc.

        Example 2
        user: Tell us where the giant panda live.
        assistant: They eat bamboo shoots as well as bamboo shoots and bamboo shoots. It has been recorded that they sometimes catch and eat small animals such as insects.
        """
    chatgpt = Chatgpt(system_setting)
    question = "Tell us where the {animal_name} live."
    chatgpt.input_message(question)
    food = chatgpt.input_list[-1]["content"]
    return food


# 動物名から生態地域を生成
def chat_area(animal_name):
    system_setting = """\
        ####Settings###
        You are a scholar who knows animals.
        
        ####Situation###.
        A question from a user who is curious about animals about what the animals eat

        ####Request###.
        Please answer the user's question.
        Here are some examples

        Example 1
        user: Tell us what lion eat.
        assistant: Eats large mammals such as zebras, wild boars, gnus, antelopes, etc.

        Example 2
        user: Tell us what giant panda eat.
        assistant: They eat bamboo shoots as well as bamboo shoots and bamboo shoots. It has been recorded that they sometimes catch and eat small animals such as insects.
        """
    chatgpt = Chatgpt(system_setting)
    question = "Tell us what {animal_name} eat."
    chatgpt.input_message(question)
    area = chatgpt.input_list[-1]["content"]
    return area


# 動物名から豆知識を生成
def chat_trivia(animal_name):
    system_setting = """\
        ####Settings###
        You are a scholar who knows animals.

        ####Situation###.
        A user is curious about animals and asks you about animal trivia

        ####Requirement###
        Please answer the user's question.
        Here are some examples

        Example 1
        user: Tell me some trivia about lions.
        assistant: Lions spend most of the day sleeping. Lions originally spend 15 to 20 hours a day sleeping or lying down to relax. The success rate of temporary hunting is 20% to 30%. Hunting is not done every day, but every few days. In zoos, fasting days are set aside in accordance with wild ecology, and food is given every few days.

        Example 2
        user: Tell me some trivia about giant pandas.
        assistant: Pandas are actually carnivores, and are classified in the Carnivora family. While herbivores have long intestines that are more than 20 times their body length, 
        the panda's intestines are about 4 times its body length. From this point of view, pandas are carnivores. Pandas spend much of the day eating, but only 20% of 
        the bamboo and bamboo grass they eat can be digested. Their eyes are surprisingly sharp and scary. They eat all day long.
        """
    chatgpt = Chatgpt(system_setting)
    question = "Tell me some trivia about {animal_name}"
    chatgpt.input_message(question)
    trivia = chatgpt.input_list[-1]["content"]
    return trivia


# contextを受け取って動物を推論し生態と豆知識を返す関数(OpenAIからエラーが帰ってくる．多分アクセス過多)
def chat(context):
    animal_name = chat_inference(context)
    food = chat_food(animal_name)
    area = chat_area(animal_name)
    trivia = chat_trivia(animal_name)
    knowledge = {
        "name": animal_name,
        "food": food,
        "area": area,
        "trivia": trivia,
    }
    return knowledge
