amount = int(input(""))
if (amount >= 100 and amount <= 100000):

    n_t = amount / 1000
    n_f = (amount - n_t * 1000) / 500
    n_h = (amount - n_f * 500 - n_t * 1000) / 100
    print(str(n_t) + " of 1000 Rupees")
    print(str(n_f) + " of 500 Rupees")
    print(str(n_h) + " of 100 Rupees")

else:
    print("Amount out of range")

