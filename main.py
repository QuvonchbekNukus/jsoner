import json
file_name = ""

def get_drivers():
    with open(file_name,"r") as file:
        drivers = json.load(file)
        return drivers
def add_driver(full_name,telefon,car_type,car_num):
    baza = get_drivers()
    last_driver_id = baza[len(baza) - 1]["id"]
    driver = {
        "id":last_driver_id + 1,
        "fullname":full_name,
        "telefon":telefon,
        "car_type":car_type,
        "car_num":car_num,
    }
    baza.append(driver)
    with open(file_name,"w") as file:
        json.dump(baza,file)
def searchby_name(name):
    baza = get_drivers()
    drivers = []
    for i in baza:
        if name.lower() in i["fullname"].lower():
            drivers.append(i)
    return drivers

def json_formatter(mas):
    for i in mas:
        print("ID: ",i["id"])
        print("FIO: ",i["fullname"]),
        print("Telefon: ",i["telefon"]),
        print("Mashina tipi: ",i["car_type"]),
        print("Mashina nomeri: ",i["car_num"],"\n")

def from_input():
    fio = input("FIO: ")
    tel = input("Telefon: ")
    mashinatipi = input("Mashina tipi: ")
    mashinanomeri = input("Mashina nomeri: ")
    add_driver(full_name=fio,car_num=mashinanomeri,telefon=tel,car_type=mashinatipi)

def delete(id):
    baza = get_drivers()
    for i in baza:
        if i["id"] == id:
            baza.remove(i)
    with open(file_name,"w") as file:
        json.dump(baza,file)

def searchby_carnum(car_num):
    baza = get_drivers()
    driver = []
    for i in baza:
        if i["car_num"].lower() == car_num.lower():
            driver.append(i)
    return driver
