from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from Whatapp.weather import get_weather

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def weather():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    weather = get_weather(incoming_msg)
    if weather is not False:
        msg.body(f"{incoming_msg}: {weather['cities'][incoming_msg]['temp']}")
        responded = True
    else:
        msg.body('Error Try Again')

    return str(resp)


if __name__ == '__main__':
    app.run(port=8000)
