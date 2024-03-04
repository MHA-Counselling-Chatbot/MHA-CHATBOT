# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
# #
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import Restarted
from rasa_sdk.events import FollowupAction
import requests
import re




f=open("log.txt","a")
s=open("suggestion.csv","a")
a="<cybercell_contact>"
b="<contact_number>"
c="<cybercell_address>"

# name1="मैं अनामिका हूं।"
# name2="मेरा नाम अनामिका है। "
# name3="मैं अनामिका बोल रही हूं।"
# name4="अनामिका"
# name5="मैं अनामिका।"

regex1=r'[D][r][.]'
regex2=r'[A][d][v][.]'
regex3=r'[0-9][0-9][0-9][0-9][0-9][#][#][#][#][#]'
regex4=r'[0-9][0-9][-][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
regex5=r'[0-9][0-9][0-9][-][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
regex6=r'[1][5][5][2][6][0]'

number=r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'





url = 'http://10.12.10.70:5013/gen'


list1=[]


import csv
# class ActionRestarted(Action):

#     def name(self) -> Text:
#         return "action_restart"

#     def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         #name1 = tracker.get_slot("name")
#         list1.clear()
#         print("clear current list")
        

#         return []
    

name_value=""

class ActionResponseInfo(Action):

    def name(self) -> Text:
        return "action_response_info"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #name1 = tracker.get_slot("name")
        print("inside action response class")

        test_case=tracker.latest_message["text"]

        #if test_case=="क्या आप कृपया साझा करेंगे कि मैं किससे बातचीत कर रहा हूं?"
        #if test_case=="हेलो रक्षक।" or test_case=="हेलो रक्षक":


        # itn=tracker.latest_message["intent"]["name"]
        # if itn=="name_info":
        #     global name_value
        #     nameX=test_case.split(" ")[3]
        #     name_value=nameX
        #     print(name_value)    
        

        #print("intent==",tracker.latest_message["intent"])

        if test_case=="restart":
           
            dispatcher.utter_message(name_value+"Conversation ends here. Please write your analysis/suggestion in 3-4 lines. First write your first name then type colon then start writing. example \"Armita: analysis_part\" ")
            
            #f.write("###"+"\n")
            return []
        
        t=test_case
        t.lower()
        if (test_case.startswith("Armita:")|test_case.startswith("Priyanshu:")|test_case.startswith("Saroj:")|(test_case.startswith("Anubhav:"))):
            # g=open("suggestion.csv","a")
            # gw=csv.writer(g)
            # sug_l=[[list1],[test_case]]
            # gw.writerows(sug_l)
            # g.close()
            list1.clear()
            print("clear list")
            dispatcher.utter_message("Writing logs. Wait. Done. Now start new conversation")
            return []




        
        #f.write(test_case+"\n")
        #url = 'http://10.12.10.70:5005/gen'
        
        ##[user,bot,user,bot]
        l=len(list1)
        print("len of list==",l)

        if l>=2:

            pre_bot=list1[l-1]

            pre_user= list1[l-2]
            t="[soc][user]"+pre_user+"[bot]"+pre_bot+"[user]"+test_case
            
            data={'text': t}


        else:
            test_case1="[soc][user]"+test_case
            data = {'text': test_case1}


        print("data===",data)
        response = requests.post(url, json=data)
        result = response.json()
        x=result['text']
        changed_x=x

        

        ## changing name information
        f.write(x+"\n")

        # if itn=="name_info" and (greet1 in x or greet2 in x):
        #     l_w=x.split(" ")
        #     l_w[3]=name_value
            
        #     name_string=""
        #     for lw in l_w:
        #         f.write(lw+" ")
        #         name_string=name_string+" "+lw

        #     changed_x=name_string
        #     print("changes name string==",changed_x)

        
        if a in x or b in x or c in x:
            changed_x= "कृपया प्रत्येक राज्य के लिए ईमेल पता और साइबर सेल नंबर प्राप्त करने के लिए ""https://cybercrime.gov.in/webform/Crime_NodalGrivanceList.aspx"" पर जाएं। यदि आपका राज्य उस सूची में नहीं है तो कृपया राष्ट्रीय पुलिस हेल्पलाइन 112, राष्ट्रीय महिला हेल्पलाइन 181 और साइबर अपराध हेल्पलाइन 1980 पर कॉल करें।"
        
        ###logic for removing Dr. and Adv. numbers and name
            
        elif re.search(regex1,x) or re.search(regex2,x) or re.search(regex3,x):
            changed_x="कृपया किसी भी कानूनी सहायता या मानसिक परामर्श सहायता के लिए ""http://www.ncw.nic.in/helplines"" पर जाएं।"

        elif re.search(regex4,x) or re.search(regex5,x):
            changed_x="कृपया शिकायत दर्ज कराने के लिए +91-11-26944880 या +91-11-26944883 पर संपर्क करें। अधिक जानकारी और हेल्पलाइन नंबरों के लिए कृपया ""http://www.ncw.nic.in/helplines""पर जाएं। "    

        elif re.search(regex6,x):
            changed_x="कृपया राज्यवार संपर्क नंबर और ईमेल पते के लिए ""https://cybercrime.gov.in/webform/Crime_NodalGrivanceList.aspx"" पर जाएं या कोई कानूनी सहायता या मानसिक परामर्श सहायता के लिए कृपया ""http://www.ncw.nic.in/helplines"" पर जाएं। आप किसी भी मदद के लिए राष्ट्रीय पुलिस हेल्पलाइन 112, राष्ट्रीय महिला हेल्पलाइन 181 और साइबर अपराध हेल्पलाइन 1980 पर भी संपर्क कर सकते हैं। "     

        
        elif re.search(number,x):
            changed_x= "कृपया शिकायत दर्ज कराने के लिए +91-11-26944880 या +91-11-26944883 पर संपर्क करें। अधिक जानकारी और हेल्पलाइन नंबरों के लिए कृपया ""http://www.ncw.nic.in/helplines""पर जाएं।"    

            
    


        ##storing into list
        list1.append(test_case)
        list1.append(result['text'])

        print("generated response from llama model:",result['text'])
        x=changed_x
        print("Response which is given to user and storing into log==",x)
        #f.write(x+"\n")
        print("list1==",list1)
        dispatcher.utter_message(text=x)

        return []
    


class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        print("inside action default class")

        test_case=tracker.latest_message["text"]

        if test_case=="restart":
           
            dispatcher.utter_message("Conversation ends here. Please write your analysis/suggestion in 3-4 lines. First write your first name then type colon then start writing. example \"Armita: analysis_part\" ")
            
            #f.write("###"+"\n")
            return []
        
        t=test_case
        t.lower()
        if (test_case.startswith("Armita:")|test_case.startswith("Priyanshu:")|test_case.startswith("Saroj:")|(test_case.startswith("Anubhav:"))):
            # g=open("suggestion.csv","a")
            # gw=csv.writer(g)
            # sug_l=[[list1],[test_case]]
            # gw.writerows(sug_l)
            # g.close()
            list1.clear()
            print("clear list")
            dispatcher.utter_message("Writing logs. Wait. Done. Now start new conversation")
            return []




        
        #f.write(test_case+"\n")
        #url = 'http://10.12.10.70:5005/gen'
        
        ##[user,bot,user,bot]
        l=len(list1)
        print("len of list==",l)

        if l>=2:

            pre_bot=list1[l-1]

            pre_user= list1[l-2]
            t="[soc][user]"+pre_user+"[bot]"+pre_bot+"[user]"+test_case
            
            data={'text': t}


        else:
            test_case1="[soc][user]"+test_case
            data = {'text': test_case1}


        print("data===",data)
        response = requests.post(url, json=data)
        result = response.json()
        x=result['text']
        changed_x=x

        ###logic for <cybercell_contact> , <cybercell_address>, <contact_number>
        
        if a in x or b in x or c in x:
            changed_x= "Kindly visit ""https://cybercrime.gov.in/webform/Crime_NodalGrivanceList.aspx"" to obtain the email address and cyber cell number for each state. Please call the National Police Helpline at 112, the National Women's Helpline at 181, and the Cybercrime Helpline at 1980 if your state is not on that list."
        
        ###logic for removing Dr. and Adv. numbers and name
            
        elif re.search(regex1,x) or re.search(regex2,x) or re.search(regex3,x):
            changed_x="Kindly visit""http://www.ncw.nic.in/helplines1"" for any legal aid or mental counselling aid."

        
        elif re.search(regex4,x) or re.search(regex5,x):
            changed_x="Please contact +91-11-26944880 or +91-11-26944883 for filing a complaint. For more information and helpline numbers kindly visit""http://www.ncw.nic.in/helplines1""."    

            
        
        elif re.search(regex6,x):
            changed_x="Please visit ""https://cybercrime.gov.in/webform/Crime_NodalGrivanceList.aspx"" for state wise contact numbers and email addresses or Kindly visit""http://www.ncw.nic.in/helplines1"" for any lega help or mental counselling help. You can also reach out the National Police Helpline at 112, the National Women's Helpline at 181, and the Cybercrime Helpline at 1980 for any help. "     

            
        
        elif re.search(number,x):
            changed_x= "Please contact +91-11-26944880 or +91-11-26944883 for filing a complaint. For more information and helpline numbers kindly visit""http://www.ncw.nic.in/helplines1""."    

            
            

            


        ##storing into list
        list1.append(test_case)
        list1.append(result['text'])

        print("generated response from llama model:",result['text'])
        x=changed_x
        print("Response which is given to user and storing into log==",x)
        #f.write(x+"\n")
        print("list1==",list1)
        dispatcher.utter_message(text=x)

        return []
  
            

  
     

# class ValidateEventForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_event_form"

#     @staticmethod
#     def platform_db() -> List[Text]:
#          """Database of supported platfrom"""

#          return ["whatsapp", "facebook", "instagram"]

#     # def validate_platform(
#     #     self,
#     #     slot_value: Any,
#     #     dispatcher: CollectingDispatcher,
#     #     tracker: Tracker,
#     #     domain: DomainDict,
#     # ) -> Dict[Text, Any]:
#     #     """Validate platform values."""

#     #     if slot_value.lower() in self.platform_db():
#     #         # validation succeeded, set the value of the "cuisine" slot to value
#     #         #dispatcher.utter_message(response="utter_platform_info")
#     #         #dispatcher.utter_message(response="utter_ask_platfromBlock")
#     #         return {"platform": slot_value}
#     #     else:
#     #         # validation failed, set this slot to None so that the
#     #         # user will be asked for the slot again
#     #         return {"platform": None}

#     def validate_duration(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate platform values."""


#         #duration= next(tracker.get_latest_entity_values("duration"),None)
#         print(slot_value)
#         print(type(slot_value))
#         list1=["week","months","year","month","weeks"]
        
#         for i in list1:
#             if i in slot_value:
#                 val=i.lower()
#                 break
        
        
#         #print(slot_value)
#         print("duration=",val)

#         if(val=="week" or val=="weeks"):
#             dispatcher.utter_message(text="I'm surprised you've been dealing with this problem for so long.")
#                 ##dispatcher.utter_message(response="utter_ask_event_form_platform")
#             return {"duration": slot_value}

#         if(val=="month" or val=="months"):
#             dispatcher.utter_message(text="I'm surprised to learn that you've been dealing with this problem for so long.")
#                 #dispatcher.utter_message(response="utter_ask_event_form_platform")

#             return {"duration": slot_value}
#         else:
#                 # validation failed, set this slot to None so that the
#                 # user will be asked for the slot again
#             return {"duration": None}               
                


#     def validate_platformBlock(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Platform is blocked or not."""
#         #print(slot_value)
        
#         y=["yes","YES","Yes"]
#         n=["No","no"]
#         #print(type(slot_value))
#         #print(slot_value)
#         if(type(slot_value)==list):
#              for i in slot_value:
#                 if i.lower() in y:
#                     x="yes"
#                     break
#                 if i.lower() in n:
#                     x="no"
#                     break
#         else:        
#             x= slot_value.lower()
#         print("block Information=",x )
#         if x in y:
#             # validation succeeded, set the value of the "cuisine" slot to value
#             dispatcher.utter_message(text="This is very great that you bloked him. If he is still bothering you then you can take legal action on him.")
#             return {"platformBlock": slot_value}
#         if x in n:
#             # validation succeeded, set the value of the "cuisine" slot to value
#             dispatcher.utter_message(text="Please take screenshot of all the evidences and then block and report his account.")
#             ##ActionPlatformInfo.run(ActionPlatformInfo,Any,Any, Dict[Text, Any])
#             #tracker._set_slot("platformBlock",slot_value)
#             text1= (tracker.get_slot("platform"))
#             print(text1)
#             text1.lower()
#             list1= text1.split(" ")
#             print(list1)
#             app=["whatsapp","instagram","insta","facebook","snapchat","Facebook","Whatsapp"]
#             if("whatsapp" in list1):
#                 dispatcher.utter_message(text=" For blocking any contact in Whatsapp : Select the chat in your chats list> press Options > View contact > Block > Block.")    
#             if ("facebook" in list1) :
#                 dispatcher.utter_message(text=" For blocking any contact in Facebook: Go to the profile that you want to report by clicking its name in your Feed or searching for it and then Click more to the right and select Find support or report profile.")     


#             return {"platformBlock": slot_value}        

#             ##return{rasa_sdk.events.FollowupAction("action_platform_info") } 
#         else:
#             # validation failed, set this slot to None so that the
#             # user will be asked for the slot again
#             return {"platformBlock": None}        




#     def validate_event(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate platform values."""

#         crime=["follow","chase","chasing","following","stalking","stalk", "abusing","harassment", "sexual favour","asking for sexual favour","writing vulger comments", "blackmail","blackmailing","harass","abuse","abusing","someone using my photos and identity","someone using my identity","someone using my pics and videos","impersonation","vulgar comment","bad comments"]
#         #print(type(slot_value))
#         print(slot_value)
#         if(type(slot_value)==list):
#              for i in slot_value:
#                 if i.lower() in crime:
#                     x=i.lower()
#                     break
#         else:        
#             x= slot_value.lower()
#         print("crime=",x)    
#         if x in crime:
#             # validation succeeded, set the value of the "cuisine" slot to value
#             #dispatcher.utter_message(response="utter_ask_time_duration")
#             #return {"event": slot_value}
#             return {"event": x}
#         else:
#             # validation failed, set this slot to None so that the
#             # user will be asked for the slot again
#             return {"event": None} 
            



# # class ActionLatestText(Action):
# #     def name(self) -> Text:
# #         return "action_latest_text"

# #     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
# #         text1= next(tracker.latest_message.text)
# #         text1.lower()
# #         if(text1._contains_("hell with your greetings")):
# #             dispatcher.utter_message(text="Please calm down. Aap apni problem btaye so I can help you.")
# #         #dispatcher.utter_message(text="Namste "+ user_name+" Kya aap apni problem ko detail me explain kar sakte hai jisse mai aapki shi se help kar saku?") 

# #         return[]    

# class ActionNameInfo(Action):
#     print("working in action name info")
#     def name(self) -> Text:
#         return "action_name_info"


#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         user_name= next(tracker.get_latest_entity_values("name"),None)
#         dispatcher.utter_message(text="Hello"+ user_name+" would you please explain your issue in detail to assist you in a better way?") 

#         return[]
        
# # class ActionDurationInfo(Action):
# #     def name(self) -> Text:
# #         return "action_duration_info"

# #     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
# #         duration= next(tracker.get_latest_entity_values("duration"),None)
# #         if(duration=="week"):
# #             dispatcher.utter_message(text="Hume bhut dukh hai ki aap itne days se es problem ko face kar rhi hain.")
# #         if(duration=="month"):
# #             dispatcher.utter_message(text="I am shocked to know that aap itne months se es problme ko face kar rhi hai.")

# #         return[]

# class ActionTimingInfo(Action):
#     print("===actioin timing info=====")
#     def name(self) -> Text:
#         return "action_timing_info"

#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         org1= tracker.get_slot("org")
#         org=org1.lower()
#         NCW=["ncw", "national commission for women"]
#         MWCD=["mwcd","ministry","ministry of women and child developmemt"]
#         cybercell=["cybercell","cyber cell"]
#         cybercrime=["cybercrime","cyber crime","national cyber reporting portal"]

#         if(org in NCW):
#             dispatcher.utter_message(text="You can contact NCW from 09:00 AM to 5:30 PM and also you can sent an email.")
#         if(org in MWCD):
#             dispatcher.utter_message(text="You can write an email to MWCD anytime for any information and support.")
#         if(org in cybercrime):
#             dispatcher.utter_message(text="Its 24*7 from 10:00 AM to 06:00 PM for (Delhi, Rajasthan, Uttarakhand, Chattisgardh, Uttar Pradesh, Asam, Tamilnadu aur Andra Pradesh) and Monday to Friday For the rest of the states and Uninion teritories.")
#         if(org in cybercell):
#             dispatcher.utter_message(text="This is 24*7 service. You can contact cyber cell anytime")

#         return[]


# class ActionOrganization(Action):
#     print("======action organization ========")
#     def name(self) -> Text:
#         return "action_organization"

#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         org= tracker.get_slot("org")
#         if(org=="NCW"):
#             dispatcher.utter_message(text="We appreciate your choice. Kindly let me know whether you would like to file an online/offline complaint.")
#         if(org=="MWCD"):
#             dispatcher.utter_message(text="For reporting to MWCD, kindly send an email to MWCD through complaint-mwcd@gov.in along with the incident details and relevant documents, if any that would help in the investigation procedure.")
#         if(org=="cybercell"):
#             dispatcher.utter_message(text="We appreciate your choice Could you please share your present place of residence?")
#         if(org=="cybercrime"):
#             dispatcher.utter_message(text="For Filing a complaint on cyber crime reporting portal: please go to the www.cybercrime.gov.in, click on the 'Report Other Cyber Crime' tab, then 'File a complaint,' and finally accept the declaration. Please read the instructions and declarations thoroughly. Afterwards, create login credentials to submit your complaint.")
        
#         return[]


# class ActionAboutOrganization(Action):
#     print("======action about organization=======")
#     def name(self) -> Text:
#         return "action_about_organization"
        
#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         org= tracker.get_slot("org")
#         if(org=="NCW"):
#             dispatcher.utter_message(text="The National Commission for Women was set up as statutory body in January 1992 under the National Commission for Women Act, 1990 ( Act No. 20 of 1990 of Govt.of India ) to review the Constitutional and Legal safeguards for women, recommend remedial legislative measures, facilitate redressal of grievances and advise the Government on all policy matters affecting women.")
#         if(org=="cybercell"):
#             dispatcher.utter_message(text="The cyber cell is a designated cell to tackle the cybercrime by involving the technical experts during the investigation.The cyber cell will investigate the case using the technical expertise required for the case and help you accordingly.") 
#         if(org=="cybercrime"):
#             dispatcher.utter_message(text="This portal is an initiative of Government of India to facilitate victims/complainants to report cyber crime complaints online. This portal caters to complaints pertaining to cyber crimes only with special focus on cyber crimes against women and children. Complaints reported on this portal are dealt by law enforcement agencies/ police based on the information available in the complaints.")
#         if(org=="MWCD"):
#             dispatcher.utter_message(text="The Department of Women and Child Development is a separate Ministry with effect from 30th January, 2006, earlier since 1985. The Ministry was constituted with the prime intention of addressing gaps in State action for women and children for promoting inter-Ministerial and inter-sectoral convergence to create gender equitable and child-centered legislation, policies and programmes. Women and Child can complaint any of crime to MWCD.")


# ##Women ke liye Constitutional and lagal safety measures ko review karne ke liye, complainnt ko address karne ke liye and women se related kisi nhi policy par Govermnet ko advise karne ke liye National Comission For Women Act, 1990 ke under National Commision for Wome ko January 1990 me set up kiya gay tha.
#         return[]
#     ##National commission for wome ek statutory body hain jisko January 1992  me bnaya gya tha  under the national commison women for women act, 1992 

# class ActionHelpMode(Action):
#     print("action help mode info=====")
#     def name(self) -> Text:
#         return "action_help_mode"
        
#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         help= next(tracker.get_latest_entity_values("mode"),None)

#         org_list=["ncw","national commission for women"]
#         org1= (tracker.get_slot("org"))
#         org= org1.lower()

#         if(help=="online" and org in org_list ):
#             dispatcher.utter_message(text="To report the complaint online, please go to http://ncwapps.nic.in/onlinecomplaintsv2/ to access the NCW portal for filing your complaint. Please read the FAQs carefully before submitting your complaint by clicking on 'Complaint Registration'.")
#         if(help=="offline" and org in org_list):
#             dispatcher.utter_message(text="Your decision is respected. Please send a written application containing all the important details and documents through post or by hand to National Commission for Women,Plot No.21, FC33, Jasola Institutional Area,New Delhi-110025 for reporting offline reporting to NCW.")

#         return[]
# ## Online complaint file karne ke liye please go to http://ncwapps.nic.in/onlinecomplaintsv2/   and register your complaint. Please complaint submit karne se phle FAQ ko dhyan se read kijiye by clicking on "Complaint Registration".
# class ActionContact(Action):
#     print("action contact info=====")
#     def name(self) -> Text:
#         return "action_contact"
#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         org= tracker.get_slot("org")
#         if(org=="NCW"):
#             dispatcher.utter_message(text="For complaint-related queries, you can contact on 011-26944880, 26944883. You can also contact 24x7 nationwide helpline no. of NCW 7827-170-170.")
#         if(org=="cybercell"):
#             dispatcher.utter_message(text="----------Grievance Officer Details--------")
#         if(org=="cybercrime"):
#             dispatcher.utter_message(text="You may call on the Helpline Number - 155260 for 24*7.")
#         if(org=="MWCD"):
#             dispatcher.utter_message(text="You can also call on 7827170170 for Information/Support/Counselling options by 24*7 for nationwide.")        
         


#         return[]    
# # class ActionPlatformInfo(Action):
# #     def name(self) -> Text:
# #         return "action_platform_info"
# #     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
# #         text1= tracker.get_slot("platform")
# #         affirm1=tracker.get_slot("platformBlock").lower()
        
# #         text1.lower()
# #         list1= text1.split(" ")
# #         print(list1)
# #         app=["whatsapp","instagram","insta","facebook","snapchat"]
# #         if(affirm1=="no"):

# #             if("whatsapp" in list1):
# #                 dispatcher.utter_message(text=" Whatsapp me block karne ke liye: Select the chat in your chats list, then press Options > View contact > Block > Block.")    
# #             if ("facebook" in list1) :
# #                 dispatcher.ytter_message(text=" Facebook me blosk karne ke liye: Go to the profile that you want to report by clicking its name in your Feed or searching for it and then Click more to the right and select Find support or report profile.")       
            
# #         if(affirm1=="yes"):

# #             dispatcher.utter_message(text="This is very great that you bloked him. Yadi wah aapko abhi bhi disturbed kar raha hai to Aap es case me legal action le sakati hain.")



# #         return[]    


# # class ActionPlatformInfo(Action):
# #     def name(self) -> Text:
# #         return "action_platform_info"
# #     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
# #         text1= (tracker.get_slot("platform"))
# #         print(text1)
# #         text1.lower()
# #         list1= text1.split(" ")
# #         print(list1)
# #         app=["whatsapp","instagram","insta","facebook","snapchat"]
# #         if("whatsapp" in list1):
# #             dispatcher.utter_message(text=" Whatsapp me block karne ke liye: Select the chat in your chats list, then press Options > View contact > Block > Block.")    
# #         if ("facebook" in list1) :
# #             dispatcher.utter_message(text=" Facebook me blosk karne ke liye: Go to the profile that you want to report by clicking its name in your Feed or searching for it and then Click more to the right and select Find support or report profile.")       
            
        
# #         return[]    
           

    

# class ActionLocation(Action):
#     print("action location info=====")
#     def name(self) -> Text:
#         return "action_location"

#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         #org= next(tracker.get_latest_entity_values("org"),None)
#         org=(tracker.get_slot("org"))
        
#         dict1={ "ANDAMAN & NICOBAR" : "digpint-anp@gov.in",
#                 "ANDHRA PRADESH" : "cybercrimes-cid@ap.gov.in",
#                 "ARUNACHAL PRADESH": "spsit@arupol.nic.in",
#                 "ASSAM":"digp-cid@assampolice.gov.in",
#                 "BIHAR":"cybercell-bih@nic.in",
#                 "CHANDIGARH":"dig-chd@nic.in",
#                 "CHHATTISGARH":	"aigtech-phq.cg@gov.in",
#                 "DADRA & NAGAR HAVELI":"phq-dd@nic.in",
#                 "DAMAN & DIU":	"phq-dd@nic.in",
#                 "DELHI": "ncrp.delhi@delhipolice.gov.in",
#                 "GOA":	"spcyber@goapolice.gov.in",
#                 "GUJARAT":	"cc-cid@gujarat.gov.in",
#                 "HARYANA" :	"sp-cybercrimephq.pol@hry.gov.in",
#                 "HIMACHAL PRADESH":	"polcyberps-shi-hp@nic.in",
#                 "JAMMU & KASHMIR":"igcrime-jk@nic.in",
#                 "JHARKHAND":"spcyberps@jhpolice.gov.in",
#                 "KARNATAKA":"spctrcid@ksp.gov.in",
#                 "KERALA":"ncrpkerala.pol@kerala.gov.in",
#                 "LADAKH":"itsec-phq@police.ladakh.gov.in",
#                 "LAKSHADWEEP":"cctns-lk@nic.in",
#                 "MADHYA PRADESH":"niranjan.vayangankar889@mppolice.gov.in",
#                 "MAHARASHTRA":	"sp.cbr-mah@gov.in",
#                 "MANIPUR":	"sp-cybercrime.mn@manipur.gov.in",
#                 "MEGHALAYA":"sspcid-meg@gov.in",
#                 "MIZORAM":	"digcid-mz@mizoram.gov.in",
#                 "NAGALAND":	"cybercrimeps-ngl@gov.in",
#                 "ODISHA":"dirscrb.odpol@nic.in",
#                 "PUDUCHERRY":"cybercell-police.py@gov.in",
#                 "PUNJAB":"aigcc@punjabpolice.gov.in",
#                 "RAJASTHAN":"ccps-raj@nic.in",
#                 "SIKKIM":"spcid@sikkimpolice.nic.in",
#                 "TAMIL NADU":"sp1-ccdtnpolice@gov.in",
#                 "TELANGANA":"cybercell-t4c14@tspolice.gov.in",
#                 "TRIPURA":"spcybercrime@tripurapolice.nic.in",
#                 "UTTARAKHAND":"ccps.deh@uttarakhandpolice.uk.gov.in",
#                 "UTTAR PRADESH":"sp-cyber.lu@up.gov.in",
#                 "WEST BENGAL" :	"ccpwb@cidwestbengal.gov.in"}

        
#         if(org=="cybercell"):
#             #org= next(tracker.get_latest_entity_values("location"),None)
#             loca1= tracker.get_slot("location")
#             loca= loca1.upper()
#             email=dict1.get(loca)
#             dispatcher.utter_message(text="Thank you for the location detail. Kindly send a email to  <"+ email+">")

#         # if(org=="cybercrime"):
#         #     dispatcher.utter_message(text="please go to the www.cybercrime.gov.in, click on the Report Other Cyber Crime tab, then File a complaint, and finally accept the declaration. Please read the instructions and declarations thoroughly. Afterwards, create login credentials to submit your complaint")
        
#         return[]



# class ActionEventForm(Action):
#     print("action event form=====")

#     def name(self) -> Text:
#         return "action_event_form"


#     async def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         event_list = (tracker.get_slot("event"))
#         ##name1= tracker.get_slot("name")
#         #print(event_list)
#         event1=event_list
#         #crime=["follow","chase","chasing","following","stalking","stalk", "abusing","harassment", "sexual favor","asking for sexual favor","writing vulger comments", "blackmail","blackmailing","harass","abuse","abusing",
#         # "someone using my photos and identity","someone using my identity","someone using my pics and videos","impersonation","vulgar comment","bad comments"]

#         stalking=["follow","chase","chasing","following","stalking","stalk"]
#         harassment=["abusing","harassment", "sexual favour","asking for sexual favour","writing vulgar comment", "blackmail","blackmailing","torture","harass","defame","abuse","abusing","vulgar comment","bad comments"]
#         masquerading=["someone using my photos and identity","someone using my identity","someone  using my pics and videos","impersonation"]
        

#         '''for i in event_list:
            
#             if i.lower() in stalking:
#                 event1=i.lower()
#                 break
                
#             elif i.lower() in harassment:
#                 event1=i.lower()
#                 break

#             elif i.lower() in masquerading: 
#                 event1=i.lower()
#                 break '''      

#         print("crime_detected=",event1)
#         if(event1=="None"):
#             dispatcher.utter_message(text="Can you please explain your problem in more detail so I can help you?")
#         if event1 in stalking:
#             dispatcher.utter_message(text= " I must tell you that you are facing the case of stalking. Stalking is an offense under Section 354D of IPC through the Criminal Law (Amendment) Act 2013 which is liable for legal action.")
#         if event1 in harassment:
#             dispatcher.utter_message(text= " This is an instance of online harassment which is an offense under 354A of IPC through the Criminal Law. (Amendment) Act, 2013.Do you want me to tell you further about this law?")
#         if event1 in masquerading:
#             dispatcher.utter_message(text= " What we have discussed, it's sound the case of masquerading which is a punishable offense under IPC 500 and 509 section under Section 66D of the IT Amendment Act, 2008 for outraging the modesty of women.") 
        
            

#         return []     