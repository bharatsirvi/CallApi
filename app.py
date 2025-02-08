from flask import Flask, jsonify, request
from twilio.rest import Client
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("SID")
TWILIO_AUTH_TOKEN = os.getenv("TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/make-call', methods=['GET'])
def make_call():
    try:
        receiver_phone_number = request.args.get('phone')
        message = request.args.get('message', 'Alerting! Ram ram sa ram ram sa ram ram.')

        if not receiver_phone_number:
            return jsonify({"error": "Receiver phone number is required"}), 400

        # TwiML response with dynamic message
        twiml_response = f"<Response><Say voice='Polly.Aditi' language='en-IN'>{message}</Say></Response>"

        # Initiate the call
        call = client.calls.create(
            to=receiver_phone_number,
            from_=TWILIO_PHONE_NUMBER,
            twiml=twiml_response  # Twilio will read this message
        )

        return jsonify({"message": "Call initiated", "call_sid": call.sid}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
