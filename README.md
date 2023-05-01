## Introduction
Welcome to the Pizzabot! This chatbot has been developed using the open-source machine learning framework [Rasa](https://rasa.com/).The chatbot allows users to book  flights to different destinations of Nepal. It can be extented to handle queries related to flight schedules, ticket prices, and seat availability. 

## About RASA
Rasa is an open-source machine learning framework that enables the development of conversational AI chatbots. The Rasa stack consists of two main components:
 
1. Rasa NLU 
2.  Rasa Core
 
 Rasa NLU handles the natural language understanding aspect of the chatbot, and Rasa Core handles the dialogue management aspect.



## Getting Started

Before getting started with the chatbot, make sure you have the following requirements installed:

- Python 3 
- pip (package manager for Python)

To install Rasa, you can use the following pip command:<br />
```pip install -r requirements.txt```

Once you have Rasa installed, you can clone this repository and navigate to the directory containing the chatbot files.

## Training the Chatbot
To train the chatbot, you can use the following command:<br />
```rasa train```

## Running the Chatbot
**Step 1: To run the chatbot, you can use the following command:**<br />
```rasa run```


**Step 2: For basic validations you need to be connected to action server**<br />
To run the action server, you can use the following command:<br />
```rasa run actions```

**Step 3: Accessing the chatbot via RASA CLI**<br />
Now we have the Rasa server up and running, and the chatbot will be available to chat with through the Rasa command line interface.
To talk with the bot, you can use the following command:<br />
```rasa shell```


## Running the application via docker
First you should have docker installed on your system. With that to run the chatbot in docker environment, you can use the following command:<br />
```docker-compose up```

## Customizing the Chatbot<br />
The chatbot's behavior and responses are defined in the data/nlu.yml and data/domain.yml files. You can modify these files to add your own custom intents and responses. Additionally, the chatbot's conversational flow is defined in the stories.yml file, and you can modify this file to add custom actions and change the flow of the conversation.





