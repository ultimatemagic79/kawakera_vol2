import os

secret = os.environ.get("DJANGO_SECRET_KEY")
print(secret)
