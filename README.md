# Weather App

## Project Description
This Weather App allows users to get current weather information for any city. It utilizes a weather API to fetch real-time weather data and displays it in a user-friendly format.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yashkumaranshukumar435-star/weather-app.git
   cd weather-app
   ```
2. Install the required dependencies:
   ```bash
   npm install
   ```

## Setup API Key
1. Sign up at [OpenWeather](https://openweathermap.org/) to obtain your API key.
2. Create a `.env` file in the root directory of the project.
3. Add the following line, replacing `YOUR_API_KEY` with your actual API key:
   ```bash
   API_KEY=YOUR_API_KEY
   ```

## Usage Examples for CLI Commands
- To get weather information for a specific city:
  ```bash
  node app.js --city "CityName"
  ```
- To get weather information for your current location:
  ```bash
  node app.js --location
  ```

## Features List
- Current weather information
- Ability to check weather by city or by current location
- User-friendly CLI interface

## Requirements
- Node.js (v12 or higher)
- npm (v6 or higher)
- A valid API key from OpenWeather

## License
This project is licensed under the MIT License.