# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("<your SID>", "<your token>")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="<your phone number>", 
                       from_="<phone of sender>", 
                       body="Motion detected: http://192.168.0.10/page.php") #link to web server
