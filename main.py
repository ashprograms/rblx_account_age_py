from datetime import datetime
import requests

targetUserId = input("UserID> ")
accountData = requests.get(f"https://users.roblox.com/v1/users/{targetUserId}")

if accountData.status_code != 200:
    print(f"Error: HTTP{accountData.status_code}\nIs the UserId correct?")
    exit()
else:
    createdDateTime = datetime.strptime(accountData.json()["created"], '%Y-%m-%dT%H:%M:%S.%fZ')
    print(f"Account created at (YYYY-MM-DD): {createdDateTime.year}-{createdDateTime.month}-{createdDateTime.day}")
    exit()
