# Unauthorized Sales Detection API

This REST API endpoint is designed to identify unauthorized sales transactions by comparing product listings with actual sales records. It receives two lists in JSON format: one containing product listings (including product ID and authorized seller ID) and the other containing actual sales transactions (including product ID and seller ID). The API then processes these lists and returns any unauthorized sales transactions found.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.x
- Flask (install using `pip install Flask`)

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the Flask application by executing `python app.py`.
4. Use Postman or any other HTTP client to send POST requests to the `/detect_unauthorized_sales` endpoint with JSON data containing product listings and sales transactions. In case of using Postman, add a Header called `content-type` and set the value to `application/json`. Then copy the JSON file you want to test in the Body section. Make the method `POST` and send the request to `http://127.0.0.1:5000/detect_unauthorized_sales` if you are running the app locally with a default port.
5. The endpoint will process the data and return a response indicating any unauthorized sales transactions.

## Sample Request

```json
{
  "productListings": [
    {"productID": "123", "authorizedSellerID": "A1"},
    {"productID": "456", "authorizedSellerID": "A2"},
    {"productID": "789", "authorizedSellerID": "A3"}
  ],
  "salesTransactions": [
    {"productID": "123", "sellerID": "B2"},
    {"productID": "456", "sellerID": "A2"},
    {"productID": "789", "sellerID": "C1"},
    {"productID": "123", "sellerID": "A1"},
    {"productID": "456", "sellerID": "B3"}
  ]
}```
