from twilio.rest import TwilioRestClient 
 
# temporary SID
ACCOUNT_SID = "ACbec6453793a6556106fb9b1458b8a1fb" 
#temporary secret
AUTH_TOKEN = "1797babb76a8f68db5c40608f11" #missing characters 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
 #set the details here
client.messages.create(
	to="+44[target phone number]", 
	from_="[from text]", 
	body="[body of message]",  
)