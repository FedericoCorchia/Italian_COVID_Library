import sys
import geopandas
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
    functions = [icl.get_admin_sites, icl.get_admin_sites_types, icl.get_eligible, icl.get_equip_contracts, icl.get_equip_contracts_payments, icl.get_istat_region_data, icl.get_national_trend, icl.get_over_80, icl.get_province_cases, icl.get_region_cases, icl.get_vaccine_admin, icl.get_vaccine_admin_summary, icl.get_vaccine_ages, icl.get_vaccine_deliveries, icl.get_vaccine_summary, icl.get_istat_region_data]
    for function in functions:
        try:
            function()
        except Exception as e:
            assert isinstance(e, icl_b.ItaCovidLibConnectionError)
            
def test_getter_functions_with_arguments_cannot_connect():
    # to be performed under no Internet connection.
    functions = [icl.get_national_trend, icl.get_region_cases, icl.get_province_cases]
    for function in functions:
        try:
            function(latest=True)
        except Exception as e:
            assert isinstance(e, icl_b.ItaCovidLibConnectionError)
    try:
        icl.get_istat_region_data(index="age_range")
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
            
def test_istat_region_data_ranging():
    try:
        istat_region_data = icl.get_istat_region_data()
        assert len(istat_region_data["1":"5"].index) != 5
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)

def test_admin_sites_ranging():
    try:
        admin_sites = icl.get_admin_sites()
        assert len(admin_sites["1":"5"].index) != 5
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
    
def test_admin_sites_types_ranging():
    try:
        admin_sites_types = icl.get_admin_sites_types()
        assert len(admin_sites_types["1":"5"].index) != 5
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
    
def test_vaccine_summary_ranging():
    try:
        vaccine_summary = icl.get_vaccine_summary()
        assert len(vaccine_summary["1":"5"].index) == 6
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
    
def test_over_80_ranging():
    try:
        over_80 = icl.get_over_80()
        assert len(over_80["1":"5"].index) == 4
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
        
def test_prepare_for_plotting_on_map_incompatibilities():
    try:
        equip_contracts = icl.get_equip_contracts()
        try:
            icl.prepare_for_plotting_on_map(equip_contracts, on="region")
        except Exception as e:
            assert isinstance(e, icl_b.ItaCovidLibKeyError)
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)

def test_prepare_for_plotting_on_map_incompatibilities_2():
    try:
        region_cases = icl.get_region_cases()
        try:
            icl.prepare_for_plotting_on_map(region_cases, on="province")
        except Exception as e:
            assert isinstance(e, icl_b.ItaCovidLibKeyError)
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
        
def test_prepare_for_plotting_on_map_output_is_geodataframe():
    try:
        region_cases_geodataframe = icl.prepare_for_plotting_on_map(source=icl.get_region_cases(), on="regions")
        assert isinstance(region_cases_geodataframe, geopandas.geodataframe.GeoDataFrame)
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
        
def test_tell_total_vaccinated_1():
    try:
        total_vaccinated_ever = icl.tell_total_vaccinated(1)
        vaccinated_first_group = icl.tell_total_vaccinated(1, stop_date="2020-10-01")
        vaccinated_second_group = icl.tell_total_vaccinated(1, start_date="2020-10-02", stop_date="2020-10-03")
        vaccinated_third_group = icl.tell_total_vaccinated(1, start_date="2020-10-04")
        assert total_vaccinated_ever == vaccinated_first_group+vaccinated_second_group+vaccinated_third_group
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
        
def test_tell_total_vaccinated_2():
    try:
        total_vaccinated_ever = icl.tell_total_vaccinated(2)
        vaccinated_first_group = icl.tell_total_vaccinated(2, stop_date="2020-10-01")
        vaccinated_second_group = icl.tell_total_vaccinated(2, start_date="2020-10-02", stop_date="2020-10-03")
        vaccinated_third_group = icl.tell_total_vaccinated(2, start_date="2020-10-04")
        assert total_vaccinated_ever == vaccinated_first_group+vaccinated_second_group+vaccinated_third_group
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
        
def test_tell_total_vaccinated_3():
    try:
        total_vaccinated_ever = icl.tell_total_vaccinated(3)
        vaccinated_first_group = icl.tell_total_vaccinated(3, stop_date="2020-10-01")
        vaccinated_second_group = icl.tell_total_vaccinated(3, start_date="2020-10-02", stop_date="2020-10-03")
        vaccinated_third_group = icl.tell_total_vaccinated(3, start_date="2020-10-04")
        assert total_vaccinated_ever == vaccinated_first_group+vaccinated_second_group+vaccinated_third_group
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)

def test_tell_manufacturer_delivered_doses_all():
    try:
        manufacturer="all"
        total_delivered_ever = icl.tell_manufacturer_delivered_doses(manufacturer)
        delivered_first_group = icl.tell_manufacturer_delivered_doses(manufacturer, stop_date="2020-10-01")
        delivered_second_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-02", stop_date="2020-10-03")
        delivered_third_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-04")
        assert total_delivered_ever == delivered_first_group+delivered_second_group+delivered_third_group
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
        
def test_tell_manufacturer_delivered_doses_pfizer():
    try:
        manufacturer="Pfizer/BioNTech"
        total_delivered_ever = icl.tell_manufacturer_delivered_doses(manufacturer)
        delivered_first_group = icl.tell_manufacturer_delivered_doses(manufacturer, stop_date="2020-10-01")
        delivered_second_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-02", stop_date="2020-10-03")
        delivered_third_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-04")
        assert total_delivered_ever == delivered_first_group+delivered_second_group+delivered_third_group
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
        
def test_tell_manufacturer_delivered_doses_moderna():
    try:
        manufacturer="Moderna"
        total_delivered_ever = icl.tell_manufacturer_delivered_doses(manufacturer)
        delivered_first_group = icl.tell_manufacturer_delivered_doses(manufacturer, stop_date="2020-10-01")
        delivered_second_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-02", stop_date="2020-10-03")
        delivered_third_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-04")
        assert total_delivered_ever == delivered_first_group+delivered_second_group+delivered_third_group
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
        
def test_tell_manufacturer_delivered_doses_astrazeneca():
    try:
        manufacturer="Vaxzevria (AstraZeneca)"
        total_delivered_ever = icl.tell_manufacturer_delivered_doses(manufacturer)
        delivered_first_group = icl.tell_manufacturer_delivered_doses(manufacturer, stop_date="2020-10-01")
        delivered_second_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-02", stop_date="2020-10-03")
        delivered_third_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-04")
        assert total_delivered_ever == delivered_first_group+delivered_second_group+delivered_third_group
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
        
def test_tell_manufacturer_delivered_doses_janssen():
    try:
        manufacturer="Janssen"
        total_delivered_ever = icl.tell_manufacturer_delivered_doses(manufacturer)
        delivered_first_group = icl.tell_manufacturer_delivered_doses(manufacturer, stop_date="2020-10-01")
        delivered_second_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-02", stop_date="2020-10-03")
        delivered_third_group = icl.tell_manufacturer_delivered_doses(manufacturer, start_date="2020-10-04")
        assert total_delivered_ever == delivered_first_group+delivered_second_group+delivered_third_group
    except Exception as e:
        assert isinstance(e, icl_b.ItaCovidLibConnectionError)
