

import boto3



#active resource
s3 = boto3.resource('s3')
#print bucket name 
for bucket in s3.buckets.all():
    print(bucket.name)
#AWS CLI locally configured
    #ACCESS_KEY_ID = ''
    #ACCESS_SECRET_KEY = ''
#define the bucket where you want to upload your data
BUCKET_NAME = 'ronycfd'
#BUCKET_NAME = input('Enter the bucket name you want to upload ')
#defining the date which needs to upload
data = open('testrony.txt', 'rb')
s3.Bucket(BUCKET_NAME).put_object(Key='testrony.txt', Body=data)
#s3.meta.client.upload_file( 'testrony.txt',ronycfd, 'testrony.txt')
print ("-----------------Done------------------")




