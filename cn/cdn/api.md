# API接口概览
对系统提供的API接口进行说明，供其它业务系统集成调用

此类接口为当前稳定的版本，推荐大家使用

## 域名管理接口列表-V3版本

| 接口名称     | 接口功能     | 备注                           |
| -------- | ------ | ---------------------------------------- |
| AddCdnDomain  | 添加加速域名 | [访问](#添加加速域名) |
| StopCdnDomain | 关闭加速域名 | [访问](#关闭加速域名) |
| StartCdnDomain | 启动加速域名 | [访问](#启动加速域名) |
| DeleteCdnDomain | 删除加速域名 | [访问](#删除加速域名) |
| GetCdnDomainList | 获取加速域名列表 | [访问](#获取加速域名列表) |
| GetCdnDomain | 获取加速域名配置 | [访问](#获取加速域名配置) |

## 缓存配置管理接口列表-V3版本
| 接口名称     | 接口功能     | 备注                           |
| -------- | ------ | ---------------------------------------- |
| EditOriginConfig | 修改源站配置 | [访问](#修改源站配置) |
| DeleteOriginConfig | 删除源站配置 | [访问](#删除源站配置) |
| SetRefer | 防盗链设置 | [访问](#防盗链设置) |
| DeleteRefer |删除防盗链 | [访问](#删除防盗链) |
| SetCacheConfig | 缓存设置 | [访问](#缓存设置) |
| EditCacheConfig | 修改缓存设置 | [访问](#修改缓存设置) |
| DeleteCacheConfig | 删除缓存设置 | [访问](#删除缓存设置) |
| SetHttpHeaderConfig | HttpHeader设置 | [访问](#HttpHeader设置) |
| EditHttpHeaderConfig | 修改HttpHeader | [访问](#修改HttpHeader) |
| DeleteHttpHeaderConfig | 删除HttpHeader | [访问](#删除HttpHeader) |
| SetHttpsInfo | Https证书设置 | [访问](#Https证书设置) |
| DeleteHttpsInfo | 删除Https证书 | [访问](#删除Https证书) |

## 刷新预热接口列表-V3版本

| 接口名称     | 接口功能     | 备注                           |
| -------- | ------ | ---------------------------------------- |
| CreateRefreshTask | 缓存批量刷新 | [访问](#缓存批量刷新) |
| DescribeRefreshTask | 刷新任务结果查询 | [访问](#刷新任务结果查询) |
| createPreload | 缓存预热 | [访问](#缓存预热) |
| preloadQuery | 预热任务查询 | [访问](#预热任务查询) |

## 数据查询接口列表-V3版本

| 接口名称     | 接口功能     | 备注                           |
| -------- | ------ | ---------------------------------------- |
| DescribeCacheHitFlux | 命中流量统计 | [访问](#命中流量统计) |
| DescribeCacheHitNum | 命中请求数统计 | [访问](#命中请求数统计) |
| DescribeHttpCode | 状态码请求数统计 | [访问](#状态码请求数统计) |
| DescribeBandwidth | 带宽统计 | [访问](#带宽统计) |
| DescribeFlux | 流量统计 | [访问](#流量统计) |
| DescribeOriginBandwidth |回源带宽统计 | [访问](#回源带宽统计) |
| DescribeOriginFlux | 回源流量统计 | [访问](#回源流量统计) |
| DescribeVisitor | 请求数统计 | [访问](#请求数统计) |

## 辅助工具列表-V3版本

| 接口名称     | 接口功能     | 备注                           |
| -------- | ------ | ---------------------------------------- |
| DescribeDownloadLog | 日志下载 | [访问](#日志下载) |
| queryCdnIp | IP归属查询 | [访问](#IP归属查询) |

# 调用方式-V3版本
## 请求结构

### 服务地址
服务入口地址为：http://[hostAddress]/ccsp/action/api/v3/Action

注：Action为请求操作的功能名称，内容按各接口实际情况替换。

### 通信协议
支持通过 HTTP 通道进行请求通信。

### 请求方法
支持HTTP GET和POST方法发送请求，GET请求时，请求参数需要全部包含在请求的URL路径中。

### 字符编码
请求及返回结果请使用 UTF-8 字符集进行编码。

注意：编码时空格要转换成 “%20” , 而不是 “+”。

### 公共请求参数

公共请求参数是每个接口都需要使用到的请求参数，如非必要, 在各个接口单独的文档中不再对这些参数进行说明.

公共请求参数具体列表如下：

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| accessKeyId | String | 是 | 访问服务的身份标识 |
| signature   | String | 是 | 签名字符串，关于签名的计算方法，请参见签名机制小节 |
| timestamp   | Long   | 是 | 请求的时间戳，从格林威治时间1970年01月01日00时00分00秒起至现在的总毫秒数。|

### 签名机制

API接口服务会对每个访问的请求进行身份验证，所以每次提交请求，都需要在请求中包含签名（signature）信息。服务端通过使用 accessKeyId和 secretKey 进行对称加密的方法来验证请求的发送者身份。

accessKeyId和secretKey在统创建系用户时，自动生成。其中 accessKeyId用于标识访问者的身份；secretKey是用于加密签名字符串和服务器端验证签名字符串的密钥，必须严格保密，只有用户自己知道。

用户在访问时，按照下面的方法对请求进行签名处理：

```
signature=hmacsha1((accessKeyId+”\n”+timestamp).getBytes(),secureKey. getBytes())；

import java.security.MessageDigest;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
String hmacsha1(byte[] data, byte[] key) {
SecretKeySpec signingKey = new SecretKeySpec(key, “HmacSHA1”);
Mac mac = Mac.getInstance(HMAC_SHA1);
mac.init(signingKey);
byte[] rawHmac = mac.doFinal(data);
return org.apache.commons.codec.binary.Base64.encodeBase64String(rawHmac);
}

```

注意：“\n” 是换行符，不要将 “\” 转义。也就是说，不要用 “\\n”。

### 请求样例

http://[hostAddress]/ccsp/action/api/v3/Action?xxx&accessKeyId=xxx&timestamp=xxx&signature=xxx&参数1=XXX&参数2=xxx&...参数n=xxx

## 应答结构
### 数据格式
所有API接口，返回数据格式为标准JSON格式。

### 公共应答参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| requestId | String | 是 | 用户每次请求返回对应的唯一标识 |
| httpCode  | String | 是 | HTTP状态码，描述一次请求对应的HTTP状态。|
| code | String | 是 | 本次请求服务执行状态码，具体内容，详见返回状态码小节。|
| message | String | 是 | 本次请求的描述信息。|
| totalCount | int | 否 | 查询结果总数（查询类接口用于客户端分页用）|
| data | List<Object> | 否 | 返回的数据实体对象集合 |

### 应答样例
#### 成功样例

```
{
"requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
"httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": [
        {
		/*具体的接口返回内容*/
        }
    ]
}
```

#### 失败样例
```
{
 "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
 "httpCode": "400",
 "code": " Missing.Parameter",
 "message": "The request parameter is miss.password",
 "data": [
        {
        }
    ]
}
```

### 返回状态码

API有完善的错误码机制，API调用失败会返回响应的Http码、错误码以及错误描述。
Http码为4XX的是客户端错误，建议用户根据错误描述，修正请求后重新提交。
Http码为5XX的是服务内部错误，此时建议重试。

#### 公共HTTP状态码

| httpCode        |  描述                            |
| --------- | ------ |
| 200  | 成功 |
| 400  | 缺少参数或参数无效 |
| 401  | 鉴权错误 |
| 403  | 没有权限 |
| 500  | 服务内部错误 |

#### 公共CODE状态码
| code      |  描述                                  |
| --------- | ------ |
| Invalid.Paramater | 无效的参数，一般为参数格式错误 |
| Missing.Parameter | 缺少参数。|
| Forbidden.[XXX] | 鉴权错误，一般为没有权限|
| Internal.Error | 服务内部错误 |
| Success | 成功 |

# 支持接口列表
## 域名管理接口列表
### 添加加速域名
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/AddCdnDomain

#### 接口描述
添加加速域名

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 域名（要求必须通过工信部备案）|
| origin | String | 是 | 源站设置，支持配置一个域名或多个源站IP,多源站IP地址间以;分隔，端口可配置区间 0 ~ 65535。域名模式：www.xxx.com:8080 IP模式：61.1.1.1:8080;62.2.2.2:8080 |
| icpNumber | String | 是 | 域名备案号 |
| serviceType |  String |否| 服务类型，为空时默认静态加速。web：静态加速 download：下载加速 video：视频加速|

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 关闭加速域名
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/StopCdnDomain

#### 接口描述
关闭加速域名。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 域名（要求必须通过工信部备案）|

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 启动加速域名
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/StartCdnDomain

#### 接口描述
启动加速域名。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 域名（要求必须通过工信部备案）|

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 删除加速域名
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DeleteCdnDomain

#### 接口描述
删除加速域名

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 域名（要求必须通过工信部备案）|

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 获取加速域名列表
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/GetCdnDomainList

#### 接口描述
获取所有加速域名列表。

#### 请求参数

参见公共请求参数

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Item> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| id | Long | - | 加速域名数据唯一标识 |
| domainName | String | - | 加速域名 |
| icpNumber | String | - | 域名备案号 |
| status | String | - | 加速域名状态，online：已启动 deploying：部署中 deployfailed：部署失败 offline：已关闭 |
| serviceType | String | - | 服务类型 web：静态加速 download：下载加速 video：视频加速 |
| cname | String | - | CDN分配的后辍加速域名 |
| createTime | Date | - | 创建时间,格式yyyy-MM-dd HH:mm:ss |

#### 返回样例

```
{
    "requestId": "123d4387-15cb-4e3f-8c14-a90ca5137c31",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 2,
    "data": [
        {
            "id": 1,
            "domainName": "xx.ngaa.com.cn",
            "icpNumber": "1232222111",
            "status": "deploying",
            "serviceType": "web",
            "cname": "xx.ngaa.com.cn.ngaagslb.cn",
            "createTime": "2017-07-04 08:21:37"
        },
        {
            "id": 2,
            "domainName": "www.xx.zhoufengjie.cn",
            "icpNumber": "IC1B1",
            "status": "deploying",
            "serviceType": "download",
            "cname": "www.xx.zhoufengjie.cn.ngaagslb.cn",
            "createTime": "2018-03-15 05:44:05"
        }
    ]
}
```

### 获取加速域名配置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/GetCdnDomain

#### 接口描述
获取加速域名配置

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainId | Long | 否 | 加速域名唯一标识，domainName为空时，此值不能为空。|
| domainName | String | 否 | 加速域名，domainId为空时，此值不能为空。|


#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Item> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| domainId | Long | - | 加速域名数据唯一标识 |
| domainName | String | - | 加速域名 |
| icpNumber | String | - | 域名备案号 |
| status | String | - | 加速域名状态，online：已启动 deploying：部署中 deployfailed：部署失败 offline：已关闭 |
| serviceType | String | - | 服务类型 web：静态加速 download：下载加速 video：视频加速 |
| cname | String | - | CDN分配的后辍加速域名 |
| createTime | Date | - | 创建时间,格式yyyy-MM-dd HH:mm:ss |
| refer | Refer | - | 防盗链信息，详见【Refer】描述 |
| headers | List<HeaderItem> | - | Header信息集合，详见【HeaderItem】描述 |
| caches | List<CacheItem> | - | 缓存信息集合，详见【CacheItem】描述 |
| origins | List<OriginItem> | - | 源站信息集合，详见【OriginItem】描述 |
| cert | Cert | - | 证书信息对象，详见【Cert】描述 |


【Refer】
| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| refChain | String | - | 防盗链类型 onVisit：白名单 offVisit：黑名单|
| refName | String | - | 防盗链内容，域名或IP |
| refInclude | String | - | 是否包含空Refer 0：不包含 1：包含 |

【HeaderItem】
| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| headerId | Long | - | Header数据唯一标识 |
| headerKey | String | - | Header Key仅支持  Content-Disposition Content-Language  Access-Control-Allow-Origin  Access-Control-Allow-Methods  Access-Control-Max-Age |
| headerValue | String | - | 值。当headerKey设置为“Access-Control-Allow-Origin”时，值仅能设置为 * ，或者一个域名（需要以http:// 或https://开头）|

【CacheItem】
| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| cacheId | Long | - | 缓存数据唯一标识 |
| rType | String | - | 缓存类型 1：文件 2：目录|
| tSuffix | String | - | 内容 |
| cacheTime | Integer | - | 缓存时间 |
| timeUnit | String | - | 缓存时间单位 second：秒 day：天 minute：分 hour：小时 |

【OriginItem】
| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| originId | Long | - | 源站数据唯一标识 |
| address | String | - | 源站地址（IP或域名）|
| port | Integer | - | 源站端口 |

【Cert】
| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| certId | Long | - | 证书数据唯一标识 |
| createTime | Date | - | 证书创建时间，格式yyyy-MM-dd HH:mm:ss |
| validTime | Date | - | 证书生效时间，格式yyyy-MM-dd HH:mm:ss |

#### 返回样例

```
{
    "requestId": "c835098b-1ee5-4235-a1c1-e4897079e010",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 1,
    "data": [
        {
            "domainId": 1,
            "domainName": "www.xx.zhoufengjie.cn",
            "icpNumber": "1113312222",
            "serviceType": "web",
            "cname": "www.xx.zhoufengjie.cn.org.net",
            "status": "deploying",
            "createTime": "2017-07-04 08:21:37",
            "refer": {
                "refChain": "onVisit",
                "refName": "aaaa.com",
                "refInclude": "0"
            },
            "header": [
                {
                    "headerId": 1,
                    "headerKey": "Content-Language",
                    "headerValue": "CN"
                },
                {
                    "headerId": 2,
                    "headerKey": "Access-Control-Allow-Origin",
                    "headerValue": "http://1.com"
                }
            ],
            "cache": [
                {
                    "cacheId": 1,
                    "rType": "1",
                    "tSuffix": "mp3/mp4",
                    "cacheTime": "1",
                    "timeUnit": "day"
                },
                {
                    "cacheId": 2,
                    "rType": "1",
                    "tSuffix": "html",
                    "cacheTime": "10",
                    "timeUnit": "day"
                },
            ],
            "origins": [
                {
                    "originId": 1,
                    "address": "61.10.100.1",
                    "port": "80"
                }
            ]
        }
    ]
}
```


## 缓存配置管理接口列表
### 修改源站配置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/EditOriginConfig

#### 接口描述

修改加速域名源站配置。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 域名（要求必须通过工信部备案）|
| origin | String | 是 | 源站设置，支持配置一个域名或多个源站IP,多源站IP地址间以;分隔，端口可配置区间 0 ~ 65535。域名模式：www.xxx.com:8080 IP模式：61.1.1.1:8080;62.2.2.2:8080 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 删除源站配置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DeleteOriginConfig

#### 接口描述

删除加速域名源站配置。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| originId | Long | 是 | 源站数据唯一标识 |
| domainName | String | 是 | 域名（要求必须通过工信部备案）|

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 防盗链设置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/SetRefer

#### 接口描述

设置加速域名防盗链。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainId | Long | 否 |  加速域名唯一标识，domainName为空时，此值不能为空。|
| domainName | String | 否 | 加速域名，domainId为空时，此值不能为空。|
| refChain | String | 是 | 防盗链类型 onVisit：白名单 offVisit：黑名单|
| refName | String | 是 | 防盗链内容，域名或IP |
| refInclude | Integer | 是 | 是否包含空Refer 0：不包含 1：包含 |


#### 返回参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 删除防盗链
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DeleteRefer

#### 接口描述

删除防盗链

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainId | Long | 否 |  加速域名唯一标识，domainName为空时，此值不能为空。|
| domainName | String | 否 | 加速域名，domainId为空时，此值不能为空。|


#### 返回参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 缓存设置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/SetCacheConfig

#### 接口描述

设置加速域名缓存。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainId | Long | 否 |  加速域名唯一标识，domainName为空时，此值不能为空。|
| domainName | String | 否 | 加速域名，domainId为空时，此值不能为空。|
| rType | String | 是 | 缓存类型 1：文件 2：目录|
| tSuffix | String | 是 | 内容 |
| cacheTime | Integer | 是 | 缓存时间 |
| timeUnit | String | 是 | 缓存时间单位 second：秒 day：天 minute：分 hour：小时 |


#### 返回参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 修改缓存设置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/EditCacheConfig

#### 接口描述

修改加速域名缓存。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainId | Long | 否 |  加速域名唯一标识，domainName为空时，此值不能为空。|
| domainName | String | 否 | 加速域名，domainId为空时，此值不能为空。|
| cacheId | Long | 是 | 缓存数据唯一标识 |
| rType | String | 是 | 缓存类型 1：文件 2：目录|
| tSuffix | String | 是 | 内容 |
| cacheTime | Integer | 是 | 缓存时间 |
| timeUnit | String | 是 | 缓存时间单位 second：秒 day：天 minute：分 hour：小时 |


#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```


### 删除缓存设置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DeleteCacheConfig

#### 接口描述

删除加速域名缓存。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainId | Long | 否 |  加速域名唯一标识，domainName为空时，此值不能为空。|
| domainName | String | 否 | 加速域名，domainId为空时，此值不能为空。|
| cacheId | Long | 是 | 缓存数据唯一标识 |


#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### HttpHeader设置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/SetHttpHeaderConfig

#### 接口描述

设置加速域名HttpHeader。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 加速域名，domainId为空时，此值不能为空。|
| headerKey | String | 是 |Header Key仅支持 Content-Disposition  Content-Language  Access-Control-Allow-Origin Access-Control-Allow-Methods Access-Control-Max-Age |
| headerValue | String | 是 | 值。当headerKey设置为“Access-Control-Allow-Origin”时，值仅能设置为 * ，或者一个域名（需要以http:// 或https://开头）|

#### 返回参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 修改HttpHeader
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/EditHttpHeaderConfig

#### 接口描述

修改加速域名HttpHeader。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 加速域名，domainId为空时，此值不能为空。|
| configId | Long | 是 | Header数据唯一标识 |
| headerKey | String | 是 | Header Key仅支持  Content-Disposition Content-Language  Access-Control-Allow-Origin Access-Control-Allow-Methods Access-Control-Max-Age |
| headerValue | String | 是 | 值。当headerKey设置为“Access-Control-Allow-Origin”时，值仅能设置为 * ，或者一个域名（需要以http:// 或https://开头）|

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```


### 删除HttpHeader
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DeleteHttpHeaderConfig

#### 接口描述

删除加速域名HttpHeader。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 加速域名 |
| configId | Long | 是 | httpHeader数据唯一标识 |


#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```


### Https证书设置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/SetHttpsInfo

#### 接口描述

设置加速域名Https证书。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 加速域名，domainId为空时，此值不能为空。|
| privateKey | String | 是 | 私钥 |
| cert | String | 是 | 证书 |
| httpsType | Integer | 是 | 配置类型 1：http 回源 2：协议跟随回源 |

#### 返回参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 删除Https证书
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DeleteHttpsInfo

#### 接口描述

删除加速域名Https证书。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainName | String | 是 | 加速域名 |


#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

/****
### IP黑白名单设置
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/SetAccessIp

#### 接口描述

设置IP黑白名单。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainId | Long | 否 |  加速域名唯一标识，domainName为空时，此值不能为空。|
| domainName | String | 否 | 加速域名，domainId为空时，此值不能为空。|
| ipAccRest | String | 是 | 类型 onVisit：白名单 offVisit：黑名单 |
| ipAccRestContent | String | 是 | IP黑白名单内容，多个IP使用逗号连接 |

#### 返回参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```

### 删除IP黑白名单
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DeleteAccessIp

#### 接口描述

删除IP黑白名单。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domainId | Long | 否 |  加速域名唯一标识，domainName为空时，此值不能为空。|
| domainName | String | 否 | 加速域名，domainId为空时，此值不能为空。|

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 返回的数据实体对象集合 此接口为空数组对象 |


#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": []
}
```
****/


## 刷新预热接口列表
### 缓存批量刷新
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/CreateRefreshTask

#### 接口描述

创建Cache缓存刷新任务，支持批量URL刷新和目录刷新。每次任务创建成功后返回本次任务标识和提交失败的URL数据。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| url | String | 是 | URL列表，支持多URL，以英文逗号”,”分隔，刷新任务单次最多支持1000个URL，目录方式刷新任务时，限制每天只能刷新100个目录 |
| taskType | int | 是 | 任务刷新方式，0:URL刷新；1：目录刷新 |

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | Object | - | 返回的数据实体对象  |
| taskId | String | - | 任务标识 |
| failUrl | String  | - | 不合法的URL列表，以英文逗号”,”分隔 |


#### 返回样例

```
{
    "requestId": "f2c84d9a-aa0d-487e-8a5d-24f93cd7d258",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 1,
    "data": [
        {
            "taskId": "148237248263205634",
            "failUrl": "http://xxx/3.jpg,http://xxx/2.jpg"
        }
    ]
}
```

### 刷新任务结果查询
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeRefreshTask

#### 接口描述

查询Cache缓存刷新任务结果。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| taskId | String | 是 | 任务标识 |
| url | String | 否 | URL |

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | Object | - | 返回的数据实体对象  |
| taskId | String | - | 任务标识 |
| url | String | 否 | URL |
| status | int | 否 | 状态，0：等待中；1：处理中；2：成功；3：失败 |
| taskType | int | 否 |  任务刷新方式，0:URL刷新；1：目录刷新 |

#### 返回样例

```
{
    "requestId": "48e7ca59-7a54-48a9-a597-4bf96bea582a",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 3,
    "data": [
        {
            "taskId": "148237143539484309",
            "url": "http://www.zhouds.cn/3.jpg",
            "status": 3,
            "taskType": 0
        },
        {
            "taskId": "148237143539484309",
            "url": "http://www.zhouds.cn/2.jpg",
            "status": 3,
            "taskType": 0
        },
        {
            "taskId": "148237143539484309",
            "url": "http://www.zhouds.cn/1.jpg",
            "status": 3,
            "taskType": 0
        }
    ]
}
```

### 缓存预热
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/createPreload

#### 接口描述

创建Cache缓存预热任务，支持批量URL预热。每次任务创建成功后返回本次任务标识和失败描述。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| publishUrls | String | 是 | URL列表，支持多URL，以英文逗号”,”分隔，预热任务单次最多支持100个URL |

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | Object | - | 返回的数据实体对象  |
| taskId | String | - | 任务标识 |
| msg | String  | - | 失败描述 |


#### 返回样例

```
{
    "requestId": "f2c84d9a-aa0d-487e-8a5d-24f93cd7d258",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 1,
    "data": [
        {
            "taskId": "148237248263205634",
            "msg": "http://xxx/3.jpg,http://xxx/2.jpg"
        }
    ]
}
```

### 预热任务查询
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/preloadQuery

#### 接口描述

查询Cache缓存预热任务结果。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| taskId | String | 是 | 任务标识 |

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | Object | - | 返回的数据实体对象  |
| taskId | String | - | 任务标识 |
| status | int | 否 | 状态，0：等待中；1：处理中；2：成功；3：失败 |
| msg | String  | - | 失败描述 |

#### 返回样例

```
{
    "requestId": "48e7ca59-7a54-48a9-a597-4bf96bea582a",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 1,
    "data": [
        {
            "taskId": "148237248263205634",
            "status": 1,
            "msg": ""
        }       
    ]
}

```


## 数据查询接口列表
### 命中流量统计
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeCacheHitFlux

#### 接口描述
查询命中流量信息，参数中的查询条件间为AND关系。默认以5分钟纬度分组聚合数据，返回聚合后的命中流量数据。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 频道列表，支持多频道，以英文逗号”,”分隔，最多支持10个频道同时查询 |
| startTime | Date | 是 | 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |
| endTime | Date | 是 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |

#### 返回参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| time | Date | - | 时间,格式yyyyMMddHHmm |
| flux | Long | - | 命中流量，单位Byte |

#### 返回样例

```
{
    "requestId": "1b234d37-e051-44cc-bea2-9fed665382ad",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 3,
    "data": [
        {
            "time": "201804121450",
            "flux": 14608275484
        },
        {
            "time": "201804121500",
            "flux": 24403363124
        },
        {
            "time": "201804121455",
            "flux": 14898737789
        }
    ]
}
```

### 命中请求数统计
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeCacheHitNum

#### 接口描述

查询命中请求数信息，参数中的查询条件间为AND关系。默认以5分钟纬度分组聚合数据，返回聚合后的命中请求数数据。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 频道列表，支持多频道，以英文逗号”,”分隔，最多支持10个频道同时查询 |
| startTime | Date | 是 | 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |
| endTime | Date | 是 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| time | Date | - | 时间,格式yyyyMMddHHmm |
| count | Long | - | 命中次数 |

#### 返回样例

```
{
    "requestId": "5dc54e2a-4801-4d87-bf5c-58fc5d687457",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 3,
    "data": [
        {
            "time": "201804121450",
            "count": 8332
        },
        {
            "time": "201804121500",
            "count": 16387
        },
        {
            "time": "201804121455",
            "count": 10715
        }
    ]
}
```

### 状态码请求数统计
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeHttpCode

#### 接口描述
查询http状态码信息，参数中的查询条件间为AND关系。默认以5分钟纬度分组聚合数据，返回聚合后的数据。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 频道列表，支持多频道，以英文逗号”,”分隔，最多支持10个频道同时查询 |
| startTime | Date | 是 | 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |
| endTime | Date | 是 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| httpCode | Long | - | 状态码 |
| codeData | List<SubItem> | - | 状态码对象集合，见【SubItem】描述|

【SubItem】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| time | Date | - | 时间,格式yyyyMMddHHmm |
| count | Long | - | 状态码数量|

#### 返回样例

```
{
    "requestId": "1b0cb068-9359-4d7b-a3e0-83fd12801975",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 5,
    "data": [
        {
            "httpCode": "416",
            "codeData": [
                {
                    "time": "201804121250",
                    "count": 0
                },
                {
                    "time": "201804121300",
                    "count": 0
                },
                {
                    "time": "201804121255",
                    "count": 0
                }
            ]
        },
        {
            "httpCode": "405",
            "codeData": [
                {
                    "time": "201804121250",
                    "count": 0
                },
                {
                    "time": "201804121300",
                    "count": 0
                },
                {
                    "time": "201804121255",
                    "count": 0
                }
            ]
        },
       {
            "httpCode": "200",
            "codeData": [
                {
                    "time": "201804121250",
                    "count": 0
                },
                {
                    "time": "201804121300",
                    "count": 0
                },
                {
                    "time": "201804121255",
                    "count": 0
                }
            ]
        },
       {
            "httpCode": "206",
            "codeData": [
                {
                    "time": "201804121250",
                    "count": 0
                },
                {
                    "time": "201804121300",
                    "count": 0
                },
                {
                    "time": "201804121255",
                    "count": 0
                }
            ]
        },
       {
            "httpCode": "500",
            "codeData": [
                {
                    "time": "201804121250",
                    "count": 0
                },
                {
                    "time": "201804121300",
                    "count": 0
                },
                {
                    "time": "201804121255",
                    "count": 0
                }
            ]
        }
]
}
```

### 带宽统计
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeBandwidth

#### 接口描述
查询带宽数据。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 频道列表，支持多频道，以英文逗号”,”分隔，最多支持10个频道同时查询 |
| startTime | Date | 是 | 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |
| endTime | Date | 是 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| time | Date | - | 统计时间点 |
| bandwidth | String | - | 带宽值. 单位为 bps  |

#### 返回样例

```
{
    "requestId": "ab9220ca-9d01-44d0-bade-fab9139f4d3c",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 2,
    "data": [
        {
            "time": "2018-04-13 00:00:00",
            "bandwidth": “123456”
        },
        {
            "time": "2018-04-13 00:05:00",
            "bandwidth": “123456”
        }
    ]
}
```

### 流量统计
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeFlux

#### 接口描述
查询流量数据。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 频道列表，支持多频道，以英文逗号”,”分隔，最多支持10个频道同时查询 |
| startTime | Date | 是 | 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |
| endTime | Date | 是 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| time | Date | - | 时间,格式yyyyMMddHHmm |
| flux | Long | - | 命中流量，单位Byte |

#### 返回样例

```
{
    "requestId": "ab9220ca-9d01-44d0-bade-fab9139f4d3c",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 2,
    "data": [
        {
            "time": "2018-04-13 00:00:00",
            "flux": “123456”
        },
        {
            "time": "2018-04-13 00:05:00",
            "flux ": “123456”
        }
    ]
}

```

### 请求数统计
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeVisitor

#### 接口描述
查询请求数数据。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 频道列表，支持多频道，以英文逗号”,”分隔，最多支持10个频道同时查询 |
| startTime | Date | 是 | 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |
| endTime | Date | 是 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| time | Date | - | 统计时间点 |
| pv | Long | - | 请求数量 |

#### 返回样例

```
{
    "requestId": "ab9220ca-9d01-44d0-bade-fab9139f4d3c",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 2,
    "data": [
        {
            "time": "2018-04-13 00:00:00",
            "pv": “123456”
        },
        {
            "time": "2018-04-13 00:05:00",
            "pv": “123456”
        }
    ]
}
```

### 回源带宽统计
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeOriginBandwidth

#### 接口描述
查询回源带宽数据。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 频道列表，支持多频道，以英文逗号”,”分隔，最多支持10个频道同时查询 |
| startTime | Date | 是 | 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |
| endTime | Date | 是 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| time | Date | - | 统计时间点 |
| bandwidth | String | - | 回源带宽值, 单位为 bps |

#### 返回样例

```
{
    "requestId": "ab9220ca-9d01-44d0-bade-fab9139f4d3c",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 2,
    "data": [
        {
            "time": "2018-04-13 00:00:00",
            "bandwidth": “123456”
        },
        {
            "time": "2018-04-13 00:05:00",
            "bandwidth": “123456”
        }
    ]
}
```

### 回源流量统计
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeOriginFlux

#### 接口描述
查询回源流量数据。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 频道列表，支持多频道，以英文逗号”,”分隔，最多支持10个频道同时查询 |
| startTime | Date | 是 | 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |
| endTime | Date | 是 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| time | Date | - | 统计时间点 |
| flux | Long | - | 回源流量值, 单位为 byte |

#### 返回样例

```
{
    "requestId": "ab9220ca-9d01-44d0-bade-fab9139f4d3c",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 2,
    "data": [
        {
            "time": "2018-04-13 00:00:00",
            "flux": “123456”
        },
        {
            "time": "2018-04-13 00:05:00",
            "flux": “123456”
        }
    ]
}
```

## 辅助工具列表
### 日志下载
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/DescribeDownloadLog

#### 接口描述
查询日志文件列表信息，参数中的查询条件间为AND关系。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 频道列表，支持多频道，以英文逗号”,”分隔，最多支持10个频道同时查询 |
| day | Date | 是 | |日期，格式yyyy-MM-dd |

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| createTime | Date | - | 文件创建时间，格式yyyy-MM-dd HH:mm:ss |
| fileName | String | - | 文件名称，格式<domain>_<day>.gz |
| fileLength | Float | - | 文件大小，单位MB，四舍五入保留两位小数 |
| downloadPath | String | - | 日志下载URL地址。|

注意：
downloadPath 说明：
下载地址需以日志下载地址接口方式访问获取。在返回的URL地址后，加入API公共参数即可。

例如：返回的某URL为：http://xxx/ccsp/action/api/downloadLog?clusterServerIp=xx.10.10.xx&day=20170227&fileName=xxx.com_20170227010000.gz

加入公共参数后：

http://xxx/ccsp/action/api/downloadLog?clusterServerIp=xx.10.10.xx&day=20170227&fileName=xxx.com_20170227010000.gz &accessKeyId=NGAA-xxx&signature=GkPCONEaaxxxx&timestamp=1488190799470

#### 返回样例

```
{
    "requestId": "01d7d86c-dd74-416e-8ee0-e17d86ea2108",
    "httpCode": "200",
    "code": "Success",
    "message": "Success",
    "totalCount": 2,
    "data": [
        {
            "createTime": "2016-12-01 01:14:13",
            "fileName": "test.zhouds.cn_20161130.gz",
            "fileLength": "0.42",
            "downloadPath": "http://xxx/ccsp/action/api/downloadLog?clusterServerIp=xx.10.10.xx&day=20170227&fileName=xxx.com_20170227010000.gz"
        },
        {
            "createTime": "2016-12-01 01:14:13",
            "fileName": "www.zhouds.cn_20161130.gz",
            "fileLength": "0.42",
            "downloadPath": "http://xxx/ccsp/action/api/downloadLog?clusterServerIp=xx.10.10.xx&day=20170227&fileName=xxx.com_20170227010000.gz"
       
        }
    ]
}
```

### IP归属查询

#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/queryCdnIp

#### 接口描述
查询IP归属地信息

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| ip | String | 是 | 设备IP |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List<Object> | - | 域名对象集合，见【Item】描述 |

【Item】
| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| ip | String | -  | 设备IP |
| isbelong | boolean | - | false:不存在，true：存在 |
| region | String | - | 归属地信息 |

#### 返回样例

```
{
    "requestId":"1b1b9a4a-5fcc-4370-9060-e9f8696b9e4a",
    "httpCode":"200",
    "code":"Success",
    "message":"Success",
    "totalCount":1,
    "data":[
        {	
            "ip": "45.120.103.146",
            "isbelong": true,
            "region": "北京联通"
       	}
    ]
}
```

