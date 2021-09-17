import pandas as pd
import requests
import io


def get_vaccine_ages_sum_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv")

def get_vaccine_deliveries_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/consegne-vaccini-latest.csv")

def get_eligible():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea.csv")

def get_admin_sites_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-latest.csv")

def get_admin_sites_kinds():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-tipologia.csv")

def get_vaccine_admin_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv")

def get_vaccine_admin_sum_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv")

def get_vaccine_sum_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv")

def get_national_trend():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")

def get_national_trend_latest():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-latest.csv")

def get_equip_contracts():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-contratti-dpc-forniture.csv")

def get_equip_contracts_payments():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-pagamenti-contratti-dpc-forniture.csv")

def get_province_cases():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv")

def get_province_cases_latest():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province-latest.csv")

def get_region_cases_latest():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv")

def get_region_cases():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")

def get_over_80():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-over80.csv")

def get_istat_region_data():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv")



def get(url):
    """Docstring to be added when function is completed."""
    try:
        downloaded_content = requests.get(url).content
        dataframe = pd.read_csv(io.StringIO(downloaded_content.decode('utf-8')))
        return dataframe
    except requests.exceptions.MissingSchema:
        print("ERROR Unvalid URL provided")
    except requests.exceptions.ConnectionError:
        print("ERROR Connection failure")



