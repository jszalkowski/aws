# -*- encoding:utf-8 -*-

from fabric.api import task, lcd, local

import os.path
import boto3

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

S3_BUCKET = "kajip-private"
S3_KEY_PREFIX = "lambda"

s3 = boto3.resource("s3")


@task
def upload(domain):
    """Lambda FunctionをS3にアップロード"""
    work_dir = "{0}/{1}".format(CURRENT_DIRECTORY, domain)
    dist_dir = "{0}/_dist".format(CURRENT_DIRECTORY)
    dist_file = "{0}/{1}.zip".format(dist_dir, domain)
    lambda_s3_key = "{0}/{1}.zip".format(S3_KEY_PREFIX, domain)

    with lcd(work_dir):
        local("zip -r {0}/{1} * -x *.pyc .DS_Store".format(dist_dir, domain))
    s3.meta.client.upload_file(dist_file, S3_BUCKET, lambda_s3_key)
