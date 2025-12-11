import requests
import pyfiglet

ascii_logo = pyfiglet.figlet_format("Leahcim")

#Hårdkodade URLs för PoC
TOKEN_URL  = "http://10.3.10.104:3000/api/token"
SECRET_URL = "http://10.3.10.104:3000/api/verify"
FLAG_URL   = "http://10.3.10.104:3000/api/flag"

#Funktion för att begära token från API
def get_token(token_url):
    response = requests.post(token_url)
    data = response.json()
    return data["token"]

#Funktion för att med token i HEADER verifiera token och få en secret key.
def get_secret(secret_url, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(secret_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["secret"]
    else:
        raise RuntimeError("Failed to connect")

def get_flag(flag_url, token, secret):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"secret": secret}
    response = requests.post(flag_url, headers=headers, json=payload)
    data = response.json()
    return data["flag"]


def main():
    token = get_token(TOKEN_URL)
    secret = get_secret(SECRET_URL, token)
    flag = get_flag(FLAG_URL, token, secret)
    print(ascii_logo)
    print("[+]   SUCCESS, Flag found in time   [+]")
    print(f"[+]  {flag}  [+]")


if __name__ == "__main__":
    main()