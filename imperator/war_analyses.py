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

    wars=source["diplomacy"]["database"]
    
    result=[]

    for war_id in wars.keys():
        #we save the current war (wars[x])
        war=wars[war_id]
        original_attacker=war["original_attacker"]
        original_defender=war["original_defender"]
        war_name=warname(war["war_name"]["name"],war["war_name"]["ordinal"],war["war_name"]["first"]["name"],war["war_name"]["second"]["name"])
        start_date=war["start_date"]

        attacker_pops_enslaved=war["attacker_pops"]["enslaved"]
        attacker_pops_killed=war["attacker_pops"]["killed"]

        defender_pops_enslaved=war["defender_pops"]["enslaved"]
        defender_pops_killed=war["defender_pops"]["killed"]

        result.append([war_id,original_attacker,original_defender,war_name,start_date,attacker_pops_enslaved,attacker_pops_killed,defender_pops_enslaved,defender_pops_killed])
        
    output=pandas.DataFrame(result)
    output.columns = ["war_id","original_attacker","original_defender","war_name","start_date","attacker_pops_enslaved","attacker_pops_killed","defender_pops_enslaved","defender_pops_killed"]
    return output

def warname(name,ordinal,first,second):
    output = "no clue lol"
    return output
    