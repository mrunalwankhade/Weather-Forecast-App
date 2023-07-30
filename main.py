import streamlit as st
import plotly.express as px
from backend import get_data

# Add title,subtitle,widgets
st.title("Weather Forcast for the Next 5 Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days ")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temp/sky data
    try:
        filter_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filter_data]
            dates = [dict["dt_txt"] for dict in filter_data]
        # create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_condition = filter_data = [dict["weather"][0]["main"] for dict in filter_data]
            image_paths = [images[condition] for condition in sky_condition]
            print(sky_condition)
            st.image(image_paths, width=85)
    except KeyError:
        st.write(f"Sry we are unable to gather data for {place}.Please try with another nearer city.")