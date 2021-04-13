import re

user_pattern = r"[U][$]([A-Z][a-z]{2,})[U][$]"
pass_pattern = r"[P][@][$](\w{5,}[0-9])[P][@][$]"

count = int(input())
registration = 0
for _ in range(count):
    data = input()
    match_user = re.findall(user_pattern, data)
    match_pass = re.findall(pass_pattern, data)
    if len(match_user) > 0 and len(match_pass) > 0:
        print("Registration was successful")
        print(f"Username: {str(match_user[0])}, Password: {str(match_pass[0])}")
        registration += 1
    else:
        print("Invalid username or password")
print(f"Successful registrations: {registration}")