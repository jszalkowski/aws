# -*- encoding:utf-8 -*-

from fabric.api import task, lcd, local

import os.path
import cli

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIRECTORY = os.path.abspath(CURRENT_DIRECTORY + "/../templates")


@task
def create_domain(domain):
    """terraformの新規ドメインを生成"""
    with lcd(CURRENT_DIRECTORY):
        local("cp -r {0}/_terraform {1}".format(TEMPLATES_DIRECTORY, domain))


@task
def tf_plan(domain):
    """ドメインに対して terraform plan コマンドを実行"""
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, domain)
    tf_s3_key = "terraform/{0}/terraform.tfstate".format(domain)

    cli.tf_plan(work_dir, tf_s3_key=tf_s3_key)


@task
def tf_apply(domain):
    """ドメインに対して terraform apply コマンドを実行"""
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, domain)
    tf_s3_key = "terraform/{0}/terraform.tfstate".format(domain)

    cli.tf_apply(work_dir, tf_s3_key=tf_s3_key)


@task
def tf_destroy(domain):
    """ドメインに対して terraform destroy コマンドを実行"""
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, domain)
    tf_s3_key = "terraform/{0}/terraform.tfstate".format(domain)

    cli.tf_destroy(work_dir, tf_s3_key=tf_s3_key)


@task
def tf_plan_destroy(domain):
    """ドメインに対して terraform plan -destroy コマンドを実行"""
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, domain)
    tf_s3_key = "terraform/{0}/terraform.tfstate".format(domain)

    cli.tf_plan_destroy(work_dir, tf_s3_key=tf_s3_key)
