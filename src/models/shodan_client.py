from shodan import APIError
from shodan import Shodan


class ShodanClient:
    def __init__(self, api_key: str) -> None:
        self.client = Shodan(api_key)

    def minecraft_servers(self):
        try:
            results = self.client.search("minecraft")
            print("Results found: {}".format(results["total"]))
            for result in results["matches"]:
                print("IP: {}".format(result["ip_str"]))
                print(result["data"] + "\n")
        except APIError as e:
            print("Error: {}".format(e))
