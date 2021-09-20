import pandas as pd
import requests
import io

# ====================================================================================
# FOR ALL get_<resource_name>() FUNCTIONS
#
# .rename(columns={...}) translates column names (originally in Italian) into English.
# ====================================================================================

def get_vaccine_ages_summary_latest():
    """Returns dataframe about COVID-19 vaccine administrations per age group in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with requested data.
    
    Dataframe Columns
    -----------------
    age_group : str
        Age groups
    total : int
        Total of administered vaccines
    males : int
        Total of male persons to which vaccine has been administered
    females : int
        Total of female persons to which vaccine has been administered
    first_dose : int
        Number of first doses
    second_dose : int
        Number of second doses
    previously_infected : int
        Number of vaccine administrations to individuals infected between 3 and 6 months before, as such completing the vaccination cycle with a single dose
    last_update : str
        Date of last update"""
    
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv").rename(columns={"fascia_anagrafica":"age_group","totale":"total","sesso_maschile":"males","sesso_femminile":"females","prima_dose":"first_dose","seconda_dose":"second_dose","pregressa_infezione":"previously_infected","ultimo_aggiornamento":"last_update"})

def get_vaccine_deliveries_latest():
    """Returns dataframe about COVID-19 vaccine deliveries in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with requested data.
    
    Dataframe Columns
    -----------------
    region_code : str
        Code of delivery region
    manufacturer : str
        Vaccine manufacturer name
    date_of_delivery : datetime
        Date of delivery
    number_of_doses : int
        Number of delivered doses on date date_of_delivery
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    ISTAT_region_code : int
        ISTAT region code
    region : str
        Official region name"""
    
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/consegne-vaccini-latest.csv").rename(columns={"area":"region_code","fornitore":"manufacturer","data_consegna":"date_of_delivery","numero_dosi":"number_of_doses","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_eligible():
    """Returns dataframe about eligible persons for COVID-19 vaccine administration in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with requested data.
    
    Dataframe Columns
    -----------------
    region_code : str
        Code of delivery region
    region : str
        Official region name
    age_group : str
        Age group
    population : int
        Total population per given age group"""
    
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea.csv").rename(columns={"area":"region_code","nome_area":"region","fascia_anagrafica":"age_group","totale_popolazione":"population"})

def get_admin_sites_latest():
    """Returns dataframe about COVID-19 vaccine administrations points in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with requested data.
    
    Dataframe Columns
    -----------------
    region_code : str
        Region code
    province : str
        Province
    municipality : str
        Municipality
    place : str
        Name of place of administration
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    ISTAT_region_code : str
        ISTAT region code
    region : str
        Official region name"""
    
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-latest.csv").rename(columns={"area":"region_code","provincia":"province","comune":"municipality","presidio_ospedaliero":"place","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_admin_sites_types():
    """Returns dataframe on types of COVID-19 vaccine administration points in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
    Pandas dataframe with requested data.
    
    Dataframe Columns
    -----------------
    region_code : str
        Region code
    place : str
        Name of place of administration
    type : str
        Type of administration place: OSPEDALIERO (hospital) or TERRITORIALE (local)
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    ISTAT_region_code : str
        ISTAT region code
    region : str
        Official region name"""
    
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-tipologia.csv").rename(columns={"area":"region_code","denominazione_struttura":"place","tipologia":"type","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_vaccine_admin_latest():
    """Returns dataframe on COVID-19 vaccine administration in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    -------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with requested data.
    
    Dataframe Columns
    -----------------
    date : datetime
        Date of administration
    Manufacturer : str
        Vaccine manufacturer name
    region_code : str
        Region code
    age_group : str
        Age group
    males : int
        Number of male individuals who have been given the vaccine
    females : int
        Number of female individuals who have been given the vaccine
    first_dose : int
        Number of first doses
    second_dose : int
        Number of second doses
    previously_infected : int
        Number of vaccine administrations to individuals who have already been infected by COVID-19 between 3 and 6 months before and as such completing the vaccination cycle with just one dose
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    ISTAT_region_code : int
        ISTAT region code
    region : str
        Official region name
    
    See Also
    --------
    get_vaccine_admin_summary_latest : a concise version (summary) of this function"""
    
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv").rename(columns={"data_somministrazione":"date","fornitore":"manufacturer","area":"region_code","fascia_anagrafica":"age_group","sesso_maschile":"males","sesso_femminile":"females","prima_dose":"first_dose","seconda_dose":"second_dose","pregressa_infezione":"previously_infected","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_vaccine_admin_summary_latest():
    """Returns dataframe about COVID-19 vaccine administration in Italy (summary version)
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with requested data.
    
    Dataframe Columns
    -----------------
    date : datetime
        Date of administration
    region_code : str
        Region code
    total : int
        Total amount of doses
    males : int
        Number of male individuals who have been given the vaccine
    females : int
        Number of female individuals who have been given the vaccine
    first_dose : int
        Number of first doses
    second_dose : int
        Number of second doses
    previously_infected : int
        Number of vaccine administrations to individuals who have already been infected by COVID-19 between 3 and 6 months before and as such completing the vaccination cycle with just one dose
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    ISTAT_region_code : int
        ISTAT region code
    region : str
        Official region name
    
    See Also
    --------
    get_vaccine_admin_latest : a complete version of this function with more data"""
    
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv").rename(columns={"data_somministrazione":"date","area":"region_code","totale":"total","sesso_maschile":"males","sesso_femminile":"females","prima_dose":"first_dose","seconda_dose":"second_dose","pregressa_infezione":"previously_infected","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_vaccine_summary_latest():
    """Returns dataframe with a synthesis of COVID-19 vaccines deliveries and administrations in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with requested data.
    
    Dataframe Columns
    -----------------
    region_code : str
        Region code
    administered_doses : int
        Number of administered doses
    delivered_doses : int
        Number of delivered doses
    administration_percent : number
        Percentage of administered doses over delivered doses
    last_update : datetime
        Date and time of last update
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    ISTAT_region_code : int
        ISTAT region code
    region : str
        Official region name
    
    See Also
    --------
    get_vaccine_deliveries_latest : more info on COVID-19 vaccine deliveries
    get_vaccine_admin_summary_latest : more info on COVID-19 vaccine administrations (concise version)
    get_vaccine_admin_latest : more info on COVID-19 vaccine administrations (complete version)"""
    
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv").rename(columns={"area":"region_code","dosi_somministrate":"administered_doses","dosi_consegnate":"delivered_doses","percentuale_somministrazione":"administration_percent","ultimo_aggiornamento":"last_update","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_national_trend():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv").rename(columns={"data":"date","stato":"country","ricoverati_con_sintomi":"hospitalized_with_symptoms","terapia_intensiva":"intensive_care","totale_ospedalizzati":"hospitalized","isolamento_domiciliare":"isolation","totale_positivi":"cases","variazione_totale_positivi":"cases_variation","nuovi_positivi":"new_cases","dimessi_guariti":"recovered_released","deceduti":"deaths","casi_da_sospetto_diagnostico":"cases_from_clinical_suspects","casi_da_screening":"cases_from_screening","totale_casi":"cumulative_cases","tamponi":"swabs","casi_testati":"tested","note":"notes","ingressi_terapia_intensiva":"intensive_care_in","note_test":"test_notes","note_casi":"case_notes","totale_positivi_test_molecolare":"molecular_test_cases","totale_positivi_test_antigenico_rapido":"antigen_test_cases","tamponi_test_molecolare":"molecular_tests","tamponi_test_antigenico_rapido":"antigen_tests"})

def get_national_trend_latest():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-latest.csv").rename(columns={"data":"date","stato":"country","ricoverati_con_sintomi":"hospitalized_with_symptoms","terapia_intensiva":"intensive_care","totale_ospedalizzati":"hospitalized","isolamento_domiciliare":"isolation","totale_positivi":"cases","variazione_totale_positivi":"cases_variation","nuovi_positivi":"new_cases","dimessi_guariti":"recovered_released","deceduti":"deaths","casi_da_sospetto_diagnostico":"cases_from_clinical_suspects","casi_da_screening":"cases_from_screening","totale_casi":"cumulative_cases","tamponi":"swabs","casi_testati":"tested","note":"notes","ingressi_terapia_intensiva":"intensive_care_in","note_test":"test_notes","note_casi":"case_notes","totale_positivi_test_molecolare":"molecular_test_cases","totale_positivi_test_antigenico_rapido":"antigen_test_cases","tamponi_test_molecolare":"molecular_tests","tamponi_test_antigenico_rapido":"antigen_tests"})

def get_equip_contracts():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-contratti-dpc-forniture.csv").rename(columns={"fornitore":"manufacturer","stato_fornitore":"country","gruppo_articoli":"product_group","sottogruppo_articoli":"article_subgroup","categoria":"category","sottocategoria":"subcategory","tipologia_fornitura":"equipment_kind","fornitura":"equipment","protocollo_atto_negoziale":"negotiation_protocol","data_atto_negoziale":"negotiation_date","file_atto_negoziale":"negotiation_file","integrazione_rettifica":"errata","protocollo_integrazione_rettifica":"errata_protocol","data_integrazione_rettifica":"errata_date","file_integrazione_rettifica":"errata_file","tipologia_cig":"cig_type","cig":"cig","quantita":"quantity","prezzo_unitario":"unit_price","totale_articolo":"total_price","stato_contratto":"agreement_state","ceduti_commissario_straordinario":"ceded","note":"notes","data_aggiornamento":"update_date"})

def get_equip_contracts_payments():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-pagamenti-contratti-dpc-forniture.csv").rename(columns={"protocollo_atto_negoziale":"negotiation_protocol","totale_fornitura":"total_equipment","totale_pagato":"total_paid","pagato_donazioni":"donations","pagato_altri_fondi":"other_funds","fondo_pagamento":"payment_fund","ceduti_commissario_straordinario":"ceded","note":"notes","data_aggiornamento":"update_date"})

def get_province_cases():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv").rename(columns={"data":"date","stato":"country","codice_regione":"region_code","denominazione_regione":"region","codice_provincia":"province_code","denominazione_provincia":"province","sigla_provincia":"province_abbreviation","lat":"lat","long":"long","totale_casi":"cumulative_cases","note":"notes","codice_nuts_1":"NUTS1_code","codice_nuts_2":"NUTS2_code","codice_nuts_3":"NUTS3_code"})

def get_province_cases_latest():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province-latest.csv").rename(columns={"data":"date","stato":"country","codice_regione":"region_code","denominazione_regione":"region","codice_provincia":"province_code","denominazione_provincia":"province","sigla_provincia":"province_abbreviation","lat":"lat","long":"long","totale_casi":"cumulative_cases","note":"notes","codice_nuts_1":"NUTS1_code","codice_nuts_2":"NUTS2_code","codice_nuts_3":"NUTS3_code"})

def get_region_cases_latest():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv").rename(columns={"data":"date","stato":"country","codice_regione":"region_code","denominazione_regione":"region","ricoverati_con_sintomi":"hospitalized_with_symptoms","terapia_intensiva":"intensive_care","totale_ospedalizzati":"hospitalized","isolamento_domiciliare":"isolation","totale_positivi":"cases","variazione_totale_positivi":"cases_variation","nuovi_positivi":"new_cases","dimessi_guariti":"recovered_released","deceduti":"deaths","casi_da_sospetto_diagnostico":"cases_from_clinical_suspects","casi_da_screening":"cases_from_screening","totale_casi":"cumulative_cases","tamponi":"swabs","casi_testati":"tested","note":"notes","ingressi_terapia_intensiva":"intensive_care_in","note_test":"test_notes","note_casi":"case_notes","totale_positivi_test_molecolare":"molecular_test_cases","totale_positivi_test_antigenico_rapido":"antigen_test_cases","tamponi_test_molecolare":"molecular_tests","tamponi_test_antigenico_rapido":"antigen_tests","codice_nuts_1":"NUTS1_code","codice_nuts_2":"NUTS2_code"})

def get_region_cases():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv").rename(columns={"data":"date","stato":"country","codice_regione":"region_code","denominazione_regione":"region","ricoverati_con_sintomi":"hospitalized_with_symptoms","terapia_intensiva":"intensive_care","totale_ospedalizzati":"hospitalized","isolamento_domiciliare":"isolation","totale_positivi":"cases","variazione_totale_positivi":"cases_variation","nuovi_positivi":"new_cases","dimessi_guariti":"recovered_released","deceduti":"deaths","casi_da_sospetto_diagnostico":"cases_from_clinical_suspects","casi_da_screening":"cases_from_screening","totale_casi":"cumulative_cases","tamponi":"swabs","casi_testati":"tested","note":"notes","ingressi_terapia_intensiva":"intensive_care_in","note_test":"test_notes","note_casi":"case_notes","totale_positivi_test_molecolare":"molecular_test_cases","totale_positivi_test_antigenico_rapido":"antigen_test_cases","tamponi_test_molecolare":"molecular_tests","tamponi_test_antigenico_rapido":"antigen_tests","codice_nuts_1":"NUTS1_code","codice_nuts_2":"NUTS2_code"})

def get_over_80():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-over80.csv").rename(columns={"codice_regione":"region_code","codice_nuts_1":"NUTS1_code","descrizione_nuts_1":"NUTS1_description","codice_nuts_2":"NUTS2_description","denominazione_regione":"region","range_eta":"age_range","totale_genere_maschile":"males","totale_genere_femminile":"females","totale_generale":"total"})

def get_istat_region_data():
    return get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv").rename(columns={"codice_regione":"region_code","codice_nuts_1":"NUTS1_code","descrizione_nuts_1":"NUTS1_description","codice_nuts_2":"NUTS2_code","denominazione_regione":"region","sigla_regione":"region_abbreviation","latitudine_regione":"lat","longitudine_regione":"long","range_eta":"age_range","totale_genere_maschile":"males","totale_genere_femminile":"females","totale_generale":"total"})



def get(url):
    """Returns a dataframe from the .csv file at which the URL provided as a parameter points, properly parsing it. Meant to be invoked by get_<resource_name>() functions.
    
    Parameters
    ----------
    url : str
       URL at which the required .csv file is.
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
       Pandas dataframe with the data from the .csv file at which url points.

    See Also
    --------
    Any function whose name begins with get_ : uses get(url)"""

    try:
        downloaded_content = requests.get(url).content
        dataframe = pd.read_csv(io.StringIO(downloaded_content.decode('utf-8')))
        return dataframe
    # handles the case when string url has not the syntax of a real URL
    except requests.exceptions.MissingSchema:
        print("ERROR Unvalid URL provided")
    # handles connection issues (both lack of Internet connection or URL leading to no website)
    except requests.exceptions.ConnectionError:
        print("ERROR Connection failure")


def quick_total_administered_doses():
    """PART OF THE QUICK FUNCTIONS - returning quickly values of common interest without having to manually extract them from data
    
    Returns the amount of all administered doses ever.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    int
        Integer with the amount of all administered doses ever
    
    See Also
    --------
    get_vaccine_summary_latest : also includes regional data"""
    
    source_dataframe = get_vaccine_summary_latest()
    # get_vaccine_summary_latest() also returns a column administered_doses, with the amount of all doses ever administered per region. Sum is performed on all regional values.
    return int(source_dataframe["administered_doses"].sum())

def quick_total_vaccinated():
    """PART OF THE QUICK FUNCTIONS - returning quickly values of common interest without having to manually extract them from data
    
    Returns the number of individuals who have completed the vaccination cycle (with double dose for Pfizer/Biontech, Moderna and AstraZeneca, with single dose for Johnson&Johnson, with single dose for individuals previously infected with COVID-19 between 3 and 6 months before vaccination.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    int
        Integer with the amount of individuals who have completed the vaccination cycle"""
    
    #source_dataframe = get_vaccine_admin_latest()
    # acquired dataframe lists all second doses and previously infected individuals completing the cycle with one single dose per day. Sum is performed on all daily values.
    #return int(source_dataframe["second_dose"].sum()+source_dataframe["previously_infected"].sum())
    pass

def quick_total_distributed_doses():
    """PART OF THE QUICK FUNCTIONS - returning quickly values of common interest without having to manually extract them from data
    
    Returns the number of all distributed doses ever in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    int
        Integer with the number of all distributed doses ever"""
    
    pass

def quick_total_administration_points():
    """PART OF THE QUICK FUNCTIONS - returning quickly values of common interest without having to manually extract them from data
    
    Returns the number of all vaccine administration points in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    int
        Integer with the number of all vaccine administration points in Italy
    
    See Also
    --------
    get_admin_sites_latest : returns specific info on vaccine administration points
    get_admin_sites_types : returns vaccine administration points types"""

    pass
