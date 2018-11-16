import sys
import requests
import os

# 環境変数にGOOGLE_API_TOKENをセットしておく
GOOGLE_API_TOKEN = os.environ['GOOGLE_API_TOKEN']


def main(content):
    url = "https://language.googleapis.com/v1/documents:analyzeSentiment?key=%s" % GOOGLE_API_TOKEN
    header = {'Content-Type': 'application/json'}
    body = {
        "document": {
            "type": "PLAIN_TEXT",
            "language": "JA",
            "content": content
        },
        "encodingType": "UTF8"
    }
    res = requests.post(url, headers=header, json=body).json()
    print(res)
    print(res['documentSentiment']['score'])
    if 0.26 <= res['documentSentiment']['score']:
        print("good")
    elif -0.25 <= res['documentSentiment']['score'] <= 0.25:
        print("neutral")
    elif -0.26 >= res['documentSentiment']['score']:
        print("bad")


if __name__ == '__main__':
    main(sys.argv[1])
