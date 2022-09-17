from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()



drone.takeoff()

x = '1'
while(x!='2'):
    print(drone.get_battery())
    x = input()
    drone.flip(x)
    drone.flip(x)
    sleep(3)

drone.land();
