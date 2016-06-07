# AMI 生成プロジェクト

EC2インスタンスを起動するための AMIファイルの生成と構成管理のプロジェクト。
Packer と Ansible を利用しています。

## 使い方

### 1. packer_variables.json ファイルの作成
packer_variables.json.tmpl を packer_variables.json にリネームし、内容を修正します。
主にAWSにアクセスする際の access_key、secret_key を指定します。

このファイルは、.gitignoreファイルでバージョン管理の対象外に指定されています。

### 2. fabric で AMI を生成
fabric の "images.create_ami" タスクを実行します。

```
$ fab images.create_ami:<プロジェクト名>
```
