# SD-Tele

* Use this script to send a text message using the Twilio API
* API key is temporary (and not valid)

## Usage

#### Install the plugin from this repository in your browser

* To do so, go to (in Chrome) Settings->Extensions
* Click (at the top) Load Unpacked Extension
* Choose the folder "ClonePage" in this repostiory

#### Browse to site to clone

* Click the plugin in the top right of the browser (bluish box). A pop up will appear, select all, copy, paste all of the code into a new Playto project

#### Create the phishing site

* Click View App In Full Screen in Playto. Copy the domain (without parameters)

#### Edit the Sending SMS Script

* in this repo is a python script, edit it

	* Edit the "to" (including country code)
	* Set the from name - this can be a word like "TrustedBank"
	* Set the body text of the message, including your link you copied

#### Done