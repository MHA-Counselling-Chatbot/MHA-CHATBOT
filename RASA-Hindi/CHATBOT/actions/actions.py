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
            dispatcher.utter_message(text="मुझे आश्चर्य है कि आप इतने लंबे समय से इस समस्या से निपट रहे हैं।")
                ##dispatcher.utter_message(response="utter_ask_event_form_platform")
            return {"duration": slot_value}

        if(val=="month" or val=="months"):
            dispatcher.utter_message(text="मुझे यह जानकर आश्चर्य हुआ कि आप इतने लंबे समय से इस समस्या से निपट रहे हैं।")
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
        
        y=["yes","YES","Yes"]
        n=["No","no"]
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
            dispatcher.utter_message(text="यह बहुत अच्छी बात है कि आपने उसे ब्लॉक कर दिया। अगर वह अब भी आपको परेशान कर रहा है तो आप उस पर कानूनी कार्रवाई कर सकते हैं।")
            return {"platformBlock": slot_value}
        if x in n:
            # validation succeeded, set the value of the "cuisine" slot to value
            dispatcher.utter_message(text="कृपया सभी सबूतों का स्क्रीनशॉट लें और फिर ब्लॉक करें और उसके खाते की रिपोर्ट करें।")
            ##ActionPlatformInfo.run(ActionPlatformInfo,Any,Any, Dict[Text, Any])
            #tracker._set_slot("platformBlock",slot_value)
            text1= (tracker.get_slot("platform"))
            print(text1)
            text1.lower()
            list1= text1.split(" ")
            print(list1)
            app=["whatsapp","instagram","insta","facebook","snapchat","Facebook","Whatsapp"]
            if("whatsapp" in list1):
                dispatcher.utter_message(text="व्हाट्सएप में किसी भी संपर्क को ब्लॉक करने के लिए: अपनी चैट सूची में चैट का चयन करें> विकल्प दबाएं> संपर्क देखें> ब्लॉक करें> ब्लॉक करें।")    
            if ("facebook" in list1) :
                dispatcher.utter_message(text=" फ़ेसबुक में किसी भी संपर्क को ब्लॉक करने के लिए: उस प्रोफ़ाइल पर जाएँ जिसे आप अपने फ़ीड में उसके नाम पर क्लिक करके या उसकी खोज करके रिपोर्ट करना चाहते हैं और फिर दाईं ओर अधिक क्लिक करें और सहायता ढूँढें या प्रोफ़ाइल की रिपोर्ट करें चुनें।")     


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

        crime=["follow","chase","chasing","following","stalking","stalk", "abusing","harassment", "sexual favour","asking for sexual favour","writing vulger comments", "blackmail","blackmailing","harass","abuse","abusing","someone using my photos and identity","someone using my identity","someone using my pics and videos","impersonation","vulgar comment","bad comments"]
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
        dispatcher.utter_message(text="नमस्ते"+ user_name+" क्या आप बेहतर तरीके से आपकी सहायता करने के लिए कृपया अपनी समस्या के बारे में विस्तार से बताएंगे?") 

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
            dispatcher.utter_message(text="आप राष्ट्रीय महिला आयोग से सुबह 09:00 बजे से शाम 5:30 बजे तक संपर्क कर सकते हैं और ईमेल भी भेज सकते हैं।")
        if(org in MWCD):
            dispatcher.utter_message(text="आप किसी भी जानकारी और सहायता के लिए कभी भी MWCD को ईमेल लिख सकते हैं।")
        if(org in cybercrime):
            dispatcher.utter_message(text="यह 24 * 7 सुबह 10:00 बजे से शाम 06:00 बजे तक (दिल्ली, राजस्थान, उत्तराखंड, छत्तीसगढ़, उत्तर प्रदेश, असम, तमिलनाडु और आंध्र प्रदेश) और सोमवार से शुक्रवार बाकी राज्यों और केंद्र शासित प्रदेशों के लिए है।")
        if(org in cybercell):
            dispatcher.utter_message(text="यह 24*7 सर्विस है। आप कभी भी साइबर सेल से संपर्क कर सकते हैं")

        return[]


class ActionOrganization(Action):
    print("======action organization ========")
    def name(self) -> Text:
        return "action_organization"

    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        org= tracker.get_slot("org")
        if(org=="NCW"):
            dispatcher.utter_message(text="हम आपकी पसंद की सराहना करते हैं। कृपया मुझे बताएं कि क्या आप ऑनलाइन/ऑफलाइन शिकायत दर्ज करना चाहते हैं।")
        if(org=="MWCD"):
            dispatcher.utter_message(text="MWCD को रिपोर्ट करने के लिए, कृपया MWCD को शिकायत-mwcd@gov.in के माध्यम से घटना के विवरण और संबंधित दस्तावेजों, यदि कोई हो, के साथ एक ईमेल भेजें, जो जांच प्रक्रिया में मदद करेगा।")
        if(org=="cybercell"):
            dispatcher.utter_message(text="हम आपकी पसंद की सराहना करते हैं क्या आप कृपया अपना वर्तमान निवास स्थान साझा कर सकते हैं?")
        if(org=="cybercrime"):
            dispatcher.utter_message(text="साइबर अपराध रिपोर्टिंग पोर्टल पर शिकायत दर्ज करने के लिए: कृपया www.cybercrime.gov.in पर जाएं, 'अन्य साइबर अपराध की रिपोर्ट करें' टैब पर क्लिक करें, फिर 'शिकायत दर्ज करें' पर क्लिक करें और अंत में घोषणा को स्वीकार करें। कृपया निर्देशों और घोषणाओं को अच्छी तरह से पढ़ें। बाद में, अपनी शिकायत सबमिट करने के लिए लॉगिन क्रेडेंशियल बनाएं।")
        
        return[]


class ActionAboutOrganization(Action):
    print("======action about organization=======")
    def name(self) -> Text:
        return "action_about_organization"
        
    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        org= tracker.get_slot("org")
        if(org=="NCW"):
            dispatcher.utter_message(text="महिलाओं के लिए संवैधानिक और कानूनी सुरक्षा उपायों की समीक्षा करने, उपचारात्मक विधायी उपायों की सिफारिश करने के लिए जनवरी 1992 में राष्ट्रीय महिला आयोग अधिनियम, 1990 (भारत सरकार के 1990 के अधिनियम संख्या 20) के तहत राष्ट्रीय महिला आयोग की स्थापना वैधानिक निकाय के रूप में की गई थी। , शिकायतों के निवारण की सुविधा प्रदान करना और महिलाओं को प्रभावित करने वाले सभी नीतिगत मामलों पर सरकार को सलाह देना।")
        if(org=="cybercell"):
            dispatcher.utter_message(text="साइबर सेल जांच के दौरान तकनीकी विशेषज्ञों को शामिल करके साइबर अपराध से निपटने के लिए एक नामित सेल है। साइबर सेल मामले के लिए आवश्यक तकनीकी विशेषज्ञता का उपयोग करके मामले की जांच करेगी और तदनुसार आपकी मदद करेगी।.") 
        if(org=="cybercrime"):
            dispatcher.utter_message(text="यह पोर्टल पीड़ितों/शिकायतकर्ताओं को साइबर अपराध की शिकायतों की ऑनलाइन रिपोर्ट करने की सुविधा प्रदान करने के लिए भारत सरकार की एक पहल है। यह पोर्टल महिलाओं और बच्चों के खिलाफ साइबर अपराधों पर विशेष ध्यान देने के साथ ही साइबर अपराधों से संबंधित शिकायतों को पूरा करता है। इस पोर्टल पर रिपोर्ट की गई शिकायतों को शिकायतों में उपलब्ध जानकारी के आधार पर कानून प्रवर्तन एजेंसियों/पुलिस द्वारा निपटाया जाता है।")
        if(org=="MWCD"):
            dispatcher.utter_message(text="महिला एवं बाल विकास विभाग 30 जनवरी, 2006 से प्रभावी एक अलग मंत्रालय है, इससे पहले 1985 से। मंत्रालय का गठन अंतर-मंत्रालयी और अंतर-क्षेत्रीय को बढ़ावा देने के लिए महिलाओं और बच्चों के लिए राज्य की कार्रवाई में अंतराल को संबोधित करने के मुख्य उद्देश्य से किया गया था। लैंगिक समानता और बाल-केंद्रित कानून, नीतियां और कार्यक्रम बनाने के लिए अभिसरण। महिला एवं बालिका किसी भी अपराध की शिकायत महिला एवं बाल विकास मंत्रालय से कर सकती हैं।")


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
            dispatcher.utter_message(text="ऑनलाइन शिकायत दर्ज करने के लिए, कृपया http://ncwapps.nic.in/onlinecomplaintsv2/ पर जाकर अपनी शिकायत दर्ज कराने के लिए NCW पोर्टल का उपयोग करें। कृपया 'शिकायत पंजीकरण' पर क्लिक करके अपनी शिकायत दर्ज करने से पहले अक्सर पूछे जाने वाले प्रश्नों को ध्यान से पढ़ें।")
        if(help=="offline" and org in org_list):
            dispatcher.utter_message(text="आपके निर्णय का सम्मान किया जाता है। कृपया एनसीडब्ल्यू को ऑफ़लाइन रिपोर्टिंग के लिए राष्ट्रीय महिला आयोग, प्लॉट नंबर 21, एफसी33, जसोला इंस्टीट्यूशनल एरिया, नई दिल्ली -110025 को डाक के माध्यम से या हाथ से सभी महत्वपूर्ण विवरणों और दस्तावेजों से युक्त एक लिखित आवेदन भेजें।")

        return[]
## Online complaint file karne ke liye please go to http://ncwapps.nic.in/onlinecomplaintsv2/   and register your complaint. Please complaint submit karne se phle FAQ ko dhyan se read kijiye by clicking on "Complaint Registration".
class ActionContact(Action):
    print("action contact info=====")
    def name(self) -> Text:
        return "action_contact"
    def run(self,dispatcher, tracker : Tracker, domain : Dict[Text,Any],) -> List[Dict[Text,Any]]:
        org= tracker.get_slot("org")
        if(org=="NCW"):
            dispatcher.utter_message(text="शिकायत संबंधी प्रश्नों के लिए, आप 011-26944880, 26944883 पर संपर्क कर सकते हैं। आप 24x7 राष्ट्रव्यापी हेल्पलाइन नंबर पर भी संपर्क कर सकते हैं। राष्ट्रीय महिला आयोग की 7827-170-170।")
        if(org=="cybercell"):
            dispatcher.utter_message(text="----------शिकायत अधिकारी विवरण--------")
        if(org=="cybercrime"):
            dispatcher.utter_message(text="आप 24*7 के लिए हेल्पलाइन नंबर - 155260 पर कॉल कर सकते हैं।")
        if(org=="MWCD"):
            dispatcher.utter_message(text="आप राष्ट्रव्यापी सूचना/सहायता/काउंसलिंग विकल्पों के लिए 24*7 तक 7827170170 पर भी कॉल कर सकते हैं।")        
         


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
            dispatcher.utter_message(text="स्थान विवरण के लिए धन्यवाद। कृपया एक ईमेल भेजें  <"+ email+">")

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
        #crime=["follow","chase","chasing","following","stalking","stalk", "abusing","harassment", "sexual favor","asking for sexual favor","writing vulger comments", "blackmail","blackmailing","harass","abuse","abusing",
        # "someone using my photos and identity","someone using my identity","someone using my pics and videos","impersonation","vulgar comment","bad comments"]

        stalking=["follow","chase","chasing","following","stalking","stalk"]
        harassment=["abusing","harassment", "sexual favour","asking for sexual favour","writing vulgar comment", "blackmail","blackmailing","torture","harass","defame","abuse","abusing","vulgar comment","bad comments"]
        masquerading=["someone using my photos and identity","someone using my identity","someone  using my pics and videos","impersonation"]
        

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
            dispatcher.utter_message(text="क्या आप कृपया अपनी समस्या को और विस्तार से बता सकते हैं ताकि मैं आपकी मदद कर सकूं?")
        if event1 in stalking:
            dispatcher.utter_message(text= "मुझे आपको बताना चाहिए कि आप पीछा करने के मामले का सामना कर रहे हैं। आपराधिक कानून (संशोधन) अधिनियम 2013 के माध्यम से IPC की धारा 354D के तहत पीछा करना एक अपराध है जो कानूनी कार्रवाई के लिए उत्तरदायी है।")
        if event1 in harassment:
            dispatcher.utter_message(text= " यह ऑनलाइन उत्पीड़न का एक उदाहरण है जो आपराधिक कानून के माध्यम से IPC की धारा 354A के तहत एक अपराध है। (संशोधन) अधिनियम, 2013। क्या आप चाहते हैं कि मैं आपको इस कानून के बारे में और बताऊं?")
        if event1 in masquerading:
            dispatcher.utter_message(text= " हमने जो चर्चा की है, वह स्वांग रचने का मामला है, जो महिलाओं की गरिमा को ठेस पहुंचाने के लिए आईटी संशोधन अधिनियम, 2008 की धारा 66डी के तहत आईपीसी 500 और 509 की धारा के तहत एक दंडनीय अपराध है।") 
        
            

        return []     