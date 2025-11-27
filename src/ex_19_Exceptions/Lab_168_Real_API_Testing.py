import requests



try:
    url= input("Enter the url\n")
    #response=requests.get("https://www.google.com")
    response=requests.get(url,timeout=3)
    print(response.status_code)

except requests.exceptions.ConnectionError:
    print('Error due to wrong URL or connectioned failed')

except requests.exceptions.Timeout:
    print("Timeout error ,not able to load the URL")

except Exception as e:
    print(e)


