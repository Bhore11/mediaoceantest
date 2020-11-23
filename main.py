import requests
import pandas as pd
from _datetime import datetime

# variables
data = pd.DataFrame()
start_date = '2018-10-09'
date_time = datetime.now()
country = ''
zip_code = '0000'
api_secret = ''
line_up_id = ''


def get_data(data, start_date, date_time, country, zip_code, line_up_id, api_secret):
    try:
        response = requests.get(
            'http://data.tmsapi.com/v1.1/movies/showings?startDate=' + start_date + '&country=' + country + '&postalCode=' + zip_code +
            '&api_key=' + api_secret)

    # http://data.tmsapi.com/v1.1/movies/showings?startDate=<start_date>&zip=<zip_code>&api_key=<api_secret>

    # GET http://data.tmsapi.com/v1.1/lineups?country=USA&postalCode=78701&api_key=<your key>
    except:
        print('API call dint complete')

    if data.shape[0] != 0:
        return data, True
    else:
        return data, False


data, success_api = get_data(data=data,
                             start_date=start_date,
                             line_up_id=line_up_id,
                             date_time=datetime.now().isoformat(),
                             country='USA',
                             zip_code='78701',
                             api_secret='q8657nc64jp3uquravmpe9hn')

print('Run Success')