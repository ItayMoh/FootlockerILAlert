# FootlockerILAlert

A simple script in python alerting a new shoe launch in Footlocker.co.il using a discord webhook.

### How to use:
1. Install the required lbraries using pip install -r /path/to/requirements.txt 
2. Paste your discord webhook under the global variable WEBHOOKURL in line 6. [How to create discord webhook can be found here](https://hookdeck.com/webhooks/platforms/how-to-get-started-with-discord-webhooks#discord-webhook-example)
3. Run it in the background

### How does it work?
For detailed expleneation look [Here](https://developingg.blogspot.com/2022/07/developing-footlocker-il-alert-bot-from.html)

The script is checking for changes in the amount of released stock using the api responsible for stock.
If a change is occuring, it will send an alert to the discord channel notifying everyone that is in the channel using @all with descriptive image and url to purchase the item.
