def bank(a, years):

    for year in range(years):
        a += a * 0.10
    return a


deposit = 3000
years = 5
final_anount = bank(3000, 5)

print(f'Сумма на счете через', years, 'лет:', final_anount, 'руб.')