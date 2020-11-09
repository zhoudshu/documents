云直播控制台提供地址生成器功能，支持通过填写地址拼接信息，辅助用户快速生成推流/播放地址。其中直播地址主要由域名（domain）、应用名称（AppName）、流名称（StreamName）以及鉴权 Key 组成。

![](https://main.qcloudimg.com/raw/891a0d8db4d94cd92498d0d0d3944ade.png)

地址生成后，可通过**选择复制**、**单击复制按钮**的方式提取地址信息。


## 注意事项
- 云直播暂无地址生成历史记录功能，请生成地址后，复制保存。

##  前提条件
已登录 [云直播控制台]()，并添加 [推流/播放域名]()。

## 配置参数说明

<table>
<thead><tr><th>配置参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>生成类型与域名</td>
<td>可选择<strong>推流域名</strong>或<strong>播放域名</strong>。</td>
</tr><tr><td>AppName</td>
<td>直播的应用名称，用于区分直播流媒体文件存放路径，默认为 live。<br>仅支持填写英文字母、数字和符号。</td>
</tr><tr><td>StreamName</td>
<td>自定义的流名称，每路直播流的唯一标识符。<br>仅支持填写英文字母、数字和符号。</td>
</tr><tr><td>过期时间</td>
<td><li>播放地址过期时间为设置时间戳加播放鉴权设置的有效时间。<li>推流地址过期时间即设置时间。</td>
</tbody></table>

<h2 id="push">生成推流地址</h2>

### 操作步骤
1. 登录云直播控制台，选择【辅助工具】[【地址生成器】]()，进入地址生成器。
2. 选择生成类型为**推流域名**，并选择您已添加到域名管理的推流域名。
3. 填写 AppName，默认值为：live。
4. 填写流名称 StreamName，例如：`liveteststream`。
5. 选择地址过期时间，例如：`2020-06-09 15:36:04`。
6. 单击【生成地址】即可。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

### 推流地址说明
推流支持 RTMP 协议，可通过地址生成器功能生成前缀为`rtmp://`的推流地址。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

<h2 id="play">生成播放地址</h2>

### 操作步骤
1. 登录云直播控制台，选择 辅助工具】[【地址生成器】]()，进入地址生成器。
2. 选择生成类型为**播放域名**，并选择您已添加到域名管理的播放域名。
3. 填写 AppName，默认值为：live。
4. 填写流名称 StreamName，例如：`liveteststream`。
5. 选择地址过期时间，例如：`2020-06-09 15:36:04`。
6. 选择是否引用已创建的转码模板。
6. 单击【生成地址】即可。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

