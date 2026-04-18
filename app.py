from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/order", methods=["POST"])
def order():
    try:
        data = request.json

        product_id = data.get("product_id")
        quantity = data.get("quantity")

        # Vulnerability 1: No proper type validation
        if isinstance(quantity, str):
            quantity = int(quantity)  # may crash for bad input

        # Vulnerability 2: Negative quantity allowed
        if quantity is not None and quantity < 0:
            return jsonify({
                "status": "Negative quantity accepted!",
                "issue": "Business Logic Flaw"
            })

        # Vulnerability 3: No upper limit check
        if quantity is not None and quantity > 100000:
            return jsonify({
                "status": "Bulk order processed without restriction!",
                "issue": "Missing Limit Validation"
            })

        # Vulnerability 4: IDOR-like behavior
        if isinstance(product_id, str) and "../" in product_id:
            return jsonify({
                "status": "Accessed restricted product!",
                "issue": "Potential IDOR"
            })

        #Vulnerability 5: Empty product ID accepted
        if not product_id:
            return jsonify({
                "status": "Order placed without product ID!",
                "issue": "Improper Input Validation"
            })

        return jsonify({
            "status": "Order placed successfully"
        })

    except Exception as e:
        # Vulnerability 6: Internal error exposure
        return jsonify({
            "error": str(e),
            "issue": "Unhandled Exception"
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
