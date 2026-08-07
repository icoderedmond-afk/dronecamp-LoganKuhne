from easytello import tello

drone = tello.Tello()

def setup():
    drone.takeoff()
    drone.up(60)

def leg_one():
    for _ in range(4):
        drone.cw(90)
        drone.forward(40)

def leg_two():
    for _ in range(4):
        drone.ccw(90)
        drone.forward(40)

def leg_three():
    for _ in range(4):
        drone.up(40)
        drone.down(40)

def tear_down():
    drone.land()

def main():
    setup()
    leg_one()
    leg_two()
    leg_three()
    tear_down()

if __name__ == "__main__":
    main()
