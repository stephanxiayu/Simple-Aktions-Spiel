from replit import clear
from dictonary import logo

print(logo)



liste={}
stopping=False

def findHighestValue(alle_gebote):
    highestgebot=0
    for key in alle_gebote:
       amount= alle_gebote[key]
       if amount>highestgebot:
           highestgebot=amount
           winner=key     
    print(f"Winner ist {winner} mit dem gebot ${highestgebot}")       


while not stopping:
    name=input("Dein Name ist? ")
    gebot=int(input("dein Gebot in $ ist? "))
    liste[name]=gebot
    neuesGebot=input("neues Gebot? ja oder nein ").lower()
    if neuesGebot=="nein":
       stopping=True
    else:
        clear()
        stopping=False  
  
findHighestValue(alle_gebote=liste)
   