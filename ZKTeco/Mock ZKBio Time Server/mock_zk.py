from http.server import HTTPServer, BaseHTTPRequestHandler
import json, urllib.parse

TOKEN = "mock_token_12345"

class ZKHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if "/api-token-auth/" in self.path or "/jwt-api-token-auth/" in self.path:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"token": TOKEN}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if "/iclock/api/transactions/" in self.path:
            data = {
                "count": 2,
                "next": None,
                "previous": None,
                "data": [
                    {
                        "id": 1,
                        "emp_code": "HR-EMP-00001",
                        "first_name": "Paula",
                        "last_name": "Refaat",
                        "punch_time": "2026-05-15 09:00:00",
                        "punch_state": "0",
                        "punch_state_display": "Check In",
                        "terminal_alias": "Main_Entrance"
                    },
                    {
                        "id": 2,
                        "emp_code": "HR-EMP-00001",
                        "first_name": "Paula",
                        "last_name": "Refaat",
                        "punch_time": "2026-05-15 17:00:00",
                        "punch_state": "1",
                        "punch_state_display": "Check Out",
                        "terminal_alias": "Main_Entrance"
                    }
                ]
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"[ZKMock] {self.address_string()} - {format % args}")

print("Mock ZKBio Time Server running on port 8080...")
HTTPServer(("0.0.0.0", 8080), ZKHandler).serve_forever()