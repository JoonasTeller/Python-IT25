print("Tere, maailm!")
aasta = str(2020)
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = aasta+lause_keskosa+liblikas
print(lause)

#Pilved
#korgus = float(input("Pilvede aluse kõrgust km:"))
#print(type(korgus))
#Pilvede kõrgus suurem kui 6.0
#if korgus > 6.0:
#    print("Need on ülemised pilved")
#else:
#    print("Need ei ole ülemised pilved")

#bussid
inim = 40
kohad = 40
tais = inim // kohad
jaak = inim % kohad
#kui viimases on rohkem kui 0
if jaak > 0:
    lisa = 1
else:
    lisa = 0
bussid = tais + lisa

print(f"Täis: {tais}")
print(f"Viimases: {jaak}")
print(f"Busse kokku: {bussid}")
