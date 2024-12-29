# METAR Fetcher

[🇹🇷 Türkçe README için tıklayın](TURKISH_README.md)

A Python tool to fetch the latest METAR or SPECI data for a given station code using data from Turkey's Meteorology General Directorate ([MGM](https://rasat.mgm.gov.tr)). The tool fetches the latest METAR or SPECI report, whichever is more recent.

## Features
- Fetches the latest METAR or SPECI data for a specific station.
- Parses HTML content to extract METAR and SPECI information.

## Installation

```bash
# Clone the repository
git clone https://github.com/hasanbahadirkoca/metar-fetcher.git
cd metar-fetcher

# Install dependencies
pip install requests
```

## Usage

### Example Code

```python
from metar_fetcher import MetarFetcher

station_code = "LTCB"  # Replace with your desired station code
fetcher = MetarFetcher(station_code)

try:
    print("Latest METAR:", fetcher.fetch_latest_metar())
except Exception as e:
    print("Error:", str(e))
```

### Output Example

```
Latest METAR/SPECI: LTCB 281250Z 24004KT 9999 FEW020 SCT030 BKN100 15/10 Q1018
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
