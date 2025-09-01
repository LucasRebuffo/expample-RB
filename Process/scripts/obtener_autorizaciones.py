import requests

basePath = "{gblBaseAPIPath}"

# parametros a pasar
id_autorizacion = "{gblIDAutorizacion}"

# Si hay Id de autorizacion en los query params se manda solo ese, sino se manda cuit, dni y fecha
url = f"{basePath}/api/autorizaciones/{id_autorizacion}"
print(f"URL de la API: {url}")


headers = {"Authorization": "Bearer {gblAccesTokenAPI}"}
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Autorizaciones encontradas:")
        print(response.json())
        SetVar("loc005RespuestaAutorizaciones", response.json())
        SetVar("loc005Excepcion", False)
    elif response.status_code == 400:
        print("Error 400: Faltan parámetros obligatorios.")
        SetVar("loc005RespuestaAutorizaciones", None)
        SetVar("loc005Excepcion", "Faltan parámetros obligatorios.")
    elif response.status_code == 404:
        print("Error 404: No se encontraron autorizaciones.")
        SetVar("loc005RespuestaAutorizaciones", None)
        SetVar("loc005Excepcion", "No se encontraron autorizaciones.")
    elif response.status_code == 500:
        print("Error 500: Error en el servidor.")
        SetVar("loc005RespuestaAutorizaciones", None)
        SetVar("loc005Excepcion", "Error en el servidor.")
    else:
        print(f"Error {response.status_code}: {response.text}")

except requests.RequestException as e:
    print(f"Error de conexión: {e}")
    SetVar("loc005RespuestaAutorizaciones", None)
    SetVar("loc005Excepcion", str(e))
