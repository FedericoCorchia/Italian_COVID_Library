# Italian_COVID_Library
A Python library for COVID-19 infections and vaccinations in Italy data retrieval and analysis.

## Installing Italian_COVID_Library
Simply clone this repository and use it as a normal Python package:

`git clone https://github.com/FedericoCorchia/Italian_COVID_Library`

## Requirements
Functioning of Italian_COVID_Library requires the following:
- Python (guaranteed for version 3.8.5 or higher, TO BE CHECKED FOR PREVIOUS VERSIONS)
- pandas
- numpy
- requests
- setuptools

After cloning the repository, you may directly implement all of the above with the following command, which creates a specific Conda environment for Italian_COVID_Library with all dependencies, downloading them if needed:

`conda env create -f itacovidlib_env.yml`

## Usage
Instructions on using Italian_COVID_Library, also including practical tutorials:

MANUAL PAGES YET TO BE CREATED

## Data Sources
For data on COVID-19 cases in Italy: [pcm-dpc/COVID-19](https://github.com/pcm-dpc/COVID-19) - "COVID-19 Italia - Monitoraggio situazione" by Dipartimento della Protezione Civile

For data on vaccinations in Italy: [italia/covid19-opendata-vaccini](https://github.com/italia/covid19-opendata-vaccini) - "Open Data su consegna e somministrazione dei vaccini anti COVID-19 in Italia - Commissario straordinario per l'emergenza Covid-19", by Commissario straordinario per l'emergenza Covid-19 - Presidenza del Consiglio dei Ministri

Both are released under **Creative Commons - Attribution 4.0 International (CC BY 4.0)** [Full license](https://creativecommons.org/licenses/by/4.0/legalcode) - [Summary](https://creativecommons.org/licenses/by/4.0/deed.en)

Downloader functions provide the original data as they are without any modification apart from translating them into English.

## Further project details
This is a programming project for the Software and Computing for Nuclear and Subnuclear Physics course, Master Course in Nuclear and Subnuclear Physics, University of Bologna.
