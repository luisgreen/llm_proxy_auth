from flask import Flask, request, Response, jsonify
import requests
import os

app = Flask(__name__)
# Configure these variables with your LLM API details
LLM_API_URL = os.getenv('LLM_API_URL')
REQUIRED_BEARER_TOKEN = os.getenv('REQUIRED_BEARER_TOKEN')


def stream_response(response):
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            yield chunk


@app.route('/', defaults={'path': ''}, methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"])
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"])
def proxy_request(path):
    # Check for Authorization header
    print(request.json)
    auth_header = request.headers.get('Authorization')
    if auth_header != f"Bearer {REQUIRED_BEARER_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

    # Forward request to LLM API with the same headers and body
    try:
        headers = {
            # 'Authorization': auth_header,
            'Content-Type': 'application/json',
        }

        # Stream the response
        response = requests.post(
            f"{LLM_API_URL}/{path}",
            headers=headers,
            json=request.json,
            stream=True
        )

        return Response(stream_response(response), content_type=response.headers.get('Content-Type'))

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to connect to LLM API", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
