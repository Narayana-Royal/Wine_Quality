import streamlit as st
import pickle
import pandas as pd
# import sklearn
# import numpy as np
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
# from xgboost import XGBRegressor

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'    
]

cities = ['Auckland', 'Mirpur', 'Delhi', 'Johannesburg', 'Kolkata',
       'Colombo', 'Trinidad', 'Bangalore', 'London', 'Cape Town',
       'Wellington', 'Pallekele', 'Cardiff', 'Hamilton', 'Dubai',
       'Adelaide', 'Chandigarh', 'Sydney', 'Lauderhill', 'Centurion',
       'Barbados', 'Nottingham', 'Abu Dhabi', 'Mumbai', 'Southampton',
       'St Lucia', 'Melbourne', 'Mount Maunganui', 'Chittagong',
       'Manchester', 'Durban', 'St Kitts', 'Christchurch', 'Nagpur',
       'Lahore']

pipe = pickle.load(open(r"C:\Users\RUTHVIK\Desktop\internship\Innomatics proj\Productionize a ML Model\pipe.pkl",'rb'))

st.title('T20 Match Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))

with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

col3, col4 = st.columns(2)

with col3:
    score = st.number_input('Current Score')

with col4:
    overs = st.number_input('Overs completed')

col5, col6 = st.columns(2)

with col5:
    wickets = st.number_input('Wickets out')

with col6:
    last_five = st.number_input('Last Five Overs Score')

col7, col8 = st.columns(2)

with col7:
    AverageScore = st.number_input('AverageScore')

with col8:
    Wickets_In_Last5 = st.number_input('Wickets_In_Last5')

if st.button('Predict Probability'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = (score/overs)

    input_df = pd.DataFrame({'AverageScore':[AverageScore], 'battingTeam':[batting_team],'bowlingTeam':[bowling_team], 'city':[selected_city], 'delivery_left':[balls_left], 'score':[score], 'CurrentRunRate':[crr],  'wicketsLeft':[wickets_left], 'Run_In_Last5':[last_five],  'Wickets_In_Last5':[Wickets_In_Last5]})

    result = pipe.predict(input_df)

    st.text("Score Prediction:" + str(result[0]))