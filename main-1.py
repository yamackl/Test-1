import random

karakterler = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

a = int(input("Kaç karakterlik bir şifre oluşturmak istersiniz? "))

if a <= 50 and a >= 5:
    b = ""
    for i in range(a):
        b += random.choice(karakterler)
    print(b)

else:
    print("min 5 max 50 karakter girebilirsiniz")

