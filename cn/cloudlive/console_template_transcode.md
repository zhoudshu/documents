直播转码功能（包含视频转码和音频转码），是指将直播现场推送出来的原始流，在云端转换为不同编码格式、不同分辨率、不同码率的转码流推送给观众，以满足不同网络环境、不同终端设备等各种场景下的播放需求。 本文将向您介绍如何通过控制台创建、修改及删除转码模板。

**创建转码模板有以下方式：**

- 通过云直播控制台创建转码模板，具体操作步骤请参见 [创建标准转码模板](#C_trans)、[创建极速高清转码模板](#C_topspeed)、[创建纯音频转码模板](#C_audio)。


## 注意事项
- 模板创建成功后，可与播放域名进行关联。关联成功后约20分钟 - 30分钟生效。
- 绑定转码模板后，可在对应的直播流 StreamName 后加上 `_转码模板名称` 来生成转码流地址。若同时设置了宽高或长短边，推流原始分辨率尽可能接近设置值的比例，以避免画面拉伸变形。
- 绑定转码模板后，会在对应的模板下显示绑定规则 [解绑模板](#untie)。
- 单个推流域名可关联**多个转码模板**，转码模板不能关联**播放域名**。

<span id="create"></span>
## 创建转码模板
<span id="C_trans"></span>
### 创建标准转码模板

1. 登录云直播控制台，【功能配置】>[【转码配置】]()。
2. 单击【创建转码模板】，选择转码类型为『**标准转码**』，进行如下配置：
	- 基础配置项：包含模板名称、视频码率、画面分辨率等配置项，具体请参见 [标准转码基础配置说明](#C_trans_normal)。
	- 高级配置项（非必填）：单击【高级配置】展开内容即可选择配置，具体请参见 [标准转码高级配置说明](#C_trans_high)。
3. 填写完成后，单击【保存】即可。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

<table id="C_trans_normal">
<tr><th width="20%">标准转码基础配置项</th><th>是否必填</th><th>说明</th></tr>
<tr>
<td>转码类型</td>
<td>是</td>
<td>可选择转码类型，包括<b>标准转码</b>、极速高清转码、纯音频转码。</td>
</tr><tr>
<td>模板名称</td>
<td>是</td>
<td>直播转码模板名称，仅支持纯字母、字母数字组合，不支持纯数字，请输入1个 - 10个字符。</td>
</tr><tr>
<td>模板描述</td>
<td>否</td>
<td>直播转码模板简介描述，仅支持中文、英文、数字、_、-。</td>
</tr><tr>
<td>推荐参数</td>
<td>否</td>
<td>支持<b>流畅、标清、高清</b>三种类型，选择后，系统会自动填入对应的推荐视频码率和视频高度，可自行修改。</td>
</tr><tr>
<td>视频码率 <br>（单位：Kbps）</td>
<td>是</td>
<td>输出平均码率，取值范围：100Kbps - 8000Kbps。<ul style="margin:0">
	<li>1000Kbps以内仅支持整百填写。</li>
	<li>1000Kbps以上仅支持整500填写。</li></ul>
</td>
</tr><tr>
<td>画面分辨率</td>
<td>是</td>
<td>默认【按宽高设置】。<li>输入值为高度值，可切换为【按长短边设置】，输入值为短边值。<li>输入值范围为 0px - 3000px，数值填写需为2的倍数，另一边默认会按分辨率等比例缩放。</td>
</tr></table>


<table id="C_trans_high">
<tr><th width="20%">标准转码高级配置项 </th><th>是否必填</th><th>说明</th></tr>
<tr>
<td>编码方式</td>
<td>否</td>
<td>默认原始码率，可选 H.264 和 H.265 两种编码方式。</td>
</tr><tr>
<td>视频帧率</td>
<td>否</td>
<td>取值范围 0fps - 60fps，不填则使用系统默认值 0fps。</td>
</tr><tr>
<td>关键帧间隔 GOP <br>（单位：s/秒）</td>
<td>否</td>
<td>GOP 设置范围2秒 - 6秒，GOP 越大、延时越高，若不设置则采用系统默认值。</td>
</tr><tr>
<td>参数限制</td>
<td>否</td>
<td>默认关闭，可手动开启。<br>开启参数限制后，当输入的直播流原始参数小于设置的输出参数时，将按照原始参数输出直播流，可以防止低质量直播流被强行拉高参数值，影响实际画面。</td>
</tr></table>


   

<span id="C_topspeed"></span>

### 创建极速高清转码模板
1. 登录云直播控制台，【功能配置】>[【转码配置】](/transcode)。
2. 单击【创建转码模板】，选择转码类型为『**极速高清转码**』进行如下配置：
	- 基础配置项：包含模板名称、视频码率、画面分辨率等配置项，具体请参见 [极速高清转码基础配置说明](#C_topspeed_normal)。
	- 高级配置项（非必填）：单击【高级配置】展开内容即可选择配置，具体请参见 [极速高清转码高级配置说明](#C_topspeed_high)。
3. 单击【保存】即可。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

<table  id="C_topspeed_normal">
<tr><th width="20%">极速高清转码基础配置项</th><th>是否必填</th><th>说明</th>
</tr><tr>
<td>转码类型</td>
<td>是</td>
<td>可选择转码类型，包括标准转码、<b>极速高清转码</b>、纯音频转码。</td>
</tr><tr>
<td>模板名称</td>
<td>是</td>
<td>直播转码模板名称，仅支持纯字母、字母数字组合，不支持纯数字，请输入3个 - 10个字符。</td>
</tr><tr>
<td>模板描述</td>
<td>否</td>
<td>直播转码模板简介描述，仅支持中文、英文、数字、_、-。</td>
</tr><tr>
<td>推荐参数</td>
<td>否</td>
<td>支持<b>流畅、标清、高清</b>三种类型，选择后，系统会自动填入对应的推荐视频码率和视频高度，可自行修改。</td>
</tr><tr>
<td>视频码率 <br>（单位：Kbps）</td>
<td>是</td>
<td>输出平均码率，取值范围：100Kbps - 8000Kbps。<li>1000Kbps以内仅支持整百填写。</li><li>1000Kbps以上仅支持整500填写。</li></td>
</tr><tr>
<td>画面分辨率</td>
<td>是</td>
<td>默认【按宽高设置】。<li>输入值为高度值，可切换为【按长短边设置】，输入值为短边值。</li><li>输入值范围为 0px - 3000px，数值填写需为2的倍数，另一边默认会按分辨率等比例缩放。</li></td>
</tr>
</table>

<table  id="C_topspeed_high">
<tr><th width="20%">极速高清转码高级配置项</th><th>是否必填</th><th>说明</th>
</tr><tr>
<td>编码方式</td>
<td>否</td>
<td>默认原始码率，可选 H.264 和 H.265 两种编码方式。</td>
</tr><tr>
<td>视频帧率</td>
<td>否</td>
<td>取值范围 0fps - 60fps，不填则使用系统默认值 0fps。</td>
</tr><tr>
<td>关键帧间隔GOP <br>（单位：s/秒）</td>
<td>否</td>
<td>GOP 设置范围2秒 - 6秒，GOP 越大、延时越高，若不设置则采用系统默认值。</td>
</tr><tr>
<td>参数限制</td>
<td>否</td>
<td>默认关闭，可手动开启。<br>开启参数限制后，当输入的直播流原始参数小于设置的输出参数时，将按照原始参数输出直播流，可以防止低质量直播流被强行拉高参数值，影响实际画面。</td>
</tr></table>

<span id="C_audio"></span>
### 创建纯音频转码模板

1. 登录云直播控制台，【功能配置】>[【转码配置】]()。
2. 单击【创建转码模板】，选择可用类型为『**纯音质**』，填写 [配置项](#C_audio_normal)，并单击【保存】即可。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

<table id="C_audio_normal">
<tr><th width="20%">纯音频转码基础配置项</th><th>是否必填</th><th>说明</th>
</tr><tr>
<td>转码类型</td>
<td>是</td>
<td>可选择转码类型，包括标准转码、极速高清转码、<strong>纯音频转码</strong>。</td>
</tr><tr>
<td>模板名称</td>
<td>是</td>
<td>直播转码模板名称，仅支持纯字母、字母数字组合，不支持纯数字，请输入3个 - 10个字符。</td>
</tr><tr>
<td>模板描述</td>
<td>否</td>
<td>直播转码模板简介描述，仅支持中文、英文、数字、_、-。</td>
</tr>
</table>

<span id="related"></span>
## 关联域名
1. 登录云直播控制台，进入【功能配置】>[【转码配置】]()。
2. 在域名绑定窗口中，选择您需绑定的**转码模板**及**推流域名**，单击【确定】即可绑定成功。
![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)
>?支持通过单击【添加】为当前模板绑定多个推流域名。


<span id="modify"></span>
## 修改模板
1. 登录云直播控制台，进入【功能配置】>[【转码配置】]()。
2. 选择您已创建成功的转码模板，并单击右侧的【编辑】，进入修改模板信息。
3. 单击【保存】即可。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

<span id="delete"></span>
## 删除模板
>!   若模板已被关联，需要先 [解绑模板](#untie)，才可以进行删除操作。 

1. 登录云直播控制台，进入【功能配置】>[【转码配置】]()。
2. 选择未关联推流域名的转码模板，单击【删除】。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

3. 确认是否删除当前转码模板，单击【确定】即可成功删除。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

