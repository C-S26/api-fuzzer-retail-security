from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/order", methods=["POST"])
def order():
    try:
<<<<<<< HEAD
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
=======
        data = request.get_json(silent=True) or {}

        product_id = str(data.get("product_id", ""))
        quantity_raw = data.get("quantity")

        # -----------------------------
        # Detect patterns FIRST
        # -----------------------------

        if "../" in product_id or ".." in product_id:
            return jsonify({"status": "accessed restricted product"})

        if "or 1=1" in product_id.lower():
            return jsonify({"status": "possible injection"})

        if "drop table" in product_id.lower():
            return jsonify({"status": "possible injection"})

        if "<script>" in product_id.lower():
            return jsonify({"status": "script detected"})

        # -----------------------------
        # Convert quantity safely
        # -----------------------------
        try:
            quantity = int(quantity_raw)
        except:
            return jsonify({"status": "invalid quantity input"}), 400

        # -----------------------------
        # Logic flaws
        # -----------------------------
        if quantity < 0:
            return jsonify({"status": "negative quantity accepted"})

        if quantity > 100000:
            return jsonify({"status": "bulk order processed"})

        # -----------------------------
        # Missing product ID
        # -----------------------------
        if product_id.strip() == "":
            return jsonify({"status": "missing product id"})

        return jsonify({"status": "order placed successfully"})

    except Exception as e:
        return jsonify({"status": "server error", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
>>>>>>> d1411b8 (retail updated)
