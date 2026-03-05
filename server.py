import http.server
import socketserver
import urllib.request
import json
import socket

PORT = 5050

class PharmacyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/api/nobetci'):
            try:
                # Eczacı odasına doğrudan sunucudan (bilgisayardan) istek atıyoruz
                req = urllib.request.Request(
                    "https://www.eskisehireo.org.tr/eskisehir-nobetci-eczaneler/",
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
                )
                with urllib.request.urlopen(req, timeout=10) as response:
                    html = response.read().decode('utf-8')
                
                # Başarılı cevabı JSON olarak dönüyoruz
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response_data = json.dumps({"contents": html}, ensure_ascii=False)
                self.wfile.write(response_data.encode('utf-8'))
            except Exception as e:
                # Hata durumunda
                self.send_response(500)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                error_data = json.dumps({"error": str(e)})
                self.wfile.write(error_data.encode('utf-8'))
        else:
            # Diğer tüm durumlarda (index.html vb.) standart statik sunucu gibi davran
            super().do_GET()

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

with socketserver.TCPServer(("", PORT), PharmacyHandler) as httpd:
    ip = get_local_ip()
    print("=====================================================")
    print(" Nöbetçi Eczane Sistemi Çalışıyor!")
    print(" Lütfen tabletinizden şu adrese girin:")
    print(f" ---> http://{ip}:{PORT}")
    print("=====================================================")
    httpd.serve_forever()
