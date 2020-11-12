
为了让用户更加快速地掌握并使用控制台，我们将一些常用服务根据不同用户的不同使用需求进行了划分整理，目前控制台主要分为基础服务、场景服务、数据中心和直播工具箱四个模块用于不同的使用场景。

## 基础服务
基础服务主要提供云直播的接入使用，如果您仅需要接入基础的云直播服务，仅需在基础服务模块内操作即可。


<table>
<tr><th width="17%">功能名称</th>
<th>功能描述</th>
</tr>
<tr>
<td ><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_overview.md">概览</a></td>
<td><ul style = "margin-bottom: 0px;"><li>可以查看计费宽带/流量的趋势等相关数据、直播的实时数据、直播在线人数。</li>
<li>可按需更改时间粒度。</li></ul></td>
</tr><tr>
<td><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_domainmgr.md">域名管理</a></td>
<td><ul style = "margin-bottom: 0px;"><li>可添加并管理自有加速域名，并对域名进行 CNAME 配置。</li>
<li>可在线生成对应直播地址。</li>
<li>可对直播域名调用已创建的录制、转码、截图、水印、回调功能模板。</li>
<li>可对直播域名配置鉴权、HTTPS 协议、加速区域、源站等信息。</li></ul></td>
</tr><tr>
<td><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_streammgr.md">流管理</a></td>
<td>可对直播在线流、历史流以及禁推流进行管理，并对直播流进行禁止和恢复推流等操作。</td>
</tr></tr>
</table>

## 场景服务
场景服务集成了云直播的一些周边服务，包括：转码、水印、截图。如需要使用相关服务可在本模块进行相关配置。


<table>
<tr><th width="17%">功能名称</th><th>功能描述</th></tr>
<tr>
<td ><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_template.md">功能配置</a></td>
<td><ul style= "margin: 0"><li>供了直播中所需的录制、转码、截图、水印等功能的配置模板服务，为降低页面跳转复杂度，特在此新增了模板绑定域名的流程。</li>
<li>针对各触发事件设置接收相关回调信息的路径。</li></ul></td>
</tr><tr>
<td><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_tools_streamevent.md">断流诊断</a></td>
<td><ul style= "margin: 0"><li>可以快速查看直播推流断流的记录与断流原因。</li></ul></td>
</tr></tr>
</table>


## 数据中心
数据分析为用户提供了专业的数据分析服务，可查询时间粒度内流量/带宽、转码、水印、转推、截图消耗情况，并且提供日志下载功能，方便用户进行资源监控，掌握有用数据。

<table>
<tr><th width="17%">功能名称</th><th>功能描述</th>
</tr><tr>
<td >数据统计</a></td>
<td><ul style = "margin-bottom: 0px;">
<li><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_analysis_increment.md" >增值功能</li>
<li><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_analysis_opt.md" >运营数据</li></ul></td>
</tr><tr>
<td><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_analysis_streamquery.md">流数据查询</a></td>
<td>可查询单个视频流的推流、播放数据详情，并将数据导出到本地。</td>
</tr><tr>
<td>日志分析</td>
<td>
<ul style = "margin-bottom: 0px;">
<li><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_mediainfo_picture.md">截图信息下载</li>
<li><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_mediainfo_record.md">录制信息下载</li>
<li><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_logdownload.md">日志下载</li></ul></td>
</tr>
</tr>
</table>

## 直播工具箱
直播工具箱主要围绕直播流程提供了一些保障服务的附属功能。

<table>
<tr><th width="17%">功能名称</th><th>功能描述</th>
</tr><tr>
<td ><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_tools_producer.md">地址生成器</a></td>
<td>支持通过填写地址拼接信息，辅助用户快速生成推流/播放地址。</td>
</tr><tr>
<td><a href = "https://github.com/zhoudshu/documents/blob/main/cn/cloudlive/console_tools_webpush.md">Web推流</a></td>
<td>可实现快速生成推流地址，在线推流测试直播功能。</td>
</tr></tr>
</table>
