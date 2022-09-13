import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Thread, ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_room = self.scope['url_route']['kwargs']['chat_room']
        self.room_group_chat = self.chat_room
        await self.channel_layer.group_add(
            self.room_group_chat,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group

        await self.channel_layer.group_discard(
            self.room_group_chat,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        thread = text_data_json.get('thread_id')
        user = text_data_json['user_id']
        reciever_id = text_data_json['reciever_id']

        await self.channel_layer.group_send(
            str(reciever_id),
            {
                'type': 'chat_message',
                'message': message,
                'thread': thread,
                'user': user,
                'reciever_id': reciever_id,

            }
        )
        await self.create_chat_message(message, thread, user)

        # chat message

    async def chat_message(self, event):
        message = event['message']
        thread = event['thread']
        user = event['user']
        reciever_id = event['reciever_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'thread': thread,
            'user': user,
            'reciever_id': reciever_id,

        }))

    async def error_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'error': "sender and reciever cannot be same"
        }))

    @database_sync_to_async
    def create_chat_message(self, message, thread, user):
        msg = ChatMessage.objects.create(message=message, thread_id=thread, user_id=user)
        msg.save()
        return msg



# class ChatConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         self.chat_room = self.scope['url_route']['kwargs']['chat_room']
#         self.room_group_chat = self.chat_room
#         await self.channel_layer.group_add(
#                     self.room_group_chat,
#                     self.channel_name
#                 )
#         await self.send({
#                     "type": "websocket.accept",
#                 })
#         # await self.accept()
#
#     async def websocket_disconnect(self, event):
#                 # Leave room group
#
#         await self.channel_layer.group_discard(
#                     self.room_group_chat,
#                     self.channel_name
#                 )
#         await self.send({
#             "type": "websocket.close"
#             })
#
#
#     @database_sync_to_async
#     def create_chat_message(self, message, thread, user):
#         msg = ChatMessage.objects.create(message=message, thread_id=thread, user_id=user)
#         msg.save()
#         return msg
#
#
#     async def websocket_receive(self, event):
#         front_text = event.get('text', None)
#         print(front_text)
#         if front_text is not None:
#             loaded_dict_data = json.loads(front_text)
#             message = loaded_dict_data['message']
#             user = loaded_dict_data['user_id']
#             thread = loaded_dict_data['thread_id']
#             reciever_id = loaded_dict_data['reciever_id']
#             print(message,user, thread, '***************&&&&&&&&&&&&&&&&&&&&&*****', reciever_id)
#             # if user == reciever_id:
#             #     await self.channel_layer.group_send(
#             #         str(user),
#             #         {
#             #             'type': 'error_message'
#             #         }
#             #     )
#             # new_event = {
#             #     'type': 'chat_message',
#             #     'text': json.dumps(front_text)
#             # }
#             await self.channel_layer.group_send(
#                 str(reciever_id),
#                 {
#                     "type": "chat_messages",
#                     'message': message,
#                     'user': user,
#                     'thread': thread,
#                     'reciever_id': reciever_id
#                 }
#             )
#             await self.create_chat_message(message, thread, user)
#
#    # chat message
#
    # async def chat_message(self, event):
    #     message = event['message']
    #     thread = event['thread']
    #     user = event['user']
    #     reciever_id = event['reciever_id']
    #
    #     # Send message to WebSocket
    #     await self.send({
    #         'message': message,
    #         'thread': thread,
    #         'user': user,
    #         'reciever_id': reciever_id,
    #
    #     }))











