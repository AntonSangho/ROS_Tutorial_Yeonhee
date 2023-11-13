from picozero import DistanceSensor
from time import sleep

ds = DistanceSensor(echo=20, trigger=21)

while True:
    dscm = ds.distance * 100
    print(dscm)
    sleep(1)