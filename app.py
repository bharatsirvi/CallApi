from flask import Flask, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("SID")
TWILIO_AUTH_TOKEN = os.getenv("TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("NUMBER")
RECEIVER_PHONE_NUMBER = os.getenv("PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/make-call', methods=['GET'])
def make_call():
    try:
        # TwiML response to play a voice message

        twiml_response = "<Response><Say voice='Polly.Aditi' language='en-IN'>Alerting! This is an emergency message. Please take immediate action.</Say></Response>"

        # Initiate the call
        call = client.calls.create(
            to=RECEIVER_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            twiml=twiml_response  # Twilio will read this message
        )

        return jsonify({"message": "Call initiated", "call_sid": call.sid}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)




