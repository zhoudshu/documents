#!/usr/bin/python
# -*- coding: UTF-8 -*-

#xl store object example list

from boto3.session import Session
from botocore.exceptions import ClientError
import boto3

access_key = "NGAA-iqiyi"
secret_key = "xxxxx"
url = "http://xls3.zhoudsh.com"

session = Session(access_key, secret_key)
s3_client = session.client('s3', endpoint_url=url)

print("test list buckets function")
buckets = s3_client.list_buckets()['Buckets']
for bucket in buckets:
    print(bucket)

print("test make buckets function")
# create_bucket function use Bucket paramemeter which is bucket prefix to create bucket object
# you can call list_buckets to find the actual bucket name
# for example bucket prefex : the full bucket ( mybucket : mybucket-ve7vd67p )
try:
    s3_client.create_bucket(Bucket="mybucket")
except ClientError as err:
    print(err)

print("test put local small object function")
# Put an object 'myobject' with contents from '/tmp/otherobject', upon success prints the etag identifier computed by server.
try:
    print(s3_client.put_object(Bucket='mybucket-ve7vd67p', Key='myobject', Body=open('/tmp/myobject','rb').read()))
except ClientError as err:
    print(err)

## Put on object 'myobject.csv' with contents from
# '/tmp/otherobject.csv' as 'application/csv'.
#try:
#    print(s3_client.put_object(Bucket='mybucket-ve7vd67p',Key='myobject.csv',
#                             Body=open('/tmp/myobject.csv', 'rb').read()
#                             ))
#except ClientError as err:
#    print(err)

print("test put local big object function")
#multi part upload example
try:
    mpu = s3_client.create_multipart_upload(Bucket='mybucket-ve7vd67p',Key="myobject.csv")
    part_info = {'Parts': [] }
    i=1
    filefd = open('/tmp/myobject.csv','rb')
    while 1:
         data = filefd.read(10 * 1024 * 1024)
         if data == b'':
           break

         response = s3_client.upload_part(Bucket='mybucket-ve7vd67p',
                   Key="myobject.csv", PartNumber=i, UploadId=mpu["UploadId"],Body=data)
         part_info['Parts'].append({
             'PartNumber': i,
             'ETag': response['ETag']
         })
         i += 1
    s3_client.complete_multipart_upload(Bucket="mybucket-ve7vd67p", Key="myobject.csv",UploadId=mpu["UploadId"],MultipartUpload=part_info)

except ClientError as err:
    print(err)

print("test get objects function")
## Get a full object and prints the original object stat information.
try:
     resp = s3_client.get_object(Bucket='mybucket-ve7vd67p', Key='myobject')
     with open('/tmp//otherobject','wb') as f:
        f.write(resp['Body'].read())
except ClientError as err:
    print(err)

print("test list objects function")
resp = s3_client.list_objects(Bucket='mybucket-ve7vd67p')
#print(resp)
for obj in resp['Contents']:
    print(obj)

print("test remove objects function")
try:
    s3_client.delete_object(Bucket='mybucket-ve7vd67p', Key='myobject')
    s3_client.delete_object(Bucket='mybucket-ve7vd67p', Key='myobject.csv')
except ResponseError as err:
    print(err)

print("test delete buckets function")
try:
    s3_client.delete_bucket(Bucket="mybucket-ve7vd67p")
except ClientError as err:
print(err)
