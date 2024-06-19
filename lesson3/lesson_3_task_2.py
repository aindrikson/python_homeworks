from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 15", "+79875632587")
phone2 = Smartphone("Sumsung", "Galaxy A5", "+74563214569")
phone3 = Smartphone("Google", "Pixel", "+79632147896")
phone4 = Smartphone("Honor", "X8a", "+74569871236")
phone5 = Smartphone("Xiaomi", "Redmi 9A", "+79874561234")

catalog.append (phone1)
catalog.append (phone2)
catalog.append (phone3)
catalog.append (phone4)
catalog.append (phone5)

for phone in catalog:
    print(f"{phone.mark} - {phone.model} - {phone.phone_number}")