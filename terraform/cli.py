# -*- encoding:utf-8 -*-

from fabric.api import lcd, local

TF_AWS_REGION = "ap-northeast-1"
TF_S3_BUCKET = "kajip-private"
TF_S3_KEY = "terraform/bootstrap/terraform.tfstate"


def tf_plan(work_dir, tf_aws_region=TF_AWS_REGION, tf_s3_bucket=TF_S3_BUCKET, tf_s3_key=TF_S3_KEY):
    _call_terraform("terraform plan", work_dir, tf_aws_region, tf_s3_bucket, tf_s3_key)


def tf_plan_destroy(work_dir, tf_aws_region=TF_AWS_REGION, tf_s3_bucket=TF_S3_BUCKET, tf_s3_key=TF_S3_KEY):
    _call_terraform("terraform plan -destroy", work_dir, tf_aws_region, tf_s3_bucket, tf_s3_key)


def tf_apply(work_dir, tf_aws_region=TF_AWS_REGION, tf_s3_bucket=TF_S3_BUCKET, tf_s3_key=TF_S3_KEY):
    _call_terraform("terraform apply", work_dir, tf_aws_region, tf_s3_bucket, tf_s3_key)


def tf_destroy(work_dir, tf_aws_region=TF_AWS_REGION, tf_s3_bucket=TF_S3_BUCKET, tf_s3_key=TF_S3_KEY):
    _call_terraform("terraform destroy", work_dir, tf_aws_region, tf_s3_bucket, tf_s3_key)


def _call_terraform(command, work_dir, tf_aws_region, tf_s3_bucket, tf_s3_key):
    with lcd(work_dir):
        __remote_config(tf_aws_region, tf_s3_bucket, tf_s3_key)
        local("terraform remote pull")
        local(command)
        local("terraform remote push")


def __remote_config(tf_aws_region, tf_s3_bucket, tf_s3_key):
    local(
        "terraform remote config -backend=s3 -backend-config=\"region={0}\" -backend-config=bucket=\"{1}\" -backend-config=\"key={2}\""
            .format(tf_aws_region, tf_s3_bucket, tf_s3_key))
