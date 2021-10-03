import sys

sys.path.append("../itacovidlib")
import itacovidlib.icl_backend as icl_b, itacovidlib.icl_functions as icl

def test_no_Internet_connection():
    # to be performed under no Internet connection
    try:
        icl_b.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv")
    except icl_b.ItaCovidLibConnectionError:
        print("No Internet connection exception handled successfully.")

def test_no_Internet_connection_2():
    # to be performed under no Internet connection. Same test also applies logically to all other get_<resource_name>() functions, since they work in exactly the same way.
    try:
        icl.get_vaccine_ages()
    except icl_b.ItaCovidLibConnectionError:
        print("No Internet connection exception handled successfully.")
