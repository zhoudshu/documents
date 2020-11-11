使用云直播服务，至少需要**2个**域名，一个作为推流域名，一个作为播放域名，且推流和播放不能使用相同的域名。
如果需要录制和截图功能，需要创建**静态域名**，文件的下载与CDN加速需要使用此域名提供服务。

# 域名管理

## 域名添加
### 前提条件
1. 已开通 [新流云直播服务](https://ccms.zhoudsh.com:9443/control)。
2. 已准备域名，并完成域名备案。


### 操作步骤
#### 步骤1：添加自有域名
1. 登录  [云直播控制台](https://ccms.zhoudsh.com:9443/control)，选择【域名管理】。
2. 单击【添加域名】，进入域名添加页进行如下配置：
	1. 若您需添加**推流域名**：输入域名，选择域名类型为【推流域名】，单击【确定】即可。
	2. 若您需添加**播放域名**：输入域名，选择域名类型为【播放域名】，单击【确定】即可。
	3. 若您需添加**静态域名**：输入域名，选择域名类型为【静态域名】，单击【确定】即可。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_02.png)

>!注意
>- 域名的位数限制为29位，暂不支持大写的域名，请输入不超过**29位**的小写域名地址。

#### 步骤2：完成域名 CNAME
域名添加成功后，系统会为您自动分配一个 CNAME 域名（例子以`.zhoudsh.cn`为后缀）。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受云直播服务。

>! 若您需要对已添加成功的域名进行管理，请参见 [域名管理](https://ccms.zhoudsh.com:9443/control/#/layout/live/livedomain/1604569411261)。


域名添加成功后，就可以进入下一步操作：

## 查看域名
您可以在[【域名管理】](https://ccms.zhoudsh.com:9443/control/#/layout/live/livedomain/1604569411261)页面，查看已添加域名 CNAME 配置状态、所属类型、域名开始时间。若您需要查看域名详情，单击需要查看的域名或其右侧【管理】，即可进入查看域名信息。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

## 配置域名
### 配置推流域名
为了保护直播推流的信息安全，云直播推流域名默认开启推流鉴权。您可通过推流地址详情页中的推流地址生成器，在线生成对应的推流地址。通过使用推流地址在线推流，实现直播流传输到云直播服务，即实现直播视频上传。

#### 注意事项

- 仅支持生成 RTMP 格式的推流地址。
- 生成的推流地址在设定的过期时间内均可使用，过期后需要重新生成新的推流地址。

#### 鉴权配置
1.  进入[【域名管理】](https://ccms.zhoudsh.com:9443/control/#/layout/live/livedomain/1604569411261)，单击需配置的**推流域名**或【管理】进入域名详情页。 
2.  单击【推流配置】，查看【推流配置】标签，单击右侧的【编辑】。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

3.  进入推流鉴权配置页，单击

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png) 按钮选择开启/关闭推流鉴权。

4. 修改 KEY ，单击【保存】即可成功生效。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

#### 推流地址生成器

#### 操作步骤

1. 进入[【域名管理】](https://ccms.zhoudsh.com:9443/control/#/layout/live/livedomain/1604569411261)选择需配置的推流域名或单击【管理】，进入域名详情页。
2. 选择【推流配置】>【推流地址生成器】，进行如下配置：
   1. 选择过期时间，例如：`2020-10-31 23:59:59`。
   2. 填写自定义的流名称 StreamName，例如：`liveteststream`。
   3. 单击【生成推流地址】即可生成带着 StreamName 的 RTMP 推流地址。
  
  ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

3. 配置成功后，可在 [【流管理】]( https://ccms.zhoudsh.com:9443/control/#/layout/live/onlinestream/1604570470005) 进行测试、禁用和删除。
4. 生成推流地址即可进行直播推流开播，但是观看直播要获取播放地址，具体请参见 【播放配置】 章节


#### 推流地址说明

RTMP 推流地址格式为：
```
rtmp://domain/AppName/StreamName?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)

rtmp://livepush.test.video.zhoudsh.com/live/test?txSecret=32a4e60f3c882797f4126e102643e3e1&txTime=5FA3CE08
```

其中：
- `domain`：直播推流域名。
- `AppName`：直播的应用名称，默认为 live，可自定义。
- `StreamName`：流名称，用户自定义，用于标识直播流。
- `txSecret`：开启推流鉴权后生成的鉴权串。
- `txTime`：推流地址设置的时间戳，是控制台推流地址的有效时间。

#### 录制配置
直播推流默认关闭录制功能，本文将向您介绍如何对指定推流域名关联录制模板开启录制功能，以及关联成功后如何解绑模板关闭域名录制功能。

##### 使用限制
- 录制的视频文件默认保存至后端存储系统，详见 【媒资管理】，
- 如果需要存储海量数据，建议使用产品 [对象存储](https://ccms.zhoudsh.com:9443/control/#/layout/cos/objectoverview) 控制台，需要提前开通对象存储服务。
- 模板关联成功后，指定推流域名下的推流地址开启录制功能。

##### 关联录制模板
1.	进入[【域名管理】]()，单击需配置的**推流域名** 点击【管理】进入域名详情页。
2.	选择【模板配置】页签，单击【录制配置】标签右上角的【编辑】。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

3. 选择录制配置模板，单击【保存】即可。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

##### 解绑录制模板
1. 进入[【域名管理】]()，单击需配置的**推流域名** 点击【管理】进入域名详情页。
2. 选择【模板配置】页签，单击【录制配置】标签右上角的【编辑】。
3. 单击取消相应模板的勾选，单击【保存】即可。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)


##### 录制文件获取
录制文件生成后自动存储到后端存储系统，详细参见 【媒体管理】录制信息章节：

#### 截图配置
直播推流默认关闭截图功能，本文将向您介绍如何对指定推流域名关联截图模板开启截图功能，以及关联成功后如何解绑模板关闭截图功能。

##### 注意事项
- 模板配置完后约**20分钟 - 30分钟**生效。

##### 关联截图模板

1. 进入[【域名管理】]()，单击需配置的**推流域名** 点击【管理】进入域名详情页。
2. 选择【模板配置】，单击【截图配置】标签右上角的【编辑】。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

3. 选择截图配置模板。单击【保存】即可完成配置。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

##### 解绑截图模板
1. 进入[【域名管理】]()，单击需配置的**推流域名** 点击【管理】进入域名详情页。
2. 选择【模板配置】页签，单击【截图配置】标签右上角的【编辑】。
3. 单击取消相应模板的勾选，单击【保存】即可。
   
 ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

#### 水印配置
直播推流默认关闭水印功能，本文将向您介绍如何对指定推流域名关联水印模板开启水印功能，以及关联成功后如何解绑模板关闭水印功能。
 
##### 注意事项
- 模板配置完后约20分钟 - 30分钟生效。
- 模板关联成功后，指定推流域名下的推流地址开启水印功能。

##### 关联水印模板
1.	进入[【域名管理】]()，单击需配置的**推流域名** 点击【管理】进入域名详情页。
2.	选择【模板配置】页签，单击【水印配置】标签右上角的【编辑】。
    
![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

4.	选择水印配置模板，单击【保存】即可。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

>! 您可通过单击操作栏的【预览】查看水印效果。

##### 解绑水印模板
1. 进入[【域名管理】]()，单击需配置的**推流域名** 点击【管理】进入域名详情页。
2. 选择【模板配置】页签，单击【水印配置】标签右上角的【编辑】。
3. 单击取消相应模板的勾选，单击【保存】即可。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

#### 转码配置
直播播放默认通过源码率输出，若需要对播放码率进行限制或者设定，可对推流域名进行转码模板关联。本文将向您介绍如何在推流域名下进行转码模板关联与解绑。

##### 注意事项
- 模板配置完后约20分钟 - 30分钟生效。
- 指定转码模板后，后台将生成对应码率的不同播放地址，方便用户选择调用。推流原始分辨率尽可能接近原比率以避免画面拉伸变形。
- 第一次访问新的码率地址时，首位触发链接的访问用户会感到加载时间稍长，属正常现象。


##### 关联转码模板
1. 进入[【域名管理】]()，单击需配置的**推流域名**或右侧的【管理】进入域名详情页。
2. 选择【模板配置】页签，单击【转码配置】标签右上角的【编辑】。
3. 选择不同的转码配置模板，为该域名设定模板设置的编译方式和码率。
4. 单击【保存】即可。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

##### 转码播放地址说明
配置转码模板后，播放 URL 需增加转码模板名称，拼接方式为：**播放地址_转码模板名称**。若未拼接转码模板名称，则播放的为原始直播流内容。

**例如：**播放域名关联的转码模板名称为 **hd**，原始播放地址为：
<pre>
http://domain/AppName/StreamName.flv?txSecret=Md5(key+<b style="color:yellow;">StreamName</b>+hex(time))&txTime=hex(time) 
</pre>
若您需获取播放转码后的视频，则需重新生成的新的播放地址，如下：
<pre>
http://domain/AppName/<b style="color:yellow;">StreamName_hd</b>.flv?txSecret=Md5(key+<b style="color:yellow;">StreamName_hd</b>+hex(time))&txTime=hex(time)
</pre>

<span id="Untie"></span>
##### 解绑转码模板
1. 进入[【域名管理】]()，单击需配置的推流域名或右侧的【管理】，进入域名详情页。
2. 选择【模板配置】页签，选择【转码配置】。
3. 单击右侧的【编辑】，取消相应模板的勾选。
4. 然后单击【保存】，即可取消模板与域名的关联。
    
   ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

>? 若需删除模板，可在解绑模板后，进入【功能模板】>[【转码配置】]()进行删除操作，具体请参见 [删除模板]()。

#### 回调配置

直播推流默认关闭回调功能，当推流域名已关联回调配置后，该域名下所有的推流地址都均开启回调功能。

当直播过程中根据所配置模板事项触发回调事件，系统主动发送请求到客户服务器，客户服务器负责应答请求。i

验证通过后即可获取含鉴权回调信息的 JSON 数据包。

本文将向您介绍如何对指定推流域名关联回调模板开启回调功能，以及关联成功后如何解绑模板关闭域名回调功能。


##### 关联回调模板<span id="related"></span>
1.	进入[【域名管理】]()，单击需配置的**推流域名** 点击【管理】进入域名详情页。
2.	选择【模板配置】页签，单击【回调配置】标签右上角的【编辑】。
3.	选择指定对应的回调模板，单击【保存】即可。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

##### 解绑回调模板<span id="untie"></span>

1. 进入[【域名管理】]()，单击需配置的**推流域名** 点击【管理】进入域名详情页。
2. 选择【模板配置】页签，单击【回调配置】标签右上角的【编辑】。
3. 取消关联模板的勾选，单击【保存】即可。
    
    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

### 配置播放域名

#### 操作场景
域名推流成功后，您可进入云直播控制台，使用播放地址生成器录入与推流地址 StreamName 相同的 StreamName，生成对应流的播放地址，即可通过该播放地址查看直播画面。

#### 操作步骤
1. 选择[【域名管理】](https://ccms.zhoudsh.com:9443/control/#/layout/live/livedomain/1604569411261)，单击需配置的**播放域名** 点击【管理】进入域名管理。
2. 选择【播放配置】>【播放地址生成器】，进行如下配置：
	1. 选择过期时间，例如：`2019-02-28 23:59:59`。
	2. 填写自定义的流名称 StreamName，例如：`liveteststream`。播放地址 StreamName 要与推流地址 StreamName 一致才能播放对应的流。
	3. 单击【生成播放地址】即可。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

3. 若您的播放域名未开启播放鉴权，您还可以在【播放配置】>【播放地址】标签下，查看该播放域名下 RTMP、FLV、HLS 这三种播放地址。替换播放地址中的 StreamName（流名称）关联推流地址，关联后即可通过播放地址查看直播画面。

    ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

#### 播放地址
###### 1. 播放地址生成规则
```
RTMP格式：rtmp://domain/AppName/StreamName?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)
FLV格式：http://domain/AppName/StreamName.flv?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)
M3U8格式：http://domain/AppName/StreamName.m3u8?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)
```
- **domain**：自有已备案播放域名。
- **AppName**：直播的应用名称，默认为 live，可自定义。
- **StreamName**：流名称，用户自定义，用以标识直播流。
- **txSecret**：开启播放鉴权后生成的鉴权串。
- **txTime**：播放地址设置的时间戳，用以控制台播放地址的有效时间。

>!
>- 若您开启了域名鉴权，实际过期时间等于 txTime + 鉴权有效时间。
>- 控制台为了方便使用，设置的时间即为实际过期时间。若您开启了域名鉴权，计算播放地址时会按照公式倒推出 txTime。

##### 2. 转码后的直播地址
若播放域名配置了转码模板，同时需播放转码后的直播流，转码的播放地址拼接方式为：在原始播放地址中的 StreamName 后增加`_转码模板名称`。

例如：原始播放地址为

`http://domain/AppName/StreamName.flv?txSecret=Md5(key+StreamName+hex(time))&txTime=hex(time)`

 ，关联的转码模板名称为`hd`，

则转码播放地址为

`http://domain/AppName/StreamName_hd.flv?txSecret=Md5(key+StreamName_hd+hex(time))&txTime=hex(time)`。

#### 访问控制
云直播内容默认为公开资源，您在获取播放地址后即可访问直播内容。若需要对直播内容进行访问控制，可通过鉴权设置来实现直播资源的内容保护。

##### 配置原理
URL 鉴权的原理是云直播客户通过鉴权配置生成加密 URL，并将此 URL 提供给用户，用户采用加密 URL 对云直播加速节点发起请求后，直播加速节点对其权限信息进行校验以判断请求是否合法。若请求合法，将返回正常内容，若请求非法将被拒绝，以此实现对直播资源的保护。

##### 操作步骤
1. 选择[【域名管理】](https://ccms.zhoudsh.com:9443/control/#/layout/live/livedomain/1604569411261)，单击需做鉴权配置的**播放域名** 点击【管理】进入域名管理。
2. 在【访问控制】>【鉴权配置】，单击【编辑】进入鉴权配置页。
3. 在鉴权配置页进行如下设置：
	1. 单击开启播放鉴权。
	2. 填写自定义鉴权 Key，例如：`testlive`。
	3. 单击【保存】，即可保存配置。

>?
>- 播放域名的播放鉴权默认为**关闭**状态。
> - **鉴权 Key**：用户自定义设置，支持大小写字母和数字.
> - **有效时间**：签名的有效时间，时间戳为十六进制 UNIX 时间。

  ![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

>! 开启播放域名的鉴权设置后，原有播放 URL 将无法直接访问，会返回403。开启此功能，请确保您的业务兼容以下鉴权算法，以免影响您的直播业务。

#### 高级配置

如果您有自建源站和直播源内容，并且需要通过新流云进行直播播放，可以通过为云直播播放域名设置源站信息来回源拉取直播内容。配置成功后，您可通过云直播回源拉流并进行直播内容分发。本文档将指导您如何设置源站信息。

##### 注意事项
   -  配置好相关信息后，源站设置会在**30分钟**-**1个小时**左右生效。
   - 开启源站配置功能后，该播放域名的不支持通过 StreamName 匹配其他推流域名进行拉流，而且该域名无法使用水印、转码、录制、截图、鉴黄等功能。 

##### 操作步骤
1. 进入[【域名管理】]()，单击需配置的**播放域名** 点击 右侧的【管理】进入域名详情页。
2. 选择【高级配置】，查看【源站设置】标签。
3. 单击源站设置模块的【编辑】，即可开始设置以下源站信息：
	1. 打开【源站设置】滑动开关。
	2. 选择【回源类型】
 	3. 如果选择【自定义回源】 输入 IP 地址或输入域名。
	4. 如果选择【系统回源】 选择域名。
	5. 单击【保存】即可保存配置。

>?**回源协议**指云直播回源拉流时支持的格式。**播放协议**指直播内容通过直播 CDN 分发时的播放协议。
>- 回源协议为 FLV/RTMP 时，播放协议支持 RTMP/FLV/HLS。
>- 回源协议为 HLS 时，播放协议只支持 HLS。
>- 回源协议不支持多选，播放协议支持多选。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)


## 禁用域名
若您需要禁用域名，单击需要禁用的域名右侧【禁用】，在弹窗中确认是否禁用当前域名。单击【确定】后，当该域名状态由**“已启用”**变为**“未启用”**，表示域名禁用成功。

>? 禁用域名后该域名无法访问，重新启用后可正常访问，播放域名和推流域名操作相同。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

## 启用域名
若您需要将已禁用的域名重新启用，单击所需启用的域名右侧【启用】，当该域名状态由“未启用”变为“已启用”，表示域名禁用成功。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

## 删除域名
若您需要删除域名，单击目标域名右侧的【删除】，在弹窗中确认是否需要删除当前域名，单击【确定】后即可删除域名。

![](https://github.com/zhoudshu/documents/blob/main/images/cloudlive/cloudlive_03.png)

