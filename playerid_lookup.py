import csv
import os.path
import urllib.request

def download_playeridmap():
    playeridmap = urllib.request.urlopen("https://www.smartfantasybaseball.com/PLAYERIDMAPCSV")
    with open("Player_ID_Map.csv","wb") as output:
        output.write(playeridmap.read())

class playerid_class:
    def __init__(self, line):
        self.player_id = line["IDPLAYER"]
        
        self.birth_date = line["BIRTHDATE"]
        self.full_name = line["PLAYERNAME"]
        self.first_name: line["FIRSTNAME"]
        self.last_name = line["LASTNAME"]

        self.bats = line["BATS"]
        self.throws = line["THROWS"]
        
        self.fangraphs_id = line["IDFANGRAPHS"]
        self.mlb_id = line["MLBID"]
        self.cbs_id = line["CBSID"]
        self.retro_id = line["RETROID"]
        self.baseball_reference_id = line["BREFID"]
        self.nfbc_id = line["NFBCID"]
        self.espn_id = line["ESPNID"]
        self.davenport_id = line["DAVENPORTID"]
        self.baseball_prospectus_id = line["BPID"]
        self.yahoo_id = line["YAHOOID"]
        self.rotowire_id = line["ROTOWIREID"]
        self.fanduel_id = line["FANDUELID"]
        self.ottoneu_id = line["OTTONEUID"]
        self.baseball_hq_id = line["HQID"]
        self.fantrax_id = line["FANTRAXID"]

    def __repr__(self):
        return self.player_id

    def __str__(self):
        return self.player_id

def playerid_lookup(
    player_id = None, full_name = None, birth_date = None,
    first_name = None, last_name = None, fangraphs_id = None,
    mlb_id = None, cbs_id = None, retro_id = None,
    baseball_reference_id = None, nfbc_id = None, espn_id = None,
    davenport_id = None, baseball_prospectus_id = None, yahoo_id = None,
    bats = None, throws = None, rotowire_id = None, fanduel_id = None,
    ottoneu_id = None, baseball_hq_id = None, fantrax_id = None
    ):

    if not os.path.isfile("Player_Id_Map.csv"):
        download_playeridmap()
    
    local = locals()

    args = [item for item in local if local[item] is not None]

    if args == []:
        return None
    
    with open("Player_ID_Map.csv", encoding = "utf8") as csv_file:
        playeridmap = csv.DictReader(csv_file, delimiter=",")

        col = {
            "player_id": "IDPLAYER",
            "full_name": "PLAYERNAME",
            "birth_date": "BIRTHDATE",
            "first_name": "FIRSTNAME",
            "last_name": "LASTNAME",
            "team": "TEAM", #this and many other categories are not updated enough to be useful
            "league": "LG",
            "position": "POS",
            "fangraphs_id": "IDFANGRAPHS",
            "fangraphs_name": "FANGRAPHSNAME",
            "mlb_id": "MLBID",
            "mlb_name": "MLBNAME",
            "cbs_id": "CBSID",
            "cbs_name": "CBSNAME",
            "retro_id": "RETROID",
            "baseball_reference_id": "BREFID",
            "nfbc_id": "NFBCID",
            "nfbc_name": "NFBCNAME",
            "espn_id": "ESPNID",
            "espn_name": "ESPNNAME",
            "kffl_name": "KFFLNAME",
            "davenport_id": "DAVENPORTID",
            "baseball_prospectus_id": "BPID",
            "yahoo_id": "YAHOOID",
            "yahoo_name": "YAHOONAME",
            "masterball_name": "MSTRBLLNAME",
            "bats": "BATS",
            "throws": "THROWS",
            "fantasy_pros_name": "FANTPROSNAME",
            "last_first": "LASTCOMMAFIRST",
            "rotowire_id": "ROTOWIREID",
            "fanduel_name": "FANDUELNAME",
            "fanduel_id": "FANDUELID",
            "draft_kings_name": "DRAFTKINGSNAME",
            "ottoneu_id": "OTTONEUID",
            "baseball_hq_id": "HQID",
            "razzball_name": "RAZZBALLNAME",
            "fantrax_id": "FANTRAXID",
            "fantrax_name": "FANTRAXNAME",
            "rotowire_name": "ROTOWIRENAME",
            }

        matches = []
        
        for line in playeridmap:
            match_number = len(args)
            
            for arg in args:
                if line[col[arg]] == local[arg]:
                    match_number -= 1
                    if match_number == 0:
                        matches.append(playerid_class(line))
        
        return matches
