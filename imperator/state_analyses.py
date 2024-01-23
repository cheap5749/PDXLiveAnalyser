import os
import pandas
import time
import csv
import json
def test(source):

    return "test"
    
def extract(source):

    states=source['state']['state_database']
    
    result=[]

    for state_id in states.keys():
        #we save the current war (wars[x])
        #now this level: source['state']['state_database']["state_id"]
        state=states[state_id]
        if state != "none":
            capital=state["capital"]
            area=state["area"]
            country=state["country"]
            religion=state["religion"]
            culture=state["culture"]
            try: 
                governor_policy=state["governor_policy"]
            except:
                governor_policy=""
            state_loyalty=state["state_loyalty"]
            food_value=state["food_value"]
            max_food_value=state["max_food_value"]
            cached_food_change=state["cached_food_change"]
        
            state_improvement_religious = 0
            state_improvement_civic = 0
            state_improvement_military = 0
            state_improvement_oratory = 0
            #loop in 

            for modifiers in state.keys():
                if "modifier" in modifiers :
                    modifier=state[modifiers]
                    
                    if "state_improvement_religious" in modifier["modifier"]:
                        if "size" in modifier.keys():
                            state_improvement_religious = modifier["size"]
                        else:
                            state_improvement_religious = 1
                    elif "state_improvement_civic" in modifier["modifier"]:
                        if "size" in modifier.keys():
                            state_improvement_civic = modifier["size"]
                        else:
                            state_improvement_civic = 1
                    elif "state_improvement_military" in modifier["modifier"]:
                        if "size" in modifier.keys():
                            state_improvement_military = modifier["size"]
                        else:
                            state_improvement_military = 1
                    elif "state_improvement_oratory" in modifier["modifier"]:
                        if "size" in modifier.keys():
                            state_improvement_oratory = modifier["size"]
                        else:
                            state_improvement_oratory = 1
                    else:
                        None

            result.append([state_id,capital,area,country,round(religion,2),round(culture,2),governor_policy,round(state_loyalty,0),round(food_value,0),round(max_food_value,0), round(cached_food_change,0),state_improvement_religious,state_improvement_civic,state_improvement_military,state_improvement_oratory])

    output=pandas.DataFrame(result)
    output.columns = ["state_id","capital","area","country","religion","culture","governor_policy","state_loyalty","food_value","max_food_value","cached_food_change","Buildings Supp (relig)","Pop Limit (civic)","Mil Infra","Trade Routes (orat)"]

    return output
