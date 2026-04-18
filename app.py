from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json

    account_id = request.args.get("account_id") or (request.json or {}).get("account_id")
    amount = request.args.get("amount") or (request.json or {}).get("amount")

    #  No validation (intentional vulnerability)
    if amount:
        amount = int(amount)

    if amount < 0:
        return jsonify({"status": "Negative transfer allowed!"})

    if amount > 1000000:
        return jsonify({"status": "Large transfer processed!"})

    return jsonify({"status": "Transfer successful"})

if __name__ == "__main__":
    app.run(debug=True)