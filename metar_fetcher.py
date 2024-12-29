import requests

class MetarFetcher:
    def __init__(self, station):
        self.station = station

    def fetch_latest_metar(self):
        url = f"https://rasat.mgm.gov.tr/result?stations={self.station}&obsType=1&hours=0"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Failed to fetch the page")

        content = response.text
        rows = content.split('<li>')[1:]

        latest_metar = None
        latest_time = None

        for row in rows:
            try:
                time_value = row.split('<span>')[1].split('</span>')[0].strip()
                metar_value = row.split('<pre>')[1].split('</pre>')[0].strip()

                if not latest_time or time_value > latest_time:
                    latest_time = time_value
                    latest_metar = metar_value
            except IndexError:
                continue

        if not latest_metar:
            raise Exception("Failed to extract the latest METAR")

        return latest_metar

if __name__ == "__main__":
    try:
        station_code = "LTCB"
        fetcher = MetarFetcher(station_code)
        print("Latest METAR:", fetcher.fetch_latest_metar())
    except Exception as e:
        print("Error:", str(e))
