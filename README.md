#My Blog site
###　　下面我来简单的介绍一下我的这个博客系统，主要由前台展示系统和后台编辑系统组成。整个系统采用python2.7环境下的Django1.9.8，界面布局使用的是Bootstrap3。后台实现是Django的Xadmin。

##目录一览
　**blog/</br>
　　apps/</br>
　　　article/</br>
　　　users/</br>
　　blog/</br>
　　extra_apps/</br>
　　media/</br>
　　static/</br>
　　templates/</br>
　　manage.py</br>
　　requirements.txt**</br>
		
## 一、前台概览
### 前台的主要交互逻辑是放在apps这个目录下面的,由于个人博客内容和逻辑较为简单所以只配置了两个子程序模块。

![](http://i.imgur.com/R6UvQ36.png)

## 二、后台实现
### 后台使用的是Xadmin，我直接从github将xadmin的代码植入了我的项目，并在xadmin中实现了百度的Ueditor来进行文本的编辑。
![](http://i.imgur.com/SllJtPi.png)




