import asyncio
from django.db import models
from django.db.models.signals import post_save

import websockets

from .trigger import FetchFeed


class Feed(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    expired = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


def feed_signal(sender, **kwargs):
    """Feed if any new feeds
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(FetchFeed().send_feed(feed_id=kwargs['instance'].id))
    loop.close()


post_save.connect(feed_signal, sender=Feed)