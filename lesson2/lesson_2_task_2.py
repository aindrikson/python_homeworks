year = int(input('Введите любой год: '))
def is_year_leap(year):
    if year % 4 != 0:
         return False
    else:
        return True
result = is_year_leap(year)    
print('год:', year, result)