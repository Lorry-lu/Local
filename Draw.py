import turtle

def draw_san(distance):
    if distance > 10:
        turtle.forward(distance)
        print("向前",distance)
        turtle.right(20)
        print("右转20")
        draw_san(distance - 20)

        turtle.left(40)
        print("左转40")
        draw_san(distance - 20)

        turtle.right(20)
        print("再右转20")
        turtle.backward(distance)
        print("向后",distance)

def main():
    print("a = {0},b = {1},c = {0}".format(11,22))
    turtle.left(90)
    draw_san(60)
    turtle.exitonclick()
if __name__ == '__main__':
    main()