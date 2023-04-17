
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
with open(defines.output+"output.csv", 'w', newline='') as output:
    pops = csv.writer(output,delimiter=';')
    pops.writerow(["Region","State","param","x","x","x","x","x","x","param","value","x","x","x","x","x","x"
        ])
    for filename in os.listdir("../Imperator/Analyses/Cultures"):
        curfile = os.path.join("../Imperator/Analyses/Cultures", filename)
        # checking if it is a file
        if os.path.isfile(curfile):
            print(curfile)

#import numpy as np


#########################################

            
            with open(curfile,'r') as f:
                lines = f.readlines()
                savegame=[]

                for line in lines:
                    savegame.append(line)

                #curdate=savegame[1].replace("\"","").replace("date=","").strip()

                cur_level=0
                cur_obj=""
                prev_obj=""

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
                
                for x in range(len(savegame)):
                    prev_obj=cur_obj
                        
                    #maintenant que niveau est défini, on voit si c'est un objet
                    if str(savegame[x]).strip().find("=")>=0:
                        
                        levels[cur_level]=do.get_left(str(savegame[x]).strip())
                        
                        cur_obj=do.get_left(str(savegame[x]).strip())
                        
                        #if do.is_excluded(cur_obj)==0:
                            #if levels[0].isnumeric()==True:
                        param=do.get_left(str(savegame[x]).strip())
                        value=do.get_right(str(savegame[x]).replace(".",",")).strip()

                        #if value=="bg_oil_extraction":
                        if str(value).strip().find("oil_extraction")>=0:
                            #print (value)
                            param="bg_oil_extraction"
                            value=do.get_right(str(savegame[x+1]).strip().replace(".",","))
                        elif str(value).strip().find("bg_rubber")>=0:
                            param="bg_rubber"
                            value=do.get_right(str(savegame[x+1]).strip().replace(".",","))
                                               
                        pops.writerow([curfile[curfile.find("\\")+1:].replace(".txt",""), levels[0],levels[1],levels[2],levels[3],levels[4],levels[5],levels[6],levels[7],param,value])
                        
                    if str(savegame[x]).strip().find("{")>=0:
                        cur_level+=1
                        #cur_obj=str(savegame[x-1]).strip()
                        
                    if str(savegame[x]).strip().find("}")>=0:
                        levels[cur_level]=""
                        cur_level-=1
                        
                        #prev_obj=cur_obj

print("--- %s seconds ---" % (time.time() - start_time))
