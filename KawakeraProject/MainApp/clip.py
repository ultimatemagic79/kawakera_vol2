import replicate
from PIL import Image


def image2text(img):
    """
    _summary_ : 入力画像に対し動物のプロンプトを返す関数

    Parameters
    --------------------------------
    img : string
        入力画像のパス

    Returns
    --------------------------------
    output : string
        画像に対する説明（英文）
        必要な部分が第1カンマまでだったからそこまで切り取って出力するよん.

    """

    text = replicate.run(
        "methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5",
        input={"image": open(img, "rb")},
    )
    first_comma_index = text.find(",")
    output = text[:first_comma_index]
    return output


#   テスト
if __name__ == "__main__":
    # 入力された画像のパス
    img = "/docs/img/dal.jpg"

    # 出力結果（string）
    output = clip(img)
    print(output)
