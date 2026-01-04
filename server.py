
from flask import Flask, request, jsonify
import stripe, csv

app = Flask(__name__)

stripe.api_key = "PASTE_STRIPE_SECRET_KEY"

@app.route("/lead", methods=["POST"])
def lead():
    data = request.json
    with open("leads.csv","a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([data["name"], data["phone"], data["desc"]])
    return jsonify({"status":"saved"})

@app.route("/pay", methods=["POST"])
def pay():
    intent = stripe.PaymentIntent.create(
        amount=10000,
        currency="uah",
        payment_method_types=["card"]
    )
    return jsonify(clientSecret=intent.client_secret)

app.run(port=5000)
