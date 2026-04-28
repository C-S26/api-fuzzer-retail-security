from payloads import get_payloads
from fuzzer import send_request
from analyzer import analyze
from logger import log
from config import API_URL

def run_fuzzer():
    payloads = get_payloads()
    #load payloads and test
    for payload in payloads:
        print(f"Testing payload: {str(payload)[:50]}...")
        #gather result from response
        response = send_request(API_URL, payload)
        result = analyze(response)
        #print the result
        if "Flaw" in result or "Detected" in result or "IDOR" in result:
          print(f"{result}\n")
        else:
          print(f"Result: {result}\n")

if __name__ == "__main__":
    run_fuzzer()
