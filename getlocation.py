import requests

url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

querystring = {"query":"hotels+in+haldwani","key":"AIzaSyCCnvueNvov3rXCqQKL5jeq8b15RWI8h-Y"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "fb3b1ca6-c6de-48da-8fdc-dca5a755028c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)