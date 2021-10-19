# 关于 Django 项目

## 安装 Python

## 安装 Django

> pip install Django

## 查看 Django 版本

> python3 -m django --version

## 创建 django 项目

> django-admin startproject siteName

## 新建 django 项目目录结构

```js
/*
    siteName-----------------django项目根目录，不会影响django项目
        manage.py------------命令行工具，用于django项目交互<vhttps://docs.djangoproject.com/en/3.2/ref/django-admin/>
        siteName-------------项目真正的python包目录
            __init__.py------告诉python，当前目录是一个python包
            settings.py------django项目配置文件<https://docs.djangoproject.com/en/3.2/topics/settings/>
            urls.py----------django项目的URL声明文件<https://docs.djangoproject.com/en/3.2/topics/http/urls/>
            asgi.py----------An entry-point for ASGI-compatible web servers to serve your project<https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/>
            wsgi.py----------An entry-point for WSGI-compatible web servers to serve your project<https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/>
 */
```

## 启动 Python 服务

> python3 manage.py runserver
>
> 指定端口：python3 manage.py runserver 8080

## python manage.py migrate

## Django 中的 projects 和 app

> An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

### projects 就是环境，整个项目以及 Django 的基础配置，可以理解为就是 siteName

## 创建 Django App：python manage.py startapp polls

### path()函数接收 4 个参数，route、view、kwargs、name

## 明天继续<https://docs.djangoproject.com/en/3.2/intro/tutorial02/>
