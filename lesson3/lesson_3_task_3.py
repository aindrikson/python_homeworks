from adress import Adress
from mailing import Mailing

to_adress = Adress("214032", "Смоленск", "Бабушкина", "2А", "35")
from_adress = Adress("410018", "Саратов", "Менякина", "3А", "12")
mailing = Mailing (from_adress, to_adress, "330", "6987425684")

print(f"Отправление {mailing.track} из {mailing.from_adress.index}, {mailing.from_adress.city},"
f" {mailing.from_adress.street}, {mailing.from_adress.house} - {mailing.from_adress.apartment}"
f" в {mailing.to_adress.index}, {mailing.to_adress.city}, {mailing.to_adress.street},"
f" {mailing.to_adress.house} - {mailing.to_adress.apartment}. Cтоимость {mailing.cost} рублей.")