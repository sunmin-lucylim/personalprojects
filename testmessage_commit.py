import json
import requests

url = "https://slack.com/api/chat.postMessage"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer [Token]'
}

qna_title = "[Title]"
qna_body = "[Body]"
qna_url = "[URL]"

payload_dict = {
    "channel": "#[CHANNEL]",
    "blocks": [
        {
            "type": "section",
            "text": {
                "type":"mrkdwn",
                "text":f"[QA]\n<{qna_url}|*{qna_title}*>\n>{qna_body}"
            } 
        }
    ]
}
payload = json.dumps(payload_dict)
response = requests.request("POST", url, headers=headers, data = payload)
print(response.content)


