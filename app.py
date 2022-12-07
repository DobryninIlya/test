from requests import get
from time import sleep


def main():
    r = get("https://legalchik.onrender.com/ping")
    print(r, r.text)


while True:
    try:
        main()
        sleep(599)
    except Exception as e:
        print(e)
        sleep(500)
