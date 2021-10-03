import sys
sys.path.append("../itacovidlib")
import itacovidlib.icl_backend as icl_b
import numpy as np

# ====================================================================================
# FOR ALL get_<resource_name>() FUNCTIONS
#
# .rename(columns={...}) translates column names (originally in Italian) into English.
# ====================================================================================

def get_vaccine_ages():
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
    extra_dose : int
        Number of extra doses administered to individuals requiring it
    last_update : str
        Date of last update"""
    
    data = icl_b.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv")
    if data is not None:
        return data.rename(columns={"fascia_anagrafica":"age_group","totale":"total","sesso_maschile":"males","sesso_femminile":"females","prima_dose":"first_dose","seconda_dose":"second_dose","pregressa_infezione":"previously_infected","dose_aggiuntiva":"extra_dose","ultimo_aggiornamento":"last_update"})

def get_vaccine_deliveries():
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
    
    data = icl_b.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/consegne-vaccini-latest.csv")
    if data is not None:
        return data.rename(columns={"area":"region_code","fornitore":"manufacturer","data_consegna":"date_of_delivery","numero_dosi":"number_of_doses","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

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
    
    data = icl_b.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea.csv")
    if data is not None:
        return data.rename(columns={"area":"region_code","nome_area":"region","fascia_anagrafica":"age_group","totale_popolazione":"population"})

def get_admin_sites():
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
    
    data = icl_b.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-latest.csv")
    if data is not None:
        return data.rename(columns={"area":"region_code","provincia":"province","comune":"municipality","presidio_ospedaliero":"place","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

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
    
    data = icl_b.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-tipologia.csv")
    if data is not None:
        return data.rename(columns={"area":"region_code","denominazione_struttura":"place","tipologia":"type","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_vaccine_admin():
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
    extra_dose : int
        Number of extra doses administered to individuals requiring it
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
    get_vaccine_admin_summary : a concise version (summary) of this function"""
    
    data = icl_b.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv")
    if data is not None:
        return data.rename(columns={"data_somministrazione":"date","fornitore":"manufacturer","area":"region_code","fascia_anagrafica":"age_group","sesso_maschile":"males","sesso_femminile":"females","prima_dose":"first_dose","seconda_dose":"second_dose","pregressa_infezione":"previously_infected","dose_aggiuntiva":"extra_dose","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_vaccine_admin_summary():
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
    extra_dose : int
        Number of extra doses administered to individuals requiring it
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
    get_vaccine_admin : a complete version of this function with more data"""
    
    data = icl_b.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv")
    if data is not None:
        return data.rename(columns={"data_somministrazione":"date","area":"region_code","totale":"total","sesso_maschile":"males","sesso_femminile":"females","prima_dose":"first_dose","seconda_dose":"second_dose","pregressa_infezione":"previously_infected","dose_aggiuntiva":"extra_dose","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_vaccine_summary():
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
    get_vaccine_deliveries : more info on COVID-19 vaccine deliveries
    get_vaccine_admin_summary : more info on COVID-19 vaccine administrations (concise version)
    get_vaccine_admin : more info on COVID-19 vaccine administrations (complete version)"""
    
    data = icl_b.get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv")
    if data is not None:
        return data.rename(columns={"area":"region_code","dosi_somministrate":"administered_doses","dosi_consegnate":"delivered_doses","percentuale_somministrazione":"administration_percent","ultimo_aggiornamento":"last_update","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_national_trend():
    """Returns dataframe about COVID-19 pandemic situation in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Dataframe about COVID-19 pandemic situation in Italy
    
    Dataframe Columns
    -----------------
    date : str
        Date
    country : str
        Country
    hospitalized_with_symptoms : int
        Number of hospitalized individuals with COVID-19 symptoms
    intensive_care : int
        Number of individuals in intensive care units
    hospitalized : int
        Number of hospitalized individuals, either with symptoms or in intensive care unit
    isolation : int
        Number of people placed into isolation
    cases : int
        Number of COVID-19 cases
    cases_variation : int
        Variation in the number of COVID-19 cases with respect to the previous day
    new_cases : int
        Number of new individuals diagnosed with COVID-19
    recovered_released : int
        Number of individuals released from hospital after recovery
    deaths : int
        Number of individuals died following COVID-19 infection
    cases_from_clinical_suspects : int
        Number of positive cases found after report of COVID-19-like symptoms
    cases_from_screening : int
        Number of positive cases found after screening (e.g. close contacts of a positive case)
    cumulative_cases : int
        Total number of COVID-19 cases since the beginning of the pandemic
    swabs : int
        Number of swabs performed
    tested : int
        Number of tested individuals
    notes : str
        Notes
    intensive_care_in : int
        Number of new accesses to intensive care units
    test_notes : str
        Notes on testing
    case_notes : str
        Notes on COVID-19 cases
    molecular_test_cases : int
        Number of COVID-19 cases detected through molecular tests
    antigen_test_cases : int
        Number of COVID-19 cases detected through antigen (so-called rapid) tests
    molecular_tests : int
        Total number of molecular tests performed
    antigen_tests : int
        Total number of antigen (so-called rapid) tests performed
    
    See Also
    --------
    get_national_trend_latest : only returns data referred to the current day"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
    if data is not None:
        return data.rename(columns={"data":"date","stato":"country","ricoverati_con_sintomi":"hospitalized_with_symptoms","terapia_intensiva":"intensive_care","totale_ospedalizzati":"hospitalized","isolamento_domiciliare":"isolation","totale_positivi":"cases","variazione_totale_positivi":"cases_variation","nuovi_positivi":"new_cases","dimessi_guariti":"recovered_released","deceduti":"deaths","casi_da_sospetto_diagnostico":"cases_from_clinical_suspects","casi_da_screening":"cases_from_screening","totale_casi":"cumulative_cases","tamponi":"swabs","casi_testati":"tested","note":"notes","ingressi_terapia_intensiva":"intensive_care_in","note_test":"test_notes","note_casi":"case_notes","totale_positivi_test_molecolare":"molecular_test_cases","totale_positivi_test_antigenico_rapido":"antigen_test_cases","tamponi_test_molecolare":"molecular_tests","tamponi_test_antigenico_rapido":"antigen_tests"})

def get_national_trend_latest():
    """Returns dataframe about COVID-19 pandemic situation in Italy on the current day (the last update), i.e. the most recent row of the dataframe that can be called with get_national_trend().
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe about COVID-19 pandemic situation in Italy on the current day (i.e. the last update).
    
    Dataframe Columns
    -----------------
    Please see documentation of get_national_trend()
    
    See Also
    --------
    get_national_trend : also includes the situation on all days since the beginning of the pandemic"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-latest.csv")
    if data is not None:
        return data.rename(columns={"data":"date","stato":"country","ricoverati_con_sintomi":"hospitalized_with_symptoms","terapia_intensiva":"intensive_care","totale_ospedalizzati":"hospitalized","isolamento_domiciliare":"isolation","totale_positivi":"cases","variazione_totale_positivi":"cases_variation","nuovi_positivi":"new_cases","dimessi_guariti":"recovered_released","deceduti":"deaths","casi_da_sospetto_diagnostico":"cases_from_clinical_suspects","casi_da_screening":"cases_from_screening","totale_casi":"cumulative_cases","tamponi":"swabs","casi_testati":"tested","note":"notes","ingressi_terapia_intensiva":"intensive_care_in","note_test":"test_notes","note_casi":"case_notes","totale_positivi_test_molecolare":"molecular_test_cases","totale_positivi_test_antigenico_rapido":"antigen_test_cases","tamponi_test_molecolare":"molecular_tests","tamponi_test_antigenico_rapido":"antigen_tests"})

def get_equip_contracts():
    """Returns data about COVID-19 pandemic equipment contracts for Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with data about COVID-19 pandemic equipment contracts
    
    Dataframe Columns
    -----------------
    manufacturer : str
        Equipment manufacturer name
    country : str
        Country
    product_group : str
        Official product group
    article_subgroup : str
        Official article subgroup
    category : str
        Equipment category
    subcategory : str
        Equipment subcategory
    equipment_kind : str
        Equipment kind
    equipment : str
        Equipment name
    negotiation_protocol : str
        Name of negotiation protocol
    negotiation_date : str
        Date of negotiation
    negotiation_file : str
        Negotiation file link
    errata : str
        Errata corrige
    errata_protocol : str
        Protocol errata corrige
    errata_date : str
        Date errata corrige
    errata_file : str
        File errata corrige
    tender_id_type : str
        Tender identification code type
    tender_id : str
        Tender identification code
    quantity : int
        Item quantity
    unit_price : numpy.float64
        Price per unit
    total_price : numpy.float64
        Total price
    agreement_state : str
        State of agreement
    ceded : str
        State of cession to Special Commissioner for COVID-19 emergency (ITA: Commissario Straordinario)
    notes : str
        Notes
    update_date : str
        Date of update
    
    See Also
    --------
    get_equip_contracts_payments : data about payments for COVID-19 pandemic equipment"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-contratti-dpc-forniture.csv")
    if data is not None:
        return data.rename(columns={"fornitore":"manufacturer","stato_fornitore":"country","gruppo_articoli":"product_group","sottogruppo_articoli":"article_subgroup","categoria":"category","sottocategoria":"subcategory","tipologia_fornitura":"equipment_kind","fornitura":"equipment","protocollo_atto_negoziale":"negotiation_protocol","data_atto_negoziale":"negotiation_date","file_atto_negoziale":"negotiation_file","integrazione_rettifica":"errata","protocollo_integrazione_rettifica":"errata_protocol","data_integrazione_rettifica":"errata_date","file_integrazione_rettifica":"errata_file","tipologia_cig":"cig_type","cig":"cig","quantita":"quantity","prezzo_unitario":"unit_price","totale_articolo":"total_price","stato_contratto":"agreement_state","ceduti_commissario_straordinario":"ceded","note":"notes","data_aggiornamento":"update_date"})

def get_equip_contracts_payments():
    """Returns data about payments for COVID-19 equipment in Italy, as established by contracts.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe about payments for COVID-19 equipment
    
    Dataframe Columns
    -----------------
    negotiation_protocol : str
        Name of negotiation protocol
    total_equipment : numpy.float64
        Total amount per given equipment
    total_paid : numpy.float64
        Total paid
    donations : numpy.float64
        Amount of donations
    other_funds : numpy.float64
        Amount of other funds used for that payment
    payment_fund : numpy.float64
        Amount of payment fund used for that payment
    ceded : str
        State of cession to Special Commissioner for COVID-19 emergency (ITA: Commissario Straordinario)
    notes : str
        Notes
    update_date : str
        Date of update
    
    See Also
    --------
    get_equip_contracts : data about COVID-19 equipment contracts"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-contratti-dpc-forniture/dpc-covid19-dati-pagamenti-contratti-dpc-forniture.csv")
    if data is not None:
        return data.rename(columns={"protocollo_atto_negoziale":"negotiation_protocol","totale_fornitura":"total_equipment","totale_pagato":"total_paid","pagato_donazioni":"donations","pagato_altri_fondi":"other_funds","fondo_pagamento":"payment_fund","ceduti_commissario_straordinario":"ceded","note":"notes","data_aggiornamento":"update_date"})

def get_province_cases():
    """Returns dataframe about COVID-19 cases per province in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Dataframe about COVID-19 cases per province
    
    Dataframe Columns
    -----------------
    date : str
        Date
    country : str
        Country
    region_code : int
        Region code number
    region : str
        Official region name
    province_code : int
        Province code number
    province : str
        Province
    province_abbreviation : str
        Province two-letter abbreviation
    lat : numpy.float64
        Latitude
    long : numpy.float64
        Longitude
    cumulative_cases : int
        Total number of COVID-19 cases since the beginning of the pandemic
    notes : str
        Notes
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    NUTS3_code : str
        European classification of territorial units NUTS: level NUTS3
    
    See Also
    --------
    get_province_cases_latest : only returns data referred to the current day"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv")
    if data is not None:
        return data.rename(columns={"data":"date","stato":"country","codice_regione":"region_code","denominazione_regione":"region","codice_provincia":"province_code","denominazione_provincia":"province","sigla_provincia":"province_abbreviation","lat":"lat","long":"long","totale_casi":"cumulative_cases","note":"notes","codice_nuts_1":"NUTS1_code","codice_nuts_2":"NUTS2_code","codice_nuts_3":"NUTS3_code"})

def get_province_cases_latest():
    """Returns dataframe about COVID-19 cases per province in Italy on the current day (the last update), i.e. the most recent row of the dataframe that can be called with get_province_cases().
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Dataframe about COVID-19 cases per province on the current day
    
    Dataframe Columns
    -----------------
    Please see get_province_cases() documentation
    
    See Also
    --------
    get_province_cases : also includes the situation on all days since the beginning of the pandemic"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province-latest.csv")
    if data is not None:
        return data.rename(columns={"data":"date","stato":"country","codice_regione":"region_code","denominazione_regione":"region","codice_provincia":"province_code","denominazione_provincia":"province","sigla_provincia":"province_abbreviation","lat":"lat","long":"long","totale_casi":"cumulative_cases","note":"notes","codice_nuts_1":"NUTS1_code","codice_nuts_2":"NUTS2_code","codice_nuts_3":"NUTS3_code"})

def get_region_cases_latest():
    """Returns dataframe about COVID-19 cases per region in Italy on the current day (the last update), i.e. the most recent row of the dataframe that can be called with get_region_cases().
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe about COVID-19 cases per region on the current day
    
    Dataframe Columns
    -----------------
    Please see documentation of get_region_cases()
    
    See Also
    --------
    get_region_cases : also includes the situation on all days since the beginning of the pandemic"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv")
    if data is not None:
        return data.rename(columns={"data":"date","stato":"country","codice_regione":"region_code","denominazione_regione":"region","ricoverati_con_sintomi":"hospitalized_with_symptoms","terapia_intensiva":"intensive_care","totale_ospedalizzati":"hospitalized","isolamento_domiciliare":"isolation","totale_positivi":"cases","variazione_totale_positivi":"cases_variation","nuovi_positivi":"new_cases","dimessi_guariti":"recovered_released","deceduti":"deaths","casi_da_sospetto_diagnostico":"cases_from_clinical_suspects","casi_da_screening":"cases_from_screening","totale_casi":"cumulative_cases","tamponi":"swabs","casi_testati":"tested","note":"notes","ingressi_terapia_intensiva":"intensive_care_in","note_test":"test_notes","note_casi":"case_notes","totale_positivi_test_molecolare":"molecular_test_cases","totale_positivi_test_antigenico_rapido":"antigen_test_cases","tamponi_test_molecolare":"molecular_tests","tamponi_test_antigenico_rapido":"antigen_tests","codice_nuts_1":"NUTS1_code","codice_nuts_2":"NUTS2_code"})

def get_region_cases():
    """Returns dataframe about COVID-19 cases per region in Italy.
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe about COVID-19 cases per region
    
    Dataframe Columns
    -----------------
    date : str
        Date
    country : str
        Country
    region_code : int
        Region code number
    region : str
        Official region name
    lat : numpy.float64
        Latitude
    long : numpy.float64
        Longitude
    hospitalized_with_symptoms : int
        Number of hospitalized individuals with COVID-19 symptoms
    intensive_care : int
        Number of individuals in intensive care units
    hospitalized : int
        Number of hospitalized individuals, either with symptoms or in intensive care unit
    isolation : int
        Number of people placed into isolation
    cases : int
        Number of COVID-19 cases
    cases_variation : int
        Variation in the number of COVID-19 cases with respect to the previous day
    new_cases : int
        Number of new individuals diagnosed with COVID-19
    recovered_released : int
        Number of individuals released from hospital after recovery
    deaths : int
        Number of individuals died following COVID-19 infection
    cases_from_clinical_suspects : int
        Number of positive cases found after report of COVID-19-like symptoms
    cases_from_screening : int
        Number of positive cases found after screening (e.g. close contacts of a positive case)
    cumulative_cases : int
        Total number of COVID-19 cases since the beginning of the pandemic
    swabs : int
        Number of swabs performed
    tested : int
        Number of tested individuals
    notes : str
        Notes
    intensive_care_in : int
        Number of new accesses to intensive care units
    test_notes : str
        Notes on testing
    case_notes : str
        Notes on COVID-19 cases
    molecular_test_cases : int
        Number of COVID-19 cases detected through molecular tests
    antigen_test_cases : int
        Number of COVID-19 cases detected through antigen (so-called rapid) tests
    molecular_tests : int
        Total number of molecular tests performed
    antigen_tests : int
        Total number of antigen (so-called rapid) tests performed
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    
    See Also
    --------
    get_region_cases_latest : only returns data referred to the current day"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")
    if data is not None:
        return data.rename(columns={"data":"date","stato":"country","codice_regione":"region_code","denominazione_regione":"region","ricoverati_con_sintomi":"hospitalized_with_symptoms","terapia_intensiva":"intensive_care","totale_ospedalizzati":"hospitalized","isolamento_domiciliare":"isolation","totale_positivi":"cases","variazione_totale_positivi":"cases_variation","nuovi_positivi":"new_cases","dimessi_guariti":"recovered_released","deceduti":"deaths","casi_da_sospetto_diagnostico":"cases_from_clinical_suspects","casi_da_screening":"cases_from_screening","totale_casi":"cumulative_cases","tamponi":"swabs","casi_testati":"tested","note":"notes","ingressi_terapia_intensiva":"intensive_care_in","note_test":"test_notes","note_casi":"case_notes","totale_positivi_test_molecolare":"molecular_test_cases","totale_positivi_test_antigenico_rapido":"antigen_test_cases","tamponi_test_molecolare":"molecular_tests","tamponi_test_antigenico_rapido":"antigen_tests","codice_nuts_1":"NUTS1_code","codice_nuts_2":"NUTS2_code"})

def get_over_80():
    """Returns data on over 80 individuals in Italy
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with data on over 80 individuals
    
    Dataframe Columns
    -----------------
    region_code : int
        Region code number
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS1_description : str
        Description of level NUTS1 of the European classification of territorial units NUTS
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    region : str
        Official region name
    age_range : str
        Age range
    males : int
        Number of male individuals
    females : int
        Number of female individuals
    total : int
        Total number of over 80 individuals"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-over80.csv")
    if data is not None:
        return data.rename(columns={"codice_regione":"region_code","codice_nuts_1":"NUTS1_code","descrizione_nuts_1":"NUTS1_description","codice_nuts_2":"NUTS2_code","denominazione_regione":"region","range_eta":"age_range","totale_genere_maschile":"males","totale_genere_femminile":"females","totale_generale":"total"})

def get_istat_region_data():
    """Returns data about Italian regions from ISTAT (Italian National Institute of Statistics).
    
    Parameters
    ----------
    None
    
    Raises
    ------
    None
    
    Returns
    -------
    pandas.core.frame.DataFrame
        Pandas dataframe with data about Italian regions from ISTAT
    
    Dataframe Columns
    -----------------
    region_code : int
        Region code number
    NUTS1_code : str
        European classification of territorial units NUTS: level NUTS1
    NUTS1_description : str
        Description of level NUTS1 of the European classification of territorial units NUTS
    NUTS2_code : str
        European classification of territorial units NUTS: level NUTS2
    region : str
        Official region name
    region_abbreviation: str
        Region name abbreviation
    lat : numpy.float64
        Latitude
    long : numpy.float64
        Longitude
    age_range : str
        Age range
    males : int
        Number of male individuals
    females : int
        Number of female individuals
    total : int
        Total number of individuals"""
    
    data = icl_b.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv")
    if data is not None:
        return data.rename(columns={"codice_regione":"region_code","codice_nuts_1":"NUTS1_code","descrizione_nuts_1":"NUTS1_description","codice_nuts_2":"NUTS2_code","denominazione_regione":"region","sigla_regione":"region_abbreviation","latitudine_regione":"lat","longitudine_regione":"long","range_eta":"age_range","totale_genere_maschile":"males","totale_genere_femminile":"females","totale_generale":"total"})

def tell_total_administered_doses():
    """Returns the amount of all administered doses ever.
    
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
    get_vaccine_summary : also includes regional data"""
    
    data = get_vaccine_summary()
    if data is not None:
        # get_vaccine_summary_latest() also returns a column administered_doses, with the amount of all doses ever administered per region. Sum is performed on all regional values.
        return int(data["administered_doses"].sum())

def tell_total_vaccinated(dose_number):
    """Depending on the int value provided as dose_number:
    dose_number = 1: returns the number of individuals who have been injected at least one vaccine dose in Italy (independently of it being enough for vaccination cycle completion, as is the case with Janssen vaccine or for individuals with recent COVID-19 injection, for whom only one dose is required;
    dose_number = 2: returns the number of individuals who have completed the vaccination cycle in Italy (with double dose for Pfizer/BioNTech, Moderna and Vaxzevria (AstraZeneca), with single dose for Janssen, with single dose for individuals previously infected with COVID-19 between 3 and 6 months before vaccination;
    dose_number = 3: returns the number of individuals who have been injected an extra dose of vaccine in Italy, being eligible for it depending on their medical condition (commonly referred to as "third dose" in media).
    
    Parameters
    ----------
    dose_number : int
        Dose number of interest. See above for the meaning of dose_number = 1, 2 or 3. Other int values yield an error.
    
    Raises
    ------
    None
    
    Returns
    -------
    numpy.int64
        NumPy integer (see above for its meaning, depending on dose_number being equal to 1, 2 or 3).
    
    See Also
    --------
    get_vaccine_admin : full data about vaccine administration in Italy"""

    data = get_vaccine_admin()
    if data is not None:
        if dose_number == 1:
            # Previously infected individuals data are also added, since the dataframe returned by get_vaccine_admin() keeps them separate from first doses count
            return data.sum()["first_dose"]+data.sum()["previously_infected"]
        elif dose_number == 2:
            # For vaccines requiring two doses data on second doses are taken, for vaccines requiring one single dose data on first doses are taken, for all vaccines data on previously infected individuals, completing the vaccination cycle with one single dose, are also taken, since their data are kept separate from first and second doses data
            return data[data["manufacturer"]!="Janssen"].sum()["second_dose"]+data[data["manufacturer"]=="Janssen"].sum()["first_dose"]+data.sum()["previously_infected"]
        elif dose_number == 3:
            return data.sum()["extra_dose"]
        else:
            print("ERROR Unvalid number code. Please see documentation for help on possible options.")

def tell_total_admin_points():
    """Returns the number of all vaccine administration points in Italy.
    
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
    get_admin_sites : returns specific info on vaccine administration points
    get_admin_sites_types : returns vaccine administration points types"""

    # get_admin_sites_types() returns all administration points, one per row
    data = get_admin_sites_types()
    if data is not None:
        return len(data.index)

def tell_manufacturer_delivered_doses(manufacturer):
    """Returns the number of delivered vaccine doses from the manufacturer given as a parameter in Italy. If string "all" is provided as parameter, it returns the number of delivered vaccine doses from all manufacturers.
    
    Parameters
    ----------
    manufacturer : str
        Vaccine manufacturer name or str "all". ONLY ACCEPTED MANUFACTURERS AND SPELLINGS ARE "Pfizer/BioNTech", "Moderna", "Vaxzevria (AstraZeneca)" AND "Janssen". Str "all" triggers return of number of delivered doses from all manufacturers.
    
    Raises
    ------
    None
    
    Returns
    -------
    numpy.int64
        Number of delivered vaccine doses from chosen manufacturer or all manufacturers, according to parameter
    
    See Also
    --------
    get_vaccine_deliveries : full data about vaccine deliveries per manufacturer"""

    # get_vaccine_deliveries() returns all delivered doses per day and per manufacturer in a DataFrame. A sum must be performed over days for the chosen manufacturer. np.int64() to avoid a numpy.float64 obj being produced in case of null result. If the str "all" is provided, the function returns all delivered doses for all manufacturers.
    data = get_vaccine_deliveries()
    if data is not None:
        if manufacturer=="all":
            all_delivered_doses = np.int64(data.sum()["number_of_doses"])
            return all_delivered_doses
        else:
            manufacturer_delivered_doses = np.int64(data[data["manufacturer"]==manufacturer].sum()["number_of_doses"])
            if manufacturer_delivered_doses == 0:
                print('ERROR No vaccine manufacturer recognized with name "{}". Only accepted names and spellings are "Pfizer/Biontech", "Moderna", "Vaxzevria (AstraZeneca)" and "Janssen".'.format(manufacturer))
            else:
                return manufacturer_delivered_doses

### TO DO
# - Turn error messages into exceptions
# - Percentage option in tell functions
# - Fix Raises in docstrings and/or remove None indication which is ambiguous
# - Fix type int when it should be numpy.int64 in docstrings
