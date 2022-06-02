import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join a room
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # leave a room
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
        user = self.scope['user'].get_username(),

        if user == None or user == "":
            user = "Anonymous"


        response = {
            'type': 'chat_message',
            'message': message,
            'user': user,
            'bold': text_data_json['bold'],
            'italic': text_data_json['italic'],
            'underlined': text_data_json['underlined'],
            'color': text_data_json['color'],
        }
        # send message to room group
        async_to_sync(self.channel_layer.group_send)(self.room_group_name, response)

    def chat_message(self, event):
        message = event['message']
        user = event['user']

        self.send(text_data=json.dumps(event))
