## 想到收集班里同学的电话都很麻烦、不自动，于是想搞个这个东西，初步应支持收集字符串和小文件
# ez-infocollector
# 关于部署
- 需要mysql，在coding.io演示环境下可以直接部署，但是需要绑定一个mysql服务
- 修改数据库链接信息，请在cjs.py的connect()中修改，或者直接添加环境变量VCAP_SERVICE，格式与coding.io演示平台的相同
- 启动命令行见Procfile

# 关于这个只有我一个人的项目
- 没搞完
- infoforms/下新建文件夹并填写main.cjsx数据表结构、form.html表单源码即可完成一个调查的新建
- 支持验证码，但是不支持验证码错误后返回原来的表单内容，不会搞
- 访问url:export/<调查名称>，输入鉴权码即可导出调查结果，鉴权码在entrance.py的aucode变量中设置
