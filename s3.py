import boto3
from botocore.client import Config


#active resource
s3 = boto3.resource('s3')
#print bucket name 
for bucket in s3.buckets.all():
    print(bucket.name)

#AWS CLI locally configured
#ACCESS_KEY_ID = ''
#ACCESS_SECRET_KEY = ''

BUCKET_NAME = input('Enter the bucket name you want to upload ')
#defining the date which needs to upload
data = open('', 'rb')
s3.Bucket(BUCKET_NAME).put_object(Key='bitmoji.png', Body=data)

print ("Done")




