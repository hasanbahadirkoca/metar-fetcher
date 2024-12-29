# METAR Alıcı

[🇬🇧 English README](README.md)

Bir istasyon kodu için en güncel METAR veya SPECI verilerini Türkiye Meteoroloji Genel Müdürlüğü'nden ([MGM](https://rasat.mgm.gov.tr){:target="_blank"}) alan Python aracı. Bu araç, METAR veya SPECI raporlarından hangisi daha güncel ise onu getirir.

## Özellikler
- Belirtilen bir istasyon için en güncel METAR veya SPECI verisini getirir.
- HTML içeriğini ayrıştırarak METAR ve SPECI bilgilerini çıkartır.

## Kurulum

```bash
# Depoyu klonlayın
git clone https://github.com/hasanbahadirkoca/metar-fetcher.git
cd metar-fetcher

# Bağımlılıkları yükleyin
pip install requests
```

## Kullanım

### Örnek Kod

```python
from metar_fetcher import MetarFetcher

station_code = "LTCB"  # İstasyon kodunuzu buraya girin
fetcher = MetarFetcher(station_code)

try:
    print("Latest METAR:", fetcher.fetch_latest_metar())
except Exception as e:
    print("Hata:", str(e))
```

### Çıktı Örneği

```
Latest METAR: LTCB 281250Z 24004KT 9999 FEW020 SCT030 BKN100 15/10 Q1018
```

## Katkıda Bulunun
Katkılar memnuniyetle karşılanır! Lütfen bir konu açın veya iyileştirmelerle bir pull request gönderin.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.
