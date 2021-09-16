import pandas as pd
import requests
import io

def get(url):
    """Docstring to be added when function is completed."""
    try:
        downloaded_content = requests.get(url).content
        dataframe = pd.read_csv(io.StringIO(downloaded_content.decode('utf-8')))
        return dataframe
    except requests.exceptions.MissingSchema:
        print("Unvalid URL provided")
    except requests.exceptions.ConnectionError:
        print("Failure to connect to URL")

        

