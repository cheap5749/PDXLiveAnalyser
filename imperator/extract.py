import os
import sys
import pandas
import time
import csv
import json
import openpyxl
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider
from IPython.display import display, HTML
import locale
#%autoreload 1
#because shitty duplicate keys, now there is a global duplicate count, and every object whose key is duplicate, like "ruler_term" has now it's own duplicate number
global global_dupl_count
global_dupl_count=0
def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    global global_dupl_count
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            global_dupl_count=global_dupl_count+1
            d[k+str(global_dupl_count)] = v
        else:
            d[k] = v
    return d

def extract(filepath, filename, create_excel, create_csv, delete_melted):
    filename = "mp_rome_grand_camp_821"
    filepath = "D:/python/Imperator/analyses/"
    savegame = filepath+filename

    with open(savegame, encoding="utf-8") as source:
        source=json.load(source,object_pairs_hook=dict_raise_on_duplicates)

            
    from imperator import country_analyses
    from imperator import state_analyses
    from imperator import province_analyses
    from imperator import pop_analyses

    from imperator import char_analyses
    from imperator import rulerterm_analyses

    from imperator import war_analyses
    from imperator import battle_analyses



    rulerterms = rulerterm_analyses.extract(source)
    provinces = province_analyses.extract(source)
    countries = country_analyses.extract(source)
    provinces = province_analyses.extract(source)
    game_date=source["date"]
    pops = pop_analyses.extract(source)
    chars = char_analyses.extract(source)
    wars = war_analyses.extract(source)
    battles = battle_analyses.extract(source)

    countries["country_name_key"]=countries["historical"]
    countries["total_income"]=round(countries["economy_lastmonth_tax_income"]+countries["economy_lastmonth_tax_income"]+countries["economy_lastmonth_tax_income"])
    countries = countries.sort_values("total_holdings",ascending=False).query('total_income > 10 & total_holdings > 0')
    if create_excel == True:
        with pandas.ExcelWriter("D:/python/"+filename+"_"+game_date+".xlsx") as writer:

            rulerterms.to_excel(writer, sheet_name='rulers')  
            countries.to_excel(writer, sheet_name='countries')  
            provinces.to_excel(writer, sheet_name='provinces')  
            pops.to_excel(writer, sheet_name='pops')  
            chars.to_excel(writer, sheet_name='chars')  
            wars.to_excel(writer, sheet_name='wars')
            battles.to_excel(writer, sheet_name='battles')

