import os
import pandas
import time
import csv
import json
def test(source):
    source=source["country"]["country_database"]
    print (source["112"])
    
def extract(source):

    attributes={
    "tag": ["tag","N/A","N/A"],
    "country_name_key": ["country_name","name","N/A"],
    "total_population": ["total_population","N/A","N/A"],
    "total_holdings": ["total_holdings","N/A","N/A"],
    "historical": ["historical","N/A","N/A"],
    "country_type": ["country_type","N/A","N/A"],
    "graphical_culture": ["graphical_culture","N/A","N/A"],
    "manpower": ["currency_data","manpower","N/A"],
    "max_manpower": ["max_manpower","N/A","N/A"],
    "monarch": ["monarch","N/A","N/A"],
    "co_ruler": ["co_ruler","N/A","N/A"],
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
    "economy_lastmonth_tax_income": ["economy","lastmonthincometable",0],
    "economy_lastmonth_trade_income": ["economy","lastmonthincometable",1],
    "economy_lastmonth_vassal_income": ["economy","lastmonthincometable",2],
    "economy_lastmonthexpense": ["economy","lastmonthexpense","N/A"],
    "telemetry_gold_tax": ["economy","telemetry_gold_tax","N/A"],
    "religious_unity": ["religious_unity","N/A","N/A"],
    "foreign_religion_pops": ["foreign_religion_pops","N/A","N/A"],
    "government_key": ["government_key","N/A","N/A"],
    "active_inventions": ["active_inventions","N/A","N/A"],
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
    source=source["country"]["country_database"]
    currentobj=[]
    for x in source.keys():
        if int(x) < 100000 :
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
                        
                if "tech" in attr:
                    attr_value = round(source[x]["technology"][attr]["level"] + source[x]["technology"][attr]["progress"]/100,2)
                if attr == "ports" and "ports" in source[x]:
                    attr_value = len(source[x]["ports"])
                if attr == "manpower" :
                    #attr_value = type(attr_value)
                    attr_value = round(attr_value*500,0)
                if attr == "max_manpower" :
                    #attr_value = type(attr_value)
                    attr_value = round(attr_value*500,0)
                if attr == "total_holdings" :
                    #attr_value = type(attr_value)
                    attr_value = int(attr_value)
                if "income" in attr:
                    attr_value = float(source[x]["economy"][attributes[attr][1]][attributes[attr][2]])
                    
                if "active_inventions" in attr:
                    attr_value = sum(source[x]["active_inventions"])
                else: None
                
                try:
                    attr_value = int(attr_value)
                except:
                    None
                    
                result.append(attr_value)
            currentobj.append(result)

    countries=pandas.DataFrame(currentobj, index=(x for x in source.keys()))
    countries.columns = attributes.keys()
    
    with open("imperator/mappings/countries_names.csv") as countries_names:
        countries_names = pandas.read_csv(countries_names, sep=";", header=None)
        countries_names.columns = ["country_name_key", "country_name"]
    
    countries = countries.merge(countries_names, how='left', on='country_name_key')

    return countries
