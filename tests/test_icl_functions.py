import sys

import os
working_dir = os.path.basename(os.path.normpath(os.getcwd()))

sys.path.append("../itacovidlib")
if working_dir == "covid_lib":
    from itacovidlib.icl_functions import get, COVIDDataSource
elif working_dir == "tests":
    sys.path.append("../itacovidlib")
    from icl_functions import get, COVIDDataSource

def test_wrong_url():
    data_source_with_nonsense_url = COVIDDataSource("nonsense_url")
    test_dataframe = get(data_source_with_nonsense_url)

def test_wrong_url_2():
    data_source_with_wrong_url = COVIDDataSource("http://fakeurl")
    test_dataframe = get(data_source_with_wrong_url)
