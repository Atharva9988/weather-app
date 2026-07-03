# 🌦️ Weather App

A Python command-line application that fetches real-time weather information for multiple cities concurrently using asynchronous programming. The application retrieves data from the OpenWeather API, displays the results in the terminal, and stores them in a JSON file for later use.

---

## ✨ Features

- Fetches real-time weather data for multiple cities
- Uses asynchronous programming with `asyncio` and `httpx`
- Retrieves current temperature and weather description
- Saves weather data to a JSON file
- Uses environment variables to securely manage API keys
- Lightweight and easy to extend

---

## 🛠️ Technologies Used

- Python 3
- asyncio
- httpx
- python-dotenv
- OpenWeather API
- JSON

---

## 📁 Project Structure

```text
weather-app/
│── main.py
│── requirements.txt
│── .gitignore
│── README.md
│── weather.json          # Generated after running the program
└── .env                  # Create this yourself (not included)
```

---

## 🚀 Setup

### 1. Clone the repository

```bash
git clone https://github.com/Atharva9988/weather-app.git
cd weather-app
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Obtain an OpenWeather API Key

Create a free account at:

https://openweathermap.org/api

Generate an API key.

### 5. Create a `.env` file

Create a file named `.env` in the project root and add:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

---

## ▶️ How to Run

Execute the application using:

```bash
python main.py
```

---

## 📤 Output

### Terminal Output

The application fetches weather information for the configured cities and displays:

- City Name
- Temperature (°C)
- Weather Description

Example:

```text
------------------------------
City: Mumbai
Temperature: 30°C
Description: Clear Sky

------------------------------
City: Delhi
Temperature: 36°C
Description: Haze

------------------------------
City: Pune
Temperature: 28°C
Description: Broken Clouds
```

---

### JSON Output

After successful execution, a file named **`weather.json`** is created in the project directory.

Example:

```json
[
    {
        "city": "Mumbai",
        "temperature": 30,
        "description": "Clear Sky"
    },
    {
        "city": "Delhi",
        "temperature": 36,
        "description": "Haze"
    },
    {
        "city": "Pune",
        "temperature": 28,
        "description": "Broken Clouds"
    }
]
```

---

## 📋 Requirements

- Python 3.10 or later
- Internet connection
- OpenWeather API Key

---

## 🔮 Future Improvements

- Accept city names as user input
- Add humidity and wind speed
- Display weather icons
- Support 5-day weather forecasts
- Export weather data to CSV
- Build a graphical user interface (GUI)

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Atharva Thorve**

GitHub: https://github.com/Atharva9988
