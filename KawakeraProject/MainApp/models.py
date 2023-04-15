from django.db import models


# Create your models here.
class MainApp(models.Model):
    """モデル"""

    photo = models.ImageField(verbose_name="画像")

    def __str__(self):
        return self.title


class Result(models.Model):
    "リザルト画面のモデル"
    photo = models.ImageField(verbose_name="画像")
    ecology = models.TextField(verbose_name="生態")
    mame = models.TextField(verbose_name="豆知識")

    def __str__(self):
        return self.title
