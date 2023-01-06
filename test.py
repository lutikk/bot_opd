import requests as req

ss = req.post('https://luxuryduty.ru/api/dutys/get_stikers/', json={'id': 1})

lol = ss.json()
print(lol['response']['text'])