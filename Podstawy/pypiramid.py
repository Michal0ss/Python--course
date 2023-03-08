from urllib import response

from pyramidoop import Pyramid, play_again

while True:
    n = int(input("enter how many numbers: "))
    if n != 0 and n != 1:
        break

Pyramid.pyramid1(n)
Pyramid.pyramid2(n)
while play_again():
    Pyramid.pyramid1(n)
    Pyramid.pyramid2(n)

# sprobowac uzyc random do utworzenia piramidy z randomowych lub pomieszanych z tablicy znakow liczb

