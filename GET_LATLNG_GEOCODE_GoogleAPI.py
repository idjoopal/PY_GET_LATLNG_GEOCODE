GOOGLE_API_KEY = 'Your-API-KEY' 

############################################################
# function extract_lat_long_via_address
# parameter : insert string address or zipcode
# return : 3 strings
#   - lat : latitude
#   - lng : longitude
#   - name : Standard address used by Google Map
############################################################
def extract_lat_long_via_address(address_or_zipcode):
    lat, lng, name = None, None, None
    api_key = GOOGLE_API_KEY
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint, verify=False)
    if r.status_code not in range(200, 299):
        # 결과 response 코드가 200~299가 아닐 때
        return None, None, None
    try:
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
        name = results['formatted_address']
    except:
        pass
    return lat, lng, name
############################################################

str = 'Seoul'
print(extract_lat_long_via_address(str))
