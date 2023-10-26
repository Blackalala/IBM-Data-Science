import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
response = requests.get(url)

if response.status_code == 200:
    with open("spacex_launch_dash.csv", "wb") as file:
        file.write(response.content)
else:
    print("Failed to download the file.")
    
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/spacex_dash_app.py"
response = requests.get(url)

if response.status_code == 200:
    with open("spacex_dash_app.py", "wb") as file:
        file.write(response.content)
else:
    print("Failed to download the file.")
