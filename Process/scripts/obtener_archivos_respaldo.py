import requests

basePath = "{gblBaseAPIPath}"

autorizacion_id = "{loc005AutorizacionId}"
token = "{gblAccesTokenAPI}"

url = f"{basePath}/api/autorizaciones/{autorizacion_id}/archivos-medicos"

headers = {"Authorization": "Bearer {gblAccesTokenAPI}"}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        SetVar("loc005RespuestaArchivos", response.json())
        Setvar("loc005Excepcion", False)
    elif response.status_code == 400:
        print("400 Bad Request: Faltan parámetros obligatorios")
        SetVar("loc005RespuestaArchivos", None)
        Setvar("loc005Excepcion", "Faltan parámetros obligatorios")
    elif response.status_code == 404:
        print("404 Not Found: No se encontraron autorizaciones o archivos")
        SetVar("loc005RespuestaArchivos", None)
        Setvar("loc005Excepcion", "No se encontraron autorizaciones o archivos")
    elif response.status_code == 500:
        print("500 Internal Server Error: Error en el servidor")
        SetVar("loc005RespuestaArchivos", None)
        Setvar("loc005Excepcion", "Error en el servidor")
    else:
        print(f"Error {response.status_code}: {response.text}")

except requests.RequestException as e:
    print(f"Error de conexión: {e}")
    SetVar("loc005RespuestaArchivos", None)
    Setvar("loc005Excepcion", str(e))
