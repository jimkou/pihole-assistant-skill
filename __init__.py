from mycroft import MycroftSkill, intent_file_handler,  intent_handler
from adapt.intent import IntentBuilder
import subprocess
import re
#Imports to retrieve data from pihole api
import json 
import requests 
import urllib.request 


def pihole_api(query):
    url = "http://localhost/admin/api.php?"
    source = urllib.request.urlopen(url).read() 
    json_raw = json.loads(source)
    data_dict = {
        "domains_being_blocked" : str(json_raw['domains_being_blocked']),
        "dns_queries_today" : str(json_raw['dns_queries_today']),
        "ads_blocked_today" : str(json_raw['ads_blocked_today']),
        "ads_percentage_today" : str(json_raw['ads_percentage_today']),
        "unique_domains" : str(json_raw['unique_domains']),
        "queries_forwarded" : str(json_raw['queries_forwarded']),
        "queries_cached" : str(json_raw['queries_cached']),
        "clients_ever_seen" : str(json_raw['clients_ever_seen']),
        "unique_clients" : str(json_raw['unique_clients']),
        "dns_queries_all_types" : str(json_raw['dns_queries_all_types']),
        "ads_blocked_today" : str(json_raw['ads_blocked_today']),
        "gravity_last_updated" : str(json_raw['ads_blocked_today'])

                    }
    if query is "all_stats":
        return data_dict
    else:
        return data_dict[query] 

class PiholeAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    
    #No acceptable request
    @intent_handler('assistant.pihole.advertisements.intent')
    def handle_assistant_pihole_default(self, message):
    
        self.speak_dialog('assistant.pihole.advertisements')
      
    #DISABLE PIHOLE
    @intent_handler('assistant.pihole.disable.intent')
    def handle_assistant_pihole_disable(self, message):
        output = subprocess.getoutput("pihole disable")
        already_disabled = ""

        if "already disabled" in output:
            already_disabled = "already"
        self.speak_dialog('assistant.pihole.disable',{"already_disabled" : already_disabled})
    
    #ENABLE PIHOLE
    @intent_handler('assistant.pihole.enable.intent')
    def handle_assistant_pihole_enable(self, message):
        output = subprocess.getoutput("pihole enable")
        already_enabled = ""

        if "already enabled" in output:
            already_enabled = "already"
        self.speak_dialog('assistant.pihole.enable',{"already_enabled" : already_enabled})
    
    #CHECK PIHOLE STATUS
    @intent_handler('assistant.pihole.status.intent')
    def handle_assistant_pihole_status(self, message):
        output = subprocess.getoutput("pihole status")
        if "enabled"  in output:
            status = "enabled"
            self.speak_dialog('assistant.pihole.status',{"status":status})
        elif "disabled" in output:
            status = "disabled"
            self.speak_dialog('assistant.pihole.status',{"status":status})

    #RESTART PIHOLE DNS RESOLVER
    @intent_handler('assistant.pihole.restartdns.intent')
    def handle_assistant_pihole_restartdns(self, message):
        subprocess.call('pihole restartdns',shell=True)
        self.speak_dialog('assistant.pihole.restartdns')

    #FLUSH PIHOLE LOGS
    @intent_handler('assistant.pihole.flush.intent')
    def handle_assistant_pihole_flush(self, message):
        output = subprocess.getoutput("pihole flush | grep Deleted")
        #keep only the queries that flushed
        queries = str(re.findall("\d+", output)[0])
        self.speak_dialog('assistant.pihole.flush',{'number':queries})
    
    #Ads blocked today
    @intent_handler('assistant.pihole.ads_blocked_today.intent')
    def handle_assistant_pihole_ads_blocked_today(self, message):
        
        output = pihole_api("ads_blocked_today")
        output['ads_percentage_today'] = float(round(output['ads_percentage_today'] ,1))
        self.speak_dialog('assistant.pihole.ads_blocked_today',{'number':output})

    #Pihole Stats
    @intent_handler('assistant.pihole.all_stats.intent')
    def handle_assistant_pihole_stats(self, message):
        
        output = pihole_api("all_stats")
        
        self.speak_dialog('assistant.pihole.all_stats',{

            'domains_being_blocked':output['domains_being_blocked'],
            'dns_queries_today':output['dns_queries_today'],
            'ads_blocked_today':output['ads_blocked_today'],
            'ads_percentage_today':output['ads_percentage_today'],
            'unique_domains':output['unique_domains'],
            'queries_forwared':output['queries_forwarded'],
            'queries_cached':output['queries_cached'] 
        
            })


def create_skill():
    return PiholeAssistant()

