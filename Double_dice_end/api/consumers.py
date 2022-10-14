import json
import random

from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
CONN_LIST = []

class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        # print("握手")
        # 有客户端向后端发送websocket连接请求时，自动触发。
        # 服务端允许与客户端连接(握手)
        self.accept()

        # 获取群号，获取路由匹配中的
        # group = self.scope['url_route']['kwargs'].get("group")

        # 将这个客户端的连接对象加入到某个地方（内存 or redis）
        # async_to_sync(self.channel_layer.group_add)(group, self.channel_name)
        CONN_LIST.append(self)
        # 给客户端发消息
        self.send("建立连接成功")

    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发接收消息
        text = message['text']
        print("接收到消息", text)
        # player骰子1
        if text == 'dice_1':
            dice = random.randint(1, 6)
            for conn in CONN_LIST:
                conn.send(text_data=json.dumps({'dice_1': dice}))
        # player骰子2
        elif text == 'dice_2':
            dice = random.randint(1, 6)
            for conn in CONN_LIST:
                conn.send(text_data=json.dumps({'dice_2': dice}))
        else:
            text_data_json = json.loads(message['text'])
            My_chess = text_data_json["my_chess"]
            Enemy_chess = text_data_json["enemy_chess"]
            Dice = text_data_json["dice"]
            Index = text_data_json["index"]
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
            elif My_point < Enemy_point:
                winner = player[1]
            else:
                winner = player[2]

            for conn in CONN_LIST:
                conn.send(text_data=json.dumps({"status": Game_over, "winner": winner, "my_point": My_point, "enemy_point": Enemy_point,
                             "my_col1_point": my_col1_point, "my_col2_point": my_col2_point,
                             "my_col3_point": my_col3_point, "enemy_col1_point": enemy_col1_point,
                             "enemy_col2_point": enemy_col2_point, "enemy_col3_point": enemy_col3_point,
                             "enemy_chess": Enemy_chess, "my_chess": My_chess, "index": Index}))
        # group = self.scope['url_route']['kwargs'].get("group")
        # if text == "关闭":
        #     # 服务端主动关闭连接, 给客户端发送一条断开连接的消息
        #     self.close()
        #     # raise StopConsumer() # 服务器断开连接时，执行StopConsumer()， 后面的websocket_disconnect不再执行
        #     return
        # 通知组内所有的客户端，执行xx_oo方法，在此方法中自己可以去定义任意的功能。
        # async_to_sync(self.channel_layer.group_send)(group, {"type": "xx.oo", 'message': message})

        # for conn in CONN_LIST:
        #     conn.send(res)
        # res = "{}SB".format(text)
        # self.send("不要回复不要回复")
        # 服务端与客户端主动断开连接
        # self.close()

    # def xx_oo(self, event):
    #     text = event['message']['text']
    #     self.send(text)

    def websocket_disconnect(self, message):
        # 客户端与服务端断开连接时，自动触发。
        # group = self.scope['url_route']['kwargs'].get("group")
        # async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
        print("断开连接")
        CONN_LIST.remove(self)
        raise StopConsumer()