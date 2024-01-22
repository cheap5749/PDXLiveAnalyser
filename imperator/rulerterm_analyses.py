import os
import pandas
import time
import csv
import json
def test(source):
    print (source)
    
def extract(source):

    currentobj=[]
    source = source["country"]["country_database"]
    for x in source.keys():
        term_count=1
        for y in source[x].keys():
            if "ruler_term" in y :
                country_tag=source[x]["tag"]
                ruler=source[x][y]["character"]
                start=source[x][y]["start_date"]
                
                
                try :
                    gov=source[x][y]["government"]
                    party=source[x][y]["party"]
                    result = [country_tag,x,term_count,ruler,start,gov,party]
                except:
                    try:
                        gov=source[x][y]["government"]
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