import pandas as pd
import requests
import io

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
