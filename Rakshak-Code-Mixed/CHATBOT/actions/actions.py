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
from rasa_sdk.events import FollowupAction
# #
# #
# class ActionNameInfo(Action):

#     def name(self) -> Text:
#         return "action_name_info"

#     def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         name1 = tracker.get_slot("name")
#         print(name1)
#         print(tracker)
#         msg="hello {} how can i help you?".format(name1)
#         dispatcher.utter_message(text=msg)

#         return []

class ValidateEventForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_event_form"

    @staticmethod
    def platform_db() -> List[Text]:
         """Database of supported platfrom"""

         return ["whatsapp", "facebook", "instagram"]

    # def validate_platform(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate platform values."""

    #     if slot_value.lower() in self.platform_db():
    #         # validation succeeded, set the value of the "cuisine" slot to value
    #         #dispatcher.utter_message(response="utter_platform_info")
    #         #dispatcher.utter_message(response="utter_ask_platfromBlock")
    #         return {"platform": slot_value}
    #     else:
    #         # validation failed, set this slot to None so that the
    #         # user will be asked for the slot again
    #         return {"platform": None}

    def validate_duration(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate platform values."""


        #duration= next(tracker.get_latest_entity_values("duration"),None)
        print(slot_value)
        print(type(slot_value))
        list1=["week","months","year","month","weeks"]
        
        for i in list1:
            if i in slot_value:
                val=i.lower()
                break
        
        
        #print(slot_value)
        print("duration=",val)

        if(val=="week" or val=="weeks"):
            dispatcher.utter_message(text="Hume bhut dukh hai ki aap itne dino se es problem ko face kar rhi hain.")
                ##dispatcher.utter_message(response="utter_ask_event_form_platform")
            return {"duration": slot_value}

        if(val=="month" or val=="months"):
            dispatcher.utter_message(text="I am shocked to know that aap itne months se es problem ko face kar rhi hain.")
                #dispatcher.utter_message(response="utter_ask_event_form_platform")

            return {"duration": slot_value}
        else:
                # validation failed, set this slot to None so that the
                # user will be asked for the slot again
            return {"duration": None}               
                


    def validate_platformBlock(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Platform is blocked or not."""
        #print(slot_value)
        
        y=["yes","YES","Yes","hmm","haa","ha"]
        n=["nhi","nahi","Nahi","Na","No","no","na","NAHI","NHI"]
        #print(type(slot_value))
        #print(slot_value)
        if(type(slot_value)==list):
             for i in slot_value:
                if i.lower() in y:
                    x="yes"
                    break
                if i.lower() in n:
                    x="no"
                    break
        else:        
            x= slot_value.lower()
        print("block Information=",x )
        if x in y:
            # validation succeeded, set the value of the "cuisine" slot to value
            dispatcher.utter_message(text="This is very great that you bloked him. Yadi wah aapko abhi bhi disturb kar raha hai to Aap es case me legal action le sakati hain.")
            return {"platformBlock": slot_value}
        if x in n:
            # validation succeeded, set the value of the "cuisine" slot to value
            dispatcher.utter_message(text="Please saare evidence/chats ka screenshot lekr us account ko report and blok kijiye.")
            ##ActionPlatformInfo.run(ActionPlatformInfo,Any,Any, Dict[Text, Any])
            #tracker._set_slot("platformBlock",slot_value)
            text1= (tracker.get_slot("platform"))
            print(text1)
            text1.lower()
            list1= text1.split(" ")
            print(list1)
            app=["whatsapp","instagram","insta","facebook","snapchat","Facebook","Whatsapp"]
            if("whatsapp" in list1):
                dispatcher.utter_message(text=" Whatsapp me block karne ke liye: Select the chat in your chats list> press Options > View contact > Block > Block.")    
            if ("facebook" in list1) :
                dispatcher.utter_message(text=" Facebook me block karne ke liye: Go to the profile that you want to report by clicking its name in your Feed or searching for it and then Click more to the right and select Find support or report profile.")     


            return {"platformBlock": slot_value}        

            ##return{rasa_sdk.events.FollowupAction("action_platform_info") } 
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"platformBlock": None}        




    def validate_event(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate platform values."""

        crime=["follow","chase","chasing","picha","peecha","following","stalking","stalk", "abusing","harassment", "sexual favor maang raha hai","sexual favor maang","pics aur videos pr vulger comment karta hain", "blackmail","torture","harass kar raha hai","abuse","abusing","someone using my photos and identity","Koi mere photos and name ka use kar raha hai","koi mere  name, photos aur Insta reel ka use kar ke mai hone ka natak kr rha hai","impersonation","koi mera name and pics ka use kar raha hai", "koi mera photos and videos use kara rah hai","vulgar comment","bad comments"]
        #print(type(slot_value))
        print(slot_value)
        if(type(slot_value)==list):
             for i in slot_value:
                if i.lower() in crime:
                    x=i.lower()
                    break
        else:        
            x= slot_value.lower()
        print("crime=",x)    
        if x in crime:
            # validation succeeded, set the value of the "cuisine" slot to value
            #dispatcher.utter_message(response="utter_ask_time_duration")
            #return {"event": slot_value}
            return {"event": x}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"event": None} 
            



# class ActionLatestText(Action):
#     def name(self) -> Text:
#         return "action_latest_text"

#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         text1= next(tracker.latest_message.text)
#         text1.lower()
#         if(text1._contains_("hell with your greetings")):
#             dispatcher.utter_message(text="Please calm down. Aap apni problem btaye so I can help you.")
#         #dispatcher.utter_message(text="Namste "+ user_name+" Kya aap apni problem ko detail me explain kar sakte hai jisse mai aapki shi se help kar saku?") 

#         return[]    

class ActionNameInfo(Action):
    print("working in action name info")
    def name(self) -> Text:
        return "action_name_info"


    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        user_name= next(tracker.get_latest_entity_values("name"),None)
        dispatcher.utter_message(text="Namste "+ user_name+" Kya aap apni problem ko detail me explain kar sakti hain jisse mai aapki shi se help kar saku?") 

        return[]
        
# class ActionDurationInfo(Action):
#     def name(self) -> Text:
#         return "action_duration_info"

#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         duration= next(tracker.get_latest_entity_values("duration"),None)
#         if(duration=="week"):
#             dispatcher.utter_message(text="Hume bhut dukh hai ki aap itne days se es problem ko face kar rhi hain.")
#         if(duration=="month"):
#             dispatcher.utter_message(text="I am shocked to know that aap itne months se es problme ko face kar rhi hai.")

#         return[]

class ActionTimingInfo(Action):
    print("===actioin timing info=====")
    def name(self) -> Text:
        return "action_timing_info"

    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        org1= tracker.get_slot("org")
        org=org1.lower()
        NCW=["ncw", "national commission for women"]
        MWCD=["mwcd","ministry","ministry of women and child developmemt"]
        cybercell=["cybercell","cyber cell"]
        cybercrime=["cybercrime","cyber crime","national cyber reporting portal"]

        if(org in NCW):
            dispatcher.utter_message(text="Yadi aap koi bhi problem face kar rahi hain to aap NCW se morning 9 baje se evening 05:30 ke beech contact kar sakte hain. Yah Monday to Friday (Working days) me aap kisi bhi time email bhej sakti hain.")
        if(org in MWCD):
            dispatcher.utter_message(text="Ydi aap koi problem face kar rahe hai to aap Ministry of Women and Child development ko kbhi bhi mail kar sakti hai.")
        if(org in cybercrime):
            dispatcher.utter_message(text="Aap (Delhi, Rajasthan, Uttarakhand, Chattisgardh, Uttar Pradesh, Asam, Tamilnadu aur Andra Pradesh) ke liye 24*7 aur morning 10.00 baje se evening 6.00 ke beech kabhi bhi hamse contact kar sakte hain. Working Day - Rest of the states men aur Uninion teritories men yah kewal monday to friday hai.")
        if(org in cybercell):
            dispatcher.utter_message(text="Yh 24*7 service hain. Aap kbhi bhi cyber cell ko contact kar sakti hain.")

        return[]


class ActionOrganization(Action):
    print("======action organization ========")
    def name(self) -> Text:
        return "action_organization"

    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        org= tracker.get_slot("org")
        if(org=="NCW"):
            dispatcher.utter_message(text="Kya aap mujhe btayenge ki aap kis mode(online/offline) me complaint file karna chahti hain?")
        if(org=="MWCD"):
            dispatcher.utter_message(text="We appreciate your choice. Please apni incident ka detail me description likh kr ke mwcd@gov.in pr mail kre.")
        if(org=="cybercell"):
            dispatcher.utter_message(text="We appreciate your choice ki aap cyber cell ke through complaint file karna chahti hai iske liye Kya aap please mujhe apne state location ko share kar sakti hai?")
        if(org=="cybercrime"):
            dispatcher.utter_message(text="National Cyber Crime Reporting Portal me complaint file karne ke liye : please go to the www.cybercrime.gov.in, click on the Report Other Cyber Crime tab, then File a complaint, and finally accept the declaration. Please read the instructions and declarations thoroughly. Afterwards, create login credentials to submit your complaint")
        
        return[]


class ActionAboutOrganization(Action):
    print("======action about organization=======")
    def name(self) -> Text:
        return "action_about_organization"
        
    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        org= tracker.get_slot("org")
        if(org=="NCW"):
            dispatcher.utter_message(text="Women's related Constitutional and lagal safety measures ko review karne ke liye, Complaint ko address karne ke liye and women se related kisi bhi policy par Government ko advise karne ke liye, January, 1992 me National Comission For Women Act, 1990 ke under National Commision for Women ko set up kiya gya hain.")
        if(org=="cybercell"):
            dispatcher.utter_message(text="Cyber cell ek designated cell hai cybercrime ko tackle krne ke liye by involving the technical experts during  the investigation. They will investigate the case using the technical expertise required for the case and help you accordingly.") 
        if(org=="cybercrime"):
            dispatcher.utter_message(text="Yah portal Government of India ka ek initiative hai to faciliate victims.Yah portal women and childs ke against cyber crime pr special focus dene ke saath hi cyber crimes related complaints ko cater krta hai. Es portal pr report kiye gye complaints law enforcement agencies dwara deal kiya jata hai based on the information available in the complaints.")
        if(org=="MWCD"):
            dispatcher.utter_message(text="The department of women and child development ek separate ministry 30 january, 2006 se hai jo ki 1985 se hai.For promoting inter-Ministerial  and inter-sectoral convergence to create gender equitable and child-centered legislation, policies and programmes ke kaaran Ministry ko bnya gya tha. Women and child kisi bhi crime se related MWCD ko complaint kr skti hai.")


##Women ke liye Constitutional and lagal safety measures ko review karne ke liye, complainnt ko address karne ke liye and women se related kisi nhi policy par Govermnet ko advise karne ke liye National Comission For Women Act, 1990 ke under National Commision for Wome ko January 1990 me set up kiya gay tha.
        return[]
    ##National commission for wome ek statutory body hain jisko January 1992  me bnaya gya tha  under the national commison women for women act, 1992 

class ActionHelpMode(Action):
    print("action help mode info=====")
    def name(self) -> Text:
        return "action_help_mode"
        
    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        help= next(tracker.get_latest_entity_values("mode"),None)

        org_list=["ncw","national commission for women"]
        org1= (tracker.get_slot("org"))
        org= org1.lower()

        if(help=="online" and org in org_list ):
            dispatcher.utter_message(text="Online complaint file karne ke liye please go to http://ncwapps.nic.in/onlinecomplaintsv2/   and register your complaint. Please complaint submit karne se phle FAQ ko dhyan se read kijiye by clicking on \"Complaint Registration\"")
        if(help=="offline" and org in org_list):
            dispatcher.utter_message(text="Your decision is respected. Please send a written application containing all the important details and documents through post or by hand to National Commission for Women,Plot No.21, FC33, Jasola Institutional Area,New Delhi-110025 for reporting offline reporting to NCW.")

        return[]
## Online complaint file karne ke liye please go to http://ncwapps.nic.in/onlinecomplaintsv2/   and register your complaint. Please complaint submit karne se phle FAQ ko dhyan se read kijiye by clicking on "Complaint Registration".
class ActionContact(Action):
    print("action contact info=====")
    def name(self) -> Text:
        return "action_contact"
    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        org= tracker.get_slot("org")
        if(org=="NCW"):
            dispatcher.utter_message(text=" NCW me complaint related queries krne ke liye aap : 011-26944880, 26944883 par call kar sakti hain and also kisi aur information or help ke liye aap Nationwide helpline no. 7827-170-170 pr bhi contact kar sakti hain.")
        if(org=="cybercell"):
            dispatcher.utter_message(text="----------Grievance Officer Details--------")
        if(org=="cybercrime"):
            dispatcher.utter_message(text="Cyber crime ko contact karne ke liye aap Helpline Number - 155260  par call kar skati hain.")
        if(org=="MWCD"):
            dispatcher.utter_message(text="You can call on 7827170170 for Information options by 24*7 for nationwide. Aap 7827170170 par call kar sakti kisi bhi information ke liye")        
         


        return[]    
# class ActionPlatformInfo(Action):
#     def name(self) -> Text:
#         return "action_platform_info"
#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         text1= tracker.get_slot("platform")
#         affirm1=tracker.get_slot("platformBlock").lower()
        
#         text1.lower()
#         list1= text1.split(" ")
#         print(list1)
#         app=["whatsapp","instagram","insta","facebook","snapchat"]
#         if(affirm1=="no"):

#             if("whatsapp" in list1):
#                 dispatcher.utter_message(text=" Whatsapp me block karne ke liye: Select the chat in your chats list, then press Options > View contact > Block > Block.")    
#             if ("facebook" in list1) :
#                 dispatcher.ytter_message(text=" Facebook me blosk karne ke liye: Go to the profile that you want to report by clicking its name in your Feed or searching for it and then Click more to the right and select Find support or report profile.")       
            
#         if(affirm1=="yes"):

#             dispatcher.utter_message(text="This is very great that you bloked him. Yadi wah aapko abhi bhi disturbed kar raha hai to Aap es case me legal action le sakati hain.")



#         return[]    


# class ActionPlatformInfo(Action):
#     def name(self) -> Text:
#         return "action_platform_info"
#     def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
#         text1= (tracker.get_slot("platform"))
#         print(text1)
#         text1.lower()
#         list1= text1.split(" ")
#         print(list1)
#         app=["whatsapp","instagram","insta","facebook","snapchat"]
#         if("whatsapp" in list1):
#             dispatcher.utter_message(text=" Whatsapp me block karne ke liye: Select the chat in your chats list, then press Options > View contact > Block > Block.")    
#         if ("facebook" in list1) :
#             dispatcher.utter_message(text=" Facebook me blosk karne ke liye: Go to the profile that you want to report by clicking its name in your Feed or searching for it and then Click more to the right and select Find support or report profile.")       
            
        
#         return[]    
           

    

class ActionLocation(Action):
    print("action location info=====")
    def name(self) -> Text:
        return "action_location"

    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        #org= next(tracker.get_latest_entity_values("org"),None)
        org=(tracker.get_slot("org"))
        
        dict1={ "ANDAMAN & NICOBAR" : "digpint-anp@gov.in",
                "ANDHRA PRADESH" : "cybercrimes-cid@ap.gov.in",
                "ARUNACHAL PRADESH": "spsit@arupol.nic.in",
                "ASSAM":"digp-cid@assampolice.gov.in",
                "BIHAR":"cybercell-bih@nic.in",
                "CHANDIGARH":"dig-chd@nic.in",
                "CHHATTISGARH":	"aigtech-phq.cg@gov.in",
                "DADRA & NAGAR HAVELI":"phq-dd@nic.in",
                "DAMAN & DIU":	"phq-dd@nic.in",
                "DELHI": "ncrp.delhi@delhipolice.gov.in",
                "GOA":	"spcyber@goapolice.gov.in",
                "GUJARAT":	"cc-cid@gujarat.gov.in",
                "HARYANA" :	"sp-cybercrimephq.pol@hry.gov.in",
                "HIMACHAL PRADESH":	"polcyberps-shi-hp@nic.in",
                "JAMMU & KASHMIR":"igcrime-jk@nic.in",
                "JHARKHAND":"spcyberps@jhpolice.gov.in",
                "KARNATAKA":"spctrcid@ksp.gov.in",
                "KERALA":"ncrpkerala.pol@kerala.gov.in",
                "LADAKH":"itsec-phq@police.ladakh.gov.in",
                "LAKSHADWEEP":"cctns-lk@nic.in",
                "MADHYA PRADESH":"niranjan.vayangankar889@mppolice.gov.in",
                "MAHARASHTRA":	"sp.cbr-mah@gov.in",
                "MANIPUR":	"sp-cybercrime.mn@manipur.gov.in",
                "MEGHALAYA":"sspcid-meg@gov.in",
                "MIZORAM":	"digcid-mz@mizoram.gov.in",
                "NAGALAND":	"cybercrimeps-ngl@gov.in",
                "ODISHA":"dirscrb.odpol@nic.in",
                "PUDUCHERRY":"cybercell-police.py@gov.in",
                "PUNJAB":"aigcc@punjabpolice.gov.in",
                "RAJASTHAN":"ccps-raj@nic.in",
                "SIKKIM":"spcid@sikkimpolice.nic.in",
                "TAMIL NADU":"sp1-ccdtnpolice@gov.in",
                "TELANGANA":"cybercell-t4c14@tspolice.gov.in",
                "TRIPURA":"spcybercrime@tripurapolice.nic.in",
                "UTTARAKHAND":"ccps.deh@uttarakhandpolice.uk.gov.in",
                "UTTAR PRADESH":"sp-cyber.lu@up.gov.in",
                "WEST BENGAL" :	"ccpwb@cidwestbengal.gov.in"}

        
        if(org=="cybercell"):
            #org= next(tracker.get_latest_entity_values("location"),None)
            loca1= tracker.get_slot("location")
            loca= loca1.upper()
            email=dict1.get(loca)
            dispatcher.utter_message(text="Cyber cell me complaint report krne ke liye aap apne issue ko detail me likh kr ke  <"+ email+"> pr mail kijiye.")

        # if(org=="cybercrime"):
        #     dispatcher.utter_message(text="please go to the www.cybercrime.gov.in, click on the Report Other Cyber Crime tab, then File a complaint, and finally accept the declaration. Please read the instructions and declarations thoroughly. Afterwards, create login credentials to submit your complaint")
        
        return[]



class ActionEventForm(Action):
    print("action event form=====")

    def name(self) -> Text:
        return "action_event_form"


    async def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        event_list = (tracker.get_slot("event"))
        ##name1= tracker.get_slot("name")
        #print(event_list)
        event1=event_list
       
        stalking=["follow","chase","chasing","picha","peecha","following","stalking","stalk"]
        harassment=["abusing","harassment", "sexual favor maang raha hai","sexual favor maang","pics aur videos pr vulgar comment karta hain", "blackmail","torture","harass kar raha hai","abuse","abusing","vulgar comment","bad comments"]
        masquerading=["someone using my photos and identity","Koi mere photos and name ka use kar raha hai","koi mere  name, photos aur Insta reel ka use kar ke mai hone ka natak kr rha hai","impersonation","koi mera name and pics ka use kar raha hai", "koi mera photos and videos use kara rah hai"]
        

        '''for i in event_list:
            
            if i.lower() in stalking:
                event1=i.lower()
                break
                
            elif i.lower() in harassment:
                event1=i.lower()
                break

            elif i.lower() in masquerading: 
                event1=i.lower()
                break '''      

        print("crime_detected=",event1)
        if(event1=="None"):
            dispatcher.utter_message(text="Please kya aap apni problem ko thoda aur detail me explain kr skti hain jisse mai aapki help kar saku.")
        if event1 in stalking:
            dispatcher.utter_message(text= " Patiently reply karne ke kiye thanks. Main samjhta hoon ki aap stalking ke issue ka samna kar rahi hain joki IPC section 354D,Criminal Law (Amendment) Act 2013 ke under ek offence hai. Es case me aap leagal action bhi le sakti hain.")
        if event1 in harassment:
            dispatcher.utter_message(text= " Sabhi queries ka patiently answer karne ke liye thanks. As I understand , yah ek online harassment ka case hai jo IPC section 354A ,Criminal Law (Amendment) Act 2013 ke under ek offence hain.")
        if event1 in masquerading:
            dispatcher.utter_message(text= " Sabhi queries ka patiently answer karne ke liye thanks. As I understand that ki aap masquerading ke issue ko face kar rahe hain jo ki Criminal Law (Amendment) Act, aur Information Technology(Amendment) Act 2008 ki IPC section ke under Section 500 and 509 ke  66D ke antargat women defamation ek criminal offense hain.") 
        
            

        return []     