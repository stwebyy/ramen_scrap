## ramen_scrapを使うにあたり

このアプリはscrapyを使用しています。
後学のため、自分の辞書が割りとして扱うため、各ファイルにdescriptionを設けています。
また、以下のステップでscrapyを使用できます。

### 1.導入
pip install scrapy

scrapy startproject <project_name>

ex.)
scrapy startproject ramen

### 2.items(ここに実際の動作を記載していく)の編集
抽出する情報の一単位分を表すクラス。
CSV ならその１行、データベースなら１レコードに相当するオブジェクトです。

ex.)
date = scrapy.Field()

Item の属性を表すもので、CSVやデータベースのカラムに相当します。

### 3.スパイダー（スクレイピング・クローリングの設定を行う）ディレクトリの作成
どのようにクロールしてどのようにデータを取り出すかを規定します。
cd <project_name>

scrapy genspider <スパイダー名> <クロール対象ドメイン名>

ex.)
scrapy genspider ramen_serach tabelog.com


