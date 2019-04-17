## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name_01
* name{"name": null}
 - utter_greet
 - action_check_status
 - slot{"status": "received"} 
 - utter_status_received 

## story_name_02
* name{"name": null}
 - utter_greet
 - action_check_status
 - slot{"status": "rejected"} 
 - utter_status_rejected 

## story_name_03
* name{"name": null}
 - utter_greet
 - action_check_status
 - slot{"status": "interview"} 
 - utter_status_interview 

## story_name_04
* name{"name": null}
 - utter_greet
 - action_check_status
 - slot{"status": "unknown"} 
 - utter_status_unknown  

## story_name_05
* greet
 - utter_name
* name{"name" : null}
 - utter_greet_simple
* inquiry
 - utter_simple_message
 - action_check_status
 - slot{"status": null} 
 - utter_status_generic 
   
## story_process_01
* greet
 - utter_name
* name{"name" : null}
 - utter_greet_simple
* process
 - utter_check
* status{"role_type" : null}
 - action_provide_process

## story_check_01
* greet
 - utter_name
* check
 - utter_check
* status{"role_type" : null}
 - action_check_positions
 - slot{"positions": null}
 - utter_positions
