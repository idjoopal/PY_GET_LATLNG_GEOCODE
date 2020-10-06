############################################################
# function extract_lat_long_via_address
# parameter : insert string address or zipcode
# return : 3 strings
#   - lat : latitude
#   - lng : longitude
#   - name : Standard address used by OpenStreet Map
############################################################
def extract_lat_long_via_address(address_or_zipcode):
    lat, lng, name = None, None, None
    
    base_url = "https://nominatim.openstreetmap.org/search"
    endpoint = f"{base_url}?q={address_or_zipcode}&format=geocodejson"
    
    r = requests.get(endpoint, verify=False)
    if r.status_code not in range(200, 299):
        # print("not 200")
        return None, None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        results = r.json()
        lat = results['features'][0]['geometry']['coordinates'][1]
        lng = results['features'][0]['geometry']['coordinates'][0]
        name = results['features'][0]['properties']['geocoding']['label']
    except:
        pass
    return lat, lng, name
    
############################################################

str = 'Seoul'
print(extract_lat_long_via_address(str))
