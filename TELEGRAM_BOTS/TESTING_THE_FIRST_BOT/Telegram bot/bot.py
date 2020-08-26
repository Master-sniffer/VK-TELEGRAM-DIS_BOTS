import requests

TOKEN = '1379710116:AAG9BmigUQlgZKnQ3_JEWqKo--7HbbiF1O0'
MAIN_URL=f'https://api.telegram.org/bot{TOKEN}'

payload={
    'chat_id':158404626,
    "text":"Salam aleikum, brat",
    'reply_to_message_id': 2
}

r = requests.post(f"{MAIN_URL}/sendMessage", data=payload)
print (r.json())