import random 
import string 

def get_payloads():
    return [
        "A" * 10000,
        "' OR 1=1 --",
        "!@#$%^&*()",
        "",
        None,
        str(-999999999),
        str(999999999999999),
        "../../etc/passwd"
    ]