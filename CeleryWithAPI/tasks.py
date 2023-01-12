from celery import shared_task
from django.conf import settings
from django.http import HttpResponse
import time
import os

@shared_task
def drochivo(path):
    time.sleep(4)
    print("Pizdes!")
    return True