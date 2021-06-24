# Download the helper library from https://www.twilio.com/docs/python/install

import os
from twilio.rest import Client

import datetime
date = datetime.datetime.now() 
def sendsms():
    account_sid = "#"
    auth_token = "#"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                         body=f"Face detected at {date}",
                         from_='#',
                         to='#'
                     )

    print(f"Messaged successfully !!")