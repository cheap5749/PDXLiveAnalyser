
import dictionaries as dico
import fonctions as do
import defines

import time
import csv
# import required module
import os
# assign directory
#directory = 'files'
 
# iterate over files in
# that directory
start_time = time.time()

#obj="population"
#obj="provinces"

with open(defines.output+"output.csv", 'w', newline='') as output:
    provs = csv.writer(output,delimiter=';')
    #provs.writerow(["Region","State","param","x","x","x","x","x","x","param","value","x","x","x","x","x","x"])
    #for filename in os.listdir(defines.directory):
        #curfile = os.path.join(defines.directory, filename)
        # checking if it is a file
        #if os.path.isfile(curfile):
           # print(curfile)
    with open(defines.output+"output2.csv", 'w', newline='') as output2:
        pops = csv.writer(output2,delimiter=';')
#import numpy as np

    

#########################################

            
        with open(defines.input,'r') as f:
                lines = f.readlines()
                savegame=[]

                for line in lines:
                    savegame.append(line)

                curdate=savegame[3].replace("\"","").replace("date=","").strip()
                year=curdate[:3]
                pays=savegame[4].replace("\"","").replace("meta_player_name=","").strip()

                cur_level=0
                cur_obj=""
                prev_obj=""
                pop = 0
                
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
                obj_index=1
                print("--- %s seconds ---" % (time.time() - start_time))
                
                for x in range(len(savegame)):
                    prev_obj=cur_obj
                        
                    #maintenant que niveau est défini, on voit si c'est un objet
                    if str(savegame[x]).strip().find("=")>=0:
                        
                        levels[cur_level]=do.get_left(str(savegame[x]).strip())
                        
                        param=do.get_left(str(savegame[x]).strip())
                        value=do.get_right(str(savegame[x]).replace(".",",")).replace("\"","").strip()
#en cours: préparation provinces
                        if levels[0] == "provinces":
                            if str(param).strip().find("buildings")>=0 and value == "{" and levels[1].isnumeric() == True :
                                param="buildings"
                                value=do.get_right(str(savegame[x+1]).strip().replace(" ","+"))
                                value=eval(value)
                            elif str(param).strip().find("date")>=0 or str(param).strip().find("change")>=0:
                                value=do.get_right(str(savegame[x]).strip())
                            if do.is_info(levels[0])==1 and do.is_param(param)==1:
                                provs.writerow([levels[1],param,value])

#fini:classement des pops
                        if levels[1] == "population":
                            if param == "culture" :
                                dico.popcul.update({levels[2]:value})
                                pop +=1
                            elif param == "religion" :
                                dico.poprel.update({levels[2]:value})
                                pop +=1
                            elif param == "type" :
                                dico.poptyp.update({levels[2]:value})
                                pop +=1
                            if pop == 3 :
                                # on a choppé les 3 paramètres, on peut imprimer
                                pops.writerow([levels[2],dico.poptyp.get(levels[2]),dico.popcul.get(levels[2]),dico.poprel.get(levels[2])])
                                pop = 0
#to do: autres ("country","state") surtout
# diplomacy pour les guerres en cours (les passées?)



                        
#la mécanique pour s'y retrouver dans les niveaux de save
                    if str(savegame[x]).strip().find("{")>=0:
                        cur_level+=1
                                                
                    if str(savegame[x]).strip().find("}")>=0:
                        levels[cur_level]=""
                        cur_level-=1
                        
#fin

old_name = defines.output+"output.csv"
new_name = defines.output+pays+"_"+year+"_provs.csv"

print (old_name)
print (new_name)
# Renaming the file
os.replace(old_name, new_name)

old_name = defines.output+"output2.csv"
new_name = defines.output+pays+"_"+year+"_pops.csv"

print (old_name)
print (new_name)
# Renaming the file
os.replace(old_name, new_name)
print("--- %s seconds ---" % (time.time() - start_time))
