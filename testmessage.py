import json
import requests

url = "https://slack.com/api/chat.postMessage"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer xoxb-553591163476-974425218322-lEOFsFDC1hOumYJbLIQAubIY'
}

qna_title = "왜 크레딧이 지급이 안 될까요?"
qna_body = "3일전에 작업한 것 크레딧이 안들어왔어요."
qna_url = "https://tower.deepnatural.ai/admin"

payload_dict = {
    "channel": "#api_test",
    "blocks": [
        {
            "type": "section",
            "text": {
                "type":"mrkdwn",
                "text":"[QA]\n<https://tower.deepnatural.ai/admin|*왜 크레딧이 지급이 안 될까요?*>\n>3일전에 작업한 것 크레딧이 안들어왔어요."
            } 
        }
    ]
}
payload = json.dumps(payload_dict)
response = requests.request("POST", url, headers=headers, data = payload)
print(response.content)


