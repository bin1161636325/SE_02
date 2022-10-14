from django.db import models

# Create your models here.
class Playerrank(models.Model):
    # 玩家用户名
    name = models.CharField(max_length=200)

    # 玩家头像
    picture_url = models.CharField(max_length=200, null=True, blank=True)

    # 玩家手机号
    phonenumber = models.CharField(max_length=200)

    # 玩家分数
    point = models.IntegerField()


