def calculateBissextusYear(year):
    if(year%4 != 0):
        return False
    elif(year%4 == 0):
        if(year%100 == 0 and year%400 != 0):
            return False
        elif(year%100 == 0 and year%400 == 0):
            return True
    return True

#Count the quantity of bissextus yeats between the given year and 1900
def quantityOfBissextusYears(year):
    # Variable responsible for adding the one plus day in bissextus years
    sumBissextus = 0
    while (year > 1900):
        if (calculateBissextusYear(year) == True):
            sumBissextus += 1
            year -= 1
        else:
            year -= 1
    return sumBissextus

#Count the number of days between the year choosen and 1900
def countNumberOfDays(year):
    sumBissextus =  quantityOfBissextusYears(year)
    quantityOfDays = ((year - 1900) * 365) + sumBissextus
    return  quantityOfDays

print(countNumberOfDays(2016))
print(quantityOfBissextusYears(2016))
