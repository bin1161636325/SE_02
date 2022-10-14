# 二锅骰（微信小程序小游戏）
## 文件内容：
  - Double_dice_front为前端,主要用vue框架实现,是HBuilder集成环境下开发的,在微信小程序上开发的小游戏。
  - Double_dice_end为后端,主要用django框架实现,是python集成环境下开发的,利用虚拟交换机来进行在线对战以及调用API功能。
  - test_front为单元测试前端,主要实现单元测试功能,方便后端编写API文档。
## 开启django：
  - 用django打开Double_dice_end，在Terminal中输入`python manage.py runserver 0.0.0.0:8000`开启端口,注意，服务器ip需要改变，在Edit Configurations里改为本机的ip，然后在setting中配置添加您的ip即可。
## 开启小程序前端：
  - 用HBuilder打开Double_dice_front,运行后打开微信小程序开发软件,然后扫描二维码即可。
## 体验版：
  - ![osMju5JGfwTZYmtv3PjkXPWfs398](https://user-images.githubusercontent.com/78547679/195796930-beafddcf-aae6-4e45-b787-502696ea270d.jpg)
