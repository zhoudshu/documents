# web推流
## 操作场景
新流云为您提供 Web 推流功能，可实现快速生成推流地址，在线推流测试直播功能。

注意: 当前功能为试用功能，在一些浏览器不能成功

## 前提条件
- 已登录 [云直播控制台]()。
- 已添加 [推流域名]()。
- 您的设备已安装摄像头，并浏览器支持 Flash 插件调用摄像头权限。

## 操作步骤
1. 登录云直播控制台，选择【辅助工具】 [【Web推流】]()。
2. 在 Web 端推流的页面进行以下设置：
	- 选择推流域名。
	- 填写自定义的流名称 StreamName，例如：`test`。
	- 选择过期时间，例如：`2020-04-13 23:59:59`。
	- 编辑 AppName，用于区分同一个域名下多个 App 的地址路径，默认值为 live。
3. 单击【开始推流】，授权允许调用摄像头，即可开始推流。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_67.png)

4. 若您在【域名管理】中已添加播放域名，即可在下方查看对应生成的播放地址。其中，播放地址由以下4部分组成：

![](https://main.qcloudimg.com/raw/72989c8f55fe7f2ed596bd09882f5a09.png)

支持 RTMP、FLV 和 HLS 协议，查看播放地址：

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_68.png)
