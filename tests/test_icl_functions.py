import sys
from hypothesis import given
import hypothesis.strategies as st

sys.path.append("../itacovidlib")
import itacovidlib.icl_backend as icl_b, itacovidlib.icl_functions as icl

@given(fake_site_name=st.text(min_size=1, alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z","_","-"]))
def test_get_gets_fake_url(fake_site_name):
    try:
        icl_b._get("http://"+fake_site_name)
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)

def test_get_gets_correct_url_but_cannot_connect():
    # to be performed under no Internet connection
    links = ["https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv",
             "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/consegne-vaccini-latest.csv",
             "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea.csv",
             "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-latest.csv",
             "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-tipologia.csv",
             "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv",
             "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv",
             "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-latest.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-contratti-dpc-forniture.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-pagamenti-contratti-dpc-forniture.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province-latest.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-over80.csv",
             "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv"]
    for link in links:
        try:
            icl_b._get(link)
        except Exception as e:
            assert isinstance(e, icl_b.ItaCovidLibConnectionError)

def test_getter_functions_cannot_connect():
    # to be performed under no Internet connection.
    functions = [icl.get_admin_sites, icl.get_admin_sites_types, icl.get_eligible, icl.get_equip_contracts, icl.get_equip_contracts_payments, icl.get_istat_region_data, icl.get_national_trend, icl.get_over_80, icl.get_province_cases, icl.get_region_cases, icl.get_vaccine_admin, icl.get_vaccine_admin_summary, icl.get_vaccine_ages, icl.get_vaccine_deliveries, icl.get_vaccine_summary]
    for function in functions:
        try:
            function()
        except Exception as e:
            assert isinstance(e, icl_b.ItaCovidLibConnectionError)
            

def test_istat_region_data_ranging():
    istat_region_data = icl.get_istat_region_data()
    assert len(istat_region_data[0:5].index) != 5

def test_admin_sites_ranging():
    admin_sites = icl.get_admin_sites()
    assert len(admin_sites[0:5].index) != 5
    
def test_admin_sites_types_ranging():
    admin_sites_types = icl.get_admin_sites_types()
    assert len(admin_sites_types[0:5].index) != 5
    
def test_vaccine_summary_ranging():
    vaccine_summary = icl.get_vaccine_summary()
    assert len(vaccine_summary[0:5].index) == 6
    
def test_over_80_ranging():
    over_80 = icl.get_over_80()
    assert len(over_80[0:5].index) == 4
    

