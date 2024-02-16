import pandas
    
def extract(source):

    families=source["family"]["families"]
    
    result=[]

    for family_id in families.keys():
        family=families[family_id]
        family_key=""
        family_owner=""
        family_prestige=""
        family_culture=""
        family_members=""
        if type(family) != str: 
            if "key" in family: family_key=family["key"]
            if "owner" in family: family_owner=family["owner"]
            if "prestige" in family: family_prestige=family["prestige"]
            if "minor_family" in family: family_key="Commoner"
            if "culture" in family: family_culture=family["culture"]
            if "member" in family: family_members=len(family["member"])
            result.append([family_id,family_key,family_owner,family_prestige,family_culture,family_members])
        # else: print(family)


    output=pandas.DataFrame(result)

    output.columns = ["family_id","family_key","family_owner","family_prestige","family_culture","family_members"]

    return output
