# -*- encoding:utf-8 -*-

from fabric.api import task, lcd, local

import os.path
import yaml
import json

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIRECTORY = os.path.abspath(CURRENT_DIRECTORY + "/../templates")


@task
def create_project(project):
    """AMIを生成するためのプロジェクトを生成"""
    with lcd(CURRENT_DIRECTORY):
        local("cp -r {0}/_ami_template {1}".format(TEMPLATES_DIRECTORY, project))


@task
def create_ansible_role_to_project(project, role):
    """プロジェクトに新規の個別 Ansible Roleを追加する"""
    print "TODO"


@task
def add_ansible_common_role_to_project(project):
    """プロジェクトに共通 Ansible Roleを追加する"""
    print "TODO"


@task
def create_ami(project):
    """Packerを利用してAMIを生成"""
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, project)

    __create_packer_variables(project)
    with lcd(work_dir):
        local("packer build -var-file=packer_variables.json packer.json")


def __create_packer_variables(project):
    """Packerの設定ファイルを生成"""
    variables = __load_credential_variables()
    variables.update(__load_local_variables(project))
    __save_variables(project, variables)


def __load_credential_variables():
    """AWSのCredential情報をロード"""
    with open("{0}/aws_credentials.yml".format(CURRENT_DIRECTORY), "r") as f:
        return yaml.load(f)


def __load_local_variables(project):
    """プロジェクト固有パラメータをロード"""
    with open("{0}/{1}/packer_variables.yml".format(CURRENT_DIRECTORY, project), "r") as f:
        return yaml.load(f)


def __save_variables(project, variables):
    """AWSのCredential情報をロード"""
    with open("{0}/{1}/packer_variables.json".format(CURRENT_DIRECTORY, project), "w") as f:
        return f.write(json.dumps(variables, indent=2))
