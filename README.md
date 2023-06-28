Module 9: AI-assisted Chatbot - Rakshak


1. Overview


This module offers an AI-assisted chatbot, named Rakshak. Rakshak is built with the aim of counseling the victims and making them aware of the laws & cyber-safety tips while being empathetic and cordial towards them. Rakshak can converse with the users in English, Hindi and Hinglish (Hindi+English code-mixed).


2. Infrastructure Requirement


* Rasa 2.8.0
   * pip3 install -U pip
   * pip3 install rasa
   * rasa init
   * For detailed installation instructions, you may refer to https://rasa.com/docs/rasa/installation/installing-rasa-open-source/
* Python-3.8.1




3. I/O format


The users will tell their problems and then Rakshak will reply back to the user according to their emotional and mental state and try to enquire about the problem faced by the user and help them accordingly.  



4. Execution instruction


* Clone the repository or download the zip folder from the github repository “https://github.com/MHA-Counselling-Chatbot/MHA-CHATBOT”


* Create virtual environment
   * Windows
      * pip install virtualenv 
      * virtualenv  pathOf Virtualenv -p software you want to install.
   * Linux
      * conda create -n envName


* Activate the created environment
   * Windows
      * pathof VirtualEnc/Scripts/activate
   * Linux
      * conda activate envName


* Install required software
   * Python-3.8.1
   * Rasa-2.8.0


* Go to the downloaded folder MHA-CHATBOT/ and choose which language model you want to run:
   * RASA-English/
   * RASA-Hindi/
   * RASA-Code-Mixed/

* Go to RASA-Code-Mixed/CHATBOT/

* Train new model 
   * rasa train (This command will train new model)

* Run the model
   * rasa run -vv --enable-api --cors "*"  (This command will run the model)
   * rasa run actions


* Run the index.html file from the front-end folder  on the local host server or manually in the web browser.
* Directory Structure
    
MHA-CHATBOT/

    RASA-English/
        CHATBOT/
            actions/
            data/
            front-end/
                index.html
            tests/
            config.yml
            credentials.yml
            domain.yml
            endpoints.yml
            Story_graph.dot

    RASA-Hindi/
        CHATBOT/
            actions/
            data/
            front-end/
                index.html
            tests/
            config.yml
            credentials.yml
            domain.yml
            endpoints.yml
            Story_graph.dot

    RASA-Code-Mixed/
        CHATBOT/
            actions/
            data/
            front-end/
                index.html
            tests/
            config.yml
            credentials.yml
            domain.yml
            endpoints.yml
            story_graph.dot



