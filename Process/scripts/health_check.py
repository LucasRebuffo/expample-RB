import requests

basePath = "{gblBaseAPIPath}"

url = f"{basePath}/api/ping"

headers = {"Authorization": "Bearer {gblAccesTokenAPI}"}

try:
    response = requests.get(url, timeout=5, headers=headers)
    if response.status_code == 200:
        print("Health check OK:", response.json())
        print("Status:", response.json().get("status"))
        print("Message:", response.json().get("message"))
        if response.json().get("status") == "ok":
            SetVar("loc005Excepcion", False)
            SetVar("gblHelthCheck", True)
        else:
            SetVar("loc005Excepcion", "Health check failed")
            SetVar("gblHelthCheck", False)
    else:
        print(
            f"Health check failed with status {response.status_code}: {response.text}"
        )
        SetVar(
            "loc005Excepcion", f"Health check failed with status {response.status_code}"
        )
        SetVar("gblHelthCheck", False)
        
except requests.RequestException as e:
    print("Health check error:", e)
    SetVar("loc005Excepcion", str(e))
    SetVar("gblHelthCheck", False)
