import json
from helpers.data_helpers import get_current_war_data
from helpers.db_helpers import update_wars

# Define the base URL and clan ID
base_url = 'http://127.0.0.1:5000'
clan_id = '2YG89L2JU'
file_path = 'processed_clan_data.json'

# Call the get_current_war_data function
clan_data = get_current_war_data(base_url, clan_id)

if clan_data is not None:
    print("API call successful!")
    
    # Extract the relevant data and transform it
    processed_data = {
        "clan": {
            "attacks": clan_data['data']['clan'].get('attacks', 0),
            "clanLevel": clan_data['data']['clan'].get('clanLevel', 0),
            "destructionPercentage": clan_data['data']['clan'].get('destructionPercentage', 0),
            "tag": clan_data['data']['clan'].get('tag', 'Unknown'),
            "members": []
        },
        "opponent": {
            "attacks": clan_data['data']['opponent'].get('attacks', 0),
            "clanLevel": clan_data['data']['opponent'].get('clanLevel', 0),
            "destructionPercentage": clan_data['data']['opponent'].get('destructionPercentage', 0),
            "tag": clan_data['data']['opponent'].get('tag', 'Unknown'),
            "members": []
        },
        "preparationStartTime": clan_data['data'].get('preparationStartTime', ''),
        "startTime": clan_data['data'].get('startTime', ''),
        "state": clan_data['data'].get('state', ''),
        "teamSize": clan_data['data'].get('teamSize', 0),
        "attacks_list": []
    }

    # Process the members for both clan and opponent
    def process_members(members, is_opponent=False):
        processed_members = []
        for member in members:
            attacks_used = len(member.get('attacks', [])) if 'attacks' in member else 0
            processed_member = {
                "name": member.get('name', 'Unknown'),
                "tag": member.get('tag', 'Unknown'),
                "townhallLevel": member.get('townhallLevel', 0),
                "mapPosition": member.get('mapPosition', 0),
                "opponentAttacks": member.get('opponentAttacks', 0),
                "attacksUsed": attacks_used,
                "attacks": member.get('attacks', []),  # Keep attacks to process them later
                "bestOpponentAttack": member.get('bestOpponentAttack', {}),
                "total_final_stars": 0  # Initialize the final stars to 0
            }
            processed_members.append(processed_member)
        return processed_members

    # Process clan members
    processed_data["clan"]["members"] = process_members(clan_data['data']['clan']['members'])

    # Process opponent members
    processed_data["opponent"]["members"] = process_members(clan_data['data']['opponent']['members'], is_opponent=True)

    # Collect all attacks into a single list for sorting by order
    all_attacks = []
    
    def collect_attacks(members):
        for member in members:
            for attack in member.get('attacks', []):
                all_attacks.append({
                    "attackerTag": attack.get('attackerTag', 'Unknown'),
                    "defenderTag": attack.get('defenderTag', 'Unknown'),
                    "destructionPercentage": attack.get('destructionPercentage', 0),
                    "duration": attack.get('duration', 0),
                    "order": attack.get('order', 0),
                    "stars": attack.get('stars', 0)
                })

    # Collect attacks from clan and opponent members
    collect_attacks(processed_data["clan"]["members"])
    collect_attacks(processed_data["opponent"]["members"])

    # Sort the collected attacks by the "order" key
    processed_data["attacks_list"] = sorted(all_attacks, key=lambda x: x['order'])

    # Calculate total final stars for each attacker based on the defender's remaining stars
    defender_max_stars = {}

    for attack in processed_data["attacks_list"]:
        defender_tag = attack["defenderTag"]
        attacker_tag = attack["attackerTag"]
        attack_stars = attack["stars"]

        # Each defender can offer up to 3 stars, initialize defender's max stars if not present
        if defender_tag not in defender_max_stars:
            defender_max_stars[defender_tag] = 0

        # Calculate how many new stars this attacker actually earned
        if attack_stars < defender_max_stars[defender_tag]: 
            final_stars_for_attack = 0
        else:
            final_stars_for_attack = attack_stars - defender_max_stars[defender_tag]

        # Update the max stars earned against this defender
        defender_max_stars[defender_tag] = max(defender_max_stars[defender_tag], attack_stars)

        # Assign the final stars to the attacker
        attack["total_final_stars"] = final_stars_for_attack

        # Update the attacker's total final stars in clan or opponent members
        def update_attacker_stars(tag, final_stars, members_key):
            for member in processed_data[members_key]["members"]:
                if member["tag"] == tag:
                    member["total_final_stars"] += final_stars
                    break

        # Update for clan members
        update_attacker_stars(attacker_tag, final_stars_for_attack, "clan")

        # Update for opponent members
        update_attacker_stars(attacker_tag, final_stars_for_attack, "opponent")

    # Write the processed data to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(processed_data, json_file, indent=2)

    print(f"Data successfully written to {file_path}")

    # Pass the processed data to update_wars function
    opponent_tag = processed_data["opponent"].get('tag', None)

    if opponent_tag:
        update_wars(processed_data, opponent_tag)
        print(f"Wars data updated successfully with opponent tag: {opponent_tag}")
    else:
        print("Opponent tag not found in the processed data.")
else:
    print("API call failed.")
    
'''
import json
from helpers.data_helpers import get_current_war_data
from helpers.db_helpers import update_wars

# Define the base URL and clan ID
base_url = 'http://127.0.0.1:5000'
clan_id = '2YG89L2JU'
file_path = 'clan_war_data.json'

# Call the get_current_war_data function
clan_data = get_current_war_data(base_url, clan_id)

if clan_data is not None:
    print("API call successful!")
    # Write the data to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(clan_data, json_file, indent=2)

    print(f"Data successfully written to {file_path}")
    
    # Extract the opponent tag value
    opponent_tag = clan_data.get('data', {}).get('opponent', {}).get('tag', None)

    if opponent_tag:
        # Call the update_wars function with the json data and opponent tag
        update_wars(clan_data, opponent_tag)
        print(f"Wars data updated successfully with opponent tag: {opponent_tag}")
    else:
        print("Opponent tag not found in the response.")
else:
    print("API call failed.")
'''