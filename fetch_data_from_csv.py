'''
TODO
Use the CSV to get data. For instance, 
players with the Highest Multiplayer Battles Won.
Interact in a separate file to calculate this from the CSV.
Once you have your list, prepare a JSON object with it.

Sample CSV data
Name,Role,Highest Gold Storage Level,Stars in Campaign Map,Current Town Hall Level,Total Obstacles Removed,Unlock Dragon in the Barracks,Total Gold Looted,Total Elixir Looted,Trophy Record,Current Clan Castle Level,Total Wall Destroyed,Total Town Halls Destroyed,Total Builder's Huts Destroyed,Total Multiplayer Battles Won,Total Defenses Won,Total Capacity Donated,Total Mortars Destroyed,Total Dark Elixir Looted,League All-Star,Total X-Bows Destroyed,Total Inferno Towers Destroyed,Total Stars scored for clan in Clan War battles,Total gold collected in Clan War bonuses,Total Eagle Artilleries Destroyed,Total Spell Capacity Donated,Village Connected to Social Network,Current Builder Hall Level,Unlock Power P.E.K.K.A,Total Builder Halls destroyed,Builder Trophy record,Total buildings geared up,Rebuild Battle Machine,Total Clan Games points,Slay the Giant Dragon,Total Stars scored for the clan in Clan War League battles,Connect account to Supercell ID,Total Season Challenges points,Total Scattershots Destroyed,Weaponized Town Halls Destroyed,Total Weaponized Builder's Huts Destroyed,Total Times Super Troops boosted,Total Siege Machines Donated,Total Capital Gold Looted,Total Capital Gold Contributed,Total Spell Towers Destroyed,Total Monoliths Destroyed,Defeat M.O.M.M.A,Attack Wins in Season,Best Builder Base Trophies,Best Trophies,Builder Base League,Builder Base Trophies,Builder Hall Level,Clan Capital Contributions,Defense Wins,Donations,Donations Received,Experience Level,Trophies,War Stars
king of kings,leader,17,269,16,5903,1,2000000000,2000000000,5872,11,91782,7753,38494,10342,1161,260943,31690,43887247,22,20994,12159,2191,2000000000,4179,5763,0,9,1,3376,4203,3,1,205040,11,755,0,149900,5082,3763,10997,173,3171,1741514,2230113,2473,1231,3,85,4203,5872,Steel League I,3651,9,2230113,4,78,2224,241,5373,2191
zoro,coLeader,17,226,16,6016,1,2000000000,2000000000,5375,11,61343,5045,19622,7412,1829,319181,10204,21898198,22,5566,3366,1284,1152901071,1394,11414,0,10,1,6861,5127,3,1,117700,5,455,0,131440,1478,1784,2051,222,1913,1622610,2035525,568,260,0,73,5127,5375,Platinum League II,4777,10,2035525,14,410,5112,240,5228,1284
YourExBf,coLeader,17,232,16,8658,1,2000000000,2000000000,5613,11,114224,7924,28360,9235,1457,215060,21561,34616656,22,12132,6171,1808,1732600017,2321,6144,0,10,1,1981,4030,3,1,154885,2,534,0,125580,2583,4097,6802,194,1748,1468725,1881819,1976,985,2,34,4030,5613,Iron League II,2956,10,1881819,1,0,555,233,4941,1808
'''

import csv
from helpers.db_helpers import update_total_multiplayer_battles_won

def process_csv_and_update_db(file_path):
    # Read CSV file
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Extract Name and Total Multiplayer Battles Won
    player_data = [{"Name": row["Name"], "Total Multiplayer Battles Won": int(row["Total Multiplayer Battles Won"])} for row in data]

    # Sort data by Total Multiplayer Battles Won in descending order
    player_data.sort(key=lambda x: x["Total Multiplayer Battles Won"], reverse=True)

    # Generate JSON
    json_data = {
        "Table Name": "Highest Multiplayer Battles Won",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Multiplayer Battles Won": player["Total Multiplayer Battles Won"],
            "Previous Rank": "-"
        } for i, player in enumerate(player_data)]
    }

    #print(json_data)
    
    # Call the update function with the generated JSON data
    update_total_multiplayer_battles_won(json_data)

# Call the function with the CSV file path
process_csv_and_update_db('full_players_data_from_clan.csv')

