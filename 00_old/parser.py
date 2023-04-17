import os
import dictionaries as dico
import fonctions as do
import defines

import time
import csv


#import numpy as np

start_time = time.time()

#########################################
with open(defines.output+"output.csv", 'w', newline='') as output:
    pops = csv.writer(output,delimiter=';')
    pops.writerow(["Date","province","provid","Country","Pop_size","pop_type","pop_cul","pop_rel","consciousness","militancy","literacy","life_needs","everyday_needs","luxury_needs","production_type","production_qty","production_value"
])
    
    with open(defines.input,'r') as f:
        lines = f.readlines()
        savegame=[]

        for line in lines:
            savegame.append(line)

        curdate=savegame[3].replace("\"","").replace("date=","").strip()
        year=curdate[:3]
        pays=savegame[4].replace("\"","").replace("meta_player_name=","").strip()

        cur_level=0
        
        cur_lvl1=""
        prev_lvl1=""
        
        cur_lvl2=""
        prev_lvl2=""
        
        cur_lvl3=""
        prev_lvl3=""
        

        levels={
        0:"",
        1:"",
        2:"",
        3:"",
        4:"",
        5:"",
        6:"",
        7:""}
        
        obj_list=[0]
        obj_index=0
        
        for x in range(len(savegame)):
            #prev_obj=cur_obj
            if str(savegame[x]).strip().find("{")>=0:
                cur_level+=1
                #cur_obj=str(savegame[x-1]).strip()
                
            if str(savegame[x]).strip().find("}")>=0:
                levels[cur_level]=""
                cur_level-=1
                
                
            #maintenant que niveau est défini, on voit si c'est un objet
            if str(savegame[x]).strip().find("=")>=0:
                
                levels[cur_level]=do.get_left(str(savegame[x]).strip())

                prev_lvl1=cur_lvl1
                cur_lvl1=levels[1]

                prev_lvl2=cur_lvl2
                cur_lvl2=levels[2]
                
                prev_lvl3=cur_lvl3
                cur_lvl3=levels[3]
                
                #if do.is_excluded(cur_obj)==0:
                if levels[0].isnumeric()==True:
                    pops.writerow([levels[0],levels[1],levels[2],levels[3],levels[4],levels[5],levels[6],levels[7],do.get_left(str(savegame[x]).strip()),do.get_right(str(savegame[x]).strip().replace(".",","))])
                else:
                        #print ("line " + str(x) + " level " + str(cur_level) + ":" + levels[cur_level] + " objet: " +do.get_left(str(savegame[x]).strip())+ " valeur: "+do.get_right(str(savegame[x]).strip().replace(".",",")))
                        #print ("line " + str(x) + " level " + str(cur_level) + ":" + levels[cur_level] + " objet: " +cur_obj )
                        #if do.is_info(cur_info)==1 and x<=7253778 and levels[2]:
                    if cur_lvl1=="provinces" and cur_lvl2!=prev_lvl2:
                        print (x,levels[1],levels[2],levels[3])
            #if prev_obj==cur_obj:
                #on est sur le même objet que ligne x-1 (en tous cas même niveau), faut chopper les attributs et
                #leurs valeurs et mettre dans la même ligne du csv
            #else:
                #on est sur un nouvel objet, il faut donc ouvrir une nouvelle ligne de csv et identifier le type d'objet
            
            

            #if cur_level>=0 and prev_index!=obj_index:
                #print (str(x+1)+"("+str(cur_level)+"): "+cur_obj.replace("=","")+" ("+str(obj_index)+")")
            #print (str(x+1)+"("+str(cur_level)+"): "+str(savegame[x]).strip())

#print (maxi)

##            isname = str(savegame[x]).find("name=")
##            isunit = str(savegame[x]).find(" ")
##            if isname!=-1 and isunit!=4:
##
##                province=do.get_value(savegame[x],"name=")
##                province_id=do.get_value(savegame[x-2],"=")
##                owner=do.get_value(savegame[x+1],"owner=")
##                controller=do.get_value(savegame[x+2],"controller=")
##
##                if len(province_id)<=4:
##
##                    cur_prov=province.replace("\"","")
##                    cur_provid=province_id
##                    cur_owner=owner
##                    cur_controller=controller
##            #on a affaire à une pop: scrap les datas
##            if do.get_poptype(str(savegame[x]).strip())!="nope":
##                cur_pop=do.get_poptype(str(savegame[x]).strip())
##                cur_size=do.get_value(savegame[x+3],"size=")
##                cur_cul=do.get_culture(savegame[x+4].strip())
##                cur_rel=do.get_religion(savegame[x+4].strip())
##
##                is_mil =  str(savegame[x]).find("mil=")

                #pops.writerow([curdate,cur_prov,cur_provid,cur_owner,cur_size,cur_pop,cur_cul,cur_rel])
                #print ([curdate,cur_prov,cur_provid,cur_owner,cur_size,cur_pop,cur_cul,cur_rel])


                #do.get_obj_param("pop","stats",str(savegame[x]).strip())+str(x))
            #on a affaire à un rgo
            #on a affaire à un goods
old_name = defines.output+"output.csv"
new_name = defines.output+pays+"_"+year+".csv"

print (old_name)
print (new_name)
# Renaming the file
os.replace(old_name, new_name)
print("--- %s seconds ---" % (time.time() - start_time))
