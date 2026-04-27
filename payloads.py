import random
import string

def get_payloads():
    return [
        # Basic
        "A" * 10000,
        "' OR 1=1 --",
        "!@#$%^&*()",
        "",
        None,

        # Numbers
        str(-999999999),
        str(999999999999999),
        "0",

        # Path traversal / IDOR-like
        "../../etc/passwd",
        "../admin",
        "/root",

        # JSON / malformed
        "{invalid:json}",
        '{"quantity": "999999"}',

        # Special edge cases
        "null",
        "undefined",
        "NaN",

        # Mixed payloads
        "'; DROP TABLE users; --",
        "<script>alert(1)</script>",

        # Random string
        ''.join(random.choices(string.ascii_letters + string.digits, k=50))
    ]