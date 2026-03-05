import urllib.request
import json
import datetime
import os

url = "https://www.eskisehireo.org.tr/eskisehir-nobetci-eczaneler/"

req = urllib.request.Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
)

print(f"Veri çekiliyor: {url}")
try:
    with urllib.request.urlopen(req, timeout=30) as response:
        html_code = response.read().decode('utf-8')
        
    print(f"Veri başarıyla çekildi. Uzunluk: {len(html_code)} karakter.")
    
    if len(html_code) < 100:
        raise Exception("Gelen HTML verisi çok kısa. Muhtemelen bir hata var.")
        
    data = {
        "contents": html_code,
        "last_updated": datetime.datetime.now().isoformat()
    }
    
    # Save the data exactly where index.html can find it
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
        
    print("Veri 'data.json' dosyasına başarıyla kaydedildi.")

except Exception as e:
    print(f"Hata oluştu: {str(e)}")
    exit(1)
