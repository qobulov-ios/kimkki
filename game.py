import random
# """salom sz bzni oynmzga xush kelbsz oynab omadizni sinab koring yutvolshngz mumkin sovgalardi"""
# print("------------------------------------------------------------------")



# son = int(input("son kiritin"))


# presents = ['mashina', 'telfon' , 'umraga yolanma' , 'televizor' ,  'kanditsyaner'  , 'hichbalo' ,   ]



# objects = random.choices(presents)

# sonlar = random.randint(1 , 6)

# if sonlar == 1:
#     print(f"sz  {objects} yutdiz tabrikleman")
#     print('--------------------------------------')

# elif sonlar == 2:
#     print(f"sz  {objects} yutdz tabrikleman ")
#     print('--------------------------------------')

# elif sonlar == 3:
#     print(f"sz  {objects} yutdz tabrikleman ")
#     print('--------------------------------------')

# elif sonlar == 4:
#     print(f"sz  {objects} yutdz tabrikleman ")
#     print('--------------------------------------')

# elif sonlar == 5:
#     print(f"sz  {objects} yutdz tabrikleman ")
#     print('--------------------------------------')

# elif sonlar == 6:
#     print(f"sz  {objects} yutdz tabrikleman ")
#     print('--------------------------------------')






pox = int(input("pul kiritng :"))
if pox > 10:
    print("Pulingiz 10 mingdan kop oynashingz mumkn")
elif pox == 10:
    print("Pulingiz 10 min ekan ishlayapti ")
else :
    print("pulingiz kam")

sovgalar = ['malibu', 'ayqcha' , 'umraga yolanma' , 'xc narsa' ,  'kr sovun'  , 'cola' , 'xc balo' , 'notbook'  ]
jam = random.choices(sovgalar) 

print(jam)
