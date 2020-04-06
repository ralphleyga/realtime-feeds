=====
Reatime Feeds
=====

Feeds is a django app built from channels (django channels) with easy integration of realtime feed or announcements. It is useful for small pop realtime feed or announcement or use in notifications.

## Requirements
* Django 3.0 up
* Python 3.5 up
* Redis Server
* channels-redis 2.4.2 up
* channels 2.4.0 up

Quick start
-----------

1. Add "feeds" and "channels" to your INSTALLED_APPS setting like this::
    ```
    INSTALLED_APPS = [
        ...
        'channels',
        'feeds',
    ]
    ```

2. Create a routing.py at project directory::
    ```
    from channels.auth import AuthMiddlewareStack
    from channels.routing import ProtocolTypeRouter, URLRouter

    import feeds.routing

    application = ProtocolTypeRouter({
        # Empty for now (http->django views is added by default)
        'websocket': AuthMiddlewareStack(
            URLRouter(
                feeds.routing.websocket_urlpatterns
            )
        ),
    })```

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/feeds/
