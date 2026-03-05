import urllib.request
import json
import datetime
import time
import ssl

url = "https://www.eskisehireo.org.tr/eskisehir-nobetci-eczaneler/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
}

# SSL dogrulama sorunlari icin
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

max_retries = 3
html_code = None

for attempt in range(1, max_retries + 1):
    print(f"Deneme {attempt}/{max_retries} - Veri cekiliyor: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=60, context=ctx) as response:
            html_code = response.read().decode('utf-8')
        
        print(f"Veri basariyla cekildi. Uzunluk: {len(html_code)} karakter.")
        
        if len(html_code) < 100:
            print("Gelen HTML verisi cok kisa. Tekrar deneniyor...")
            html_code = None
            time.sleep(5)
            continue
        
        break  # Basarili, donguyu kir
        
    except Exception as e:
        print(f"Deneme {attempt} basarisiz: {str(e)}")
        if attempt < max_retries:
            print(f"{5 * attempt} saniye bekleniyor...")
            time.sleep(5 * attempt)
        else:
            print("Tum denemeler basarisiz oldu.")

if html_code and len(html_code) >= 100:
    data = {
        "contents": html_code,
        "last_updated": datetime.datetime.now().isoformat()
    }
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
        
    print("Veri 'data.json' dosyasina basariyla kaydedildi.")
else:
    print("HATA: Gecerli veri cekilemedi!")
    exit(1)
