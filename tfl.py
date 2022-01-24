import requests


class TFL:
    base_url = "https://api.tfl.gov.uk/Line/"

    def get_disruptions(self, lines):
        # lines = ",".join(lines)
        resp = requests.get(f"https://api.tfl.gov.uk/Line/{lines}/Disruption")
        return resp.json()

    def get_status_by_mode(self, mode):
        resp = requests.get(f"https://api.tfl.gov.uk/Line/Mode/{mode}/Status")
        return resp.json()
