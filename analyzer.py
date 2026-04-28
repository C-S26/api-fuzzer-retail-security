def analyze(response):
    if isinstance(response, str):
        return "Request Failed (Connection/Input Issue)"

    if response.status_code >= 500:
        return "Server Crash Detected"

    if response.status_code == 400:
        return "Input Validation Detected"

    text = response.text.lower()

    if "negative quantity accepted" in text:
        return "Logic Flaw: Negative Quantity Accepted"

    if "bulk order processed" in text:
        return "Missing Limit Validation"

    if "accessed restricted product" in text:
        return "Potential IDOR"

    if "possible injection" in text:
        return "Injection Attempt Detected"

    if "script detected" in text:
        return "XSS-like Payload Detected"

    if "missing product id" in text:
        return "Improper Input Validation"

    return "No obvious issue"