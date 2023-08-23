from twilio.rest import Client

account_sid = 'AC46efb628867a73cc1a31614e4075c74d'
auth_token = '4ff3b15af50281002e92ecfc754db7db'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12292807900',
  body='Sadia call you for being her fuckbuddy',
  to='+918875187588'
)

print("message sent")