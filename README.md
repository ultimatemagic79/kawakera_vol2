## 概要

![](docs/img/summary.png)


# .envファイルの作成
- .env.exampleを複製して.envという名前に変える
- POSTGRESという名前がついた環境変数はすべてpostgresという名前に設定する
- SECRET_KEYを設定する

## SECRET_KEYを生成する方法

```
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
```

生成した文字列を.envの
DJANGO_SECRET_KEY="django-insecure-"
の -django-insecure- の後ろにくっつける
