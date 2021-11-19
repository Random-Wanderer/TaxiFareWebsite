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


pickup = st.text_input('Date Time?', 'Enter Date and time for pick up')
lon_up = st.text_input('Pickup Longitude', 'pickup_longitude')
lat_up = st.text_input('Pickup Latitude', 'pickup_latitude')
lat_off = st.text_input('Dropoff Latitude', 'dropoff_latitude')
lon_off = st.text_input('Dropoff longitude', 'dropoff_longitude')
count = st.text_input('How many passengers?', 'passenger_count')

#param = st.container()
#param =

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
