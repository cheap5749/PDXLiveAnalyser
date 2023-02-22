import time
#import csv

start_time = time.time()
output = [0] #open("output/structure.csv", "w", newline='')
text_file=open("output/structure.csv", "w", newline='')
#writer = csv.writer(output)

def get_value(string,lookupstring):
    return string.strip().replace(lookupstring,"").replace("\"","")
def get_culture(string):
    middle=string.find("=")
    return string[:middle]
def get_religion(string):
    middle=string.find("=")
    return string[-middle+1:]

#import numpy as np
with open('input/autosave.v2','r') as f:
    lines = f.readlines()
    savegame=[0]
    output="Start\r\n"
    for line in lines:
        savegame.append(line)
    level=0
    for x in range(len(savegame)):
        addition=""
        if str(savegame[x]).count("{")>=1:
            level+=1
            
        if str(savegame[x]).count("}")>=1:
            level-=1
            addition+="\r\n"
            
        if level>=1:
            addition+=","*level
        if level==0:
            addition+="\r\n"
            
        addition+=str(savegame[x]).strip().replace("{","").replace("}","")
        #if str(savegame[x]).count("{")==0 and str(savegame[x]).count("}"):
        #print(addition)
        output+=addition

text_file.write(output)
text_file.close()
print("--- %s seconds ---" % (time.time() - start_time))
