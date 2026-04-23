import math

def create_point(x, y,):
    point = [x, y]
    return point

x1 = float(input("Anna x1 arvo: "))
y1 = float(input("Anna y1 arvo: "))
Piste1 = create_point(x1,y1)

x2 = float(input("Anna x2 arvo: "))
y2 = float(input("Anna y2 arvo: "))
Piste2 = create_point(x2,y2)

def distance(p1, p2):
    dist = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    return dist

tulos = distance(Piste1,Piste2)
print(f"Pisteiden p1 ja p2 etäsisyys on {tulos}")