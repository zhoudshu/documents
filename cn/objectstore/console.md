# 控制台使用指南
## 空间管理
### 创建空间
   在使用对象存储之前，您需要首先创建存储空间以用来存储文件。具体的操作步骤：
   1. 进入 XLS3 管理控制台界面。
   2. 单击新建空间。
   
   **注意：存储空间的命名必须符合命名规范，同时创建后不支持更改存储空间名称。**
   
   **存储空间的命名规则如下：**
   - 字符长度至少为三位，
   - 仅支持英文小写、数字、-、.
   - 且首位末位不得为-、.
   
   
具体过程如下：

![创建存储空间](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_01.png)

在弹出的对话框中，选择需要的地理区域，输入对应的空间名称，点击”确认“ 按钮，

![创建空间对话框](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_02.png)

即创建完成。

### 空间概况
空间创建完毕后，点击空间的详情链接，进入空间的首页，可看到空间基本信息：

基本信息
- 所属区域
- 创建时间

使用用量
- 当前总存储量 
- 近30天下载总量   
- 近30天总API请求
   
![空间详情](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_03.png)

### 空间删除

如果您不再需要存储空间，请将其删除以免进一步产生费用。删除存储空间之前**请确保其中存储的文件已经全部清空**，否则无法删除存储空间。
具体步骤如下：
1. 点击左侧的导航菜单“存储空间”
2. 选中待删除的存储空间，点击右侧的【删除】按钮。

![删除空间入口](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_04.png)

3. 弹出删除空间对话框，点击确认，即可删除空间（删除空间之前，需要先删除完空间内的所有文件）

![删除空间对话框](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_05.png)

### 空间列表
如果创建的空间比较多，可以使用空间的查询功能，过滤需要的空间名称

![空间查询](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_06.png)

## 内容管理
### 创建目录
内容管理包含对存储文件的管理和维护，可以对目录进行创建操作，来分类和区分文件内容

操作步骤：
1. 点击具体空间进入内容管理页面。
2. 点击创建目录

![创建目录入口](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_07.png)

3. 弹出对话框，输入目录名称并且选择至少一个文件上传，然后提交，目录创建完成

![创建目录对话框](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_08.png)

**注：**

- 目录名称不可以为'..', 且不准包含以下字符: '/''@'
- 创建文件夹，需上传至少一个文件

### 文件管理
#### 文件列表

可以显示当前空间的所有文件列表，如下图：

![文件列表](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_09.png)
#### 上传文件

操作步骤：
1. 点击具体存储空间进入内容管理页面。
2. 点击进入已经存在的目录中
3. 点击上传按钮

![上传文件入口](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_10.png)

4. 弹出上传对话框，支持多文件上传

![上传文件操作](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_11.png)

5. 点击确认，开始上传文件

#### 删除文件

选定需要删除的文件，点击删除操作

![删除文件入口](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_13.png)

弹出删除对话框

![删除文件对话框](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_14.png)

点确认即完成删除

#### 下载文件

选定需要下载的文件，点击”下载“操作

![下载入口](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_15.png)
#### 文件详情

选定需要查看详情的文件，点击”详情“操作，可以设置外链地址的过期时间

![文件详情](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_16.png)

展示的文件详情包括：文件名，存储类型，设置外链地址的过期时间，外链地址

### 文件搜索
操作方法：

在内容管理子页面的右上面的资源搜索栏中进行资源搜索

![资源搜索](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_17.png)

**注意：**
**目前资源搜索仅支持资源前缀匹配，不支持通配符和后缀匹配**

## 概览
 
   主要是展示当前帐号的使用总览
   
   概览总述：
   
   ![数据汇总](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_18.png)
   
   上述图包含四个汇总指标，详见如下：
   
   - 当前总存储量 
   
   当前帐号存储的内容总量
   - 存储空间数量
   
   当前帐号使用的bucket的数量
   - 近30天总API请求
   
   当前帐号近30天api的调用次数
   - 近30天下载总量
   
   当前帐号近30天下载的总字节数
   
   曲线图：
   
   ![数据曲线图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_19.png)
   
   上述曲线图包含三个指标的图，详见如下：
   
   - 存储容量曲线图
   
   展示近30天的存储容量变化曲线图
   - 下载流量曲线图
   
   展示近30天的下载流量变化曲线图
   - API请求数
   
   展示近30天的API调用变化曲线图
## 报表中心
   此菜单包含所有统计分析的内容
   ### 存储容量
   报表的查询条件包括地区（region），存储空间（bucket）和时间。您可以手动选择某个region的某个具体空间，统计周期默认为近30天，您可以选择近7天、当月，也可以自定义起止日期。展示如下图：
   
   ![存储容量查询](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_20.png)
   
   存储容量报表页以折线图形式展现指定时间内的存储总量、新增量以及删除量，您可以点击相应的文字可使对应数据展现或隐藏。
   
   ![存储容量曲线图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_21.png)
   
   除折线图外，还有一个环状图，用于展现各存储空间所占比：统计用户账户下各个空间的存储容量比例。
   
   如下图所示
   
   ![存储容量环状图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_22.png)
   
   您可将鼠标移至环状图上查看详细信息：
   
   ![存储容量详情](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_23.png)
   
   ### 存储流量
   存储流量的报表，查询条件包括地区（region），存储空间（bucket），流量类型和时间。您可以手动选择某个region的某个具体空间；统计周期默认为近30天，可选择近7天、当月，您也可以自定义起止日期。
   
   ![存储流量查询](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_24.png)
   
   存储流量报表页以折线图形式展现指定时间内的上传流量和下载流量,您可点击相应的文字可使对应数据展现或隐藏。
   
   ![存储流量曲线图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_25.png)
   
   除折线图外，还有四个环状图，用于展现各isp占比、各地区占比、各bucket上传占比、各bucket下载占比：
   
   isp占比：统计用户账户下各个isp的流量比例
   
   地区占比：根据IP统计用户账户下不同区域的流量变化比例
   
   bucket上传占比：统计用户账户下各个空间的上传流量比例
   
   bucket下载占比：统计用户账户下各个空间的下载流量比例 如下图：
   
   ![存储流量环状图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_26.png)
   ![存储流量环状图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_26_2.png)
   
   ### 带宽
   带宽的报表，您可以手动选择某个region的某个具体空间，带宽类型和时间；统计周期默认为近30天，可选择近7天、当月，您也可以自定义起止日期。
   
   ![带宽查询](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_27.png)
   
   带宽报表页以折线图形式展现指定时间内的上传带宽趋势和下载带宽趋势,您可点击相应的文字可使对应数据展现或隐藏
   
   ![带宽曲线图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_28.png)
   
   ### 请求次数
   请求次数的报表，查询条件包括地区（region），存储空间（bucket），流量类型和时间。您可以手动选择某个region下的某个具体空间；统计周期默认为近30天，可选择近7天、当月，也可以自定义起止日期。
   
   ![请求次数查询](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_29.png)
   
   报表页以折线图形式展现指定时间内的GET请求数和PUT请求数,点击相应的文字可使对应数据展现或隐藏
   
   ![请求次数曲线图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_30.png)
   
   除折线图外，还有三个环状图，用于展现各isp占比、各地区占比、各bucket占比  
   isp占比：统计用户账户下各个isp的请求次数比例
   地区占比：根据IP统计用户账户下不同区域的请求次数比例
   bucket占比：统计用户账户下各个空间的请求次数比例
   
   ![请求次数环状图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_31.png)
   
   您可将鼠标移至环状图上查看详细信息：
   
   ![请求次数详情](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_32.png)
   
   ### 数据取回量
   数据取回量报表，只支持查询标准存储的数据取回量（标准HTTP Get的下载量），查询条件包括地区（region），存储空间（bucket）和时间。您可以手动选择某个具体空间，统计周期默认为近30天，您可以选择近7天、当月，也可以自定义起止日期。展示如下图：
   
   ![数据取回量查询](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_33.png)
   
   数据取回量报表页以折线图形式展现指定时间内的数据取回量,您可点击相应的文字可使对应数据展现或隐藏。
   
   ![数据取回量曲线图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_34.png)
   
   除折线图外，还有一个环状图，用于展现各存储空间所占比：统计用户账户下各个空间的存储容量比例。
   
   ![数据取回量环状图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_35.png)
 
   ### 服务质量
   服务质量的报表，您可以手动选择某个region下的某个具体空间，统计周期默认为近30天，可选择近7天、当月，您也可以自定义起止日期。
   
   ![服务质量查询](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_36.png)
   
   服务质量报表页以柱状图形式展现指定时间内的服务情况：
   
   ![服务质量曲线图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_37.png)
   
   除折线图外，还有四个环状图，用于展现各返回占比、异常各Bucket占比、异常返回各isp占比、异常返回各地区占比

   ![服务质量环状图](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_38.png)
   
   ### 业务分析
   业务分析的报表，您可以手动选择某个region下的某个具体空间， 业务分析报表支持Object\Referer\IP\UA的流量&请求统计。
   
   ![业务分析查询](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_39.png)
   
   #### Object统计示例：
   - Object流量统计
   
   ![Object流量统计](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_40.png)
   
   - Object请求统计
   
   ![Object请求统计](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_41.png)
   
   #### Referer统计示例：
   - Referer流量统计
   
   ![Referer流量统计](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_42.png)
   
   - Referer请求统计
   
   ![Referer请求统计](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_43.png)
   
   #### IP统计示例：
   - IP流量统计
   
   ![IP流量统计](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_44.png)
   
   - IP请求统计
   
   ![IP请求统计](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_45.png)
   #### UA统计示例：
   - UA流量统计
   
   ![UA流量统计](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_46.png)
   
   - UA请求统计
   
   ![UA请求统计](https://github.com/zhoudshu/documents/blob/main/images/objectstore/objectstore_47.png)
  
