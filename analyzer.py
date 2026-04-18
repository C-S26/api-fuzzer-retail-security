def analyze(response):
    #
    if isinstance(response, str):
        return "Request failed"
    if response.status_code >= 500:
        return "server error"
    
    text =  response.text.lower()
    
    if "negative transfer" in text:
        return "Logic Flaw: Negative Amount Accepted"

    if "large transfer" in text:
        return "Potential Overflow / Missing Limit Check"

    return "No obvious issue"

