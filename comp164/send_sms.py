# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACbee6f4d77120177a4cc01c411fb37ffc", "f301c85d9637130b1ddaf8afcb43f049")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+17733875605", 
                       from_="+19543985646", 
                       body="Motion detected: http://192.168.0.10/page.php")
