## replicateで使えそうなモデルを探す
### やり方：ダルメシアンを入力
![ダルメシアン](img/dal.jpg "入力画像")
* clip_prefix_caption : A dog standing on top of a dirt field.
* clip-caption-reward : a large black and white dog standing together near a tree in the dirt area.
* image2prompt : a ** dalmatian ** dog standing next to a black and white dog, a jigsaw puzzle by Baiōken Eishun, shutterstock contest winner, precisionism, creative commons attribution, handsome, hd

### image2promptが今の所良さそう
* localでtext生成できるか確認->ok
* 第1カンマまでが有益な情報
* 切り出して渡すコードを作成
* こっちのレポジトリでclip.py作成（完）