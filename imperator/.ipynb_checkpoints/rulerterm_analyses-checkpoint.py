import os
import pandas
import time
import csv
import json
def test(source):
    print (source)
    
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