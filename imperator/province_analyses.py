import os
import pandas
import time
import csv
import json
def test(source):
    print (source)
    
def extract(source):

    provinces=source['provinces']
    
    result=[]
    pop_placement=[]
    for province_id in provinces.keys():
        #we save the current war (wars[x])
        #now this level: source['state']['state_database']["state_id"]
        province=provinces[province_id]
        province_name=province["province_name"]["name"]
        pop_count=0
        try : state=province["state"]
        except: state="none"
        
        try : owner=province["owner"]
        except: owner="none"
        
        try: controller=province["controller"]
        except: controller="none"
        
        try: last_owner_change=province["last_owner_change"]
        except: last_owner_change="none"
        
        try: last_controller_change=province["last_controller_change"]
        except: last_controller_change="None"

        try: original_culture=province["original_culture"]
        except:original_culture="none"

        try: original_religion=province["original_religion"]
        except: original_religion="none"

        try: culture=province["culture"]
        except:culture="none"
        try: religion=province["religion"]
        except:religion="none"

        try : garrison=province["garrison"]
        except: garrison=0
        
        try : civilization_value=province["civilization_value"]
        except: civilization_value=0
        
        try : trade_goods=province["trade_goods"]
        except: trade_goods="none"

        try : num_of_roads=province["num_of_roads"]
        except: num_of_roads=0

        try : province_rank=province["province_rank"]
        except: province_rank="none"
        try : buildings=sum(province["buildings"])
        except: buildings=0
        try : looted=province["looted"]
        except: looted="none"
        try : plundered=province["plundered"]
        except: looted="none"
        try : holdings=province["holdings"]
        except: holdings="none"
        try : holy_site=province["holy_site"]
        except: holy_site="none"

        try : great_work=province["great_work"]
        except: great_work=0
        try : treasures=len(province["treasure_slots"]["treasures"])
        except: treasures=0

        #loop in 
        pop=0
        for pops in province.keys():
            if "pop" in pops and pops!="population_ratio" and pops!="growing_pop":
                try:
                    pop=province[pops]
                    pop_count=pop_count+1
                except:
                    print(pops)
                pop_placement.append([province_id,pop])

        result.append([province_id,province_name,state, owner, controller,pop_count, last_owner_change, last_controller_change, original_culture, original_religion, culture, religion, garrison, civilization_value, trade_goods, num_of_roads, province_rank, buildings, looted, plundered, holdings, holy_site, great_work, treasures])

    output=pandas.DataFrame(result)
    pop_placement=pandas.DataFrame(pop_placement)
    pop_placement.columns = ["province_id","pop"]

    output.columns = ["province_id","province_name","state", "owner", "controller","pop_count", "last_owner_change", "last_controller_change", "original_culture", "original_religion","culture", "religion", "garrison", "civilization_value", "trade_goods", "num_of_roads", "province_rank", "buildings", "looted", "plundered", "holdings", "holy_site", "great_work", "treasures"]
    output.set_index("province_id", inplace=True)

    pop_placement.set_index("pop", inplace=True)

    return output
    # return pop_placement