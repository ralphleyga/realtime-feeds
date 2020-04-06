import json

from django.forms.models import model_to_dict

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


from .models import Feed

class FeedConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.feed_name = 'realtime_feeds'
        await self.channel_layer.group_add(
            self.feed_name,
            self.channel_name
        )
        await self.accept()
        print('connect')

    async def disconnect(self, code_node):
        print('disconnect')
        await self.channel_layer.group_discard(
            self.feed_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        feed_id = data['feed_id']
        await self.channel_layer.group_send(
            self.feed_name,
            {
                'type': 'get_feed',
                'feed_id': feed_id
            }
        )

    async def get_feed(self, event):
        feed_id = event['feed_id']
        feed = await self.latest_feed(feed_id)
        feed_data = model_to_dict(feed)
        await self.send(text_data=json.dumps(feed_data))

    @database_sync_to_async
    def latest_feed(self, feed_id):
        """Get latest feed
        """
        return Feed.objects.get(id=feed_id)