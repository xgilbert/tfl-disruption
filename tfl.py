import requests


class TFL:
    url_disruption = "https://api.tfl.gov.uk/Line/"

    def get_disruptions(self, lines):
        lines = ",".join(lines)
        resp = requests.get(f"https://api.tfl.gov.uk/Line/{lines}/Disruption")
        return resp.json()
