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
    return animal_name


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
    system_setting = r"""\
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


# contextを受け取って動物を推論し生態と豆知識を返す関数
def chat(context):
    animal_name = chat_inference(context)
    food = chat_food(animal_name)
    area = chat_area(animal_name)
    trivia = chat_trivia(animal_name)
    knowledge = {name: value for name, value in locals().items() if name == name}
    return knowledge
