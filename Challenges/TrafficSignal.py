# Challenge 1
# You have to ask about the color of the traffic light from the user, if:
# it is green, then print go,
# it is yellow, then print wait,
# it is red, then print stop
# green -> go
# yellow -> wait
# red -> stop
def TrafficSignal_Alert(color):
    if color == "green":
        print("go")
    elif color == "red":
        print("stop")
    elif color == "yellow":
        print("wait") 

color = str(input("Traffic Alert : "))
TrafficSignal_Alert(color)
        
            
