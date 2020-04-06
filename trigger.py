import json
import websockets

from django.conf import settings

class FetchFeed():
    ws_url = f"ws://localhost:8000/feeds/"

    async def send_feed(self, feed_id):
        async with websockets.connect(self.ws_url) as websocket:
            await websocket.send(json.dumps({
                'feed_id': feed_id
            }))
