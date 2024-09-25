#Django signals are executed synchronously by default. 
#This means that when a signal is triggered, the handler is called immediately, and the execution of the program waits for the signal handler to finish before continuing.

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started...")
    time.sleep(3)
    print("Signal handler completed.")

new_user = User.objects.create_user('new_user')

#When the new user Object is created, the signal handler runs synchronously. You'll notice the program pauses for 3 seconds when the signal is triggered.
#The rest of the process will wait until the signal handler finishes execution, confirming that the signal is executed synchronously.

#-----------------------------------------
#Django Signals
#Yes, by default, Django signals run in the same thread as the caller. 
#Signals are not multi-threaded unless explicitly handled with a background task or threading library.

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

#Save User object to trigger the signal
print(f"Main thread: {threading.current_thread().name}")
new_user = User.objects.create_user('new_user')


#When we run this piece of code you will observe that both the main process and the signal handler print the same thread name. 
#This indicates that the signal runs in the same thread as the caller.
#-----------------------------------------


#Do Django signals run in the same database transaction as the caller by default?

#By default, Django signals can participate in the same database transaction as the caller. 
#If a signal is triggered within a transaction block (like transaction.atomic()), it will be a part of that transaction.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal is part of the transaction.")
    else:
        print("Signal is not part of the transaction.")

# Trigger the signal within a transaction
with transaction.atomic():
    new_user = User.objects.create_user('new_user')

#The message "Signal is part of the transaction" will be printed, proving that

#---------------------------------

#Topic: Custom Classes in Python

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(10, 5)
for dimension in rect:
    print(dimension)
