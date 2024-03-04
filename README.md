# Module 9: AI-Assisted Chatbot

** Objective and Relevance **

* Artificial Intelligence Assisted Counselling Chatbot (named as Rakshak)
* Languages: English, Hindi and Code-mixed 
* Empathy-awareness
* Facebook, Whatsapp, Web Integration 
* Victims may not express themselves freely to the investigative agencies or their parents or guardians
* Chatbot would facilitate the conversation with the victims
* Chatbot could provide useful suggestions to come out of the mental trauma by conversing in an empathetic way (understanding the victim’s emotions) 
* Chatbot could also provide some legal suggestions and assistance

# Requirements:
* Create environment  for running trained model
  - conda create -n model
* Python
  - conda install python==3.8.0
* Torch
  - pip install torch==1.10.1
  - cuda==11.1
* Transformers
  - pip install transformers==4.36.2
* PEFT
  - pip install peft==0.7.1
  - When you installed PEFT, it will change torch version, so again install torch using given command(we did this because our GPU does not support torch 2.x)
* Pandas
  - pip install pandas==2.0.3
* Datasets
  - pip install datasets==2.16.1
* TRL
  - pip install trl==0.7.7
* Bitsandbytes
  - pip install bitsandbytes==0.41.3

* Create environment for RASA model
  - conda create -n rasa
* Python
  - conda install python==3.8.1 
* RASA
  - pip install rasa==2.8.0
  - If getting “Descriptors cannot not be created directly” error while running rasa model, then install protobuf using below command
    - pip install protobuf==3.20.*

# Hardware Requirement:
* GPU and cuda>=11.1

# Running Generation model
* Activate the model environment
* Download the model from "https://drive.google.com/drive/folders/1n_uzrbSocH-gKI0h4E002jsaBnRt_0Qw?usp=drive_link"
* Put the model in the folder from where model_api.py can access the model
* Use "python model_api.py" for running the model file
  
# Training RASA
* Use "Rakshak_English_Updated" or "Rakshak_Hindi_Updated" or "Rakshak_codemixed_Updated" rasa model
* Activate rasa environemnt
* Use "rasa train" for training RASA model
  
# Running RASA
* rasa run -vv --enable-api --cors "*"
* rasa tun actions

# Web Interface
* Activate model environemnt
* Run "python web.py"
  
  
# Dialogue flow of conversations(used for training the model):
* Greeting("Hello Rakshak" or "हेलो रक्षक।")
* Name Information or Privacy concern from user
* Event narration
  - Online stalking
  - Online harassment
  - Online Masquerading
* Help information
  - Legal help
  - Law information
  - Organisation name
    - NCW
    - Cyber crime
    - Cyber cell
    - MWCD
  - Helpline numbers(nationwide numbers or state wise information)
* Counselling help
  - Women-in-distress
  - NCW
* Other queries(Charges, timing information etc.)
* Closing remark

# Limitations

* Event narration
  - Grammatical error or wrong sentences formation
  - “He got my pictures along with my boyfriend and try to blackmailing me.”
     - Correct: He got my pictures along with my boyfriend and tried to blackmail me.”
  - Ambiguous words
    - I am uncomfortable
    - “वह मेरा फ़ायदा उठ रहा है”


