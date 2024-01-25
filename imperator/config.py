#partie en cours à analyser
#impacte les dossiers de sauvegarde, les noms de fichier, etc

current_game="mp_rome_grand_camp"

# is_multiplayer=False
is_multiplayer=True


jeu_path={"imp":{"input":"../Imperator/save games/","output":"D:/python/Imperator/","ext":".rome"},
          "ck":{"input":"../Crusader Kings III/save games/","output":"D:/python/Crusader Kings III/","ext":".rome"},
          "eu":{"input":"../Europa Universalis IV/save games/","output":"D:/python/Europa Universalis IV/","ext":".rome"},
          "vic":{"input":"../Victoria 3/save games/","output":"D:/python/Victoria 3/","ext":".rome"},
          "hoi":{"input":"../Hearts of Iron IV/save games/","output":"D:/python/Hearts of Iron IV/","ext":".rome"}}
#poll time in seconds

pollTime=60*10
jeu = "imp"

pays="rome"
# keyword = "test"
keyword="grand_camp"

code_multi=["","mp_"]
direct_extract=False