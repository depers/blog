# blog
这是我大二时写的博客系统，那个时候一心想做一个网站，但是苦于Python Web相关的中文教程特别少，所以系统的功能做的都比较简单。该博客系统主要由前台展示系统和后台编辑系统组成。整个系统采用Python的web框架[Django](https://www.djangoproject.com/)+[Xadmin](https://github.com/sshwsfc/xadmin)的组合开发，界面布局风格使用的是[Bootstrap3](http://www.bootcss.com/)。

## 项目演示
### 系统前台
项目演示地址：[http://www.bravedawn.cn/blog/Home/](http://www.bravedawn.cn/blog/Home/)

![前台演示](/resource/one.gif)

### 系统后台

![后台演示](/resource/two.gif)

## 组织结构
blog    
|--apps 编写业务逻辑   
|--blog 项目配置   
|--extra_apps Xadmin文件    
|--media 存放上传的多媒体文件    
|--static 静态文件     
|--templates 网页网页模板     

## 相关技术
|技术|说明|官网|
|--|--|--|
|Django|Python Web框架|[https://www.djangoproject.com](https://www.djangoproject.com)|
|django-pure-pagination|提供分页功能|[https://github.com/jamespacileo/django-pure-pagination/](https://github.com/jamespacileo/django-pure-pagination/)|
|Xadmin|直接可用Django后台管理系统|[http://sshwsfc.github.io/xadmin/](http://sshwsfc.github.io/xadmin/)|
|DjangoUeditor|在Django应用中集成百度Ueditor HTML编辑器|[https://github.com/zhangfisher/DjangoUeditor](https://github.com/zhangfisher/DjangoUeditor)|
|Bootstrap|简洁，直接可用的前端开发框架|[http://www.bootcss.com/](http://www.bootcss.com/)|

## 环境搭建
- 安装python2.7.5、mysql5.6、Nginx1.10.
- 安装相关包
  - 安装virtualenv，`pip install vitualenv`
  - 激活虚拟环境`source env/bin/activate`
  - 进入项目目录，通过` pip freeze > requirements.txt `将本地的虚拟环境安装包相信信息导出来
  - 然后`pip install -r requirements.txt`安装依赖包
- 安装uwsgi，输入`pip install uwsgi`

**注意：安装MySQL-python-1.2.5问题，出现错误：`EnvironmentError: mysql_config not found`**

解决办法：`yum install mysql-devel`
## 部署
### 1.配置nginx文件

- bravedawn.cn.conf

  ```nginx
  upstream django {
  	server 127.0.0.1:8000; # 本地服务端口
  }
  # configuration of the server
  
  server {
  	# the port your site will be served on
  	listen      80;
  	# the domain name it will serve for
  	server_name www.bravedawn.cn; # 配置域名
  	charset     utf-8;
  
  	# max upload size
  	client_max_body_size 75M;   # adjust to taste
  
  	# Django media
  	location /media  {
  	    alias /usr/local/webapp/pythonweb/blog/media; # 设置media文件位置
  	}
  
  	location /static {
  	    alias /usr/local/webapp/pythonweb/blog/static; # 设置static文件位置
  	}
  
  	# Finally, send all non-media requests to the Django server.
  	location / {
  	    uwsgi_pass  django;
  	    include     uwsgi_params; # the uwsgi_params file you installed
  	}
  }
  ```

- 拉取所有需要的static file 到同一个目录

  - 在django的setting.py文件中，添加下面一行内容：

    ```STATIC_ROOT = os.path.join(BASE_DIR, "static/")```

  - 运行命令
    `python manage.py collectstatic`

- 修改setting.py

  ```python
  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = False
  ```

- 重启nginx

### 2.配置文件启动uwsgi

- uwsgi.ini

  ```
   # mysite_uwsgi.ini file
  [uwsgi]
  
  # Django-related settings
  # the base directory (full path)
  chdir=/usr/local/webapp/pythonweb/blog
  # Django's wsgi file
  module=blog.wsgi
  # the virtualenv (full path)
  
  # process-related settings
  # master
  master=true
  # maximum number of worker processes
  processes=10
  # the socket (use the full path to be safe
  socket=127.0.0.1:8000
  # ... with appropriate permissions - may be needed
  # chmod-socket = 664
  # clear environment on exit
  vacuum=true
  virtualenv=/usr/local/webapp/pythonweb/blog_venv
  logto=/tmp/mylog.log
  ```

  注：

  - chdir： 表示需要操作的目录，也就是项目的目录
        
  - module： wsgi文件的路径
        
  - processes： 进程数
        
  - virtualenv：虚拟环境的目录

- 启动uwsgi，输入`uwsgi -i uwsgi.ini &`
## 感谢
[Python升级3.6 强力Django+杀手级Xadmin打造在线教育平台](https://coding.imooc.com/learn/list/78.html)


