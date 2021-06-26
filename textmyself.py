from twilio.rest import Client

accountSID = "AC84a51e4f006c7787729bc1c3b2070699"
authToken = "561d702702fed39283b288cbd4f48adc"
myNumber = "+15593683249"
twilioNumber = "+13122783599"


def textmyself(message):
    client = Client(accountSID, authToken)
    client.messages.create(from_=twilioNumber, to=myNumber, body=message)
