from django.db import models


# Create your models here.
class MainApp(models.Model):
    """モデル"""

    photo = models.ImageField(verbose_name="画像")

    def __str__(self):
        return self.title
