import requests

# Reemplaza estos valores con tus credenciales reales

client_id = "{gblAPIClientId}"
client_secret = "{gblAPIClientSecret}"
basePath = "{gblBaseAPIPath}"

url = f"{basePath}/api/oauth/token"

payload = {
    "client_id": client_id,
    "client_secret": client_secret,
}

response = requests.post(url, data=payload)
response.raise_for_status()  # Lanza un error si la peticion falla

data = response.json()
access_token = data.get("access_token")

print("Access Token:", access_token)
SetVar("gblAccesTokenAPI", access_token)

