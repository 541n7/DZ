from time import sleep
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        z = 0
        while z < 3:
            print('Светофор переключается \n', TrafficLight.__color[z])
            if z == 0:
                sleep(7)
            elif z == 1:
                sleep(2)
            elif z == 2:
                sleep(6)
            z += 1
TrafficLight = TrafficLight()
TrafficLight.running()