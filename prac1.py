import re

def check_passwords(passwords):
    valid_passwords = []


    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$')


    password_list = passwords.split(',')


    for password in password_list:
        if pattern.match(password):
            valid_passwords.append(password)


    return ','.join(valid_passwords)


input_password = "asqwr1234@1,aF145#,2w3E*,2We3345"
output = check_passwords(input_password)
print(f"Valid passwords: {output}")
