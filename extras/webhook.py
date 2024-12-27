
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''curl -X POST -H "Content-Type: application/json" -d '{"event":"test"}' https://vickswebhook.pythonanywhere.com/webhook'''

@app.route('/webhook', methods=['POST'])
def webhook():
    # Ensure the request is a POST request
    if request.method == 'POST':
        try:
            # Get the JSON payload from the request
            data = request.json

            # Log the received data (for debugging purposes)
            print("\nReceived webhook data:", data)

            # Process the data (customize this logic as needed)
            # Example: Log a specific field if it exists
            if 'event' in data:
                event_type = data['event']
                print(f"\nProcessing event: {event_type}")

            # Respond to the webhook sender
            return jsonify({'status': 'success', 'message': 'Webhook received'}), 200
        except Exception as e:
            print(f"Error processing webhook: {e}")
            return jsonify({'status': 'error', 'message': str(e)}), 400
    else:
        return jsonify({'status': 'error', 'message': 'Invalid request method'}), 405

if __name__ == '__main__':
    app.run(debug=True, port=5000)
