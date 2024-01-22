import os
import pandas
import time
import csv
import json
def test(source):
    print (source)
    
def extract_chars(source):

    chars_attributes={
        "first_name":["first_name_loc","name","N/A"],
        "nickname":["nickname","N/A","N/A"],
        "family_name":["family_name","N/A","N/A"],
        "country":["country","N/A","N/A"],
        "home":["home_country","N/A","N/A"],
        "province":["province","N/A","N/A"],
        "birth_date":["birth_date","N/A","N/A"],
        "martial":["attributes","martial","N/A"],
        "finesse":["attributes","finesse","N/A"],
        "charisma":["attributes","charisma","N/A"],
        "zeal":["attributes","zeal","N/A"],
        "family":["family","N/A","N/A"],
        "trait":["traits","N/A","N/A"],
        "last_ruled":["last_ruler_term","N/A","N/A"],
        "culture":["culture","N/A","N/A"],
        "ethnicity":["ethnicity","N/A","N/A"],
        "religion":["religion","N/A","N/A"],
        "death_date":["death_date","N/A","N/A"],
        "death":["death","N/A","N/A"],
        "fertility":["fertility","N/A","N/A"],
        "health":["health","N/A","N/A"],
        "experience":["character_experience","N/A","N/A"],
        "popularity":["popularity","N/A","N/A"],
        "prominence":["prominence","N/A","N/A"],
        "wealth":["wealth","N/A","N/A"],
        "party":["party_type","N/A","N/A"],
        "num_ambitions":["num_ambitions","N/A","N/A"],
        "cur_ambition":["ambition","type","N/A"],
    }
    result=[]
    currentobj=[]
    for x in source["character"]["character_database"].keys():
        if 1 == 1 :
            result=[]
            for attr in chars_attributes.keys():
                attr_value = ""
                if chars_attributes[attr][0] in source["character"]["character_database"][x]:
                    if chars_attributes[attr][1] != "N/A" and chars_attributes[attr][1] in source["character"]["character_database"][x][chars_attributes[attr][0]]:
                        if chars_attributes[attr][2] == "N/A" :
                            ################ niveau 2
                            attr_value = source["character"]["character_database"][x][chars_attributes[attr][0]][chars_attributes[attr][1]]
                        if chars_attributes[attr][2] != "N/A" and chars_attributes[attr][2] in source["character"]["character_database"][x][chars_attributes[attr][0]][chars_attributes[attr][1]]:
                            ################ niveau 3
                            if chars_attributes[attr][2] in source["character"]["character_database"][x][chars_attributes[attr][0]][chars_attributes[attr][1]]:                            
                                attr_value = source["character"]["character_database"][x][chars_attributes[attr][0]][chars_attributes[attr][1]][chars_attributes[attr][2]]
                            else: None
                        else: None
                    else:
                        ########### niveau 1
                        attr_value = source["character"]["character_database"][x][chars_attributes[attr][0]]

                else: None
                
                if 1==1:
                    if "tech" in attr:
                        attr_value = round(source["character"]["character_database"][x]["technology"][attr]["level"] + source["character"]["character_database"][x]["technology"][attr]["progress"]/100,2)
                    if attr == "ports" and "ports" in source["character"]["character_database"][x]:
                        attr_value = len(source["character"]["character_database"][x]["ports"])
                    else: None
                        
                    if "income" in attr:
                        attr_value = source["character"]["character_database"][x]["economy"][chars_attributes[attr][1]][chars_attributes[attr][2]]

                    if "buildings" in attr:
                        attr_value = sum(source["character"]["character_database"][x]["buildings"])
                    result.append(attr_value)
            currentobj.append(result)
    #youhooooooo on a fini
    output=pandas.DataFrame(currentobj, index=(x for x in source["character"]["character_database"].keys()))
    output.columns = chars_attributes.keys()
    date = int(source["date"][:source["date"].find(".")])-753
    output["year"]= date
    output
    return output