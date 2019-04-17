# RASA starter-pack changes for Recruitment

Following information is info on the changes in continuation with info described in the starter-pack:
https://github.com/RasaHQ/starter-pack-rasa-stack/blob/master/README.md

# About
The package addresses the working of a simple chatbot which can perform the conversations as needed for the exercise in question. This includes modification to respective training data, action info and run script which provides working chatbot.

# Versions
rasa_core==0.13.6
rasa_nlu==0.14.6

# Working
Intents specified for action
* check
* goodbye
* thanks
* status
* greet
* name
* inquiry
* process

Allows following types of conversation:
> “Hi”

“hi, I’m Rasa’s recruiting bot. How can I help?“

> “I’d like to know which positions are open right now”

“Are you looking for a technical or a business role?”

> "A technical one"

“ML Engineer and Solutions Engineer are the open positions.”

**and**

> “Hi, my name is Ali Park. I applied for a job and would like to know when I’ll hear back”

“Hi Ali! Let me check that for you”

> “Yes, your application has been received.”
 
