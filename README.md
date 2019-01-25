# AREA 31

筑波大学国際生（31期）の居場所を地図上にプロットするWebアプリケーションです。

※このREADME.mdは開発者用に書かれています。

## 概要

「AREA 31」は、筑波大学国際生（31期）の居場所を地図上にプロットするWebアプリケーションです。

アプリケーションはDjangoで書かれています。WebサーバーとしてNginx、DBはMySQLを利用してます。
詳しくは、docker-compose.ymlの設定ファイルを確認してください。

また、本アプリケーションは1台のサーバー上で動かすことを前提としています。クラウドサービスでDBなど、別々のサービスを利用する場合は、適宜変更を加える必要があります。

## 要件（Requirement）

- Docker & Docker Compose 

本アプリケーションを起動するために、Docker、そしてDocker Composeを利用しています。

## デプロイメント

#### ビルド

Gitでスクリプトを取得したら、docker-compose.ymlがあるディレクトリでビルドを実行します。
Dockerのキャッシュが残って正しくビルドが行われない場合があるので、--no-cacheオプションをつけて実行することをおすすめします。

```sh
docker-compose build --no-cache
```

#### 起動

ビルドが終了したら、コンテナを起動します。

```sh
docker-compose up -d
```

#### マイグレーション

Djangoの機能を利用して、SQL文を発行します。
makemigrationsコマンド移行にDjangoアプリ（usersやarea31）を指定してマイグレーションを実行します。

```sh
docker-compose exec web python manage.py makemigrations <app_name>
eg.) docker-compose exec web python manage.py makemigrations users
eg.) docker-compose exec web python manage.py makemigrations mysite
```

makemigrationsコマンドで出力したSQL文を実行します。
migrateコマンドを実行してください。
```
docker-compose exec web python manage.py migrate
```

#### スーパーユーザーの登録

Djangoのズーパーユーザーを登録します。
createsuperuserコマンドを実行後、username、email address、passwordを入力してください。
```
docker-compose exec -it web python manage.py createsuperuser
```

#### アクセス

スーパーユーザーを登録したら、ブラウザからアプリケーションにアクセスします。

メインページ
http://localhost:8000/map

管理サイト
http://localhost:8000/admin


## ディレクトリ構成

| path                          | 説明                                                                                                                                                                                                                                              |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| /docker-compose.yml           | Docker Composeの設定ファイルです。                                                                                                                                                                                                                |
| /README.md                    | 本テキストです。                                                                                                                                                                                                                                  |
| /.gitattibutes                | Gitに関する設定ファイルです。                                                                                                                                                                                                                     |
| /.gitignore                   | Gitに関する設定ファイルです。                                                                                                                                                                                                                     |
| /nginx                        | nginxコンテナに関するディレクトリです。                                                                                                                                                                                                           |
| /nginx/uwsgi_params           | uwsgiの設定パラメーターです。                                                                                                                                                                                                                     |
| /nginx/conf/mysite_nginx.conf | nginxの設定ファイルです。ローカル環境以外で実行する場合は、「server_name」を正しく記載しなおしてください。                                                                                                                                        |
| /sql                          | MySQLコンテナに関するディレクトリです。                                                                                                                                                                                                           |
| /nginx/init.sql               | MySQLのコンテナ起動時に最初に投入するSQL文です。                                                                                                                                                                                                  |
| /src                          | アプリケーションのプログラム用のディレクトリです。                                                                                                                                                                                                |
| /src/manage.py                | Djangoのエントリーポイントとなるスクリプトです。                                                                                                                                                                                                  |
| /src/mysite                   | Djangoのプロジェクトディレクトリです。                                                                                                                                                                                                            |
| /src/mysite/settings.py       | Djangoの設定スクリプトです。新しくアプリを追加した場合や、DB情報を変更する場合などはこのファイルを修正して下さい。                                                                                                                                |
| /src/mysite/urls.py           | Djangoのルーティングを行うディレクトリです。                                                                                                                                                                                                      |
| /src/mysite/その他            | 基本的にはいじりません。                                                                                                                                                                                                                          |
| /src/area31                   | Djangoのアプリケーション1つです。メインとなるアプリケーションです。                                                                                                                                                                               |
| /src/area31/admin.py          | Djangoの管理サイトに登録するためのスクリプトです。                                                                                                                                                                                                |
| /src/area31/models.py         | Djangoのモデル（DB設計）を記述するためのスクリプトです。                                                                                                                                                                                          |
| /src/area31/test.py           | Djangoのテスト用のスクリプトです。                                                                                                                                                                                                                |
| /src/area31/views.py          | Djangoのビュー（ロジックと表示方法）を記述するためのスクリプトです。                                                                                                                                                                              |
| /src/area31/migrations        | Djangoのマイグレーション用のディレクトリです。                                                                                                                                                                                                    |
| /src/area31/templates         | HTMLのテンプレート用のディレクトリです。                                                                                                                                                                                                          |
| /src/area31/その他            | 基本的にはいじりません。                                                                                                                                                                                                                          |
| /src/users                    | Djangoのアプリケーション1つです。運用がしやすいため、ユーザーのみ別のアプリケションとして管理しています。また、ユーザーは、DjangoのAbstractBaseUserを継承して記述しています。その他の点は「area31」アプリケーションと同一のため記述を省略します。 |
| /src/static                   | CSSやJS資材を置くためのディレクトリです。                                                                                                                                                                                                         |
| /web                          | Djangoコンテナに関するディレクトリです。                                                                                                                                                                                                          |
| /web/Dockerfile               | Djangoコンテナを作成するためのDockerfileです。                                                                                                                                                                                                    |
| /web/requirements.txt         | Djangoコンテナ内でインストールするPythonモジュールリストです。                                                                                                                                                                                    |
| /web/requirements.txt         | Djangoコンテナ内でインストールするPythonモジュールリストです。                                                                                                                                                                                    |

## ロードマップ

本アプリケーションは段階的に機能追加します。

ここでは、各段階（Version）における大まかな機能を記載します。

ユーザーのレビューに基づき、アジャイルに機能追加を行うため、このロードマップは適宜変更します。

### Version 1

Version 1では、基本的なユーザー登録を行い、マップ上へユーザーをプロットします。

ユーザーは、基本的な自身の情報（名前、場所等）を登録し、登録した場所がユーザーの画像付きでGoogle Map上に表示されます。

場所は、1ユーザーにつき複数登録することができ、それぞれの場所にはラベル（自宅、会社等）を付すことができます。

また、ユーザーは登録した情報をいつでも編集することができます。

さらに、不特定多数のユーザーが参加できないように、アプリケーションで統一のパスワードを設定できます。

### Version 2

Version 2では、ワークスペースを導入し、同じワークスペース内のユーザー同士がお互いの位置を確認できます。

### Version 3

Version 3では、過去にいた場所を登録できる機能を追加します。

### Version 4

T.B.D. (e.g. 宴会設定機能)


## Memo

### コンテナの削除方法

以下のコマンドで、すべてのコンテナ、ボリューム、ネットワークを削除します。
```
docker container rm -f $(docker container list -aq) && docker volume rm -f $(docker volume list -q) && docker network rm $(docker network list -q)
```
