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
from helpers.db_helpers import *

def process_csv_and_update_db(file_path):
    # Read CSV file
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Extract Name and Total Multiplayer Battles Won
    multiplayer_battles_won_data = [{"Name": row["Name"], "Total Multiplayer Battles Won": int(row["Total Multiplayer Battles Won"])} for row in data]

    # Sort data by Total Multiplayer Battles Won in descending order
    multiplayer_battles_won_data.sort(key=lambda x: x["Total Multiplayer Battles Won"], reverse=True)

    # Generate JSON
    multiplayer_battles_won_json_data = {
        "Table Name": "Highest Multiplayer Battles Won",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Multiplayer Battles Won": player["Total Multiplayer Battles Won"],
            "Previous Rank": "-"
        } for i, player in enumerate(multiplayer_battles_won_data)],
        "Table Header": "Total Multiplayer Battles Won"
    }
    
    # Update the Table
    update_table(multiplayer_battles_won_json_data, "Highest Multiplayer Battles Won")
    
    # Extract Name and Total Wall Destroyed
    total_wall_destroyed_data = [{"Name": row["Name"], "Total Wall Destroyed": int(row["Total Wall Destroyed"])} for row in data]

    # Sort data by Total Wall Destroyed in descending order
    total_wall_destroyed_data.sort(key=lambda x: x["Total Wall Destroyed"], reverse=True)
    
    #Generate JSON
    wall_destroyed_json_data = {
        "Table Name": "Highest Walls Destroyed",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Walls Destroyed": player["Total Wall Destroyed"],
            "Previous Rank": "-"
        } for i, player in enumerate(total_wall_destroyed_data)],
        "Table Header": "Total Walls Destroyed"
    }
    
    # Update the Table
    update_table(wall_destroyed_json_data, "Highest Walls Destroyed")
    
    total_obstacles_removed_data = [{"Name": row["Name"], "Total Obstacles Removed": int(row["Total Obstacles Removed"])} for row in data]
    
    total_obstacles_removed_data.sort(key=lambda x: x["Total Obstacles Removed"], reverse=True)
    
    total_obstacles_removed_json_data = {
        "Table Name": "Most Obstacles Removed",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Obstacles Removed": player["Total Obstacles Removed"],
            "Previous Rank": "-"
        } for i, player in enumerate(total_obstacles_removed_data)],
        "Table Header": "Total Obstacles Removed"
    }
    
    update_table(total_obstacles_removed_json_data, "Most Obstacles Removed")
    
    total_defenses_won_data = [{"Name": row["Name"], "Total Defenses Won": int(row["Total Defenses Won"])} for row in data]
    
    total_defenses_won_data.sort(key=lambda x: x["Total Defenses Won"], reverse=True)
    
    total_defenses_won_json_data = {
        "Table Name": "Most Defenses Won",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Defenses Won": player["Total Defenses Won"],
            "Previous Rank": "-"
        } for i, player in enumerate(total_defenses_won_data)],
        "Table Header": "Total Defenses Won"
    }
    
    update_table(total_defenses_won_json_data, "Most Defenses Won")
    
    total_capacity_donated_data = [{"Name": row["Name"], "Total Capacity Donated": int(row["Total Capacity Donated"])} for row in data]
    
    total_capacity_donated_data.sort(key=lambda x: x["Total Capacity Donated"], reverse=True)
    
    total_capacity_donated_json_data = {
        "Table Name": "Most Capacity Donated",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Capacity Donated": player["Total Capacity Donated"],
            "Previous Rank": "-"
        } for i, player in enumerate(total_capacity_donated_data)],
        "Table Header": "Total Capacity Donated"
    }
    
    update_table(total_capacity_donated_json_data, "Most Capacity Donated")
    
    total_stars_scored_for_clan_in_clan_war_battles_data = [{"Name": row["Name"], "Total Stars scored for clan in Clan War battles": int(row["Total Stars scored for clan in Clan War battles"])} for row in data]
    
    total_stars_scored_for_clan_in_clan_war_battles_data.sort(key=lambda x: x["Total Stars scored for clan in Clan War battles"], reverse=True)
    
    total_stars_scored_for_clan_in_clan_war_battles_json_data = {
        "Table Name": "Most Stars scored for clan in Clan War battles",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Stars scored for clan in Clan War battles": player["Total Stars scored for clan in Clan War battles"],
            "Previous Rank": "-"
        } for i, player in enumerate(total_stars_scored_for_clan_in_clan_war_battles_data)],
        "Table Header": "Total Stars scored for clan in Clan War battles"
    }
    
    update_table(total_stars_scored_for_clan_in_clan_war_battles_json_data, "Most Stars scored for clan in Clan War battles")
    
    total_stars_scored_for_the_clan_in_clan_war_league_battles_data = [{"Name": row["Name"], "Total Stars scored for the clan in Clan War League battles": int(row["Total Stars scored for the clan in Clan War League battles"])} for row in data]
    
    total_stars_scored_for_the_clan_in_clan_war_league_battles_data.sort(key=lambda x: x["Total Stars scored for the clan in Clan War League battles"], reverse=True)
    
    total_stars_scored_for_the_clan_in_clan_war_league_battles_json_data = {
        "Table Name": "Most Stars scored for the clan in Clan War League battles",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Stars scored for the clan in Clan War League battles": player["Total Stars scored for the clan in Clan War League battles"],
            "Previous Rank": "-"
        } for i, player in enumerate(total_stars_scored_for_the_clan_in_clan_war_league_battles_data)],
        "Table Header": "Total Stars scored for the clan in Clan War League battles"
    }
    
    update_table(total_stars_scored_for_the_clan_in_clan_war_league_battles_json_data, "Most Stars scored for the clan in Clan War League battles")
    
    weaponized_town_halls_destroyed_data = [{"Name": row["Name"], "Weaponized Town Halls Destroyed": int(row["Weaponized Town Halls Destroyed"])} for row in data]
    
    weaponized_town_halls_destroyed_data.sort(key=lambda x: x["Weaponized Town Halls Destroyed"], reverse=True)
    
    weaponized_town_halls_destroyed_json_data = {
        "Table Name": "Most Weaponized Town Halls Destroyed",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Weaponized Town Halls Destroyed": player["Weaponized Town Halls Destroyed"],
            "Previous Rank": "-"
        } for i, player in enumerate(weaponized_town_halls_destroyed_data)],
        "Table Header": "Weaponized Town Halls Destroyed"
    }
    
    update_table(weaponized_town_halls_destroyed_json_data, "Most Weaponized Town Halls Destroyed")
    
    total_times_super_troops_boosted_data = [{"Name": row["Name"], "Total Times Super Troops boosted": int(row["Total Times Super Troops boosted"])} for row in data]
    
    total_times_super_troops_boosted_data.sort(key=lambda x: x["Total Times Super Troops boosted"], reverse=True)
    
    total_times_super_troops_boosted_json_data = {
        "Table Name": "Most Times Super Troops boosted",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Times Super Troops boosted": player["Total Times Super Troops boosted"],
            "Previous Rank": "-"
        } for i, player in enumerate(total_times_super_troops_boosted_data)],
        "Table Header": "Total Times Super Troops boosted"
    }
    
    update_table(total_times_super_troops_boosted_json_data, "Most Times Super Troops boosted")
    
    total_monoliths_destroyed_data = [{"Name": row["Name"], "Total Monoliths Destroyed": int(row["Total Monoliths Destroyed"])} for row in data]
    
    total_monoliths_destroyed_data.sort(key=lambda x: x["Total Monoliths Destroyed"], reverse=True)
    
    total_monoliths_destroyed_json_data = {
        "Table Name": "Most Monoliths Destroyed",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Total Monoliths Destroyed": player["Total Monoliths Destroyed"],
            "Previous Rank": "-"
        } for i, player in enumerate(total_monoliths_destroyed_data)],
        "Table Header": "Total Monoliths Destroyed"
    }
    
    update_table(total_monoliths_destroyed_json_data, "Most Monoliths Destroyed")
    
    attack_wins_in_season_data = [{"Name": row["Name"], "Attack Wins in Season": int(row["Attack Wins in Season"])} for row in data]
    
    attack_wins_in_season_data.sort(key=lambda x: x["Attack Wins in Season"], reverse=True)
    
    attack_wins_in_season_json_data = {
        "Table Name": "Most Attack Wins in Season",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Attack Wins in Season": player["Attack Wins in Season"],
            "Previous Rank": "-"
        } for i, player in enumerate(attack_wins_in_season_data)],
        "Table Header": "Attack Wins in Season"
    }
    
    update_table(attack_wins_in_season_json_data, "Most Attack Wins in Season")
    
    best_trophies_data = [{"Name": row["Name"], "Best Trophies": int(row["Best Trophies"])} for row in data]
    
    best_trophies_data.sort(key=lambda x: x["Best Trophies"], reverse=True)
    
    best_trophies_json_data = {
        "Table Name": "Best Trophies",
        "Table Data": [{
            "Rank": i + 1,
            "Player Name": player["Name"],
            "Best Trophies": player["Best Trophies"],
            "Previous Rank": "-"
        } for i, player in enumerate(best_trophies_data)],
        "Table Header": "Best Trophies"
    }
    
    update_table(best_trophies_json_data, "Best Trophies")
    
    #print(multiplayer_battles_won_json_data)
    
    # Call the update function with the generated JSON data
    #update_total_multiplayer_battles_won(multiplayer_battles_won_json_data)
    #update_total_wall_destroyed(wall_destroyed_json_data)
    #update_total_obstacles_removed(total_obstacles_removed_json_data)
    

# Call the function with the CSV file path
process_csv_and_update_db('full_players_data_from_clan.csv')

