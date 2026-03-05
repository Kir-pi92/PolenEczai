# Polen Eczanesi Nöbetçi Eczane Ekranı 🌙💊

Eskişehir Eczacı Odası verilerini kullanarak, Polen Eczanesi için özel olarak hazırlanmış modern, hızlı ve şık bir nöbetçi eczane bilgi ekranı projesidir.

## ✨ Özellikler

- **Canlı ve Güncel Veri:** Eskişehir Eczacı Odası'ndan anlık olarak nöbetçi eczaneleri çeker.
- **Modern Arayüz (Glassmorphism):** Koyu tema (Dark Mode), cam efekti (Glassmorphism) ve şık renk geçişleriyle göze hitap eden premium bir tasarım.
- **Otomatik QR Kod Üretimi:** Eczane lokasyonlarını haritada kolayca bulabilmek için navigasyon linkli QR kodlar otomatik oluşturulur. Her eczane kendine ait bir QR koda sahiptir.
- **Hava Durumu ve Saat:** Ekranın sağ üst köşesinde canlı saat ve Eskişehir için hava durumu bilgisi gömülüdür.
- **Yazdırma Modu (Print Uyumlu):** Sayfayı yazdırırken arka plan efektlerini, gereksiz butonları gizler ve eczane listesini temiz, kağıt tasarrufu sağlayan bir formatta A4 çıktısına uygun hale getirir.
- **Python Yerel Sunucu ve Scraper:** CORS engellerine takılmadan veriyi lokal ağdaki cihazlara (tablet, kiosk vb.) iletmek için hafif bir Python HTTP API (`server.py`) ve veri kaydedici (`scraper.py`) barındırır.

## 🚀 Kurulum ve Kullanım

1. Bilgisayarınızda **Python 3.x** kurulu olduğundan emin olun.
2. Proje dizininde gerekli kütüphaneleri (varsa) kurun ve terminalden sunucuyu başlatın:
   ```bash
   python server.py
   ```
3. Terminalde gösterilen `http://<LOKAL_IP_ADRESI>:5050` (örneğin `http://192.168.1.x:5050`) adresini kullanarak tabletinizden veya kiosk cihazınızdan sisteme bağlanın.
4. (Opsiyonel) Eğer veriyi statik bir `.json` olarak saklamak isterseniz `python scraper.py` dosyasını çalıştırabilirsiniz.

Bu sistem Eczane içindeki vitrin tabletleri ve bilgilendirme ekranları için tasarlanmıştır. Herkese kolaylıklar dileriz!
