# air-quality-advisory

This project is an Intelligent Air Quality Prediction and Health Advisory System designed to provide users with real-time air quality information and health advisories based on the Air Quality Index (AQI). The system utilizes various models and services to predict air quality and generate health advisories for sensitive groups.

## Project Structure

```
air-quality-advisory
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── validators.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── aqi_model.py
│   │   └── advisory_model.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── aqi_service.py
│   │   └── advisory_service.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── constants.py
│   ├── config.py
│   └── app.py
├── tests
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_models.py
│   └── test_services.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd air-quality-advisory
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Access the API at `http://localhost:5000/advisory` to get air quality data and health advisories.

## API Endpoints

- **POST /advisory**: Submit AQI data to receive health advisories.

## Testing

To run the tests, use the following command:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.