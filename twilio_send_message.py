from twilio.rest import Client

sid = 'AC9f7e22c7cbced0e5f88ec7083c299fb9'
authToken = 'e987be6954ab4b2cc57f7a8938f431cb'
client = Client(sid, authToken)

message = client.messages.create(to='whatsapp:+XXXXXXXXX',
                                 from_='whatsapp:+XXXXXXXX',
                                 body='Add message here')
