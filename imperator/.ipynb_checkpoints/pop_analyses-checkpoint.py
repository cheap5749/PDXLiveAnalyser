import os
import pandas
import time
import csv
import json
def test(source):
    print (source)
    
def extract_pops(source):

    pops_attributes={
        "religion":["religion","N/A","N/A"],
        "type":["type","N/A","N/A"],
        "culture":["culture","N/A","N/A"],
    }
    result=[]
    currentobj=[]
    for x in source["population"]["population"].keys():
        if 1 == 1 :
            result=[]
            for attr in pops_attributes.keys():
                attr_value = ""
                if pops_attributes[attr][0] in source["population"]["population"][x]:
                    if pops_attributes[attr][1] != "N/A" and pops_attributes[attr][1] in source["population"]["population"][x][pops_attributes[attr][0]]:
                        if pops_attributes[attr][2] == "N/A" :
                            ################ niveau 2
                            attr_value = source["population"]["population"][x][pops_attributes[attr][0]][pops_attributes[attr][1]]
                        if pops_attributes[attr][2] != "N/A" and pops_attributes[attr][2] in source["population"]["population"][x][pops_attributes[attr][0]][pops_attributes[attr][1]]:
                            ################ niveau 3
                            if pops_attributes[attr][2] in source["population"]["population"][x][pops_attributes[attr][0]][pops_attributes[attr][1]]:                            
                                attr_value = source["population"]["population"][x][pops_attributes[attr][0]][pops_attributes[attr][1]][pops_attributes[attr][2]]
                            else: None
                        else: None
                    else:
                        ########### niveau 1
                        attr_value = source["population"]["population"][x][pops_attributes[attr][0]]

                else: None
                
                if 1==1:
                    if "tech" in attr:
                        attr_value = round(source["population"]["population"][x]["technology"][attr]["level"] + source["population"]["population"][x]["technology"][attr]["progress"]/100,2)
                    if attr == "ports" and "ports" in source["population"]["population"][x]:
                        attr_value = len(source["population"]["population"][x]["ports"])
                    else: None
                        
                    if "income" in attr:
                        attr_value = source["population"]["population"][x]["economy"][pops_attributes[attr][1]][pops_attributes[attr][2]]

                    if "buildings" in attr:
                        attr_value = sum(source["population"]["population"][x]["buildings"])
                    result.append(attr_value)
            currentobj.append(result)
    #youhooooooo on a fini
    output=pandas.DataFrame(currentobj, index=(x for x in source["population"]["population"].keys()))
    output.columns = pops_attributes.keys()
    date = int(source["date"][:source["date"].find(".")])-753
    output["year"]= date
    output
    return output