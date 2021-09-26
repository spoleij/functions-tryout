tafel = int (input ('Van welk getal wilt u de tafel zien?     '))
def tafelVan(tafel:int):
    for tientje in range (1,11):
        print (tientje * tafel)
tafelVan(tafel)