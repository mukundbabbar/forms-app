import os
from twilio.rest import Client
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
status_callback_url = os.environ['CALLBACK_URL']
client = Client(account_sid, auth_token)
from_number = os.environ['FROM_PHONE_NUMBER']


def send_sms(to_number, errors):
    print("Sending SMS")
    try:
        message = client.messages \
            .create(
                body='Congurations! Lockdown will be over soon',
                from_=from_number,
                status_callback=status_callback_url,
                to=to_number
            )
        print(message)
    except Exception as e:
        errors.append("Error sending SMS")
        print(e)


def validate(num, errors):
    print("Validatinig Number")
    try:
        phone_number = client.lookups \
            .v1 \
            .phone_numbers(num) \
            .fetch()
        print(phone_number)
        return True
    except Exception as e:
        errors.append("Not a valid number")
        print(e)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            number = request.form['number']
            # r = requests.get(number)
            print(number)
            to_number = number
            # validate number
            if validate(to_number, errors) == True:
                # send SMS
                send_sms(number, errors)
                # Wait for delivery
        except Exception as e:
            errors.append(
                "Unable to send text number. Please provide phone number and try again."
            )
            print(e)
    return render_template('index.html', errors=errors, results=results)
    errors = []


if __name__ == '__main__':
    app.run()
