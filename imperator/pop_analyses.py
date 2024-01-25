import os
import pandas
import time
import csv
import json
def test(source):
    print (source)
    
def extract(source):

    attributes={
        "id":["N/A","N/A","N/A"],
        "religion":["religion","N/A","N/A"],
        "type":["type","N/A","N/A"],
        "culture":["culture","N/A","N/A"],
    }
    result=[]
    currentobj=[]
    source=source["population"]["population"]
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

                if attr == "id":
                    attr_value = int(x)


                result.append(attr_value)
            currentobj.append(result)
    #youhooooooo on a fini
    output=pandas.DataFrame(currentobj, index=(x for x in source.keys()))
    output.columns = attributes.keys()
    output=output.sort_values(by=["id"])
    output.set_index("id", inplace=True)
    output = output[output.religion != ""]

    return output