from django.db import models


# Create your models here.
class MainApp(models.Model):
    """モデル"""

    photo = models.ImageField(verbose_name="動物の画像")
    
    class Meta:
        verbose_name_plural = 'Main'

    def __str__(self):
        return self.title


class Result(models.Model):
    "リザルト画面のモデル"
    photo = models.ImageField(verbose_name="画像")
    area = models.TextField(verbose_name="住んでるとこ")
    mame = models.TextField(verbose_name="豆知識")
    food = models.TextField(verbose_name="食べるもの")
    
    def __str__(self):
        return self.title
