import dictionaries
def get_value(string,lookupstring):
    return str(string).strip().replace(lookupstring,"").replace("\"","")

#######fonctions pour stats de pop, à unifier?#############
def get_left(string):
    middle=string.find("=")
    return string[:middle]
def get_right(string):
    middle=string.find("=")+1
    return string[middle:]
##########fonction pour identifier une pop. eventuellement à remplacer################
def get_poptype(string):
    match dictionaries.pop_types.count(string.replace("=","")):
        case 1:
            poptype=string.replace("=","")
        case _:
            poptype="nope"
    return poptype
def is_excluded(string):
    match dictionaries.exclusion_list.count(string):
        case 1:
            excluded=1
        case _:
            excluded=0
    return excluded
    
def is_info(string):
    match dictionaries.info_list.count(string):
        case 1:
            excluded=1
        case _:
            excluded=0
    return excluded
    
def is_param(string):
    match dictionaries.param_list.count(string):
        case 1:
            excluded=1
        case _:
            excluded=0
    return excluded
#######################################
#fonction pour scanner l'intérieur d'un objet dans un niveau et en retourner toutes les valeurs de stats
    #exemple: le parser tombe sur une pop, la fonction vérifie les stats de pop et les cherche dans la string courante. si c'est une stat, la fonction renvoie une chaine [stat, valeur]
    #le parser créée une variable cur_getobjparam(x,y,z)[0] de valeur getobjparam(x,y,z)[1]
def get_obj_param(obj_type,obj_stats,teststring):
    #for stats in dictionaries.obj_dict[obj_type+"_"+obj_stats]:
    match dictionaries.obj_dict[obj_type+"_"+obj_stats].count(teststring.replace("=","")):
        case 1:
            #stat=[stats,teststring.replace(stats+"=","")]
            #stat=stats+": "+teststring.replace(stats+"=","")]
            #print (stat)
            return teststring.replace("=","")
        case _:
            return ""
def province(id,param,value):
    match param:
        case "name": return dictionaries.prov_name.update({id:value})
        case "state": return dictionaries.prov_state.update({id:value})
        case "owner": return dictionaries.prov_owner.update({id:value})
        case "controller": return dictionaries.prov_controller.update({id:value})
        case "previous_owner": return dictionaries.prov_previous_owner.update({id:value})
        case "last_owner_change": return dictionaries.prov_last_owner_change.update({id:value})
        case "last_controller_change": return dictionaries.prov_last_controller_change.update({id:value})
        case "original_culture": return dictionaries.prov_original_culture.update({id:value})
        case "original_religion": return dictionaries.prov_original_religion.update({id:value})
        case "culture": return dictionaries.prov_culture.update({id:value})
        case "religion": return dictionaries.prov_religion.update({id:value})
        case "pop": return dictionaries.prov_pop.update({id:value})
        case "garrison": return dictionaries.prov_garrison.update({id:value})
        case "civilization_value": return dictionaries.prov_civilization_value.update({id:value})
        case "trade_goods": return dictionaries.prov_trade_goods.update({id:value})
        case "num_of_roads": return dictionaries.prov_num_of_roads.update({id:value})
        case "num_foreign_culture": return dictionaries.prov_num_foreign_culture.update({id:value})
        case "province_rank": return dictionaries.prov_province_rank.update({id:value})
        case "buildings": return dictionaries.prov_buildings.update({id:value})
        case "great_work": return dictionaries.prov_great_work.update({id:value})
        # case _:
    
#get_obj_param("pop","types",1,10)
