# Maximum Non-Overlapping Job Interviews API

This REST API endpoint is designed to calculate the maximum number of non-overlapping job interviews a person can attend. It processes POST requests containing two lists: start times and end times of job interviews. The API calculates the maximum number of interviews a person can attend without any overlap and returns the result. Edge case where the interview that starts at the same time as the previous ends counts.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.x
- Flask (install using `pip install Flask`)

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the Flask application by executing `python app.py`.
4. Use Postman or any other HTTP client to send POST requests to the `/max_interviews` endpoint with JSON data containing start times and end times of job interviews. In case of using Postman, add a Header called `content-type` and set the value to `application/json`. Then copy the JSON file you want to test in the Body section. Make the method `POST` and send the request to `http://127.0.0.1:5000/max_interviews` if you are running the app locally with a default port.
5. The endpoint will process the data and return a response indicating the maximum number of non-overlapping job interviews.

## Sample Request

```json
{
  "start_times": [10, 25, 30, 40, 50, 52],
  "end_times": [25, 29, 45, 45, 55, 75]
}
```

## Sample Response

For the following sample request, this would be the response

```json
{
  "max_interviews": 4
}
```
