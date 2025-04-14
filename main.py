
import requests

def check_phone_number(phone_number):
    api_key = F'd9862b6fc7916fc0e9ad166e78318189'
    url = f"https://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data.get("valid"):
        print(f"{phone_number} is a valid phone number!")
    else:
        print(f"{phone_number} is not valid.")
        
phone_number = input("Enter a phone number (include + and country code ): ")
check_phone_number(phone_number)



    

