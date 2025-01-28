import africastalking
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

@receiver(post_save, sender=Order)
def send_sms_on_order_creation(sender, instance, created, **kwargs):
    if created:
        message = f"Hello {instance.customer.name}, your order for {instance.item} has been received."
        sms.send(message, [instance.customer.phone_number])
