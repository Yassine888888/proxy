from flask import Flask, request, Response
import requests
from requests_ntlm import HttpNtlmAuth
import json

app = Flask(__name__)

@app.route("/relai", methods=["POST"])
def relai():
    url = "http://197.13.22.3:7048/SMART/ODataV4/ODATA_TestOdata?company=IRPP2"
    data = request.get_json()
    auth = HttpNtlmAuth("YMI", "b2m-IT@2024")
    headers = {"Content-Type": "application/json"}
    try:
        r = requests.post(url, headers=headers, data=json.dumps(data), auth=auth, timeout=100, verify=False)
        return Response(r.content, status=r.status_code, content_type=r.headers.get('Content-Type'))
    except Exception as ex:
        return Response(f"Erreur proxy: {ex}", status=500)

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

