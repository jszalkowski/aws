# -*- encoding:utf-8 -*-

from fabric.api import task

import os.path
import cli

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


@task
def tf_plan(domain):
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, domain)
    tf_s3_key = "terraform/{0}/terraform.tfstate".format(domain)

    cli.tf_plan(work_dir, tf_s3_key=tf_s3_key)


@task
def tf_apply(domain):
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, domain)
    tf_s3_key = "terraform/{0}/terraform.tfstate".format(domain)

    cli.tf_apply(work_dir, tf_s3_key=tf_s3_key)


@task
def tf_destroy(domain):
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, domain)
    tf_s3_key = "terraform/{0}/terraform.tfstate".format(domain)

    cli.tf_destroy(work_dir, tf_s3_key=tf_s3_key)


@task
def tf_plan_destroy(domain):
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, domain)
    tf_s3_key = "terraform/{0}/terraform.tfstate".format(domain)

    cli.tf_plan_destroy(work_dir, tf_s3_key=tf_s3_key)
