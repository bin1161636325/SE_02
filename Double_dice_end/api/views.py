import random
import sqlite3
import json

from .serializers import PlayerrankSer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Playerrank
# Create your views here.

# 在线对战
def index(request):
    group_num = request.GET.get('num')
    return render(request, 'index.html', {"qq_group_num": group_num})

# 获取总分数
def CalculateScore(My_chess, Enemy_chess):
    # 初始化
    my_col1_point = 0
    my_col2_point = 0
    my_col3_point = 0
    enemy_col1_point = 0
    enemy_col2_point = 0
    enemy_col3_point = 0

    # 第一列
    # 消去规则
    for j in range(0, 7, 3):
        for i in range(0, 7, 3):
            if int(My_chess[j]) == int(Enemy_chess[i]):
                Enemy_chess[i] = 0

    # 计算列和
    # 我方
    dict1 = {}
    for j in range(0, 7, 3):
        if dict1.get(My_chess[j]) is None:
            dict1[My_chess[j]] = 1
        else:
            dict1[My_chess[j]] += 1

    for j in dict1:
        my_col1_point += int(j) * dict1[j] * dict1[j]

    # 敌方
    dict1 = {}
    for j in range(0, 7, 3):
        if dict1.get(Enemy_chess[j]) is None:
            dict1[Enemy_chess[j]] = 1
        else:
            dict1[Enemy_chess[j]] += 1

    for j in dict1:
        enemy_col1_point += int(j) * dict1[j] * dict1[j]

    # 第二列
    # 消去规则
    for j in range(1, 8, 3):
        for i in range(1, 8, 3):
            if int(My_chess[j]) == int(Enemy_chess[i]):
                Enemy_chess[i] = 0

    # 计算列和
    # 我方
    dict2 = {}
    for j in range(1, 8, 3):
        if dict2.get(My_chess[j]) is None:
            dict2[My_chess[j]] = 1
        else:
            dict2[My_chess[j]] += 1

    for j in dict2:
        my_col2_point += int(j) * dict2[j] * dict2[j]

    # 敌方
    dict2 = {}
    for j in range(1, 8, 3):
        if dict2.get(Enemy_chess[j]) is None:
            dict2[Enemy_chess[j]] = 1
        else:
            dict2[Enemy_chess[j]] += 1

    for j in dict2:
        enemy_col2_point += int(j) * dict2[j] * dict2[j]

    # 第三列
    # 消去规则
    for j in range(2, 9, 3):
        for i in range(2, 9, 3):
            if int(My_chess[j]) == int(Enemy_chess[i]):
                Enemy_chess[i] = 0

    # 计算列和
    # 我方
    dict3 = {}
    for j in range(2, 9, 3):
        if dict3.get(My_chess[j]) is None:
            dict3[My_chess[j]] = 1
        else:
            dict3[My_chess[j]] += 1

    for j in dict3:
        my_col3_point += int(j) * dict3[j] * dict3[j]

    # 敌方
    dict3 = {}
    for j in range(2, 9, 3):
        if dict3.get(Enemy_chess[j]) is None:
            dict3[Enemy_chess[j]] = 1
        else:
            dict3[Enemy_chess[j]] += 1

    for j in dict3:
        enemy_col3_point += int(j) * dict3[j] * dict3[j]

    My_point = my_col1_point + my_col2_point + my_col3_point
    Enemy_point = enemy_col1_point + enemy_col2_point + enemy_col3_point

    return My_point, Enemy_point

# 进入游戏触发：决定谁先手
class Gofirst(APIView):

    def post(self, request, *args, **kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        return Response({"first": random.randint(1, 2)})

# 点击骰子触发：摇骰子
class RolldiceView(APIView):

    def post(self, request, *args, **kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        return Response({"dice": random.randint(1, 6)})

# 点击盒子触发：分数计算接口, 胜利, 消除
class PointView(APIView):

    def post(self, request, *args, **kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 对数据里的双方数据进行处理
        print(request.data)
        My_chess = request.data["my_chess"]
        Enemy_chess = request.data["enemy_chess"]
        Dice = request.data["dice"]
        Index = request.data["index"]
        My_chess[int(Index)] = int(Dice)
        # print(My_chess)
        # print(Enemy_chess)

        # 初始化
        my_col1_point = 0
        my_col2_point = 0
        my_col3_point = 0
        enemy_col1_point = 0
        enemy_col2_point = 0
        enemy_col3_point = 0

        # 第一列
        # 消去规则
        for j in range(0, 7, 3):
            for i in range(0, 7, 3):
                if int(My_chess[j]) == int(Enemy_chess[i]):
                    Enemy_chess[i] = 0

        # 计算列和
        # 我方
        dict1 = {}
        for j in range(0, 7, 3):
            if dict1.get(My_chess[j]) is None:
                dict1[My_chess[j]] = 1
            else:
                dict1[My_chess[j]] += 1

        for j in dict1:
            my_col1_point += int(j) * dict1[j] * dict1[j]

        # 敌方
        dict1 = {}
        for j in range(0, 7, 3):
            if dict1.get(Enemy_chess[j]) is None:
                dict1[Enemy_chess[j]] = 1
            else:
                dict1[Enemy_chess[j]] += 1

        for j in dict1:
            enemy_col1_point += int(j) * dict1[j] * dict1[j]

        # 第二列
        # 消去规则
        for j in range(1, 8, 3):
            for i in range(1, 8, 3):
                if int(My_chess[j]) == int(Enemy_chess[i]):
                    Enemy_chess[i] = 0

        # 计算列和
        # 我方
        dict2 = {}
        for j in range(1, 8, 3):
            if dict2.get(My_chess[j]) is None:
                dict2[My_chess[j]] = 1
            else:
                dict2[My_chess[j]] += 1

        for j in dict2:
            my_col2_point += int(j) * dict2[j] * dict2[j]

        # 敌方
        dict2 = {}
        for j in range(1, 8, 3):
            if dict2.get(Enemy_chess[j]) is None:
                dict2[Enemy_chess[j]] = 1
            else:
                dict2[Enemy_chess[j]] += 1

        for j in dict2:
            enemy_col2_point += int(j) * dict2[j] * dict2[j]

        # 第三列
        # 消去规则
        for j in range(2, 9, 3):
            for i in range(2, 9, 3):
                if int(My_chess[j]) == int(Enemy_chess[i]):
                    Enemy_chess[i] = 0

        # 计算列和
        # 我方
        dict3 = {}
        for j in range(2, 9, 3):
            if dict3.get(My_chess[j]) is None:
                dict3[My_chess[j]] = 1
            else:
                dict3[My_chess[j]] += 1

        for j in dict3:
            my_col3_point += int(j) * dict3[j] * dict3[j]

        # 敌方
        dict3 = {}
        for j in range(2, 9, 3):
            if dict3.get(Enemy_chess[j]) is None:
                dict3[Enemy_chess[j]] = 1
            else:
                dict3[Enemy_chess[j]] += 1

        for j in dict3:
            enemy_col3_point += int(j) * dict3[j] * dict3[j]

        My_point = my_col1_point + my_col2_point + my_col3_point
        Enemy_point = enemy_col1_point + enemy_col2_point + enemy_col3_point

        player = ["my", "enemy", "draw"]
        Game_over = 1
        for j in range(0, 9):
            if int(My_chess[j]) == 0:
                Game_over = 0
                break

        if My_point > Enemy_point:
            winner = player[0]
            loser = player[1]
        elif My_point < Enemy_point:
            winner = player[1]
            loser = player[0]
        else:
            winner = player[2]
            loser = player[2]

        return Response({"status": Game_over, "winner": winner, "loser": loser, "my_point": My_point, "enemy_point": Enemy_point, "my_col1_point": my_col1_point, "my_col2_point": my_col2_point, "my_col3_point": my_col3_point, "enemy_col1_point": enemy_col1_point, "enemy_col2_point": enemy_col2_point, "enemy_col3_point": enemy_col3_point, "enemy_chess": Enemy_chess, "my_chess": My_chess})

# AI棋子下一步,就是自动点击盒子
class AIView(APIView):

    def post(self, request, *args, **kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 对数据里的双方数据进行处理
        print(request.data)
        My_chess = request.data["my_chess"]
        Enemy_chess = request.data["enemy_chess"]
        Dice = random.randint(1, 6)
        # print(My_chess)
        # print(Enemy_chess)

        # 先判断棋子数, 和自己以及对手能下哪
        my_num = 0
        enemy_num = 0
        index = -1
        my_empty = []
        enemy_empty = []
        for j in range(0, 9):
            if int(My_chess[j]) != 0:
                my_num = my_num + 1
            else:
                my_empty.append(j)
            if int(Enemy_chess[j]) != 0:
                enemy_num = enemy_num + 1
            else:
                enemy_empty.append(j)

        # 如果棋子数小于5
        if my_num < 5:
            # 先判断能否消（1不消，2成对消）,其余尽量都消
            for j in range(0, 9):
                if int(Dice) == Enemy_chess[j]:
                    if int(Dice) == 1:
                        pass
                    elif int(Dice) == 2:
                        dict = {}
                        for i in range(j % 3, 9, 3):
                            if dict.get(Enemy_chess[i]) is None:
                                dict[Enemy_chess[i]] = 1
                            else:
                                dict[Enemy_chess[i]] += 1

                        if int(dict[Dice]) >= 2:
                            for empty in my_empty:
                                if empty == j % 3 or empty == j % 3 + 3 or empty == j % 3 + 6:
                                    index = empty
                                    break
                            break
                        else:
                            pass
                    else:
                        dict = {}
                        for i in range(j % 3, 9, 3):
                            if dict.get(Enemy_chess[i]) is None:
                                dict[Enemy_chess[i]] = 1
                            else:
                                dict[Enemy_chess[i]] += 1

                        if dict.get(Dice) is not None:
                            for empty in my_empty:
                                if empty == j % 3 or empty == j % 3 + 3 or empty == j % 3 + 6:
                                    index = empty
                                    break
                            break
                        else:
                            pass
            if index != -1:
                return Response({"index": index, "dice": int(Dice)})

            # 如果不能消，则判断是否可以成对（5，6先不成对），尽量不要先成三对，容易被消
            for j in range(0, 9):
                if int(Dice) == My_chess[j]:
                    if int(Dice) == 5 or int(Dice) == 6:
                        pass
                    else:
                        dict = {}
                        for i in range(j % 3, 9, 3):
                            if dict.get(My_chess[i]) is None:
                                dict[My_chess[i]] = 1
                            else:
                                dict[My_chess[i]] += 1

                        if dict.get(Dice) is not None:
                            if int(dict[Dice]) <= 1:
                                for empty in my_empty:
                                    if empty == j % 3 or empty == j % 3 + 3 or empty == j % 3 + 6:
                                        index = empty
                                        break
                                break
                        else:
                            pass
            if index != -1:
                return Response({"index": index, "dice": Dice})

            # 如果是5，6且不能成对，则下自己空位最多的那列,否则5，6下对方空位最少的一列，1，2，3，4下对方较多的那列
            # 自己的空位
            col1_nullnum = 0
            col2_nullnum = 0
            col3_nullnum = 0
            for empty in my_empty:
                if empty == 0 or empty == 3 or empty == 6:
                    col1_nullnum += 1
                if empty == 1 or empty == 4 or empty == 7:
                    col2_nullnum += 1
                if empty == 2 or empty == 5 or empty == 8:
                    col3_nullnum += 1

            # 对方的空位
            enemy_col1_nullnum = 0
            enemy_col2_nullnum = 0
            enemy_col3_nullnum = 0
            for empty in enemy_empty:
                if empty == 0 or empty == 3 or empty == 6:
                    enemy_col1_nullnum += 1
                if empty == 1 or empty == 4 or empty == 7:
                    enemy_col2_nullnum += 1
                if empty == 2 or empty == 5 or empty == 8:
                    enemy_col3_nullnum += 1

            if col1_nullnum > col2_nullnum and col1_nullnum > col3_nullnum:
                for empty in my_empty:
                    if empty == 0 or empty == 3 or empty == 6:
                        index = empty
                        return Response({"index": index, "dice": Dice})
            elif col2_nullnum > col1_nullnum and col2_nullnum > col3_nullnum:
                for empty in my_empty:
                    if empty == 1 or empty == 4 or empty == 7:
                        index = empty
                        return Response({"index": index, "dice": Dice})
            elif col3_nullnum > col2_nullnum and col3_nullnum > col1_nullnum:
                for empty in my_empty:
                    if empty == 2 or empty == 5 or empty == 8:
                        index = empty
                        return Response({"index": index, "dice": Dice})
            elif col1_nullnum == col2_nullnum and col3_nullnum < col1_nullnum:
                if int(Dice) == 5 or int(Dice) == 6:
                    if enemy_col1_nullnum >= enemy_col2_nullnum:
                        for empty in my_empty:
                            if empty == 1 or empty == 4 or empty == 7:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    else:
                        for empty in my_empty:
                            if empty == 0 or empty == 3 or empty == 6:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                else:
                    if enemy_col1_nullnum >= enemy_col2_nullnum:
                        for empty in my_empty:
                            if empty == 0 or empty == 3 or empty == 6:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    else:
                        for empty in my_empty:
                            if empty == 1 or empty == 4 or empty == 7:
                                index = empty
                                return Response({"index": index, "dice": Dice})
            elif col1_nullnum == col3_nullnum and col2_nullnum < col1_nullnum:
                if int(Dice) == 5 or int(Dice) == 6:
                    if enemy_col1_nullnum >= enemy_col3_nullnum:
                        for empty in my_empty:
                            if empty == 2 or empty == 5 or empty == 8:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    else:
                        for empty in my_empty:
                            if empty == 0 or empty == 3 or empty == 6:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                else:
                    if enemy_col1_nullnum >= enemy_col3_nullnum:
                        for empty in my_empty:
                            if empty == 0 or empty == 3 or empty == 6:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    else:
                        for empty in my_empty:
                            if empty == 2 or empty == 5 or empty == 8:
                                index = empty
                                return Response({"index": index, "dice": Dice})
            elif col2_nullnum == col3_nullnum and col1_nullnum < col2_nullnum:
                if int(Dice) == 5 or int(Dice) == 6:
                    if enemy_col2_nullnum >= enemy_col3_nullnum:
                        for empty in my_empty:
                            if empty == 2 or empty == 5 or empty == 8:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    else:
                        for empty in my_empty:
                            if empty == 1 or empty == 4 or empty == 7:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                else:
                    if enemy_col2_nullnum >= enemy_col3_nullnum:
                        for empty in my_empty:
                            if empty == 1 or empty == 4 or empty == 7:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    else:
                        for empty in my_empty:
                            if empty == 2 or empty == 5 or empty == 8:
                                index = empty
                                return Response({"index": index, "dice": Dice})
            # 三行列数都一样，5，6下对方列最小的，1，2，3，4下较多的
            elif col2_nullnum == col1_nullnum == col3_nullnum:
                if int(Dice) == 5 or int(Dice) == 6:
                    if enemy_col1_nullnum >= enemy_col2_nullnum and enemy_col2_nullnum <= enemy_col3_nullnum:
                        for empty in my_empty:
                            if empty == 1 or empty == 4 or empty == 7:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    elif enemy_col2_nullnum >= enemy_col1_nullnum and enemy_col1_nullnum <= enemy_col3_nullnum:
                        for empty in my_empty:
                            if empty == 0 or empty == 3 or empty == 6:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    elif enemy_col2_nullnum >= enemy_col3_nullnum and enemy_col3_nullnum <= enemy_col1_nullnum:
                        for empty in my_empty:
                            if empty == 2 or empty == 5 or empty == 8:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                else:
                    if enemy_col1_nullnum >= enemy_col2_nullnum and enemy_col1_nullnum >= enemy_col3_nullnum:
                        for empty in my_empty:
                            if empty == 0 or empty == 3 or empty == 6:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    elif enemy_col2_nullnum >= enemy_col1_nullnum and enemy_col2_nullnum >= enemy_col3_nullnum:
                        for empty in my_empty:
                            if empty == 1 or empty == 4 or empty == 7:
                                index = empty
                                return Response({"index": index, "dice": Dice})
                    elif enemy_col3_nullnum >= enemy_col2_nullnum and enemy_col3_nullnum >= enemy_col1_nullnum:
                        for empty in my_empty:
                            if empty == 2 or empty == 5 or empty == 8:
                                index = empty
                                return Response({"index": index, "dice": Dice})
            if index != -1:
                return Response({"index": index})

        # 如果棋子数>=6
        # 看看什么时候差最大就下哪
        elif my_num >= 5:
            now_my_point, now_enemy_point = CalculateScore(My_chess, Enemy_chess)
            for empty in my_empty:
                My_chess[empty] = int(Dice)
                new_my_point, new_enemy_point = CalculateScore(My_chess, Enemy_chess)
                if new_my_point - new_enemy_point > now_my_point - now_enemy_point:
                    now_my_point = new_my_point
                    now_enemy_point = new_enemy_point
                    index = empty
                My_chess[empty] = 0

            return Response({"index": index, "dice": Dice})
        elif my_num == 8:
            return Response({"index": my_empty[0], "dice": Dice})

        return Response({"index": index, "dice": Dice})

# 查看排行榜
# 然后排行返回前几条和自己最高的那条
class RankingView(APIView):

    def post(self, request, *args, **kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 对数据里的双方数据进行处理
        print(request.data)
        name = request.data["player_name"]
        picture_url = request.data["player_picture_url"]

        stu_list = []

        qs = Playerrank.objects.order_by('-point')
        ser = PlayerrankSer(qs, many=True)
        # print(ser.data)
        print(json.dumps(ser.data))

        count = 1
        rank = 0
        for stu in qs:
            if stu.name == name:
                rank = count
            stu_list.append({
                "id": stu.id,
                "name": stu.name,
                "picture_url": stu.picture_url,
                "phonenumber": stu.phonenumber,
                "point": stu.point
            })
            count += 1

        my_qs = Playerrank.objects.filter(name=name, picture_url=picture_url)
        ser = PlayerrankSer(my_qs, many=True)
        # print(ser.data)
        print(json.dumps(ser.data))

        for stu in my_qs:
            stu_list.append({
                "id": stu.id,
                "name": stu.name,
                "picture_url": stu.picture_url,
                "phonenumber": stu.phonenumber,
                "point": stu.point,
                "rank": rank
            })

        return Response(stu_list)

# 每次页面结算结束的时候把总分数发到数据库
class Addrank(APIView):

    def post(self, request, *args, **kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 对数据里的双方数据进行处理
        print(request.data)
        name = request.data["player_name"]
        point = request.data["player_point"]
        picture_url = request.data["player_picture_url"]

        my_qs = Playerrank.objects.filter(name=name, picture_url=picture_url)
        ser = PlayerrankSer(my_qs, many=True)
        # print(ser.data)
        print(json.dumps(ser.data))

        # 如果有记录，则判断分数是否提高
        if my_qs:
            for stu in my_qs:
                if int(stu.point) >= int(point):
                    break
                else:
                    # 修改
                    Playerrank.objects.filter(name=name, picture_url=picture_url).update(point=point, picture_url=picture_url)
        else:
            Playerrank.objects.create(name=name, picture_url=picture_url, phonenumber='', point=point)

        return Response({'ret': 1})

