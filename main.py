import requests
from io import BytesIO
import json
import openpyxl


class SharePointClient:

    def __init__(self, url, site, token_url, payload):
        self.url = url
        self.site = site
        self.token_url = token_url
        self.payload = payload


    def get_token(self):
        url = self.token_url
        payload = self.payload
        hed = {'Content-Type': 'application/x-www-form-urlencoded'}

        try:
            response = requests.post(url, headers=hed, data=payload)
            json_response = json.loads(response.content)
            return json_response["access_token"]

        except KeyError as ex:
            print(f"An exception of type {type(ex).__name__} occured in class SharePointClient.get_token()\nFollowing Key was not found:\n{ex.args}")
        except requests.exceptions.HTTPError as ex:
            print(f"An exception of type {type(ex).__name__} occured in class SharePointClient.get_token()\nArguments:\n{ex.args}")

    def post_to_shp(self, token, file_data, file_name, env):
        shp_url = f"{self.url}{self.site}_api/web/GetFolderByServerRelativeUrl('/sites/Placeholdername/Shared Documents/PyUploads/{env}')/Files/add(url='{file_name}.xlsx',overwrite=false)"
        hed = {'Authorization': 'Bearer ' + token}
        try:
            response = requests.post(url=shp_url, headers=hed, data=file_data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            print(f"An exception of type {type(ex).__name__} occured in class SharePointClient.post_to_shp()\nArguments:\n{ex.args}")
