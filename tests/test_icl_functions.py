import sys

import os
working_dir = os.path.basename(os.path.normpath(os.getcwd()))

sys.path.append("../itacovidlib")
if working_dir == "covid_lib":
    from itacovidlib.icl_functions import get
elif working_dir == "tests":
    sys.path.append("../itacovidlib")
    from icl_functions import get

def test_wrong_url():
    test_dataframe = get("wrong_url")
