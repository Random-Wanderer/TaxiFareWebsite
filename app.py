import streamlit as st
import requests

'''
# Taxi Fare Model
'''

st.markdown('''

''')
'''

## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''


pickup = st.text_input('Date Time?', '2012-10-06 12:10:20')
lon_up = st.text_input('Pickup Longitude', '40.7614327')
lat_up = st.text_input('Pickup Latitude', '-73.9798156')
lat_off = st.text_input('Dropoff Latitude', '40.6513111')
lon_off = st.text_input('Dropoff longitude', '-73.8803331')
count = st.text_input('How many passengers?', '3')


params = {
    "key": ["key"],
    "pickup_datetime": [pickup],
    "pickup_longitude": [float(lon_up)],
    "pickup_latitude": [float(lat_up)],
    "dropoff_longitude": [float(lon_off)],
    "dropoff_latitude": [float(lat_off)],
    "passenger_count": [int(count)]
}


url = 'https://taxifare.lewagon.ai/predict/'

if url == 'https://taxifare.lewagon.ai/predict/':
    response = requests.get(url, params=params).json()

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

response
