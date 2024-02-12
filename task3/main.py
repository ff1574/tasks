from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/max_interviews', methods=['POST'])
def calculate_max_interviews():
    try:
        # Get the JSON data from the POST request
        data = request.json
        
        # Extract start times and end times from the JSON data
        start_times = data.get('start_times', [])
        end_times = data.get('end_times', [])
        
        # Ensure start times and end times are sorted
        start_times.sort()
        end_times.sort()
        
        # Initialize variables
        max_interviews = 0
        current_interview_end_time = float('-inf')
        
        # Iterate through each interview time
        for start_time, end_time in zip(start_times, end_times):
            # If the current interview starts after the previous one ends, attend this interview
            if start_time >= current_interview_end_time:
                max_interviews += 1
                current_interview_end_time = end_time
        
        # Prepare the response
        response = {
            "max_interviews": max_interviews
        }
        
        # Return the response with status code 200 (OK)
        return jsonify(response), 200
    
    except Exception as e:
        # If an error occurs, return an error response with status code 400 (Bad Request)
        error_response = {"error": str(e)}
        return jsonify(error_response), 400

if __name__ == '__main__':
    app.run(debug=True)
