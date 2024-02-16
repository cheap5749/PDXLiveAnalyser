import pandas
global countries_names
global gov_names
global cultures
global geography_names
with open("imperator/mappings/countries_names.csv") as countries_names:
    countries_names = pandas.read_csv(countries_names, sep=";", header=None)
    countries_names.columns = ["country_name_key", "country_name"]
    countries_names.set_index("country_name_key", inplace=True)
    
with open("imperator/mappings/gov_names.csv") as gov_names:
    gov_names = pandas.read_csv(gov_names, sep=";", header=None)
    gov_names.columns = ["gov_name_key", "gov_name"]
    gov_names.set_index("gov_name_key", inplace=True)

with open("imperator/mappings/cultures.csv") as cultures:
    cultures = pandas.read_csv(cultures, sep=";", header=None)
    cultures.columns = ["culture","group","culture_name","culture_group_name"]
    cultures.set_index("culture", inplace=True)

with open("imperator/mappings/geography_names.csv") as geography_names:
    geography_names = pandas.read_csv(geography_names, sep=";", header=None)
    geography_names.columns = ["geography_name_key", "geography_name"]
    geography_names.set_index("geography_name_key", inplace=True)


def name(object,object_type,**add_infos):
    output=""
    #country kwargs:
    country_tag = add_infos.get("country_tag", None)
    country_name = object
    capital = add_infos.get("capital", None)
    gov_type = add_infos.get("gov_type", None)
    hist_country_tag = add_infos.get("hist_country_tag", None)
    creation_date = add_infos.get("creation_date", 451)
    #culture/language kwargs:
    culture=add_infos.get("culture", None)
    language=add_infos.get("language", None)
    #geography kwargs:
    zone=add_infos.get("zone", None)
    ########## loading localization files ############

    ########## depending on object type #############
    if object_type=="country":
        #mostly used name cases: normal (based on tag), CIVILWAR_FACTION_NAME, province (PROV4546), region (ex: kharesmia_superior), area (achaea_area)
        ####simple case: we find country name in country names (yay)
        if country_name in countries_names.index:
            output = countries_names.at[country_name,"country_name"]
        #also simple, current tag is also in csv
        elif country_tag in countries_names.index:
            output = countries_names.at[country_tag,"country_name"]
        #uh oh so it's a CIVILWAR_FACTION_NAME
        elif "CIVILWAR_FACTION_NAME" in country_name and hist_country_tag in countries_names.index:
            output = countries_names.at[hist_country_tag+"_ADJ","country_name"]+" revolt"
        #ok a CIVIL war of some made up country, what is it's culture?
        elif "CIVILWAR_FACTION_NAME" in country_name and culture in cultures.index:
            output = cultures.at[culture,"culture_name"]+" revolt of "+geography_names.at["PROV"+str(capital),"geography_name"]
        #now the case of geographic zones
        elif country_name in geography_names.index and gov_type in gov_names.index :
            output = gov_names.at[gov_type,"gov_name"]+" of "+geography_names.at[country_name,"geography_name"]
        #rest: cultural government of capital
        else:
            try:
                output= cultures.at[culture,"culture_name"]+" "+gov_names.at[gov_type,"gov_name"]+" of "+geography_names.at["PROV"+str(capital),"geography_name"]
            except:
                output= culture+" "+gov_type
    elif object_type == "country_adj":
        if country_name+"_ADJ" in countries_names.index:
            output = countries_names.at[country_name+"_ADJ","country_name"]
        else:
            try:
                output= cultures.at[culture,"culture_name"]
            except:
                output= culture+" "+gov_type
    elif object_type == "gov_type":
        if object in gov_names.index:
            output = gov_names.at[object,"gov_name"]
        else:
            output= "unknown government type"
    elif object_type == "geography":
        if object in geography_names.index:
            output = geography_names.at[object,"geography_name"]
        elif "PROV"+str(object) in geography_names.index:
            output = geography_names.at["PROV"+str(object),"geography_name"]
        elif str(object[:object.find("_")]) in geography_names.index:
            output = geography_names.at[str(object[:object.find("_")]),"geography_name"]
        else:
            output= "unknown place"
    else:
        output= object_type +" non managed"
    return output