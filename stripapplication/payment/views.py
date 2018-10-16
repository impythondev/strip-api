# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import stripe
from django.conf import settings

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import StripePaymentModelSerializer
from .models import StripePayment


class PaymentCheckoutViewSet(viewsets.ViewSet):
    """
    It's strip payment checkout method API.
    accepted method :
        POST
    accepted param:
    
        {
            "name" : "hello",
            "amount" : 125,
            "currency" : "USD",
            "card_number" : "2223003122003222",
            "exp_month" :10,
            "exp_year" : 21,
            "cvv":125
        }

    """
    serializer_class = StripePaymentModelSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
      
        # check the form is valid or not.
        if serializer.is_valid(raise_exception=True):
            stripe.api_key = settings.STRIPE_PUBLIC_KEY

            # create a stripe token for process the payment.
            try:
                token = stripe.Token.create(
                        card={
                            "number": request.data['card_number'],
                            "exp_month": request.data['exp_month'],
                            "exp_year": request.data['exp_year'],
                            "cvc": request.data['cvv']
                        },
                    )
            except Exception as e:
                token = None
            
            if token:
                # create the strip payment.
                stripe.api_key = settings.STRIPE_SECRET_KEY
                charge = stripe.Charge.create(
                    amount=request.data['amount'],
                    currency=request.data['currency'],
                    description='stripe payment',
                    source=token['id']
                )

                if charge['status'] == 'succeeded':
                    
                    stripe_payment = StripePayment.objects.create(
                            name=request.data['name'],
                            amount=request.data['amount'],
                            public_key=request.data['public_key'],
                            transaction_id=charge['id'],
                            currency=request.data['currency']
                        )

                    return Response({
                        'status': status.HTTP_201_CREATED,
                        'message': 'Payment successed.',
                        'result': charge
                    })

                return Response({
                    'status': status.HTTP_406_NOT_ACCEPTABLE,
                    'message': 'Something went to worng.',
                    'result' : charge
                })

            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'You provided card details are incorrect.',
                })
