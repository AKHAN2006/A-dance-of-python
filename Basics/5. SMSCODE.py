# importing the client from the twilio
from twilio.rest import Client
import os

print("UI")
print(os.environ.get("ACCOUNT_SID"))

# Your Account Sid and Auth Token from twilio account
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

# instantiating the Client
client = Client(account_sid, auth_token)

# sending message
message = client.messages.create(body='From other system?', from_= "+18322636720"
, to=["+91 9121703462"])

# printing the sid after success
print(message.sid)