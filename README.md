# Django Strip Rest API.

It's django project to build django rest API for strip payment checkout.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Python version : python3.4
###### python installtion in ubuntu machine
**sudo add-apt-repository ppa:jonathonf/python-3.6**
**sudo apt-get update**
**sudo apt-get install python3.6**

**sudo apt-get update**
**sudo apt-get install python3.6**

###### Install virtualenv
**sudo apt-get install python3-pip**
**sudo pip3 install virtualenv**

###### Python installtion in windows machine.
https://www.python.org/downloads/

**Install virtual envoirment**

###### Installing
1. clone from repository

**git clone https://github.com/mrakrathod/strip-api.git**

2. create virtualenvoirment

**virtualenv --python=python3.6 strip_env**

3. Activate virtual envoirment

**source strip_env/bin/activate**

4. Install python dependancy packages.
Note, requirments.txt file present in project root direcotry


**pip install -r requirments.txt**

5. start project below command.

**python manage.py runserver**

6. Copy this URL on your browsers tab 

**http://localhost:8000/api/v1/payment-checkout/**
 
## API endpoints.

**Logout API docs**

URL : /api/v1/payment-checkout/

Endpoints : /payment-checkout/

Accepted Method : POST

        Accepted Param in body:
        {
            "name" : "hello",
            "amount" : 125,
            "public_key" : "sdfdsfdsfsdf",
            "currency" : "USD",
            "card_number" : "2223003122003222",
            "exp_month" :10,
            "exp_year" : 21,
            "cvv":125
        }

        Accepted success response: 
        {
          "status": 201,
          "message": "Payment successed.",
          "result": {
              "application_fee": null,
              "livemode": false,
              "currency": "usd",
              "payment_intent": null,
              "invoice": null,
              "fraud_details": {},
              "statement_descriptor": null,
              "captured": true,
              "on_behalf_of": null,
              "transfer_group": null,
              "source": {
                  "dynamic_last4": null,
                  "last4": "0005",
                  "address_state": null,
                  "address_zip_check": null,
                  "address_country": null,
                  "id": "card_1DLkSBHxVzLGpSKbUAnuRRZV",
                  "address_line2": null,
                  "address_line1": null,
                  "funding": "credit",
                  "metadata": {},
                  "cvc_check": "pass",
                  "exp_month": 1,
                  "tokenization_method": null,
                  "address_line1_check": null,
                  "brand": "American Express",
                  "object": "card",
                  "fingerprint": "C6o4xXvfnBZ22pQ7",
                  "exp_year": 2021,
                  "address_zip": null,
                  "customer": null,
                  "address_city": null,
                  "name": null,
                  "country": "US"
              },
              "receipt_number": null,
              "destination": null,
              "id": "ch_1DLkSCHxVzLGpSKbLfnYqFtf",
              "application": null,
              "balance_transaction": "txn_1DLkSDHxVzLGpSKbcy8seCWI",
              "source_transfer": null,
              "receipt_email": null,
              "metadata": {},
              "status": "succeeded",
              "amount_refunded": 0,
              "description": "stripe payment",
              "refunded": false,
              "object": "charge",
              "paid": true,
              "review": null,
              "failure_code": null,
              "customer": null,
              "outcome": {
                  "network_status": "approved_by_network",
                  "risk_level": "normal",
                  "risk_score": 31,
                  "reason": null,
                  "seller_message": "Payment complete.",
                  "type": "authorized"
              },
              "refunds": {},
              "created": 1539665208,
              "failure_message": null,
              "shipping": null,
              "amount": 200,
              "dispute": null,
              "order": null
          }
      }
		
		

**Add your own Strip API keys**   
Add below keys in stetting file.  
STRIPE_PUBLIC_KEY = ''  
STRIPE_SECRET_KEY = ''

