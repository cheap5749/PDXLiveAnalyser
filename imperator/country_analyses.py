import os
import pandas
import time
import csv
import json
def test(source):
    print (source)
    
def extract_countries(source):
    #if len(source)==0: source = "../Imperator/analyses/scythia_solo20-02-2023_15h48.json"
    #with open(source, encoding="utf-8") as source:

    #    source=json.load(source)
    country_attributes={
    "tag": ["tag","N/A","N/A"],
    "historical": ["historical","N/A","N/A"],
    "country_type": ["country_type","N/A","N/A"],
    "graphical_culture": ["graphical_culture","N/A","N/A"],
    "manpower": ["currency_data","manpower","N/A"],
    "max_manpower": ["max_manpower","N/A","N/A"],
    "gold": ["currency_data","gold","N/A"],
    "stability": ["currency_data","stability","N/A"],
    "tyranny": ["currency_data","tyranny","N/A"],
    "war_exhaustion": ["currency_data","war_exhaustion","N/A"],
    "aggressive_expansion": ["currency_data","aggressive_expansion","N/A"],
    "political_influence": ["currency_data","political_influence","N/A"],
    "military_experience": ["currency_data","military_experience","N/A"],
    "capital": ["capital","N/A","N/A"],
    "original_capital": ["original_capital","N/A","N/A"],
    "primary_culture": ["primary_culture","N/A","N/A"],
    "religion": ["religion","N/A","N/A"],
    "diplomatic_stance": ["diplomatic_stance","N/A","N/A"],
    "heritage": ["heritage","N/A","N/A"],
    "ports": ["ports","N/A","N/A"],
    "military_tech": ["technology","military_tech","level"],
    "civic_tech": ["technology","civic_tech","level"],
    "oratory_tech": ["technology","oratory_tech","level"],
    "religious_tech": ["technology","religious_tech","level"],
    "economy_tax_income": ["economy","income",0],
    "economy_trade_income": ["economy","income",1],
    "economy_vassal_income": ["economy","income",2],
    "economy_expense": ["economy","expense","expense"],
    "economy_lastyear_tax_income": ["economy","lastyearincome",0],
    "economy_lastyear_trade_income": ["economy","lastyearincome",1],
    "economy_lastyear_vassal_income": ["economy","lastyearincome",2],
    "economy_lastyearexpense": ["economy","lastyearexpense","N/A"],
    #"economy_lastmonth_tax_income": ["economy","lastmonthincome",0],
    #"economy_lastmonth_trade_income": ["economy","lastmonthincome",1],
    #"economy_lastmonth_vassal_income": ["economy","lastmonthincome",2],
    "economy_lastmonthexpense": ["economy","lastmonthexpense","N/A"],
    "telemetry_gold_tax": ["economy","telemetry_gold_tax","N/A"],
    "religious_unity": ["religious_unity","N/A","N/A"],
    "foreign_religion_pops": ["foreign_religion_pops","N/A","N/A"],
    "total_population": ["total_population","N/A","N/A"],
    "government_key": ["government_key","N/A","N/A"],
    "max_manpower": ["max_manpower","N/A","N/A"],
    "active_inventions": ["active_inventions","N/A","N/A"],
    "total_holdings": ["total_holdings","N/A","N/A"],
    "possible_holdings": ["possible_holdings","N/A","N/A"],
    "total_power_base": ["total_power_base","N/A","N/A"],
    "non_loyal_power_base": ["non_loyal_power_base","N/A","N/A"],
    "armies": ["armies","N/A","N/A"],
    "navies": ["navies","N/A","N/A"],
    "total_cohorts": ["total_cohorts","N/A","N/A"],
    "loyal_cohorts": ["loyal_cohorts","N/A","N/A"],
    "disloyal_cohorts": ["disloyal_cohorts","N/A","N/A"],
    "loyal_pops": ["loyal_pops","N/A","N/A"],
    "centralization": ["centralization","N/A","N/A"],
    "legitimacy": ["legitimacy","N/A","N/A"],
    "cultures_num_of_cultures_with_noble_rights": ["cultures","num_of_cultures_with_noble_rights","N/A"],
    }
    result=[]
    currentobj=[]
    for x in source["country"]["country_database"].keys():
        if int(x) < 100000 :
            result=[]
            for attr in country_attributes.keys():
                attr_value = ""
                if country_attributes[attr][0] in source["country"]["country_database"][x]:
                    if country_attributes[attr][1] != "N/A" and country_attributes[attr][1] in source["country"]["country_database"][x][country_attributes[attr][0]]:
                        if country_attributes[attr][2] == "N/A" :
                            ################ niveau 2
                            attr_value = source["country"]["country_database"][x][country_attributes[attr][0]][country_attributes[attr][1]]
                        if country_attributes[attr][2] != "N/A" and country_attributes[attr][2] in source["country"]["country_database"][x][country_attributes[attr][0]][country_attributes[attr][1]]:
                            ################ niveau 3
                            if country_attributes[attr][2] in source["country"]["country_database"][x][country_attributes[attr][0]][country_attributes[attr][1]]:                            
                                attr_value = source["country"]["country_database"][x][country_attributes[attr][0]][country_attributes[attr][1]][country_attributes[attr][2]]
                            else: None
                        else: None
                    else:
                        ########### niveau 1
                        attr_value = source["country"]["country_database"][x][country_attributes[attr][0]]

                else: None
                
                if source["country"]["country_database"][x]["total_population"] >= 0:
                    if "tech" in attr:
                        attr_value = round(source["country"]["country_database"][x]["technology"][attr]["level"] + source["country"]["country_database"][x]["technology"][attr]["progress"]/100,2)
                    if attr == "ports" and "ports" in source["country"]["country_database"][x]:
                        attr_value = len(source["country"]["country_database"][x]["ports"])
                    else: None
                        
                    if "income" in attr:
                        attr_value = source["country"]["country_database"][x]["economy"][country_attributes[attr][1]][country_attributes[attr][2]]

                    if "active_inventions" in attr:
                        attr_value = sum(source["country"]["country_database"][x]["active_inventions"])
                    result.append(str(attr_value))
            currentobj.append(result)
    #youhooooooo on a fini
    output=pandas.DataFrame(currentobj, index=(x for x in source["country"]["country_database"].keys()))
    output.columns = country_attributes.keys()
    date = int(source["date"][:source["date"].find(".")])-753
    output["year"]= date
    return output