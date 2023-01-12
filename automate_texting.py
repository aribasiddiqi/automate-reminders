
import random
import schedule 
import time
from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

MEDICATION_QUOTES = [
    "Hello, don't forget to take your medication!",
    "Hey friend, please take your medication <3",
    "It's almost the end of the day, please take your medication!"
]
def send_message(quotes_list=MEDICATION_QUOTES):

    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )

#Schedule time the message should be sent 
schedule.every().day.at("22:26").do(send_message, MEDICATION_QUOTES)

while True:
    schedule.run_pending()
    time.sleep(2)
