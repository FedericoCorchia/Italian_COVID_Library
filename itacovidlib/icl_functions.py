import pandas as pd
import requests
import io

class COVIDDataSource:
    def __init__(self, url: str):
        self.url = url


vaccine_age_ranges_summary_latest = COVIDDataSource("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv")
vaccine_deliveries_latest = COVIDDataSource("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/consegne-vaccini-latest.csv")
eligible = COVIDDataSource("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea.csv")
administration_sites_latest = COVIDDataSource("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-latest.csv")
administration_sites_kinds = COVIDDataSource("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-tipologia.csv")
vaccine_administration_latest = COVIDDataSource("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv")
vaccine_administration_summary_latest = COVIDDataSource("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv")
vaccine_summary_latest = COVIDDataSource("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv")
national_trend = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
national_trend_latest = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-latest.csv")
equipment_contracts = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-contratti-dpc-forniture.csv")
equipment_contracts_payments = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-pagamenti-contratti-dpc-forniture.csv")
province_cases = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv")
province_cases_latest = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province-latest.csv")
region_cases_latest = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv")
region_cases = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")
over80 = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-over80.csv")
istat_region_data = COVIDDataSource("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv")

def get(covid_data_source):
    """Docstring to be added when function is completed."""
    try:
        downloaded_content = requests.get(covid_data_source.url).content
        dataframe = pd.read_csv(io.StringIO(downloaded_content.decode('utf-8')))
        return dataframe
    except requests.exceptions.MissingSchema:
        print("Unvalid URL provided")
    except requests.exceptions.ConnectionError:
        print("Failure to connect to URL")



