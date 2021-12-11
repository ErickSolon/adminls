import requests

url = "http://testphp.vulnweb.com"
pasta_url = None

with open("adminlogin.txt", "r") as pasta:
    pasta_url = pasta.readlines()

    for x in pasta_url:
        filtro_url = url + x.replace(" ", "").replace("\n", "")
        site_admin_login = requests.get(url=filtro_url)

        if site_admin_login.ok:
            print(f"{filtro_url} -> {site_admin_login.status_code}")
