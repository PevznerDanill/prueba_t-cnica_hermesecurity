from celery import shared_task
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random


@shared_task
def long_running_task():
    channel_layer = get_channel_layer()
    group_name = 'progress_bar'
    for i in range(10):
        time.sleep(1)
        progress = (i + 1) * 10

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'progress_update',
                'progress': progress,
            }
        )

    # async_to_sync(channel_layer.group_send)(
    #     group_name,
    #     {
    #         'type': 'progress_finished',
    #         'progress': 'Task is done',
    #     }
    # )
