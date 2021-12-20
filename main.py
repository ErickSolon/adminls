import requests
import sys

try:
    header = {
    "User-Agent": ":)"
    }

    url = sys.argv[1]
    wordlist = sys.argv[2]

    with open(wordlist, "r") as pasta:
        pasta_url = pasta.readlines()

        for x in pasta_url:
            filtro_url = url + x.replace(" ", "").replace("\n", "")
            site_admin_login = requests.get(url=filtro_url, headers=header)

            if site_admin_login.ok:
                print(f"{filtro_url} -> {site_admin_login.status_code}")
            else:
                pass

except Exception as e:
    print("Erro: ", e)
    print("Modo de usar: python3 main.py http(s)://www.teste.com/pasta_do_site/ wordlist.txt")
