import os
import pandas
import time
import csv
import json
def test(source):
    print (source)
    
def extract(source):

    attributes={
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
    source=source["character"]["character_database"]
    result=[]
    currentobj=[]
    for x in source.keys():
        if 1 == 1 :
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
    #youhooooooo on a fini
    output=pandas.DataFrame(currentobj, index=(x for x in source.keys()))
    output.columns = attributes.keys()

    output
    return output