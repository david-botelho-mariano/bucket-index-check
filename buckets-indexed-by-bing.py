import requests
import time

api_key = ""
file_path = "buckets.txt"

def check_bing_indexed(bucket_name):
    endpoint = "https://api.bing.microsoft.com/v7.0/search"
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }
    params = {
        "q": f"site:s3.amazonaws.com/{bucket_name}/ | site:{bucket_name}.s3.amazonaws.com",
    }
    response = requests.get(endpoint, headers=headers, params=params)
    #print(response.text)
    data = response.json()

    time.sleep(5)

    if data.get("webPages", {}).get("value"):
      total_matches = data["webPages"]["totalEstimatedMatches"]
      #print("total_matches", total_matches)
      print(f"[WARNING]'{bucket_name}' has been indexed {total_matches} times by bing.")

    else:
      print(f"'{bucket_name}' has not been indexed by Bing.")

# Read URLs from the file
with open(file_path, 'r') as file:
    buckets_names = [line.strip() for line in file if line.strip()]

# Check each URL
for bucket_name in buckets_names:
  check_bing_indexed(bucket_name.split(" ")[-1])
