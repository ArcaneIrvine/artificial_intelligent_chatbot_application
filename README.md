# Artificial Intelligent Chat-Bot web application
This is a personal project made in python. Project's goal is creating an artificial intelligent bot trained on data i will be giving it able to communicate with the user on a webpage after the user creates an account. This project will enchance my AI, Neural Network, Natural Language Processing, Web applications and Databases skills.

### Chat Bot
To create the chatbot i first created a yaml file where i wrote down bot's data. I preprocessed the data by stemming it and saving down each needed data on lists such as words, labels etc. For the training part i used one hot encoding and a Neural Network system with 2 layers of 8 neurons using Tensorflow Deep Learning library. Trained the model on 1000 epochs and saved it after testing its accuracy and loss.

### Web Page
For the front end development i used Bootstrap and ready templates that i touched and changed to make it look better. For the back end development i used Flask and sqlalchemy for the Database. User has to fill the signup form correctly, appropriate flash errors will be thrown in case user makes mistakes. Then an OTP code is sent to the users email using flask_mail, if OTP is typed correctly then the user gets saved in the database along with his password encrypted for safety reasons. Once logged in now the user is able to start chatting with the Bot which is loaded into the website. User also has the ability to log out or delete their account which will delete their data from the Database.

### Features
Some additional features are that aside from the User's email, username and password being saved in the database their chat history with the bot also is saved along with the date seperately for each user. Aside from that in case the Bot does not know how to answer a user's question that specific question will be seperately saved in the Database as well. That is helpful for storing data useful for improving the Bot's knowledge later on.

## Requirements: Python 3.8
- numpy
- nltk
- pyyaml
- tflearn
- tensorflow
- sqlalchemy
- flask_sqlalchemy
- flask_login
- flask_mail

## Pages <br />
![signup](https://user-images.githubusercontent.com/75722160/218892670-d2f136e7-af9a-4d2d-8921-76cd87c4b3e8.png)
![chat](https://user-images.githubusercontent.com/75722160/218892679-58c6e398-e9ec-4195-9fe9-16c7933a861f.png)
## Database <br />
![user](https://user-images.githubusercontent.com/75722160/218892699-1b6fc29b-43f8-4cb0-8da8-c63a9042191b.png)
![history](https://user-images.githubusercontent.com/75722160/218892703-3d465300-0059-4611-bfa0-5aff496c01cd.png)
