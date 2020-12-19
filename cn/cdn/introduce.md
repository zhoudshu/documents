# CDN产品概述

新流CDN ( Content Delivery Network )自2014年起，自助研发了CDN全套系统，包括CDN业务运营系统、智能调度系统、高效缓存系统、内容分发系统、分布式监控系统、内部运维平台、网络性能监控系统等技术。

新流CDN产品按照业务提供精准加速服务，包括页面加速、下载加速、流媒体加速、动态加速。为客户提供订制服务有防盗链功能、深度日志分析功能、质量检测服务、等支持更多产品定制开发服务。

## 技术架构

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_01.png)

## 加速原理

### 用户访问过程
#### 1、用户在浏览器访问 www.ngaa.com.cn
#### 2、浏览器请求DNS服务器，查询到域名对应IP（此步下面详细解释）
#### 3、浏览器向CDN服务器发起TCP连接
#### 4、CDN服务器收到用户请求，先查找本地是否有缓存，若有从缓存给用户响应；若没有，CDN服务器向源站发起请求，从源站抓取内容给用户
#### 5、浏览器获取到内容并展现

### DNS解析过程：
#### 1、在浏览器访问 www.ngaa.com.cn
#### 2、浏览器查询本地缓存（host文件或者浏览器缓存）如果有记录，便直接使用；如果没有，local dns 便会进行递归迭代解析 www.ngaa.com.cn ，一般最后会获得此域名的一个cname: www.ngaa.com.cn.ngaagslb.cn  (此域名授权域为CDN所有，解析权在CDN厂商)
#### 3、local dns继续解析www.ngaa.com.cn.ngaagslb.cn 最终请求会到GSLB（全局调度系统）。
#### 4、GSLB 根据请求来源给local dns访问质量最优的解析结果
#### 5、local dns将解析结果返回给用户
#### 6、用户使用此结果来发起http请求

