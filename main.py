import asyncio
import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv(Path(__file__).parent / ".env")

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


async def fetch_weather(city: str):
    """Fetch weather data for a single city."""

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].title()
        }


async def get_weather(city: str):
    """Main weather function."""

    if not API_KEY:
        raise ValueError("OPENWEATHER_API_KEY not found in .env")

    weather = await fetch_weather(city)

    if weather is None:
        raise ValueError("City not found.")

    # Save to JSON
    with open("weather.json", "w") as file:
        json.dump(weather, file, indent=4)

    return weather


if __name__ == "__main__":

    city = input("Enter city: ")

    try:
        weather = asyncio.run(get_weather(city))

        print("\nWeather Information")
        print("-------------------")
        print(f"City        : {weather['city']}")
        print(f"Temperature : {weather['temperature']}°C")
        print(f"Description : {weather['description']}")

    except Exception as e:
        print(f"❌ {e}")