import replicate

img = "/docs/img/dal.jpg"


def create_prompt(img):
    text = replicate.run(
        "methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5",
        input={"image": open(img, "rb")},
    )
    first_comma_index = text.find(",")
    output = text[:first_comma_index]
    return output


if __name__ == "__main__":
    output = create_prompt(img)
    print(output)
