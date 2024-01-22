import os
import pandas
import time
import csv
import json
def test(source):
    print (source)
    
def extract_provinces(source):
    #if len(source)==0: source = "../Imperator/analyses/scythia_solo20-02-2023_15h48.json"
    #with open(source, encoding="utf-8") as source:

    #    source=json.load(source)
    # attributes are first identified as a list & with location in save; each attribute gets a column
    province_attributes={
        "province_name":["province_name","name","N/A"],
        "state":["state","N/A","N/A"],
        "owner":["owner","N/A","N/A"],
        "controller":["controller","N/A","N/A"],
        "previous_owner":["previous_owner","N/A","N/A"],
        "last_owner_change":["last_owner_change","N/A","N/A"],
        "last_controller_change":["last_controller_change","N/A","N/A"],
        "claim":["claim","N/A","N/A"],
        "original_culture":["original_culture","N/A","N/A"],
        "original_religion":["original_religion","N/A","N/A"],
        "culture":["culture","N/A","N/A"],
        "religion":["religion","N/A","N/A"],
        "civilization_value":["civilization_value","N/A","N/A"],
        "trade_goods":["trade_goods","N/A","N/A"],
        "num_of_roads":["num_of_roads","N/A","N/A"],
        "blockaded":["blockaded","N/A","N/A"],
        "blockaded_percent_per_navy":["blockaded_percent_per_navy","N/A","N/A"],
        "province_rank":["province_rank","N/A","N/A"],
        "buildings":["buildings","N/A","N/A"],
        "pops":["pop","N/A","N/A"],
        "looted":["looted","N/A","N/A"],
        "plundered":["plundered","N/A","N/A"],
        "holy_site":["holy_site","N/A","N/A"],
    }
    result=[]
    currentobj=[]
    #lets loop in a specific location of the save: source[xx]
    for x in source["provinces"].keys():
        if int(x) < 100000 :
            result=[]
            #since many pops per province, reset pops_count only when new province, it'll get incrementally counted after
            pops_count = 0            
            for attr in province_attributes.keys():
                attr_value = ""
                if province_attributes[attr][0] in source["provinces"][x]:
                    if province_attributes[attr][1] != "N/A" and province_attributes[attr][1] in source["provinces"][x][province_attributes[attr][0]]:
                        if province_attributes[attr][2] == "N/A" :
                            ################ niveau 2
                            attr_value = source["provinces"][x][province_attributes[attr][0]][province_attributes[attr][1]]
                        if province_attributes[attr][2] != "N/A" and province_attributes[attr][2] in source["provinces"][x][province_attributes[attr][0]][province_attributes[attr][1]]:
                            ################ niveau 3
                            if province_attributes[attr][2] in source["provinces"][x][province_attributes[attr][0]][province_attributes[attr][1]]:                            
                                attr_value = source["provinces"][x][province_attributes[attr][0]][province_attributes[attr][1]][province_attributes[attr][2]]
                            else: None
                        else: None
                    else:
                        ########### niveau 1
                        attr_value = source["provinces"][x][province_attributes[attr][0]]

                else: None
                
                if 1==1:
                    if "tech" in attr:
                        attr_value = round(source["provinces"][x]["technology"][attr]["level"] + source["provinces"][x]["technology"][attr]["progress"]/100,2)
                    if attr == "ports" and "ports" in source["provinces"][x]:
                        attr_value = len(source["provinces"][x]["ports"])
                    else: None
                        
                    if "income" in attr:
                        attr_value = source["provinces"][x]["economy"][province_attributes[attr][1]][province_attributes[attr][2]]
                    # buildings format: buildings={		1 0 0 0 1 9 0 0 0 9 3 12 3 0 0 0 0 0 0 0 0 0		}
                    # for now sum it simply, maybe later could detail what type etc
                    if "buildings" in attr:
                        attr_value = sum(source["provinces"][x]["buildings"])
                        
                    if "pops" in attr:
                        pops_count += 1
                        attr_value = pops_count
                    result.append(attr_value)
            currentobj.append(result)
    #youhooooooo on a fini
    output=pandas.DataFrame(currentobj, index=(x for x in source["provinces"].keys()))
    output.columns = province_attributes.keys()
    date = int(source["date"][:source["date"].find(".")])-753
    output["year"]= date
    return output