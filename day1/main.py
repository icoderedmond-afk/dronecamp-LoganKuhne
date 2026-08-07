from easytello import tello

def main():
    my_drone = tello.Tello()
    my_drone.takeoff()
    my_drone.forward(60)
    my_drone.land()

if __name__ == "__main__":
    main()
