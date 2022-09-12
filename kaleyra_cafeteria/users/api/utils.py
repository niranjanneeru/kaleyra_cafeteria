import requests


def sms(data):
    for name, ph_no in data.items():
        body = {
            'body': f"Hi {name}, Your Breakfast will be available in the Kaleyra Cafeteria. Admin Team",
            'sender': "KALERA",
            'to': ph_no,
            'type': "TXN",
            'template_id': "1107165959856139086"
        }
        headers = {
            'api-key': "Ad4ad639409238e113e1e420950e9ad48"
        }
        r = requests.post('https://api.in.kaleyra.io/v1/HXIN1740145135IN/messages',
                          headers=headers,
                          params=body)
        print(r.status_code)
        print(r.text)
