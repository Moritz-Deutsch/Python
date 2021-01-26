import requests
import json
import names
import random
import string
import time

bad_url = "https://chalkwoodhouse.co.za/dss/next.php"
emails = ["gmail.com","freenet.de","web.de","gmx.net","yahoo.com","hotmail.com","aol.com","hotmail.co.uk","hotmail.fr","msn.com"]
counter = 0

def send_request():
    email = names.get_full_name().replace(" ",".") + "@" + random.choice(emails)
    password = "".join(random.choice(string.ascii_letters) for i in range(random.randint(8,13)))
    payload = {"email":email,"password":password}
    requests.post(bad_url,allow_redirects=False, data=payload)
if __name__ == "__main__":
    while True:
        send_request()
        counter += 1
        print("Number of accounts: " + counter)
        time.sleep(10)