import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ProgressBarConsumer(AsyncWebsocketConsumer):
    """
    Un Consumer para un nuevo progress_bar
    """

    async def connect(self):
        self.group_name = 'progress_bar'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def progress_update(self, event):
        progress = event['progress']
        task_id = event['task_id']

        await self.send(text_data=json.dumps({
            'progress': progress,
            'task_id': task_id,
        }))
