# API接口概览
对系统提供的API接口进行说明，供其它业务系统集成调用

## 查询流列表管理-V3版本
此类接口为当前稳定的版本，推荐大家使用

| 接口名称     | 接口功能     | 备注                           |
| -------- | ------ | ---------------------------------------- |
| GetLiveOnlineStreamList | 获取在线流列表 | [访问](#获取在线流列表) |
| GetLiveHistoryStreamList | 获取历史流列表| [访问](#获取历史流列表) |

## 流管理接口-V2版本

| 接口名称     | 接口功能     | 备注                           |
| -------- | ------ | ---------------------------------------- |
| auth | 流上报外部鉴权 | [访问](#流上报外部鉴权) |
| xl_publishStream | 流上线通知 | [访问](#流上线通知) |
| xl_unpublishStream | 流下线通知 | [访问](#流下线通知) |
| streamControl | 流禁播/恢复| [访问](#流播控接口) |

## 直播流数据统计-V2版本

| 接口名称     | 接口功能     | 备注                           |
| -------- | ------ | ---------------------------------------- |
| onlineViewers | 实时在线观看人数 | [访问](#实时在线观看人数) |
| flow | 流量 | [访问](#流量) |
| bandwidth | 带宽 | [访问](#带宽) |
| uv | 独立IP数 | [访问](独立IP数) |
| pv | 请求次数 | [访问](请求次数) |

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
| data | List | 否 | 返回的数据实体对象集合 |

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


# 调用方式-V2版本
## 请求结构
### 服务地址

服务入口地址为：http://[hostAddress]/ccsp/action/api/live/Action
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

| 名称       | 类型  | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| accessKeyId | String | 是 | 访问服务的身份标识 |
| signature   | String | 是 | 签名字符串，关于签名的计算方法，请参见签名机制小节2.6 |
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

http://[hostAddress]/ccsp/action/api/live/Action?xxx&accessKeyId=xxx&timestamp=xxx&signature=xxx&参数1=XXX&参数2=xxx&...参数n=xxx

## 应答结构
### 数据格式
所有API接口，返回数据格式为标准JSON格式。

### 返回状态码

API有完善的错误码机制，API调用失败会返回响应的Http码、错误码以及错误描述。
Http码为4XX的是客户端错误，建议用户根据错误描述，修正请求后重新提交。
Http码为5XX的是服务内部错误，此时建议重试。
#### 公共HTTP状态码

| httpCode  |  描述         |
| --------- | ------ |
| 200  | 成功 |
| 400  | 缺少参数或参数无效 |
| 401  | 鉴权错误 |
| 403  | 没有权限 |
| 500  | 服务内部错误 |

#### 公共CODE状态码
| code      |  描述         |
| --------- | ------ |
| Invalid.Paramater | 无效的参数，一般为参数格式错误 |
| Missing.Parameter | 缺少参数。|
| Forbidden.[XXX] | 鉴权错误，一般为没有权限|
| Internal.Error | 服务内部错误 |
| Success | 成功 |

# 支持接口列表
## 查询流接口列表
### 获取在线流列表
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/GetLiveOnlineStreamList

#### 接口描述
获取在线流列表。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 否 | 推流域名 |
| app | String | 否 | app名称 |
| stream | String |否| 流名称 |
| startTime | Date |否| 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |
| endTime | Date | 否 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为7天 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List | - | 域名对象集合，见【Item】描述 |

【Item】

| 名称   | 类型     | 是否必须   |  描述                    |
| --------- | ------ | ------------------------------------ | ---- |
| domain | String | - | 推流域名 |
| app | String | - | app名称 |
| stream | String | - | 流名称 |
| clientIp | String | - | 推流客户端IP |
| pushStartTime | Date | - | 推流时间,格式yyyy-MM-dd HH:mm:ss |

#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": [
        {
            "domain": "push.xxxx.com",
            "app": "live",
            "stream": "test1",
            "clientIp": "123.32.33.11",
            "pushStartTime": "2020-04-24 17:35:10"
        },
        {
            "domain": "push.xxxx.com",
            "app": "live",
            "stream": "test2",
            "clientIp": "123.32.33.11",
            "pushStartTime": "2020-04-24 16:33:15"
        }
    ]
}

```

### 获取历史流列表
#### 请求地址
http://[hostAddress]/ccsp/action/api/v3/GetLiveHistoryStreamList

#### 接口描述
获取历史流列表。

#### 请求参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 否 | 推流域名 |
| app | String | 否 | app名称 |
| stream | String | 否 | 流名称 |
| startTime | Date | 否 | 数据范围开始时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为90天 |
| endTime | Date | 否 | i数据范围结束时间，格式yyyy-MM-dd HH:mm:ss，开始时间和结束时间范围上限为90天 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| data | List | - | 域名对象集合，见【Item】描述 |

【Item】

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | - | 推流域名 |
| app | String | - | app名称 |
| stream | String | - | 流名称 |
| clientIp | String | - | 推流客户端IP |
| stopReason | String | - | 断流原因 |
| pushStartTime | Date | - | 推流开始时间,格式yyyy-MM-dd HH:mm:ss |
| pushEndTime | Date | - | 推流结束时间,格式yyyy-MM-dd HH:mm:ss |

#### 返回样例

```
{
    "requestId": "971b4c4d4c7f45b9b8690fb88cb65bf5",
    "httpCode": "200",
    "code": "success",
    "message": "success",
    "totalCount": 0,
    "data": [
        {
            "domain": "push.xxxx.com",
            "app": "live",
            "stream": "test1",
            "clientIp": "123.32.33.11",
            "stopReason": "[0]success disconnect",
            "pushStartTime": "2020-04-24 17:35:10",
            "pushEndTime": "2020-04-24 18:15:10"
        },
        {
            "domain": "push.xxxx.com",
            "app": "live",
            "stream": "test2",
            "clientIp": "123.32.33.11",
            "stopReason": "[0]success disconnect",
            "pushStartTime": "2020-04-24 17:33:15",
            "pushEndTime": "2020-04-24 18:25:10"
        }
    ]
}

```


## 流管理接口-V2版本
此类接口为系统较老的版本，在将来会用新接口来代替，当前仍然在线运行，可以使用

### 流上报外部鉴权
#### 请求地址
需要推流客户提供, 比如:

http://api.haohancloud.com/l2/cdn/auth?app=live&domain=devlivepush.haohancloud.com&stream=7AZTZE7Y_C0

采用GET方法

#### 接口描述
流上下线回调前需调用此接口鉴权,用以判断CDN厂商发送直播流上下线是否通过，成功则允许推流，失败则断流禁播，上下线通知前调用此接口访问直播流鉴权，防止非本系统侧的直播流上下线通知接口被调用，
接口响应超时重试次数为0，超时默认为鉴权通过

#### 请求参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 推流域名 |
| app | String | 是 | app名称 一般为live |
| stream | String | 是 | 流名称 |

#### 返回参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| ret | String | 是 | 状态码 0: 成功 1: 失败|
| msg | String | 是 | 描述 |

#### 返回样例

```
成功：
{
    “ret”:”0”,
    “msg”:”success”
}
失败：
{
    “ret”:”1”,
    “msg”:”fail”
}

```

### 流上线通知
#### 请求地址
需要推流客户提供, 比如

http://api.haohancloud.com//l2/cdn/xl_publishStream?id=ctyuntestv3

采用GET方法

#### 接口描述
流上线回调客户的系统接口，可以根据此样例开发支持

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| id | String | 是 | 流名称 |

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
|  | String | 是 | 状态码 0: 成功 1: 失败|

#### 返回样例

```
成功：
0
失败：
1

```

### 流下线通知
#### 请求地址
需要推流客户提供, 比如

http://api.haohancloud.com//l2/cdn/xl_unpublishStream?id=ctyuntestv3

采用GET方法

#### 接口描述
流下线回调客户的系统接口，可以根据此样例开发支持

#### 请求参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| id | String | 是 | 流名称 |

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
|  | String | 是 | 状态码 0: 成功 1: 失败|

#### 返回样例

```
成功：
0
失败：
1

```

### 流播控接口
#### 请求地址
新流提供, 比如

http://ip:port/ccsp/action/api/live/streamControl

样例：使用V2版本的公共参数

https://ccsp-test.sinocache.net/action/api/live/streamControl?action=forbid&type=publish&reltime=300&channel=rtmp://push.haohan.test.cn/live/ctyuntestv3&accessKeyId=NGAA-test&timestamp=1585722543000&signature=hsseNcazSTd9YleYgcZ9nkjP9QH0=

采用GET方法

#### 接口描述

实现推流过程中对直播流的播控实现停止推流，和恢复推流

#### 请求参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
| action | String | 是 | 操作类型 forbid：禁播;resume：恢复 |
| type | String | 是 | 流类型 publish:直播流|
| reltime | Long | 是 | 过期时间 禁播过期时间（s）|
| channel |String | 是 | 视频流 完整的推流url |

#### 返回参数

| 名称      | 类型     | 是否必须   |  描述                            |
| --------- | ------ | ---------------------------------------- | ---- |
|  | String | 是 | 状态码 0: 成功 1: 失败|

#### 返回样例

```
成功：
0
失败：
1

```

## 直播流数据统计-V2版本
### 实时在线观看人数

#### 请求地址

http://ip:port/ccsp/action/api/live/onlineViewers

样例：使用V2版本的公共参数

https://ccsp-test.sinocache.net/action/api/live/onlineViewers?accessKeyId=NGAA-test&timestamp=1585723199000&signature=/x0rremnBlTqiEj3SFB5qf07YYg=

采用POST方法

#### 接口描述

在查询时刻，返回所查域名下所有正在被播放的视频(点播)/频道(直播)的实时在线观看人数（当前时刻 是当前查询时刻前一分钟的这个一分钟时间段），并按照ISP/省市区分的列表。该数据需要在5分钟内获取

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| dateTime | String | 是 | 查询时刻 格式为yyyy-MM-ddTHH:mm:ss+08:00 |
| dataInterval | String | 是 | 间隔维度 一分钟维度:"1m" |
| domains | String | 是 | 域名 多个域名使用英文“,”分隔 |
| stream | String | 否 | 直播流名，不传时默认查询域名下的全部流名，多个直播流查询使用英文“,”分隔 |
| dataIsp | Integer | 否 | 分运营商统计 默认不分运营商统计，0:开启分运营商统计；1:关闭分运营商统计 |
| dataProvince | Integer | 否 | 分省份统计 默认不分省份统计，0:开启分省份统计； 1:关闭分省份统计 |

```
{
    "dataInterval":"1m",
    "dataIsp":0,
    "dataProvince":0,
    "dateTime":"2020-04-01T15:20:00+08:00",
    "domains":"pull.haohan.test.cn",
    "stream":"live/ctyuntestv3"
}
```

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| result | List | 是 | 返回结果集 |

结果集

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 拉流域名 |
| streamData | List | 是 | 直播流数据 |
| &emsp;stream | String | 是 | 直播流名 |
| &emsp;timestamp | String | 是 | 粒度统计的时间 |
| &emsp;totalValue | String | 是 | 总在线观看人数 |
| &emsp;provinceData| List | 否 | 分省份数据 开启分省份统计时提供，开启运营商统计时也提供数据 |
| &emsp;&emsp;province | String | 否 | 省份缩写 开启运营商统计时也提供数据 |
| &emsp;&emsp;Value | String | 否  | 在线观看人数, 未开启省份统计开启运营商统计时不需要提供此数据 |
| &emsp;ispData | List | 否 | 分运营商数据 开启分运营商统计时提供 |
| &emsp;&emsp;isp | String | 否  | 运营商缩写 |
| &emsp;&emsp;value | String | 否  | 在线观看人数 |


#### 返回样例

```
{
	"result": [
		{
			"domain": "pull.haohan.test.cn",
			"streamData": [
				{
					"stream": "live/ctyuntestv3",
					"timestamp": "2020-04-01 16:05",
					"totalValue": "94",
					"value": null,
					"provinceData": [
						{
							"province": "bj",
							"value": "94",
							"ispData": [
								{
									"isp": "lt",
									"value": "64"
								}
							]
						}
					]
				},
		       ]
		}
	]
} 


```


## 直播流数据统计-V2版本
### 流量

#### 请求地址

http://ip:port/ccsp/action/api/live/flow

样例：使用V2版本的公共参数

https://ccsp-test.sinocache.net/action/api/live/flow?accessKeyId=NGAA-test&timestamp=1585730006000&signature=X+mXxXtebFSys45UsqJzNdKENAU=

采用POST方法

#### 接口描述

针对所查询的时段，返回所查域名下所有视频(点播)/频道(直播)的流量，
区分地区，运营商及终端。列表体现5分钟粒度。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| dateFrom | String | 是 | 查询时刻 格式为yyyy-MM-ddTHH:mm:ss+08:00 |
| dateTo | String | 是 | 查询时刻 格式为yyyy-MM-ddTHH:mm:ss+08:00 |
| dataType | String | 是 | 查流量就填"flow" |
| dataInterval | String | 是 | 间隔维度 5分钟维度:"5m" |
| domains | String | 是 | 域名 多个域名使用英文“,”分隔 |
| stream | String | 否 | 直播流名，不传时默认查询域名下的全部流名，多个直播流查询使用英文“,”分隔 |
| dataIsp | Integer | 否 | 分运营商统计 默认不分运营商统计，0:开启分运营商统计；1:关闭分运营商统计 |
| dataProvince | Integer | 否 | 分省份统计 默认不分省份统计，0:开启分省份统计； 1:关闭分省份统计 |
| dataDeviceType | Integer | 否 | 默认不分终端统计，0:开启分终端统计；1:关闭分终端统计 |

```
{
	"dateFrom": "2020-04-01T16:00:00+08:00",
	"dateTo": "2020-04-01T16:05:00+08:00",
	"dataIsp": 0,
	"dataProvince": 0,
	"dataDeviceType": 0,
	"dataType": "flow",
	"dataInterval": "5m",
	"domains": "pull.haohan.test.cn"
}

```

#### 返回参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| result | List | 是 | 返回结果集 |

结果集

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 拉流域名 |
| streamData | List | 是 | 直播流数据 |
| &emsp;stream | String | 是 | 直播流名 |
| &emsp;timestamp | String | 是 | 粒度统计的时间 |
| &emsp;totalValue | String | 是 | 总流量 流量值，单位为MB，保留两位小数 |
| &emsp;provinceData| List | 否 | 开启分省份统计时提供，开启运营商/终端统计时也提供数据 |
| &emsp;&emsp;province | String | 否 | 省份缩写 开启运营商统计时也提供数据 |
| &emsp;&emsp;Value | String | 否  | 流量值，单位为MB，保留两位小数，未开启省份统计开启运营商/终端统计时不需要提供此数据 |
| &emsp;ispData | List | 否 | 分运营商数据 开启分运营商统计时提供 |
| &emsp;&emsp;isp | String | 否  | 运营商缩写 |
| &emsp;&emsp;value | String | 否  | 流量值，单位为MB，保留两位小数 |
| &emsp;deviceData | List | 否 | 分终端数据 开启分终端统计时提供 |
| &emsp;&emsp;deviceType | String | 否  | 终端类型 pc,mobile,other |
| &emsp;&emsp;value | String | 否  | 流量值，单位为MB，保留两位小数 |

#### 返回样例

```
{
	"result": [
		{
			"domain": "pull.haohan.test.cn",
			"streamData": [
				{
					"stream": "live/ctyuntestv3",
					"timestamp": "2020-04-01 16:05",
					"totalValue": null,
					"value": "9400",
					"provinceData": [
						{
							"province": "bj",
							"value": "9400",
							"ispData": [
								{
									"isp": "lt",
									"value": "6400"
								}
							],
							"deviceData": [
								{
									"deviceType": "-",
									"value": "3000"
								}
							]
						}
					]
				},
		       ]
		}
	]
} 

```

## 直播流数据统计-V2版本
### 带宽

#### 请求地址

http://ip:port/ccsp/action/api/live/bandwidth

样例：使用V2版本的公共参数

https://ccsp-test.sinocache.net/action/api/live/bandwidth?accessKeyId=NGAA-test&timestamp=1585730307000&signature=Y2Zylx0JaWHlaTgNvpfS+qiQsoI=

采用POST方法

#### 接口描述

针对所查询的时段，返回所查域名下所有视频(点播)/频道(直播)的下行带宽，区分地区，运营商及终端。列表体现5分钟粒度。

#### 请求参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| dateFrom | String | 是 | 查询时刻 格式为yyyy-MM-ddTHH:mm:ss+08:00 |
| dateTo | String | 是 | 查询时刻 格式为yyyy-MM-ddTHH:mm:ss+08:00 |
| dataType | String | 是 | 查流量就填"bandwidth" |
| dataInterval | String | 是 | 间隔维度 5分钟维度:"5m" |
| domains | String | 是 | 域名 多个域名使用英文“,”分隔 |
| stream | String | 否 | 直播流名，不传时默认查询域名下的全部流名，多个直播流查询使用英文“,”分隔 |
| dataIsp | Integer | 否 | 分运营商统计 默认不分运营商统计，0:开启分运营商统计；1:关闭分运营商统计 |
| dataProvince | Integer | 否 | 分省份统计 默认不分省份统计，0:开启分省份统计； 1:关闭分省份统计 |
| dataDeviceType | Integer | 否 | 默认不分终端统计，0:开启分终端统计；1:关闭分终端统计 |

```
{
	"dateFrom": "2020-04-01T16:00:00+08:00",
	"dateTo": "2020-04-01T16:05:00+08:00",
	"dataIsp": 0,
	"dataProvince": 0,
	"dataDeviceType": 0,
	"dataType": "bandwidth",
	"dataInterval": "5m",
	"domains": "pull.haohan.test.cn"
}

```

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| result | List | 是 | 返回结果集 |

结果集

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 拉流域名 |
| streamData | List | 是 | 直播流数据 |
| &emsp;stream | String | 是 | 直播流名 |
| &emsp;timestamp | String | 是 | 粒度统计的时间 |
| &emsp;value | String | 是 | 总 流量值，单位为MB，保留两位小数 |
| &emsp;provinceData| List | 否 | 开启分省份统计时提供，开启运营商/终端统计时也提供数据 |
| &emsp;&emsp; province | String | 否 | 省份缩写 开启运营商统计时也提供数据 |
| &emsp;&emsp;Value | String | 否  | 带宽值，单位为Mbps，保留两位小数，未开启省份统计开启运营商/终端统计时不需要提供此数据 |
| &emsp;ispData | List | 否 | 分运营商数据 开启分运营商统计时提供 |
| &emsp;&emsp;isp | String | 否  | 运营商缩写 |
| &emsp;&emsp;value | String | 否  | 带宽值，单位为Mbps，保留两位小数 |
| &emsp;deviceData | List | 否 | 分终端数据 开启分终端统计时提供 |
| &emsp;&emsp;deviceType | String | 否  | 终端类型 pc,mobile,other |
| &emsp;&emsp;value | String | 否  | 带宽值，单位为Mbps，保留两位小数 |

#### 返回样例

```
{
	"result": [
		{
			"domain": "pull.haohan.test.cn",
			"streamData": [
				{
					"stream": "live/ctyuntestv3",
					"timestamp": "2020-04-01 16:05",
					"totalValue": null,
					"value": "0.94",
					"provinceData": [
						{
							"province": "bj",
							"value": "0.94",
							"ispData": [
								{
									"isp": "lt",
									"value": "0.94"
								}
							],
							"deviceData": [
								{
									"deviceType": "-",
									"value": "0.94"
								}
							]
						}
					]
				},
		       ]
		}
	]
} 

```


## 直播流数据统计-V2版本
### 独立IP数

#### 请求地址

http://ip:port/ccsp/action/api/live/uv

样例：使用V2版本的公共参数

https://ccsp-test.sinocache.net/action/api/live/uv?accessKeyId=NGAA-test&timestamp=1585730706000&signature=sZsZOO1deAoissx7nj7dnLGHHZf+g=

采用POST方法

#### 接口描述

针对所查询的时段，返回所查询频道的UV，区分地区，运营商及终端。

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| dateFrom | String | 是 | 查询时刻 格式为yyyy-MM-ddTHH:mm:ss+08:00 |
| dateTo | String | 是 | 查询时刻 格式为yyyy-MM-ddTHH:mm:ss+08:00 |
| dataType | String | 是 | 查IP就填"dip" |
| dataInterval | String | 是 | 间隔维度 一天维度:"1d" |
| domains | String | 是 | 域名 多个域名使用英文“,”分隔 |
| stream | String | 否 | 直播流名，不传时默认查询域名下的全部流名，多个直播流查询使用英文“,”分隔 |
| dataIsp | Integer | 否 | 分运营商统计 默认不分运营商统计，0:开启分运营商统计；1:关闭分运营商统计 |
| dataProvince | Integer | 否 | 分省份统计 默认不分省份统计，0:开启分省份统计； 1:关闭分省份统计 |
| dataDeviceType | Integer | 否 | 默认不分终端统计，0:开启分终端统计；1:关闭分终端统计 |

```
{
    "dateFrom":"2020-04-01T16:00:00+08:00", 
    "dateTo":"2020-04-01T16:05:00+08:00",
    "dataType": "dip",
    "dataInterval": "5m",
    "domains": "pull.haohan.test.cn"
}
```

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| result | List | 是 | 返回结果集 |

结果集

| 名称        | 类型     | 是否必须   |  描述                                       |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 拉流域名 |
| streamData | List | 是 | 直播流数据 |
|   stream | String | 是 | 直播流名 |
|   timestamp | String | 是 | 粒度统计的时间 |
|   totalValue | String | 是 | 总ip数 Ip数，单位为个 |
|   provinceData| List | 否 | 开启分省份统计时提供，开启运营商/终端统计时也提供数据 |
|       province | String | 否 | 省份缩写 开启运营商统计时也提供数据 |
|       Value | String | 否  | Ip数，单位为个，未开启省份统计开启运营商/终端统计时不需要提供此数据 |
|   ispData | List | 否 | 分运营商数据 开启分运营商统计时提供 |
|       isp | String | 否  | 运营商缩写 |
|       value | String | 否  |  Ip数，单位为个 |
|   deviceData | List | 否 | 分终端数据 开启分终端统计时提供 |
|       deviceType | String | 否  | 终端类型 pc,mobile,other |
|       value | String | 否  | Ip数，单位为个 |

#### 返回样例

```
{
	"result": [
		{
			"domain": "pull.haohan.test.cn",
			"streamData": [
				{
					"stream": "live/testlive",
					"timestamp": "2020-04-01 16:05",
					"totalValue": "1",
					"value": null,
					"provinceData": [
						{
							"province": "he",
							"value": "1",
							"ispData": [
								{
									"isp": "dx",
									"value": "1"
								}
							],
							"deviceData": [
								{
									"deviceType": "-",
									"value": "1"
								}
							]
						}
					]
				},

			]
		}
	]
}
```


## 直播流数据统计-V2版本
### 请求次数

#### 请求地址

http://ip:port/ccsp/action/api/live/pv

样例：使用V2版本的公共参数

https://ccsp-test.sinocache.net/action/api/live/pv?accessKeyId=NGAA-test&timestamp=1585730706000&signature=sZsZOO1deAoissx7nj7dnLGHHZf+g=

采用POST方法

#### 接口描述

针对所查询的时段，返回所查域名下所有直播的播放次数，区分地区，运营商及终端。列表体现五分钟粒度。
(如果是m3u8格式，请求次数需根据IP、按一天的时间粒度去重。)

#### 请求参数

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| dateFrom | String | 是 | 查询时刻 格式为yyyy-MM-ddTHH:mm:ss+08:00 |
| dateTo | String | 是 | 查询时刻 格式为yyyy-MM-ddTHH:mm:ss+08:00 |
| dataType | String | 是 | 查次数就填"hit" |
| dataInterval | String | 是 | 10分钟维度:"10m" |
| domains | String | 是 | 域名 多个域名使用英文“,”分隔 |
| stream | String | 否 | 直播流名，不传时默认查询域名下的全部流名，多个直播流查询使用英文“,”分隔 |
| dataIsp | Integer | 否 | 分运营商统计 默认不分运营商统计，0:开启分运营商统计；1:关闭分运营商统计 |
| dataProvince | Integer | 否 | 分省份统计 默认不分省份统计，0:开启分省份统计； 1:关闭分省份统计 |
| dataDeviceType | Integer | 否 | 默认不分终端统计，0:开启分终端统计；1:关闭分终端统计 |

```
{
    "dateFrom":"2020-04-01T16:00:00+08:00", 
    "dateTo":"2020-04-01T16:05:00+08:00",
    "dataType": "hit",
    "dataInterval": "5m",
    "domains": "pull.haohan.test.cn"
}
```

#### 返回参数

| 名称        | 类型     | 是否必须   |  描述                          |
| --------- | ------ | ---------------------------------------- | ---- |
| result | List | 是 | 返回结果集 |

结果集

| 名称      | 类型   | 是否必须   |  描述                              |
| --------- | ------ | ---------------------------------------- | ---- |
| domain | String | 是 | 拉流域名 |
| streamData | List | 是 | 直播流数据 |
|   stream | String | 是 | 直播流名 |
|   timestamp | String | 是 | 粒度统计的时间 |
|   totalValue | String | 是 | 总请求数单位为个 |
|   provinceData | List | 否 | 开启分省份统计时提供，开启运营商/终端统计时也提供数据 |
|       province | String | 否 | 省份缩写 开启运营商统计时也提供数据 |
|       Value | String | 否  | 请求数单位为个，未开启省份统计开启运营商/终端统计时不需要提供此数据 |
|   ispData | List | 否 | 分运营商数据 开启分运营商统计时提供 |
|       isp | String | 否  | 运营商缩写 |
|       value | String | 否  | 请求数单位为个 |
|   deviceData | List | 否 | 分终端数据 开启分终端统计时提供 |
|       deviceType | String | 否  | 终端类型 pc,mobile,other |
|       value | String | 否  | 请求数单位为个 |

#### 返回样例

```

{
	"result": [
		{
			"domain": "pull.haohan.test.cn",
			"streamData": [
				{
					"stream": "live/testlive",
					"timestamp": "2020-04-01 16:05",
					"totalValue": "14",
					"value": null,
					"provinceData": [
						{
							"province": "he",
							"value": "14",
							"ispData": [
								{
									"isp": "dx",
									"value": "14"
								}
							],
							"deviceData": [
								{
									"deviceType": "-",
									"value": "14"
								}
							]
						}
					]
				},
		         ]
		}
	]
}

```

## 补充说明-V2版本
### 省份
| 序号	| 省份(province)	 | 省份缩写 |
| ----- | ------ | ------- |
| 1	| 安徽	| AH |
| 2	| 北京	| BJ |
| 3	| 福建	| FJ |
| 4	| 甘肃	| GS |
| 5	| 广东	| GD |
| 6	| 广西	| GX |
| 7	| 贵州	| GZ |
| 8	| 海南	| HI |
| 9	| 河北	| HE |
| 10	| 河南	| HA |
| 11	| 黑龙江| HL |
| 12	| 湖北	| HB |
| 13	| 湖南	| HN |
| 14	| 吉林	| JL |
| 15	| 江苏	| JS |
| 16	| 江西	| JX |
| 17	| 辽宁	| LN |
| 18	| 内蒙古| NM |
| 19	| 宁夏	| NX |
| 20	| 青海	| QH |
| 21	| 山东	| SD |
| 22	| 山西	| SX |
| 23	| 陕西	| SN |
| 24	| 上海	| SH |
| 25	| 四川	| SC |
| 26	| 天津	| TJ |
| 27	| 西藏	| XZ |
| 28	| 新疆	| XJ |
| 29	| 云南	| YN |
| 30	| 浙江	| ZJ |
| 31	| 重庆	| CQ |
| 32	| 澳门	| MO |
| 33	| 香港	| HK |
| 34	| 台湾	| TW |

### 运营商
| 序号	| 运营商(isp)	| 运营商缩写 |
| ----- | ------ | ------- |
| 1	| 中国移动	| yd |
| 2	| 中国联通	| lt |
| 3	| 中国电信	| dx |

### 终端

| 序号	| 终端类型	| 终端类型缩写 |
| ----- | ------------- | ------- |
| 1	| 终端类型PC下的终端子类型	| PC |
| 2	| 终端类型Mobile下的终端子类型	| IOS、Android、Other |
| 3	| 终端类型Other下的终端子类型	| Other |

