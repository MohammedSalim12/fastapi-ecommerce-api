import requests
from config import SENDGRID_API_KEY, SENDER_EMAIL


def send_email(to_email: str, subject: str, content: str):
    url = "https://api.sendgrid.com/v3/mail/send"

    headers = {
        "Authorization": f"Bearer {SENDGRID_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "personalizations": [
            {
                "to": [{"email": to_email}],
                "subject": subject
            }
        ],
        "from": {"email": SENDER_EMAIL},
        "content": [
            {
                "type": "text/html",
                "value": content
            }
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json() if response.text else {"status": "sent"}
