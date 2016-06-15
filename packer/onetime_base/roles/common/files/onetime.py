# -*- encoding:utf-8 -*-

import urllib2
import os.path
import boto3

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def get_instance_id():
    response = urllib2.urlopen("http://169.254.169.254/latest/meta-data/instance-id")
    return response.read()


if __name__ == "__main__":
    print(get_instance_id())
