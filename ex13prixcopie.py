nbr=int(input("entrer le nombre de copie svp : "))
if nbr <= 10 :
    prix=nbr*0.3
elif nbr <=30 :
    prix=10*0.3 + (nbr-10)*0.25
else :
    prix=10*0.30 + 20*0.25 + (nbr-20)*0.2
print("le prix est : ",prix)
