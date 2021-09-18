import pandas as pd
import requests
import io



def get_vaccine_ages_sum_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/anagrafica-vaccini-summary-latest.csv").rename(columns={"fascia_anagrafica":"age_group","totale":"total","sesso_maschile":"males","sesso_femminile":"females","prima_dose":"first_dose","seconda_dose":"second_dose","pregressa_infezione":"previously_infected","ultimo_aggiornamento":"last_update"})

def get_vaccine_deliveries_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/consegne-vaccini-latest.csv").rename(columns={"area":"region_code","fornitore":"manufacturer","data_consegna":"date_of_delivery","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_eligible():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea.csv").rename(columns={"area":"region_code","nome_area":"region_name","fascia_anagrafica":"age_group","totale_popolazione":"population"})

def get_admin_sites_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-latest.csv").rename(columns={"area":"region_code","provincia":"province","comune":"municipality","presidio_ospedaliero":"place","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_admin_sites_types():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/punti-somministrazione-tipologia.csv").rename(columns={"area":"region_code","denominazione_struttura":"place","tipologia":"type","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_vaccine_admin_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv").rename(columns={"data_somministrazione":"date","fornitore":"manufacturer","area":"region_code","fascia_anagrafica":"age_group","sesso_maschile":"males","sesso_femminile":"females","prima_dose":"first_dose","seconda_dose":"second_dose","pregressa_infezione":"previously_infected","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_vaccine_admin_sum_latest():
    return get("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv").rename(columns={"data_somministrazione":"date","area":"region_code","totale":"total","sesso_maschile":"males","sesso_femminile":"females","prima_dose":"first_dose","seconda_dose":"second_dose","pregressa_infezione":"previously_infected","codice_NUTS1":"NUTS1_code","codice_NUTS2":"NUTS2_code","codice_regione_ISTAT":"ISTAT_region_code","nome_area":"region"})

def get_vaccine_sum_latest():
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
    """Docstring to be added when function is completed."""
    try:
        downloaded_content = requests.get(url).content
        dataframe = pd.read_csv(io.StringIO(downloaded_content.decode('utf-8')))
        return dataframe
    except requests.exceptions.MissingSchema:
        print("ERROR Unvalid URL provided")
    except requests.exceptions.ConnectionError:
        print("ERROR Connection failure")



