from flask import Flask, request, jsonify
import os
import pickle
import pandas as pd
import io  # Import io for StringIO
from tensorflow.keras.models import Sequential  # Importing Sequential model from TensorFlow's Keras

app = Flask(__name__)

# Directory to store received logs
LOG_DIRECTORY = "D:\\Flask Server\\vedanshu"
# Ensure the directory exists
os.makedirs(LOG_DIRECTORY, exist_ok=True)

# Example Keras model (Sequential model example)
model = Sequential()
# Add layers and compile the model...

# Save the model using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

def process_log_file(log_file_path):
    try:
        # Read the binary data from the file
        with open(log_file_path, 'rb') as file:
            log_data = file.read()
        
        # Decode binary data into string
        log_str = log_data.decode('utf-8')
        
        # Assuming CSV format, read into pandas DataFrame
        df = pd.read_csv(io.StringIO(log_str))
        
        # Preprocess your data here if necessary
        # Example: Select relevant columns, handle missing values, normalize data, etc.
        
        return df  # Return processed DataFrame
    except Exception as e:
        print(f"Error processing log data: {e}")
        return None  # Handle the error gracefully

@app.route('/receive_log', methods=['POST'])
def receive_log():
    try:
        log_data = request.data  # Read raw binary data
        
        # Generate a unique filename (you can adjust this as needed)
        filename = os.path.join(LOG_DIRECTORY, f"log_{len(os.listdir(LOG_DIRECTORY)) + 1}.log")

        # Write log_data to the file
        with open(filename, 'wb') as file:
            file.write(log_data)
        
        print(f"Received and saved log data to {filename}")
        return jsonify({'message': 'Log data received and saved successfully.'}), 200
    except Exception as e:
        print(f"Error processing log data: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/analyze_logs', methods=['GET'])
def analyze_logs():
    try:
        # Process each log file in the directory
        results = []
        for log_file in os.listdir(LOG_DIRECTORY):
            log_file_path = os.path.join(LOG_DIRECTORY, log_file)
            log_data = process_log_file(log_file_path)
            
            if log_data is not None:
                # Predict using the loaded model
                predictions = model.predict(log_data)
                
                # Assuming predictions is a list/array of predictions
                # You can further process or filter predictions as needed
                
                results.append(predictions)  # Append predictions to results list
        
        return jsonify({"predictions": results}), 200
    except Exception as e:
        print(f"Error analyzing log data: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=9090, host='0.0.0.0')
