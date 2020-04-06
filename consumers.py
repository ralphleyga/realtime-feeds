import json

from django.forms.models import model_to_dict

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


from .models import Feed

class FeedConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.feed_name = self.scope['url_route']['kwargs']
        await self.accept()
        print('connect')

    async def disconnect(self, code_node):
        print('disconnect')

    async def receive(self, text_data=None, bytes_data=None):
        import pdb; pdb.set_trace()
        feed = await self.latest_feed()
        print('received')

    @database_sync_to_async
    def latest_feed(self, feed_id):
        """Get latest feed
        """
        return Feed.objects.get(id=feed_id)