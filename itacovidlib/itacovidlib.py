import pandas as pd
import requests
import io

def get(url):
    """Docstring to be added when function is completed."""
    downloaded_content = requests.get(url).content
    dataframe = pd.read_csv(io.StringIO(downloaded_content.decode('utf-8')))
    return dataframe
