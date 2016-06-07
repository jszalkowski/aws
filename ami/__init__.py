# -*- encoding:utf-8 -*-

from fabric.api import task, lcd, local

import os.path

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIRECTORY = os.path.abspath(CURRENT_DIRECTORY + "/../templates")


@task
def create_project(project):
    """AMIを生成するためのプロジェクトを生成"""
    with lcd(CURRENT_DIRECTORY):
        local("cp -r {0}/_ami_template {1}".format(TEMPLATES_DIRECTORY, project))


@task
def create_ansible_role_to_project(project):
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

    with lcd(work_dir):
        local("packer build -var-file=packer_variables.json packer.json")
