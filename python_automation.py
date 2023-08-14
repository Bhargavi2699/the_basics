#prg will send 'good morning' messages to particular number every morning/day
#give it a particular time as well like 6 am or 7 am
#install schedule library for this
#a website(textbelt.com) has this API, which can be sued to send text messages.
#so we need to install requests library for this - particular for once a day messages

from credentials import mobile_number
import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : mobile_number,
        'message' : 'Hey. Good Morning!',
        'key' : 'textbelt' #can use that only once a day, try using Twilio maybe
    })
    print(resp.json())

#schedule.every().day.at('06:00').do(send_message)

schedule.every(10).seconds.do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)
