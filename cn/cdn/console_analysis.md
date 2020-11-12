## 2.统计分析
根据边缘节点日志，对带宽、回源、流量、请求内容、状态码、PV/UV、ISP地域、下载速度等信息进行计算。

### 2.1 带宽对比
带宽对比将网络设备采集带宽和日志计算带宽进行对比展示，可以选择对比日期范围

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_08.png)

### 2.2 带宽统计
基于访问日志对带宽进行计算，展示一段时间的带宽趋势。
国内带宽可以自由选择频道、运营商、省份和日期范围。其中运营商不可多选，省份在同一个运营商下可多选，不可跨运营商选择。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_09.png)

海外带宽展示海外节点的服务情况，操作方法和国内带宽一致。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_10.png)

带宽对比页面可以选择需要对比的时间，协议类型，频道，运营商，省份信息。实现对不同时间的服务带宽对比。以便于发现带宽大范围波动。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_01.png)

### 2.3 回源统计
根据上层节点日志中MISS记录计算回源部分的数据，包括回源带宽，回源响应时间信息。
回源带宽可分频道、运营商、省份、时间进行展示。其中频道可以自由选择，运营商仅可选择一个，同运营商省份可以自由选择。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_12.png)

回源响应时间根据源站响应时间计算。可分频道、运营商、省份、时间进行展示。其中频道可以自由选择，运营商仅可选择一个，同运营商省份可以自由选择。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_13.png)

### 2.4 流量统计
本页内容根据边缘节点日志计算服务流量，可分频道、运营商、省份、时间进行展示。其中频道可以自由选择，运营商仅可选择一个，同运营商省份可以自由选择。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_14.png)

### 2.5 请求排行
根据边缘日志统计用户URL的访问数量。可自由选择频道和查询日志，只支持按天查询。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_15.png)

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_16.png)

### 2.6 Cache率统计
Cache率根据所有缓存节点（包括下层，中层，上层节点）情况，根据域名的服务流量/回源流量计算域名在新流平台的缓存率。可分频道、运营商、省份、时间进行展示。其中频道可以自由选择，运营商仅可选择一个，同运营商省份可以自由选择。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_17.png)

根据日志计算http响应码，显示响应码对应的流量百分比和命中流量。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_18.png)

### 2.7 状态码统计
显示服务域名产生的状态码及分布情况，支持2xx、3xx、4xx、5xx及定制化状态码。可分频道、运营商、省份、时间进行展示。其中频道可以自由选择，运营商仅可选择一个，同运营商省份可以自由选择。除此之外，还可以只显示回源访问的状态码分布情况。
状态码分布按照5分钟统计显示，形成曲线图。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_19.png)

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_20.png)

### 2.8 PV/UV统计
PV（Page View）访问量, 即页面浏览量或点击量，衡量网站用户访问的网页数量；在一定统计周期内用户每打开或刷新一个页面就记录1次，多次打开或刷新同一页面则浏览量累计。
UV（Unique Visitor）独立访客，统计1天内访问某站点的用户数(以cookie为依据);访问网站的一台电脑客户端为一个访客。
根据边缘节点日志计算pv、uv、ip访问信息。可自由选择频道和日期范围，以折线图/柱状图显示。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_21.png)

### 2.9 ISP地域统计
根据用户访问日志中用户IP地址字段确认用户归属ISP，页面显示每个ISP访问的流量和占比信息。
可自由选择频道，选择运营商，国家，省份和时间，生成对应的地域流量统计信息

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_22.png)

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_23.png)

### 2.10 平均下载速度统计
根据边缘访问日志，计算每条访问的字节/时间，然后5分钟所有URL速度取平均值得到域名的平均下载速度。可选择域名、全部请求/回源请求和日志范围显示曲线图。

![](https://github.com/zhoudshu/documents/blob/main/images/cdn/cdn_24.png)

