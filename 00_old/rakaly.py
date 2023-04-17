
import dictionaries as dico
import fonctions as do
import defines

import time
import csv
import os
import subprocess



start_time = time.time()

takethis = str('rakaly\\rakaly.exe melt "..\Imperator\save games\\autosave.rome"')
print (takethis)

subprocess.call(takethis)

#subprocess.check_output("ls non_existent_file; exit 0", stderr=subprocess.STDOUT, shell=True)

#old_name = defines.output+"output2.csv"
#new_name = defines.output+pays+"_"+year+"_pops.csv"

#os.replace(old_name, new_name)
print("--- %s seconds ---" % (time.time() - start_time))
