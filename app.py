from requests import get
from time import sleep


def main():
    r = get("https://legalchik.onrender.com/ping")
    print(r, r.text)


while True:
    main()
    sleep(599)
