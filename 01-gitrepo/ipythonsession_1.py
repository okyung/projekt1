# coding: utf-8
import boto3
session =boto3.Session(profile_name='admin''-)
get_ipython().run_line_magic('cd', '~/code/projekt1/cd ~/code/projekt1/cd ~/code/projekt1/cd ~/code/projekt1/')
session =boto3.Session (profile_name='admin')
s3 = session.resource('s3')
new_bucket =s3.create_bucket(Bucket='projekt-dez2021')
new_bucket =s3.create_bucket(Bucket='projekt-dez2021',CreateBucketConfiguration ={
        'LocationConstraint': 'us-east2'} )
for bucket in s3.buckets.all():
    print(bucket)

ec2_client =session.client ('ec2')
ec2_client.allocate_address
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipythonsession.py 1-20')
