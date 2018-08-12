# CJSoft Ez-Infocollector

## 写些什么呢？
> 想到收集班里同学的电话都很麻烦、不自动，于是想搞个这个东西，初步应支持收集字符串和小文件

- 已达成初步目标

## What's New?
1. 导出标准的Excel文档  
2. 没有更多了  


---
## 关于部署
### 常规主机环境设置
#### linux
##### 1. Py2.7一定要有，建议解决其他依赖之前运行
```
sudo apt-get install libmysqld-dev libmysqlclient-dev
sudo apt-get install python-dev python-pip build-essential
```
##### 2. 然后用pip解决依赖
```
sudo pip install -r requirements.txt
```
#### Windows
##### 1. 搞一个Py2.7，最好自带pip
##### 2. 开cmd，进入项目目录
```
pip install -r requirements.txt
```
##### 3. 上一步如果出红字了的话，而且是mysql-python的问题的话
去[这里](http://www.codegood.com/downloads)下一个对应你Py版本的mysql-python binaries，安装。

进`<Py2.7安装目录>\Lib\site-packages\`看`MySQLdb`文件夹的大小写是否正确，如果和上面所写的不一样，请手动纠正大小写

#### config.py
大部分设置都在**config.py**当中进行
``` python
#coding=utf-8
#
# 服务器设置
# 导出的授权码
aucode="cjsoft"
# 最大上传限制
maxuploadlimit=10*1024*1024
# Session secret
secretkey="s%#$ra4$^q3$^25w&rae24s"
# 默认监听地址和端口
addres="0.0.0.0"
por=8080
# 调试模式开关
debug=False

# Baseuri、不含最后的斜线、含第一个斜线(如果不为空)
baseuri=""
```
大概就是这样，没什么要多说的  
#### 还有mysql
这个东西使用mysql数据库，连接信息并不是在config.py里修改，而是在cjs.py当中修改（有个dumb，为了能够直接在coding.io上部署而偷了一些懒），需要的权限有drop create table，以及select。

### 启动
`python entrance.py`以config.py中设置的端口和IP启动。  
也可以`python entrance.py -h <IP> -p <port>`指定IP和端口  
linux下小号端口别忘sudo

## 关于表单
在`infoforms`文件夹中新建以表单名为名字的文件夹，其中包含文件`main.cjsx`
```json
[
    "id int",
    "name text",
    "age int",
    "nick_name text"
]
```
这种以JSON描述的数据表结构的文件`main.cjsx`，注意由于文件只索引路径，所以务必要使用字符串类型如text。更多知识请移步[w3school](http://www.w3school.com.cn/sql/sql_datatypes.asp)的mysql数据类型部分
  
以及文件`form.html`  
使用html来设计表单，input元素的name应该与`main.cjsx`当中的相对应，顺序不必对应  
这有一个例子  
```html

<label><span>id</span><input type="text" name="id" placeholder="233" id="id" value="" /></label>
<label><span><font size="4">info</font></span><input type="text" name="info" id="info" value="" /></label>
<input type="file" name="fileupload"/>

```

在第一次收到get请求时会初始化数据表，并在表单文件夹中建立`db.lock`，也就是说，删除`db.lock`可以重新初始化表，但是这样会丢失数据，所以需要谨慎。  
**删除表单**：删除表单文件夹就好了。数据库不会自动drop table，，不过也不会影响，因为如果出现同名表单的话会旧数据表会被初始化掉。处女座请自行drop table  
**导出表单**：访问`<baseuri>/export/<表单名字>`，输入config.py当中的aucode，可以导出一个zip，里面有上传的文件还有一个xls  
***
这就是个自娱自乐的项目，不要太在意细节←\_←
***
欢迎联系我！
<egwcyh@qq.com>
