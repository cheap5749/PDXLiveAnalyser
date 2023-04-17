pop_types=["aristocrats","capitalists","bureaucrats","clerks","officers","clergymen","artisans","slaves","soldiers","farmers","labourers","craftsmen"]
pop_stats=["id","size","cult","rel","money","con","mil","literacy","bank","life_needs","everyday_needs","luxury_needs","movement_issue","production_type","current_producing","production_income","needs_cost"]

goods_types=["ammunition", "small_arms", "artillery", "canned_food", "barrels", "aeroplanes", "cotton", "dye", "wool", "silk", "coal", "sulphur", "iron", "timber", "tropical_wood", "rubber", "oil", "precious_metal", "steel", "cement", "machine_parts", "glass", "fuel", "fertilizer", "explosives", "clipper_convoy", "steamer_convoy", "electric_gear", "fabric", "lumber", "paper", "cattle", "fish", "fruit", "grain", "tobacco", "tea", "coffee", "opium", "automobiles", "telephones", "wine", "liquor", "regular_clothes", "luxury_clothes", "furniture", "luxury_furniture", "radio"]
goods_stats=["worldmarket_pool", "price_pool", "last_price_history", "supply_pool", "last_supply_pool", "price_history", "price_history_last_update", "price_change", "actual_sold", "actual_sold_world", "real_demand", "demand"]

exclusion_list=["enabled_dlcs","enabled_mods","game_configuration","ironman_cloud","ironman_save_name","difficulty","variables","replay","version","triggered_event","on_action","primary","date","triggered_event_temp","event","player_event","immediate","ignore","ai"]
#TODO
    #intégrer autres objets par listes et ajouter au dictionnaire de listes

obj_dict = {
  "pop_types": pop_types,
  "pop_stats": pop_stats,
  "goods_types": goods_types,
  "goods_stats": goods_stats
}

info_list =["family","character","armies","country","state","horde","mercenary","population","provinces","road_network","combat","trade","treasure_manager","great_work_manager","country_culture_manager", "diplomacy"]
info_dict = {"provinces":8813}
param_list = ["name","state","owner","controller","previous_owner","last_owner_change","last_controller_change","original_culture","original_religion","culture","religion","pop","garrison","civilization_value","trade_goods","num_of_roads","num_foreign_culture","province_rank","buildings","great_work","religion"]

popcul={
    "id":0,
    "popculture":"culture"}
poprel={
    "id":0,
    "popreligion":"religion"}
poptyp={
    "id":0,
    "poptype":"type"}
poploc={
    "id":0,
    "province":"province id"}

prov_name = {"id":0, "name":"name"}
prov_state = {"id":0, "state":"state"}
prov_owner = {"id":0, "owner":"owner"}
prov_controller = {"id":0, "controller":"controller"}
prov_previous_owner = {"id":0, "previous_owner":"previous_owner"}
prov_last_owner_change = {"id":0, "last_owner_change":"last_owner_change"}
prov_last_controller_change = {"id":0, "last_controller_change":"last_controller_change"}
prov_original_culture = {"id":0, "original_culture":"original_culture"}
prov_original_religion = {"id":0, "original_religion":"original_religion"}
prov_culture = {"id":0, "culture":"culture"}
prov_religion = {"id":0, "religion":"religion"}
prov_pop = {"id":0, "pop":"pop"}
prov_garrison = {"id":0, "garrison":"garrison"}
prov_civilization_value = {"id":0, "civilization_value":"civilization_value"}
prov_trade_goods = {"id":0, "trade_goods":"trade_goods"}
prov_num_of_roads = {"id":0, "num_of_roads":"num_of_roads"}
prov_num_foreign_culture = {"id":0, "num_foreign_culture":"num_foreign_culture"}
prov_province_rank = {"id":0, "province_rank":"province_rank"}
prov_buildings = {"id":0, "buildings":"buildings"}
prov_great_work = {"id":0, "great_work":"great_work"}