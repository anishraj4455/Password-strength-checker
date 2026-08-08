# The code is related to check password strength 
import re

def check_password(p):
    score = (len(p) >= 8) + bool(re.search(r"[A-Z]", p)) + bool(re.search(r"[0-9]", p))
    return "Strong 🟢" if score >= 2 else "Weak 🔴"

if __name__ == "__main__":
    print(check_password(input("Enterpassword: ")))
