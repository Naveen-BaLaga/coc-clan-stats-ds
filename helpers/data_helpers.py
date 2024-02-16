import requests

def get_clan_data(base_url, clan_id):
    api_endpoint = f"{base_url}/get-clan"
    
    # Set up parameters for the API call
    params = {'clan-id': clan_id}
    
    try:
        # Make the HTTP GET request
        response = requests.get(api_endpoint, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the JSON response data
            return response.json()
        else:
            # Return null for unsuccessful requests
            return None
    except Exception as e:
        # Handle any exceptions, e.g., network errors
        print(f"Error: {e}")
        return None

def get_player_data(base_url, player_id):
    api_endpoint = f"{base_url}/get-player"
    
    # Set up parameters for the API call
    params = {'player-id': player_id}
    
    try:
        # Make the HTTP GET request
        response = requests.get(api_endpoint, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the JSON response data
            return response.json()
        else:
            # Return null for unsuccessful requests
            return None
    except Exception as e:
        # Handle any exceptions, e.g., network errors
        print(f"Error: {e}")
        return None
'''
# Example usage:
base_url = "https://example-api.com"
clan_id = "123456"
clan_data = get_clan_data(base_url, clan_id)

if clan_data is not None:
    print("API call successful!")
    print(clan_data)
else:
    print("API call failed.")
'''