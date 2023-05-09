const apiKey = "2a2f3f5f7828274647633dc6d6b77617";
const url = "https://cors-anywhere.herokuapp.com/http://api.openweathermap.org/data/2.5/weather";
const weatherInfo = document.getElementById("weather-info");

function getWeather() {
    const city = document.getElementById("city").value;
    const params = {
        q: city,
        appid: apiKey,
        units: "metric",
    };
    const queryString = new URLSearchParams(params).toString();
    fetch(`${url}?${queryString}`)
        .then((response) => response.json())
        .then((data) => {
            const temperature = data.main.temp;
            const temp = (data.main.temp * 1.8 + 32).toFixed(2);
            const humidity = data.main.humidity;
            const pressure = data.main.pressure;
            const lightning = data.weather[0].description.includes("lightning");
            const rain = data.rain ? data.rain["1h"] : 0;
            const windSpeed = data.wind ? data.wind.speed : 0;
            const snow = data.snow ? data.snow["1h"] : 0;
            const airQuality =
                data.aqi && data.aqi["us-epa"] ? data.aqi["us-epa"].aqi : "N/A";

            weatherInfo.innerHTML = `
						<p>Temperature (in Celsius): ${temperature} &deg;C</p>
                        <p>Temperature (in Fahrenheit): ${temp} &deg;F</p>
						<p>Humidity: ${humidity}%</p>
						<p>Pressure: ${pressure} hPa</p>
						<p>Lightning: ${lightning ? "Yes" : "No"}</p>
						<p>Rain (1h): ${rain} mm</p>
						<p>Wind Speed: ${windSpeed} m/s</p>
						<p>Snow (1h): ${snow} mm</p>
						<p>Air Quality Index: ${airQuality}</p>
					`;
        })
        .catch((error) => {
            weatherInfo.textContent = "Error: Failed to fetch weather data";
            console.error(error);
        });
}

document.getElementById("get-weather").addEventListener("click", getWeather);

function autocomplete() {
    var input = document.getElementById('city');
    var options = {
        method: 'GET',
        url: 'https://nominatim.openstreetmap.org/search',
        params: {
            format: 'json',
            countrycodes: 'us,in', // Limit to US cities
            limit: 10, // Limit to 10 results
            featuretype: city,
            q: input.value // Search query
        }
    };
    axios(options).then(function(response) {
        var suggestions = response.data.map(function(result) {
            return result.display_name;
        });
        autocompleteDisplay(suggestions);
    }).catch(function(error) {
        console.error(error);
    });
}

function autocompleteDisplay(suggestions) {
    var input = document.getElementById('city');
    var datalist = document.createElement('datalist');
    datalist.setAttribute('id', 'city-list');
    suggestions.forEach(function(suggestion) {
        var option = document.createElement('option');
        option.setAttribute('value', suggestion);
        datalist.appendChild(option);
    });
    input.setAttribute('list', 'city-list');
    input.parentNode.insertBefore(datalist, input.nextSibling);
}

var input = document.getElementById('city');
input.addEventListener('input', function() {
    autocomplete();
});
