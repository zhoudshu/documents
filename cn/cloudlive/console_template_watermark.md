# 水印模板

云直播提供水印功能，通过直播画面叠加水印图片实现视频防盗效果。本文将向您介绍如何通过控制台创建、修改及删除水印模板。

**创建直播水印模板有以下方式：**
- 通过云直播控制台创建水印模板，具体操作请参见 [创建水印模板](#Watermark)。


## 注意事项
- 模板创建成功后，可在推流域名下进行关联。关联成功后20分钟 - 30分钟生效。


<span id="Watermark"></span>
## 创建水印模板

1. 登录云直播控制台，进入【功能配置】>[【水印配置】]()。
2. 单击【+】，新增水印模板。
3. 填写水印名称，仅支持填写中文、英文、数字、_、-，不超过30个字符。
4. 单击【选择图片】上传水印图片。
>! 为了最佳视觉效果，水印应为透明图片 png 格式；图片大小小于2M。
5. 设置水印图片显示位置，可通过以下两种方式进行调节：
	- 在水印图片配置栏上拖动图片位置。
	- 设置位置显示 X 轴方向和 Y 轴方向。
6. 单击【保存】即可。

![](https://docs.zhoudsh.com:9443/images/cloudlive/cloudlive_46.png)


## 修改模板

1. 进入【功能配置】>[【水印配置】]()。
2. 选择您已创建成功的水印模板，并单击右侧的【编辑】，即可进入修改模板信息。
3. 单击【保存】即可。

![](https://docs.zhoudsh.com:9443/images/cloudlive/cloudlive_47.png)

>? 若您需查看水印模板在画面上的效果，可单击【预览】查看。


## 删除模板
若模板已被关联，需要先解绑模板，才可以进行删除操作，具体解绑操作请参见 [解绑水印配置]()。
1. 进入【功能配置】>[【水印配置】]()。
2. 选择您已创建成功的水印模板，单击上方的删除按钮。
3. 确认是否删除当前水印模板，单击【确定】即可成功删除。

![](https://docs.zhoudsh.com:9443/images/cloudlive/cloudlive_48.png)

## 关联域名

具体操作及相关说明，请参见 [域名关联水印模板]()。

