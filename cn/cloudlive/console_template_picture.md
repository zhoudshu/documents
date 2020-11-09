
云直播提供截图功能，支持通过控制台配置的截图模板，推流域名关联模板后，在推流过程中截取直播画面，将直播截图存储至后端存储系统中。若该推流域名已关联回调配置，即可在直播过程中触发回调事件后，系统主动发送请求到客户服务器，客户服务器负责应答请求。验证通过后即可获取回调信息的 JSON 数据包。
本文将向您介绍如何通过控制台创建、修改及删除截图模板。

其中，创建截图模板有以下方式：

- 通过云直播控制台创建模板，具体操作步骤请参见 [创建截图模板](#Screenshot)。

## 注意事项

- 截图功能可单独开启使用

<span id="Screenshot"></span>
## 创建截图模板

1. 登录云直播控制台，【功能配置】>[【截图配置】]()。
2. 单击【+】，填写配置项，并单击【保存】即可。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

<table>
<thead><tr><th width="15%">配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>模板名称</td>
<td>截图模板名称，仅支持填写中文、英文、数字、_、-，不超过30个字符。</td>
</tr><tr>
<td>模板描述</td>
<td>截图模板介绍描述，仅支持填写中文、英文、数字、_、-，不超过100个字符。</td>
</tr><tr>
<td>截图间隔</td>
<td>推流过程中自动截图间隔时间，默认为10秒，取值范围：5秒 - 300秒。<br>说明：必须为5的倍数</li></td>
</tr><tr>
<td>启用智能</td>
<td>可选择是否开启功能，启用智能后，需配置回调才可收到结果。</td>
</tr><tr>
<td>可选择『当前账号』或『其他账号』。</td>
</tr><tr>
<td>文件名</td>
<td>截图文件名格式，可自定义组合参数拼装而成。默认为：<code>{StreamID}-screenshot-{Hour}-{Minute}-{Second}-{Width}x{Height}{Ext}</code>，其中：
	<ul style="margin:0">
		<li>{AppName} ：推流 AppName</li>
		<li>{PushDomain} ：推流域名</li>
		<li>{StreamID} ：流 ID</li>
		<li>{Year} ：截图时间（年）</li>
		<li>{Month} ：截图时间（月）</li>
		<li>{Day} ：截图时间（日）</li>
		<li>{Hour} ：截图时间（时）</li>
		<li>{Minute} ：截图时间（分）</li>
		<li>{Second} ：截图时间（秒）</li>
		<li>{Width} ：图片宽</li>
		<li>{Height} ：图片高</li><li>{Ext} ：扩展名（.jpg）</li>
	</ul>说明：只允许[a-z，A-Z，0-9]和符号-，!，_，.，*以及占位符。
	<br>举例：填写文件名格式为：<code> {Year}-{Month}-{Day}- {Hour}-{Ext}</code>，则在2020年01月01日14:00:00 自动截取直播画面，存储到 COS 中的文件名为：2020010114.jpg</td>
</tr>
</tbody></table>


## 修改模板

1. 进入【功能配置】>[【截图配置】]()。
2. 选择您已创建成功的截图模板，并单击右侧的【编辑】，即可进入修改模板信息。
3. 单击【保存】即可。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

## 删除模板

若模板已被关联，需要先解绑模板，才可以进行删除操作，具体解绑操作请参见 [解绑截图配置]()。

1. 进入【功能配置】>[【截图配置】]()。
2. 选择您已创建成功的截图模板，单击上方的删除按钮。
3. 确认是否删除当前截图配置模板，单击【确定】即可成功删除。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)



## 关联域名

 具体操作及相关说明，请参见 [截图配置]()。 
