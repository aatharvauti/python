import requests


print("Enter Date as dd-mm-yyyy: ")
date = input()

print("Enter Pincode: ")
pin = int(input())

print("Enter Age: ")
age = int(input())

r = requests.get(f'https://cdn-api.co-vin.in/api/v4/appointment/sessions/public/calendarByDistrict?district_id=395&date={date}')
data = r.json()

print('\nVaccine Centres: \n')

def check_hospitals():
    for x in range(len(data["centers"])):
        for y in range(len(data["centers"][x]["sessions"])):
            def print_info():
                print("Name: \t\t" + data["centers"][x]["name"])
                print("Address: \t" + data["centers"][x]["address"])
                print("Fee Type: \t" + data["centers"][x]["fee_type"])
                print("Vaccine: \t" + str(data["centers"][x]["sessions"][y]["vaccine"]))
                print("Slots: \t\t" + str(data["centers"][x]["sessions"][y]["slots"]))
                print("Availability:")
                print("\tFirst Dose: \t" + str(data["centers"][x]["sessions"][y]["available_capacity_dose1"]))
                print("\tSecond Dose: \t" + str(data["centers"][x]["sessions"][y]["available_capacity_dose2"]))
                if data["centers"][x]["sessions"][y]["precaution_dose"]:
                    print("\tBooster Dose: \t" + str(data["centers"][x]["sessions"][y]["precaution_dose"]))
                print('\n')
            if data["centers"][x]["pincode"] == pin:
                if age >= 18:
                    if data["centers"][x]["sessions"][y]["min_age_limit"] == 18 or data["centers"][x]["sessions"][y]["min_age_limit"] == 15:
                        print_info()
                else:
                    if data["centers"][x]["sessions"][y]["min_age_limit"] == 15:
                        print_info()

check_hospitals()

