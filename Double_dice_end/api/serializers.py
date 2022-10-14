from rest_framework import serializers


# 1. 定义序列化类， 依赖于模型类
# 2. 指定序列化器字段， 字段和模型类的字段一样
# max_length： 校验name存储的字符串的 最大长度
# min_length: 校验name存储的字符串的 最小长度
# 序列化器中的字符串长度，可以不写，只有在反序列化时，才会使用
class PlayerrankSer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20, label="name")
    phonenumber = serializers.CharField(max_length=20, label='phonenumber')
    picture_url = serializers.CharField(max_length=50, label='picture_url')
    point = serializers.IntegerField(label='point', default=0)