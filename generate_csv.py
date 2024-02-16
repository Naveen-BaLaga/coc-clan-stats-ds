from helpers.data_helpers import *
import json
import csv

file_path = 'output.json'
base_url = 'http://127.0.0.1:5000'
clan_id = '2YG89L2JU'

# Run the below code only if you want to pull the clan data from the API
'''

clan_data = get_clan_data(base_url, clan_id)

if clan_data is not None:
    print("API call successful!")
    #print(clan_data)
else:
    print("API call failed.")

#print(clan_data.data)

with open(file_path, 'w') as json_file:
    json.dump(clan_data, json_file, indent=2)

print(f"Data successfully written to {file_path}")
'''

# Code for loading players' tags from the clan data
try:
    # Open the JSON file and load its content as a dictionary
    with open(file_path, 'r') as json_file:
        loaded_data = json.load(json_file)

    print("Data loaded successfully as a dictionary:")
    #print(loaded_data)

except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
    
members = loaded_data["data"]["memberList"]
list_of_tags = []
for member in members:
    list_of_tags.append(member['tag'][1:])
print(list_of_tags)

# Run the below code only if you want to pull the players' data from the API
'''
for tag in list_of_tags:
    player_data = get_player_data(base_url, tag)
    if player_data is not None:
        print("API call successful!")
        print(player_data)
    else:
        print("API call failed.")
    player_file_path = tag+'.json'
    with open(player_file_path, 'w') as json_file:
        json.dump(player_data, json_file, indent=2)

    print(f"Data successfully written to {player_file_path}")
'''

# Code for writing full players' data to CSV

full_col_names = [
    "Name", "Role", "Highest Gold Storage Level", "Stars in Campaign Map",
    "Current Town Hall Level", "Total Obstacles Removed", "Unlock Dragon in the Barracks",
    "Total Gold Looted", "Total Elixir Looted", "Trophy Record", "Current Clan Castle Level",
    "Total Wall Destroyed", "Total Town Halls Destroyed", "Total Builder's Huts Destroyed",
    'Total Multiplayer Battles Won', "Total Defenses Won", "Total Capacity Donated",
    "Total Mortars Destroyed", "Total Dark Elixir Looted", "League All-Star", "Total X-Bows Destroyed",
    "Total Inferno Towers Destroyed", "Total Stars scored for clan in Clan War battles",
    "Total gold collected in Clan War bonuses", "Total Eagle Artilleries Destroyed",
    "Total Spell Capacity Donated", "Village Connected to Social Network",
    "Current Builder Hall Level", "Unlock Power P.E.K.K.A", "Total Builder Halls destroyed",
    "Builder Trophy record", "Total buildings geared up", "Rebuild Battle Machine",
    "Total Clan Games points", "Slay the Giant Dragon", "Total Stars scored for the clan in Clan War League battles",
    "Connect account to Supercell ID", "Total Season Challenges points", "Total Scattershots Destroyed",
    "Weaponized Town Halls Destroyed", "Total Weaponized Builder's Huts Destroyed",
    "Total Times Super Troops boosted", "Total Siege Machines Donated", "Total Capital Gold Looted",
    "Total Capital Gold Contributed", "Total Spell Towers Destroyed", "Total Monoliths Destroyed",
    "Defeat M.O.M.M.A", "Attack Wins in Season", "Best Builder Base Trophies", "Best Trophies",
    "Builder Base League", "Builder Base Trophies", "Builder Hall Level", "Clan Capital Contributions",
    "Defense Wins", "Donations", "Donations Received", "Experience Level",
    "Trophies", "War Stars"
]
full_csv_file_path = 'full_players_data_from_clan.csv'

# Write data to CSV file
with open(full_csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
        
    # Write column names to the CSV file
    csv_writer.writerow(full_col_names)

        
    for tag in list_of_tags:
        with open(tag+'.json', 'r') as json_file:
            player_data_json = json.load(json_file)
        pd = player_data_json["data"]
        row_data = [
        pd['name'], pd['role'], pd['achievements'][0]['value'],
        pd['achievements'][1]['value'], pd['achievements'][2]['value'],
        pd['achievements'][3]['value'], pd['achievements'][4]['value'], pd['achievements'][5]['value'],
        pd['achievements'][6]['value'], pd['achievements'][7]['value'],
        pd['achievements'][8]['value'], pd['achievements'][9]['value'],
        pd['achievements'][10]['value'],
        pd['achievements'][11]['value'], pd['achievements'][12]['value'],
        pd['achievements'][13]['value'], pd['achievements'][14]['value'], pd['achievements'][15]['value'],
        pd['achievements'][16]['value'], pd['achievements'][17]['value'],
        pd['achievements'][18]['value'], pd['achievements'][19]['value'],
        pd['achievements'][20]['value'],
        pd['achievements'][21]['value'], pd['achievements'][22]['value'],
        pd['achievements'][23]['value'], pd['achievements'][24]['value'], pd['achievements'][25]['value'],
        pd['achievements'][26]['value'], pd['achievements'][27]['value'],
        pd['achievements'][28]['value'], pd['achievements'][29]['value'],
        pd['achievements'][30]['value'],
        pd['achievements'][31]['value'], pd['achievements'][32]['value'],
        pd['achievements'][33]['value'], pd['achievements'][34]['value'], pd['achievements'][35]['value'],
        pd['achievements'][36]['value'], pd['achievements'][37]['value'],
        pd['achievements'][38]['value'], pd['achievements'][39]['value'],
        pd['achievements'][40]['value'],
        pd['achievements'][41]['value'], pd['achievements'][42]['value'],
        pd['achievements'][43]['value'], pd['achievements'][44]['value'], pd['achievements'][45]['value'],
        pd['attackWins'], pd['bestBuilderBaseTrophies'], pd['bestTrophies'],
        pd['builderBaseLeague']['name'], pd['builderBaseTrophies'],
        pd['builderHallLevel'], pd['clanCapitalContributions'], pd['defenseWins'],
        pd['donations'], pd['donationsReceived'], pd['expLevel'], pd['trophies'],
        pd['warStars']
        ]
        csv_writer.writerow(row_data)
    print(f"Data successfully written to {full_csv_file_path}")


# Code for iterating through clan members' limited data
'''
for member in members:
    row_data = [
        member['name'], member['builderBaseLeague']['name'], 
        member['clanRank'], member['donations'], member['donationsReceived'],
        member['expLevel'], member['league']['name'], member['role'],
        member['tag'], member['townHallLevel'], member['trophies'], member['previousClanRank']
        ]
    print(row_data)
'''

# # Code for writing clan members' limited data to CSV
'''
try:
    # Specify the CSV file path
    csv_file_path = 'players_data_from_clan.csv'
    col_names = [
    "Name", "Builder Base League", "Clan Rank"
    , "Donations", "Donations Received", "Experience Level", "League",
    "Role", "Tag", "Town Hall Level", "Trophies", "Previous Clan Rank"
    ]
    # Write data to CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write column names to the CSV file
        csv_writer.writerow(col_names)

        # Write each member's data as a row to the CSV file
        for member in members:
            row_data = [
                member['name'], member['builderBaseLeague']['name'],
                member['clanRank'], member['donations'], member['donationsReceived'],
                member['expLevel'], member['league']['name'], member['role'],
                member['tag'], member['townHallLevel'], member['trophies'], member['previousClanRank']
            ]
            csv_writer.writerow(row_data)

    print(f"Data successfully written to {csv_file_path}")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

'''