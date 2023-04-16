import deepl
import os

# DeepLのAPIキーの取得
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

# DeepLのTranslatorオブジェクトの作成
translator = deepl.Translator(DEEPL_API_KEY)


def deepl_translator(dictionary):
    """
    Translators
    
    Parameters
    ----------
    input : dictionary {key:value} (English)
    
    Returns
    -------
    output : dictionary {key:value}(Japanese)
    """
    for key in dictionary:
        dictionary[key] = translator.translate_text(dictionary[key], target_lang='JA')
    return dictionary
