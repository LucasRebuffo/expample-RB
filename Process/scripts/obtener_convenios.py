import requests


basePath = "{gblBaseAPIPath}"

cuit = "{gblCuit}"
fecha = "{gblFecha}"

url = f"{basePath}/api/prestaciones/{cuit}"

params = {
    "fecha": fecha,
}

headers = {"Authorization": "Bearer {gblAccesTokenAPI}"}
try:
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    SetVar("loc005RespuestaConvenios", response.json())
    SetVar("loc005Excepcion", False)
except requests.RequestException as e:
    print(f"Error al obtener prestaciones: {e}")
    SetVar("loc005RespuestaConvenios", None)
    SetVar("loc005Excepcion", str(e))
