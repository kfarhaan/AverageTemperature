days_temp = list()
days = int(input("How many day's temperature? "))
value = 0
count = 0

while(True):
    count = len(days_temp) + 1
    if count <= days:
        temp = int(input(f"Day {count}'s high temp: "))
        days_temp.append(temp)
    else: break

average_temp = sum(days_temp) / count
print('Average = ', average_temp)

highest = 0
for d in days_temp:
    if int(d) >= average_temp:
        highest += 1

print(f'{highest} day(s) above average')
