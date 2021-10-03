import sys

sys.path.append("../itacovidlib")
import itacovidlib.icl_backend#, itacovidlib.icl_functions

def test_no_Internet_connection():
    # to be performed under no Internet connection
    try:
        itacovidlib.icl_backend.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv")
    except itacovidlib.icl_backend.ItaCovidLibConnectionError:
        print("No Internet connection exception handled successfully.")

#def test_no_Internet_connection_2():
    # to be performed under no Internet connection. Same test also applies logically to all other get_<resource_name>() functions, since they work in exactly the same way.
#    try:
#        itacovidlib.icl_functions.get_vaccine_ages()
#    except itacovidlib.icl_backend.ItaCovidLibConnectionError:
#        print("No Internet connection exception handled successfully.")
