# Compare last digit of six numbers to remainder of five digits / 7 

while 1:
    six_tick = int(input("Enter six digits: "))
    last_six = six_tick % 10

    five_tick = int(six_tick / 10) # auto round so must have int
    last_five = five_tick % 7      

    print(bool(last_six == last_five))



