import streamlit as st



st.set_page_config(
    page_title="Unit Converter App by SamiaAdnan",
    page_icon="♠",
    layout="wide"

)
conversion_data = {
    "Distance":{
        "Meters":{
            "Kilometers":0.001,
            "Miles":0.00621371,
            "Feet":3.28084,
        },
        "Kilometers":{
            "Meters":1609.34,
            "Miles":0.621371,
            "Feet":3280.84
        },
        "Miles":{
            "Meters":1609.34,
            "Kilometers":1.60934,
            "Feet":5280
        },
        "Feet":{
            "Meters":0.3048,
            "Kilometers":0.003048,
            "Miles":0.000189394
        },
    },
         "Weight":{
            "Kilograms":{
                  "Grams":1000,
                  "Pounds":2.20462,
            },
            "Grams":{
                 "Kilograms":0.001,
                 "Pounds":0.00220462
            },
            "Pounds":{
                "Kilograms":0.453592,
                "Grams":453.592
            },
         },
            "Temperature":{
                "Celsius":{"Fahrenheit":lambda c:(c*9/5) + 32,
                 "Kelvin":lambda c:c +273.15
                },
                "Fahrenheit":{
                    "Celsius":lambda f:(f-32)*5/9,
                    "Kelvin":lambda f:((f-32)*5/9)+273.15
                },
                "Kelvin":{
                    "Celsius":lambda k:k - 273.15,
                    "fahrenheit": lambda k:((k - 273.15)*9/5)+32
                },
            }
}
st.markdown("<h1 style='color: purple;'> Unit Converter App♠</h1>",
unsafe_allow_html=True)
st.write("<h6 style='color:purple;'>Convert units between different categories such as Distance, Weight, and Temperature...</h6>",
unsafe_allow_html=True)
#select category
category = st.selectbox("Select category:",list(conversion_data.keys()))
from_unit = st.selectbox("From:",list(conversion_data[category].keys()))
to_unit = st.selectbox("To:",list(conversion_data[category][from_unit].keys()))
#Input value 
value = st.number_input("Enter Value:",min_value=0.0,step=0.1)
conversion_factor = conversion_data[category][from_unit][to_unit]

if callable(conversion_factor):
    result = conversion_factor(value)
else:
    result = value*conversion_factor


st.success(f"{value} {from_unit} is equal to {result} {to_unit}♠")