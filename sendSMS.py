from twilio.rest import TwilioRestClient 
 
# Twilio SID
ACCOUNT_SID = "ACbec6453793a6556106fb9b1458b8a1fb" 
# Twilio Primary Token (replace)
AUTH_TOKEN = "XXXXX"
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
#set the details here
client.messages.create(
	to="+44[target phone number]", 
	from_="[from text]", # 11 char max for short codes
	body="[body of message]",  
)
