import os
import pandas
import time
import csv
import json
#from itables import init_notebook_mode

#init_notebook_mode(all_interactive=True)

savegame = "../Victoria 3/save games/germany_1878_04_10.json"
with open(savegame, encoding="utf-8") as source:
    source=json.load(source)
from ipywidgets import interact, IntSlider
from IPython.display import display

def freeze_header(df, num_rows=30, num_columns=10, step_rows=1,
                  step_columns=1):
    """
    Freeze the headers (column and index names) of a Pandas DataFrame. A widget
    enables to slide through the rows and columns.

    Parameters
    ----------
    df : Pandas DataFrame
        DataFrame to display
    num_rows : int, optional
        Number of rows to display
    num_columns : int, optional
        Number of columns to display
    step_rows : int, optional
        Step in the rows
    step_columns : int, optional
        Step in the columns

    Returns
    -------
    Displays the DataFrame with the widget
    """
    @interact(last_row=IntSlider(min=min(num_rows, df.shape[0]),
                                 max=df.shape[0],
                                 step=step_rows,
                                 description='rows',
                                 readout=False,
                                 disabled=False,
                                 continuous_update=True,
                                 orientation='horizontal',
                                 slider_color='purple'),
              last_column=IntSlider(min=min(num_columns, df.shape[1]),
                                    max=df.shape[1],
                                    step=step_columns,
                                    description='columns',
                                    readout=False,
                                    disabled=False,
                                    continuous_update=True,
                                    orientation='horizontal',
                                    slider_color='purple'))
    def _freeze_header(last_row, last_column):
        display(df.iloc[max(0, last_row-num_rows):last_row,
                        max(0, last_column-num_columns):last_column])
output = {}
list_trucs = []
errors_list=[]
i=0
zi=0
ai=0
for x in source.keys():
    cur_obj=""
    if type(source[x])is dict:
        for y in source[x].keys():
            if type(source[x][y])is dict:
                for z in source[x][y].keys():
                    if type(source[x][y][z])is dict:
                        for a in source[x][y][z].keys():
                            if type(source[x][y][z][a])is dict:
                                for b in source[x][y][z][a].keys():
                                    if type(source[x][y][z][a][b])is dict:
                                        for c in source[x][y][z][a][b].keys():
                                            if type(source[x][y][z][a][b][c])is dict:
                                                for d in source[x][y][z][a][b][c].keys():
                                                    if type(source[x][y][z][a][b][c][d])is dict:
                                                        i+=1
                                                        cur_obj=[x,y,z,a,b,c,d]
                                                        list_trucs.append(cur_obj)
                                                    #elif type(source[x][y][z][a][b][c][d])is list:
                                                    #    i+=1
                                                    #    if len(source[x][y][z][a][b][c][d])>=1:cur_obj=[x,y,z,a,source[x][y][z][a][b][c][0]]
                                                    #    else: cur_obj=[x,y,z,a,b,c,d]
                                                    #    #cur_obj=[x,y,z,a,b,c,d]
                                                    #    list_trucs.append(cur_obj)
                                                    else:
                                                        i+=1
                                                        cur_obj=[x,y,z,a,b,c,source[x][y][z][a][b][c][d]]
                                                        list_trucs.append(cur_obj)
                                            
                                            #elif type(source[x][y][z][a][b][c])is list:
                                            #    i+=1
                                            #    cur_obj=[x,y,z,a,b,c,source[x][y][z][a][b][c][0]]
                                            #    list_trucs.append(cur_obj)
                                            else:
                                                i+=1
                                                cur_obj=[x,y,z,a,b,c,source[x][y][z][a][b][c]]
                                                list_trucs.append(cur_obj)
                                    
                                    elif type(source[x][y][z][a][b])is list:
                                        i+=1
                                        cur_obj=[x,y,z,a,b,source[x][y][z][a][b][0],""]
                                        list_trucs.append(cur_obj)
                                    else:
                                        i+=1
                                        cur_obj=[x,y,z,a,b,source[x][y][z][a][b],""]
                                        list_trucs.append(cur_obj)
                            elif type(source[x][y][z][a])is list:
                                i+=1
                                #check pk pas possible sortir cette foutue liste
                                errors_list.append(source[x][y][z][a])
                                #
                                if len(source[x][y][z][a])>=1:cur_obj=[x,y,z,a,source[x][y][z][a][0],"",""]
                                else: cur_obj=[x,y,z,a,"","",""]
                                list_trucs.append(cur_obj)
                            else:
                                i+=1
                                cur_obj=[x,y,z,a,source[x][y][z][a],"",""]
                                list_trucs.append(cur_obj)
                    elif type(source[x][y][z])is list:
                        i+=1
                        if len(source[x][y][z])>=1:cur_obj=[x,y,z,source[x][y][z][0],"","",""]
                        else: cur_obj=[x,y,z,"","","",""]
                        list_trucs.append(cur_obj)
                    else:
                        i+=1
                        cur_obj=[x,y,z,source[x][y][z],"","",""]
                        list_trucs.append(cur_obj)
            elif type(source[x][y])is list:
                i+=1
                if len(source[x][y])>=1:cur_obj=[x,y,source[x][y][0],"","","",""]
                else: cur_obj=[x,y,"","","","",""]
                list_trucs.append(cur_obj)
            else:
                i+=1
                cur_obj=[x,y,source[x][y],"","","",""]
                list_trucs.append(cur_obj)
    elif type(source[x])is list:
                i+=1
                if len(source[x])>=1:cur_obj=[x,source[x][0],"","","","",""]
                else: cur_obj=[x,"","","","","",""]
                list_trucs.append(cur_obj)
    else:
        i+=1
        cur_obj=[x,source[x],"","","","",""]
        list_trucs.append(cur_obj)

#list_trucs.append(cur_obj)
print (i)

output=pandas.DataFrame(list_trucs)
#print(output)
#freeze_header(output)
filtercol = 0
filterval = ["country","state","provinces","pop"]
#output = output[output[filtercol].isin(filterval)]
cols =["level1","level2","level3","level4","level5","level6","level7"]
output.columns = cols
#query = 'level1 == "provinces"'
#query = '1 == 1'
#output = output.query(query)
freeze_header(output,num_rows=50)
