from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the detect_unauthorized_sales endpoint, allow only the POST method
@app.route('/detect_unauthorized_sales', methods=['POST'])

# Define the detect_unauthorized_sales function
def detect_unauthorized_sales():
    try:
        # Get the JSON data from the POST request
        data = request.json
        
        # Extract product listings and sales transactions from the JSON data
        product_listings = data.get('productListings', [])
        sales_transactions = data.get('salesTransactions', [])
        
        # Create a dictionary to store authorized seller IDs for each product
        authorized_sellers = {listing['productID']: listing['authorizedSellerID'] for listing in product_listings}
        
        # Initialize a dictionary to store unauthorized sales
        unauthorized_sales = {}
        
        # Check each sales transaction against the authorized seller ID
        for transaction in sales_transactions:
            product_id = transaction['productID']
            seller_id = transaction['sellerID']
            authorized_seller_id = authorized_sellers.get(product_id)
            
            # If the seller is not authorized, add the transaction to unauthorized_sales
            if authorized_seller_id and seller_id != authorized_seller_id:
                if product_id not in unauthorized_sales:
                    unauthorized_sales[product_id] = []
                unauthorized_sales[product_id].append(seller_id)
        
        # Prepare the response
        response = {
            "unauthorizedSales": [{"productID": product_id, "unauthorizedSellerID": unauthorized_sellers} for product_id, unauthorized_sellers in unauthorized_sales.items()]
        }
        
        # Return the response with status code 200 (OK)
        return jsonify(response), 200
    
    except Exception as e:
        # If an error occurs, return an error response with status code 400 (Bad Request)
        error_response = {"error": str(e)}
        return jsonify(error_response), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
