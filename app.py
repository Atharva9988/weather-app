import asyncio
import streamlit as st

from main import get_weather

st.set_page_config(
    page_title="Weather App",
    page_icon="🌦️"
)

st.title("🌦️ Weather App")

city = st.text_input("Enter City")

if st.button("Get Weather"):

    if city.strip() == "":
        st.warning("Please enter a city name.")

    else:

        with st.spinner("Fetching weather..."):

            try:
                weather = asyncio.run(get_weather(city))

                st.success("Weather fetched successfully!")

                st.write(f"### 📍 {weather['city']}")
                st.metric("🌡️ Temperature", f"{weather['temperature']}°C")
                st.write(f"☁️ **Description:** {weather['description']}")

            except Exception as e:
                st.error(e)