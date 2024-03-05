import rocketreach
import os
import requests

## FOR ROCKET REACH API / CHECK IF SDK IS WORKING

## TO CHECK IF GET RESPONSE IS SUCCESSFUL
api_key = '1341aa3ke57a808589fd6ee516c9ef17cfecd7a3'
api_url = 'https://rocketreach.co/'
endpoint = '/api_generic/'
API_KEY = '1341aa3ke57a808589fd6ee516c9ef17cfecd7a3'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# NOTE:
''' endpoint are the different routes in the API
    api_generic OR api_searchS
'''


# Check that the SDK is working
def check_sdk():
    rr = rocketreach.Gateway(api_key=os.environ.get(api_key))
    rr.api_key = API_KEY
    print("[!] API KEY " + API_KEY)
    result = rr.account.get()
    print(f"Result: {result}")
    if result.is_success:
        print(f'Success: {result.account}')
    else:
        print(f'Error: {result.message}!')


## SAMPLE LOOKUPM USING rr.person.lookup
def lookup_person():
    lookup_result = rr.person.lookup(name='Marc Benioff', current_employer='Salesforce')
    if lookup_result.is_success:
        print(lookup_result.person)
    lookup_result = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff')
    if lookup_result.is_success:
        print(lookup_result.person)


def response_handler(response):
    try:
        print(f"Response: {api_url} + {endpoint}, {headers}")
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Error: {response.status_code},\n {response.reason}")
    except Exception as e:
        print(f"Error: {e}")

print("[!] checkiqng SDK")
check_sdk()

'''
r = requests.get('https://rocketreach.co/', headers=headers)
print(r.status_code)
print(r.reason)
#print(r.text)

response = requests.get(api_url + endpoint, headers=headers)
response_handler(response)
'''
