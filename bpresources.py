import requests 
from datetime import datetime, timedelta

better_url = 'https://better-admin.org.uk/api/activities/venue/west-reservoir-centre/activity/open-water-swimming/times?date='

default_date = '2024-06-26'

headers = {
'accept': 'application/json',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
'origin': 'https://bookings.better.org.uk',
'priority': 'u=1, i',
'referer': 'https://bookings.better.org.uk/location/west-reservoir-centre/open-water-swimming/2024-06-26/by-time',
'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
}

def get_sessions(date):
    url = better_url+date.strftime('%Y-%m-%d')
    response = requests.get(url, headers=headers)
    data = response.json()
    data = data["data"]

    if isinstance(data, dict):
        sessions = []
        for key in data:
            sessions.append(data[key])
    else:
        sessions = data
    
    return [session for session in sessions if session["spaces"] != 0]
