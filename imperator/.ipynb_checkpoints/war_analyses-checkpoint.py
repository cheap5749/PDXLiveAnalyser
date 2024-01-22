import os
import pandas
import time
import csv
import json
def test(source):
    atq_war_exhaust=0
    dump=[]
    for truc in source["diplomacy"]["database"]["39"][y]["attacker"]["countries"][z].keys():
        if "war_exhaustion" in truc:
            atq_war_exhaust=atq_war_exhaust+float(source["diplomacy"]["database"][x][y]["attacker"]["countries"][z]["war_exhaustion"])
        else:
            dump.append(["chier","chier","chier"])
    return atq_war_exhaust
    
def extract(source):
    attributes={
        "atq_id":["original_attacker","N/A","N/A"],
        "def_id":["original_defender","N/A","N/A"],
        "war_name":["war_name","name","N/A"],
        "war_nr":["war_name","ordinal","N/A"],
        "atq_name":["war_name","first","name"],
        "atq_adj":["war_name","first","adjective"],
        "def_name":["war_name","second","name"],
        "def_adj":["war_name","second","adjective"],
        "start":["start_date","N/A","N/A"],
        "wargoal_type":["take_province","type","N/A"],
        "wargoal":["take_province","state","N/A"],
        "atq_pops_slaved":["attacker_pops","enslaved","N/A"],
        "atq_pops_killed":["attacker_pops","killed","N/A"],
        "def_pops_slaved":["defender_pops","enslaved","N/A"],
        "def_pops_killed":["defender_pops","killed","N/A"],
        "battle_id":["battle","N/A","N/A"],
    }
    source=source["diplomacy"]["database"]
    result=[]
    currentobj=[]
    battles=[]
    for x in source.keys():
        result=[]
        for attr in attributes.keys():
            attr_value = ""
            if attributes[attr][0] in source[x]:
                if attributes[attr][1] != "N/A" and attributes[attr][1] in source[x][attributes[attr][0]]:
                    if attributes[attr][2] == "N/A" :
                        ################ niveau 2
                        attr_value = source[x][attributes[attr][0]][attributes[attr][1]]
                    if attributes[attr][2] != "N/A" and attributes[attr][2] in source[x][attributes[attr][0]][attributes[attr][1]]:
                        ################ niveau 3
                        if attributes[attr][2] in source[x][attributes[attr][0]][attributes[attr][1]]:                            
                            attr_value = source[x][attributes[attr][0]][attributes[attr][1]][attributes[attr][2]]
                        else: None
                    else: None
                else:
                    ########### niveau 1
                    attr_value = source[x][attributes[attr][0]]

            else: None
            result.append(attr_value)
            
        currentobj.append(result)
        

    output=pandas.DataFrame(currentobj, index=(x for x in source.keys()))
    output.columns = attributes.keys()
    #output=pandas.DataFrame(battles)
    #output.columns = ["War #","Battle #","Location","Date","Attack win?","Atq Leader","Atq Leader pop change","Def Leader","Def Leader pop change","Atq War exhaust","Def War exhaust"]
    output
    return output

def extract_rulerterms(source):

    currentobj=[]

    for x in source["country"]["country_database"].keys():
        term_count=1
        for y in source["country"]["country_database"][x].keys():
            if "ruler_term" in y :
                country_tag=source["country"]["country_database"][x]["tag"]
                ruler=source["country"]["country_database"][x][y]["character"]
                start=source["country"]["country_database"][x][y]["start_date"]
                
                
                try :
                    gov=source["country"]["country_database"][x][y]["government"]
                    party=source["country"]["country_database"][x][y]["party"]
                    result = [country_tag,x,term_count,ruler,start,gov,party]
                except:
                    try:
                        gov=source["country"]["country_database"][x][y]["government"]
                        result = [country_tag,x,term_count,ruler,start,gov,'']
                    except:
                        result = [country_tag,x,term_count,ruler,start,'','']
                finally:
                    currentobj.append(result)
                term_count=term_count+1

    #youhooooooo on a fini
    output=pandas.DataFrame(currentobj)
    output.columns = ["TAG","ID","Term Count","Ruler","Term start date","Government Type","Party"]

    return output
def battles(source):
    #ok ça c'était pour les guerres mais on peut faire les batailles aussi? on fait ça en parcourant les guerres psq c'est niché dedans
        result=[]
        battle_count=0
        for y in source["diplomacy"]["database"][x].keys():
            #pour chaque balise dans chaque guerre, on regarde si c'est une bataille, si oui gogogogo (encore une fois, batailles sont dupliquées donc battlexxxx={}
            
            if "battle" in y and x=="39":
                #and x=="39"
                battle_count=battle_count+1
                
                try :
                    location=source["diplomacy"]["database"][x][y]["location"]
                    bool_attack_win=source["diplomacy"]["database"][x][y]["result"]
                    date=source["diplomacy"]["database"][x][y]["date"]
                    
                    
                    #loop dans les pays et les unités pour choper les pertes
                    try:
                        atq_war_exhaust=0
                        try:
                            for z in range(1,10):
                                #atq_war_exhaust=z
                                for truc in source["diplomacy"]["database"][x][y]["attacker"]["countries"][z].keys():
                                    if "war_exhaustion" in truc:
                                        atq_war_exhaust=atq_war_exhaust+float(source["diplomacy"]["database"][x][y]["attacker"]["countries"][z]["war_exhaustion"])
                                    else:
                                        None
                        except:
                                #print(list(source["diplomacy"]["database"][x][y]["attacker"]["countries"].keys()))
                                A=source["diplomacy"]["database"][x][y]["attacker"]["countries"]
                                [print(a) for a in A];
                    except:
                        atq_war_exhaust="erreur"
                        
                        #A=[atq_war_exhaust,source["diplomacy"]["database"][x][y]["attacker"]["countries"][0]["war_exhaustion"]]
                        #[print(a) for a in A];
                    try:
                        def_war_exhaust=0
                        for participants in source["diplomacy"]["database"][x][y]["defender"]["countries"].keys():
                            def_war_exhaust=def_war_exhaust+source["diplomacy"]["database"][x][y]["defender"]["countries"][participants]["war_exhaustion"]
                    except:
                        def_war_exhaust=0
                    try:
                        atq_leader=source["diplomacy"]["database"][x][y]["attacker"]["leader"]
                        atq_pop=source["diplomacy"]["database"][x][y]["attacker"]["popularity_change"]
                    except:
                        atq_leader="No leader"
                        atq_pop=0
                    try:
                        def_leader=source["diplomacy"]["database"][x][y]["defender"]["leader"]
                        def_pop=source["diplomacy"]["database"][x][y]["attacker"]["popularity_change"]
                    except:
                        def_leader="No leader"
                        def_pop=0
                    result = [x,battle_count,location,date,bool_attack_win,atq_leader,atq_pop,def_leader,def_pop,atq_war_exhaust,def_war_exhaust]
                except:                  
                    result = [x,y,"échec battle #"+str(battle_count),source["diplomacy"]["database"][x][y],'','','','','','','']
                    A=["war#"+x+" (battle#"+str(battle_count)+")",y,source["diplomacy"]["database"][x][y]]
                    [print(a) for a in A];
                finally:
                    battles.append(result)
                #battles.append([x,y,'',source["diplomacy"]["database"][x][y],'','','','',''])
    
    #youhooooooo on a fini