from twilio.rest import TwilioRestClient 
 
# temporary SID
ACCOUNT_SID = "SK4b09f7c9387af3cd29a7632c5abb92ab" 
#temporary secret
AUTH_TOKEN = "0GpMTfrpozAMho56LByV5QAcQKPi" #missing characters 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
 #set the details here
client.messages.create(
	to="+44[to address]", 
	from_="[from name", 
	body="[message content]",  
)