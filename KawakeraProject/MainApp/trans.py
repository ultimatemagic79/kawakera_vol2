import deepl
import os

# DeepLのAPIキーの取得
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

# DeepLのTranslatorオブジェクトの作成
translator = deepl.Translator(DEEPL_API_KEY)


def deepl_translator(text):
    """
    Translators
    
    Parameters
    ----------
    input : string（English）
    
    Returns
    -------
    output : string (Japanese)
    """
    result = translator.translate_text(text, target_lang='JA')
    return result
