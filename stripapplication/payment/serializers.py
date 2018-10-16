from rest_framework import serializers

from django.conf import settings

from .models import StripePayment


class StripePaymentModelSerializer(serializers.ModelSerializer):
    card_number = serializers.IntegerField()
    exp_month = serializers.IntegerField()
    exp_year = serializers.IntegerField()
    cvv =  serializers.IntegerField()


    class Meta:
        model = StripePayment
        fields = ('name', 'amount', 'currency', 'card_number',
            'exp_month', 'exp_year', 'cvv')

