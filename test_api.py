from datetime import datetime

import fitbit

from fitbit_app.settings import Settings

settings = Settings()

# Access environment variables
ACCESS_TOKEN = settings.ACCESS_TOKEN
CLIENT_SECRET = settings.CLIENT_SECRET
CLIENT_ID = settings.CLIENT_ID
TOKEN_TYPE = settings.TOKEN_TYPE
REFRESH_TOKEN = settings.REFRESH_TOKEN


def refresh_cb(token):
    # This function will be called with the new access token
    print("Refreshed access token:", token)


client = fitbit.Fitbit(
    CLIENT_ID,
    CLIENT_SECRET,
    oauth2=True,
    access_token=ACCESS_TOKEN,
    refresh_token=REFRESH_TOKEN,
    refresh_cb=refresh_cb,
)


oneDate = datetime.strptime("2023-11-24", "%Y-%m-%d")
oneDayData = client.intraday_time_series(
    "activities/heart", oneDate, detail_level="1min"
)


# df = pd.DataFrame(oneDayData['activities-heart-intraday']['dataset'])

# df.head()

print(oneDayData)
