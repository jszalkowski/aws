# AMI 生成プロジェクト

EC2インスタンスを起動するための AMIファイルの生成と構成管理のプロジェクト。
Packer と Ansible を利用しています。

## 使い方

### 1. packer_variables.yml ファイルの修正
packer_variables.yml にプロジェクト固有のパラメータをYMLフォーマットで追加します。
このファイルと親ディレクトリにある aws_credentials.yml ファイルから packer_variables.json ファイルを生成します。

### 2. fabric で AMI を生成
fabric の "images.create_ami" タスクを実行します。

```
$ fab images.create_ami:<プロジェクト名>
```
