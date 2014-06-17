from os import environ

try:
    from twilio.rest import TwilioRestClient
except ImportError:
    print("You need to install Twilio: sudo pip install twilio")
    exit(0)


# In order to use this script, you need to acquire these credentials
# from twilio.com

# then enter them in your terminal using the following commands:

# export TWILIO_ACCOUNT_SID="XXXXXXXXXX"
# export TWILIO_AUTH_TOKEN="XXXXXXXXXXX"

try:
    client = TwilioRestClient(
        environ['TWILIO_ACCOUNT_SID'],
        environ['TWILIO_AUTH_TOKEN']
    )
except KeyError:
    "You need to set your Twilio credentials. See https://github.com/twilio/twilio-python"
    exit(1)

phone_numbers = [
    '+26772986824',
    # other numbers go here
]

for number in phone_numbers:
    client.calls.create(
        to=number,
        from_='+27875504585',  # I bought this number at twilio.com
        url="http://hotlines.herokuapp.com/music/"
    )
