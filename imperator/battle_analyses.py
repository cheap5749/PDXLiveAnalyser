import pandas
    
def extract(source):

    wars=source["diplomacy"]["database"]
    
    result=[]

    for war_id in wars.keys():
        #we save the current war (wars[x])
        war=wars[war_id]
        #reset battle count for wars[x]
        battle_count=0
        #loop in battles
        for battles in war.keys():
            if "battle" in battles :
            #and war_id=="1409"
                battle=war[battles]
                #now fetching base data (lvl 1 in battle)
                battle_count=battle_count+1
                battle_id=str(war_id)+"/"+str(battle_count)
                
                location=battle["location"]
                bool_attack_win=battle["result"]
                date=battle["date"]
                #battle Leaders
                if "leader" in battle["defender"]:
                    def_leader=battle["defender"]["leader"]
                else:
                    def_leader="No leader"
                    
                if "leader" in battle["attacker"]:
                    atq_leader=battle["attacker"]["leader"]
                else:
                    atq_leader="No leader"
                #Collect popularity from battle (interesting for leaderboard)
                if "popularity_change" in battle["defender"]:
                    def_popularity_change=round(battle["defender"]["popularity_change"],2)
                else:
                    def_popularity_change=0
                    
                if "popularity_change" in battle["attacker"]:
                    atq_popularity_change=round(battle["attacker"]["popularity_change"],2)
                else:
                    atq_popularity_change=0
                #Now the hard bit: collect countries involved & list them                
                atq_stats=[]

                #LISTE DES BATAILLES, COTE ATTAQUANT
                for i in range(len(battle["attacker"]["countries"])):
                    #liste des attributs de la bataille, principalement quel pays et quelles troupes
                    atq_country=""
                    unit=""
                    count=0
                    losses=0
                    remaining=0
                    captured=0
                    for j in battle["attacker"]["countries"][i]:
                        if "country" in j:
                            atq_country=battle["attacker"]["countries"][i]["country"]
                            #print("ATQ: "+str(atq_country))
                        if "sub_unit" in j:
                            if "type" in battle["attacker"]["countries"][i][j]:
                                unit=battle["attacker"]["countries"][i][j]["type"]
                            if "count" in battle["attacker"]["countries"][i][j]:
                                count=count+battle["attacker"]["countries"][i][j]["count"]
                            if "losses" in battle["attacker"]["countries"][i][j]:
                                losses=losses+battle["attacker"]["countries"][i][j]["losses"]
                            if "remaining" in battle["attacker"]["countries"][i][j]:
                                remaining=remaining+battle["attacker"]["countries"][i][j]["remaining"]
                            if "captured" in battle["attacker"]["countries"][i][j]:
                                captured=captured+battle["attacker"]["countries"][i][j]["captured"]
                    result.append([atq_country,"atq",war_id,battle_count,location,date,bool_attack_win,atq_leader,atq_popularity_change,round(count,0),round(losses,0),round(remaining,0),round(captured,0)])
                
                def_stats=[]
                #LISTE DES BATAILLES, COTE DEFENSEUR
                for i in range(len(battle["defender"]["countries"])):
                    #liste des attributs de la bataille, principalement quel pays et quelles troupes
                    def_country=""
                    unit=""
                    count=0
                    losses=0
                    remaining=0
                    captured=0
                    for j in battle["defender"]["countries"][i]:
                        if "country" in j:
                            def_country=battle["defender"]["countries"][i]["country"]
                            #print("DEF: "+str(def_country))
                        if "sub_unit" in j:
                            if "type" in battle["defender"]["countries"][i][j]:
                                unit=battle["defender"]["countries"][i][j]["type"]
                            if "count" in battle["defender"]["countries"][i][j]:
                                count=count+battle["defender"]["countries"][i][j]["count"]
                            if "losses" in battle["defender"]["countries"][i][j]:
                                losses=losses+battle["defender"]["countries"][i][j]["losses"]
                            if "remaining" in battle["defender"]["countries"][i][j]:
                                remaining=remaining+battle["defender"]["countries"][i][j]["remaining"]
                            if "captured" in battle["defender"]["countries"][i][j]:
                                captured=captured+battle["defender"]["countries"][i][j]["captured"]
                                #debug
                            #print([round(count,0),round(losses,0),round(remaining,0),round(captured,0)])

                    result.append([def_country,"def",war_id,battle_count,location,date,not(bool_attack_win),def_leader,def_popularity_change,round(count,0),round(losses,0),round(remaining,0),round(captured,0)])

    output=pandas.DataFrame(result)
    output.columns = ["Country","Atq/def","War #","Battle #","Location","Date","Win?","Leader","Leader pop change","Engaged troop","Losses","Remaining","Captured"]

    return output
