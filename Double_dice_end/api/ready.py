import json
import random

from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
CONN_LIST = []
player_name = []
player_picture_url = []

class Waiting(WebsocketConsumer):

    def websocket_connect(self, message):
        self.accept()
        CONN_LIST.append(self)
        self.send("等待中")

    def websocket_receive(self, message):
        text = message['text']
        print("接收到消息", text)
        # player骰子1
        text_data_json = json.loads(message['text'])
        player_name.append(text_data_json["user_name"])
        print(player_name)
        player_picture_url.append(text_data_json["user_url"])
        # print(len(CONN_LIST))
        print(player_picture_url)
        count = 0
        first = random.randint(1, 2)
        if len(CONN_LIST) == 2:
            for conn in CONN_LIST:
                count += 1
                if count == 1:
                    conn.send(text_data=json.dumps({'other_name': player_name[1], 'other_url': player_picture_url[1], 'start': 1, 'play1_name': player_name[0], 'play1_url': player_picture_url[0], 'play2_name': player_name[1], 'play2_url': player_picture_url[1], 'first': first}))
                else:
                    conn.send(text_data=json.dumps({'other_name': player_name[0], 'other_url': player_picture_url[0], 'start': 1, 'play1_name': player_name[0], 'play1_url': player_picture_url[0], 'play2_name': player_name[1], 'play2_url': player_picture_url[1], 'first': first}))

    def websocket_disconnect(self, message):
        # 客户端与服务端断开连接时，自动触发。
        print("断开连接")
        CONN_LIST.remove(self)
        for i in player_name:
            player_name.remove(i)
        print(player_name)
        for i in player_picture_url:
            player_picture_url.remove(i)
        print(player_picture_url)
        raise StopConsumer()