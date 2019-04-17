<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/rasa-starter-pack/704 --> 

## intent:goodbye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot

## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you

## intent:name
- My name is [Juste camp](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity -->
- I am [Josh wall](name)
- I'm [Lucy Wu](name)
- People call me [Greg Chappell](name)
- It's [David Blaine](name)
- Usually people call me [Amy Welsh](name)
- My name is [John Rambo](name)
- You can call me [Sam](name)
- Please call me [Linda Green](name)
- Name name is [Tom](name)
- I am [Richard Atten](name)
- I'm [Tracy Wind](name)
- Call me [Sally](name)
- I am [Philipp Court](name)
- I am [Charlie](name)
- I am [Charlie Sheen](name)
- I am [Ben Ten](name)
- Call me [Susan](name)
- [Lucy](name)
- [Peter](name)
- [Mark](name)
- [Joseph Tribianni](name)
- [Tan](name)
- [Pete](name)
- [Elon Musk](name)
- [Penny](name)
- name is [Andrew](name)
- I [Lora](name)
- [Stan](name) is my name
- [Susan](name) is the name
- [Ross Gueller](name) is my first name
- [Bing](name) is my last name
- Few call me as [Angelina](name)
- Some call me [Julia Moore](name)
- Everyone calls me [Laura](name)
- I am [Ganesh](name)
- My name is [Mike](name)
- just call me [Monika](name)
- Few call [Dan](name)
- You can always call me [Suraj Kumar](name)
- Some will call me [Andrew](name)
- My name is [Ajay](name)
- I call [Ding](name)
- I'm [Partia](name)
- Please call me [Leo Tolstoy](name)
- name is [Pari](name)
- name [Sanjay](name)
- Hi, my name is [Ali Park](name). I applied for a job and would like to know when I’ll hear back
- Hi, my name is [Tom Hagen](name). I applied for a job and would like to know when I’ll hear back
- Hi, my name is [Sandeep Doda](name). I applied for a job and would like to know when I’ll hear back
- Hi, I am [Ali Park](name). I applied for a job and would like to know when I’ll hear back
- Hi, I am [Roger Sterling](name). I applied for a job and would like to know when I’ll hear back
- Hi, I am [Don Draper](name). I applied for a job and would like to know when I’ll hear back
- Hi, I am [Ali Park](name). I applied for a job, What is the status of my application
- Hi, I am [Truman Capote](name). I applied for a job, What is the status of my application
- Hi, I am [Don Draper](name). I applied for a job, What is the status of my application
- Hi, [Ali Park](name) here. I would like to know the status of my job application
- Hi, [Cloud Strife](name) here. I would like to know the status of my job application
- Hi, [Vinsmoke Sanji](name) here. I would like to know the status of my job application
- Hi, I would like to know the status of my job application. I am [Jon Snow](name)
- Hi, I would like to know the status of my job application. I am [Ali Park](name)
- Hi, I would like to know the status of my job application. I am [Kill Bill](name)
- Hi, this is [Ali Park](name) here. I applied for a job and would like to know when I’ll hear back
- Hi, this is [Obiwan Kenobi](name) here. I applied for a job and would like to know when I’ll hear back
- Hi, this is [Master Yoda](name) here. I applied for a job and would like to know when I’ll hear back
- Hi, this is [Ali Park](name) here. I applied for a job, What is the status of my application
- Hi, this is [Star Lord](name) here. I applied for a job, What is the status of my application
- Hi, this is [Bruce Wayne](name) here. I applied for a job, What is the status of my application

## intent:inquiry
- I applied for a job and would like to know when I’ll hear back
- I applied for a job, What is the status of my application
- What is the status of the job application that I have applied for
- What is the status of the my job application
- My job application status please
- Please provide application status of Job I have applied for

## intent:check
- I’d like to know which positions are open right now
- I would like to know which positions are open right now
- Can you provide the list of open positions
- current open positions please
- Which positions can I apply for
- Please provide the list of positions open
- Please let me know what positions are currently open

## intent:status
- A [technical](role_type) one
- [technical](role_type)
- [technical](role_type) positions
- [Business](role_type) positions
- A [Business](role_type) one
- [Business](role_type)
- [any](role_type)

## intent:process
- Can you provide info on the interview process
- Please provide details on the interview process
- What is the due process for the interviews
- Please provide information on the interviews
- Can I get details on interview process
