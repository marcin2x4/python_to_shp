# python_to_shp
Save files to SharePoint via API call

Sample usage:

```
shp = SharePointClient(URL, SITE, TOKEN_URL, PAYLOAD)

logging.info("Getting token...")
token = shp.get_token()

logging.info("Posting to ShP...")
shp.post_to_shp(token, file_content, f"{REPORT}_{datetime.today().strftime('%Y%m%d')}", ENVS)
```
