from twilio.rest import Client
import config


client = Client(config.account_sid, config.auth_token)
call = client.messages.create(
    to="+3812234551",
    from_="Zeljka",
    body="This is my first message sent using Python! Uraaa!"
)
