# API连接信息

Endpoint :  http://xls3.xxxx.com

AccessKeyId :  NGAA-xxxx

SecretAccessKey:  ******  

为安全 单独咨询技术支持提供

# SDK

Python版本 python 2.7.x

Aws client sdk：https://github.com/boto/boto3

使用说明：https://ecloud.10086.cn/op-help-center/develop/S3%20Python%20SDK.pdf

# 桶容量查询

## 请求地址

http://[hostAddress]/action/api/v3/getBucketUsed
## 接口描述

查询对象存储桶已用大小
## 请求参数

bucketName	String	否	桶名称
## 返回参数

buketName	String	桶名称
usedSize	long	已用大小（单位:byte）
## 返回样例

{

    "requestId": "d82790a3-ed25-476f-9137-c029edd29abc",

    "httpCode": "200",
    
    "code": "Success",
    
    "message": "Success",
    
    "totalCount": 2,
    
    "data": [
    
        {
        
            "bucketName": "test-jz7mx9qr",
            
            "usedSize": 6072304
        
        },
        
        {
        
             "bucketName": "test2-jz7mx9qr",
            
            "usedSize": 6904386
        
        }
    
    ]

}

# 标准aws3接口支持清单

使用样例参见SDK python对应的样例
## ListBuckets
## CreateBucket
## DeleteBucket
## GetObject
## ListObjects
## PutObject
## DeleteObject
## DeleteObjects

# Python版本 aws3接口样例

参见本目录下的样例文件aws3_visit.py

