import requests
 
def send_request(url, payload):
    try:
        data = {
            "amount":payload,
            "account_id":payload
        }

        response = requests.post(url, json=data, timeout=5)
        return response
    except Exception as e:
        return str(e)
