# -*- encoding:utf-8 -*-

import json
import boto3


def handler(event, context):
    """EC2 インスタンスを起動"""

    ec2 = boto3.client('ec2')
    instance = ec2.run_instances(
        ImageId=event['ami_id'],
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='kajip',
        SecurityGroupIds=event['security_groups'],
        InstanceInitiatedShutdownBehavior='terminate',
        IamInstanceProfile={
            'Name': 'ec2-admin-profile'
        },
        #        UserData='string',
    )

    print(instance)
    return instance[u'Instances'][0][u'InstanceId']
