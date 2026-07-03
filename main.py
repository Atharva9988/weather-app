import asyncio
import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv

# Load the .env file
load_dotenv(Path(__file__).parent / ".env")

# Read the API key
API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


async def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }


async def main():
    if not API_KEY:
        print("❌ API_KEY not found in .env")
        return

    cities = ["Mumbai", "Delhi", "Bangalore"]

    results = await asyncio.gather(
        *(fetch_weather(city) for city in cities)
    )

    with open("weather.json", "w") as file:
        json.dump(results, file, indent=4)

    print("\nWeather Report")
    print("-" * 30)

    for result in results:
        print(
            f"{result['city']}: "
            f"{result['temperature']}°C, "
            f"{result['description']}"
        )


if __name__ == "__main__":
    asyncio.run(main())