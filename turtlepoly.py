import turtle

n_inp = input("Enter number of sides")
n = int(n_inp)
side_len_inp = input("Enter side length")
side_len = int(side_len_inp)

def draw_reg_polygon(t,n,side_len):
    for i in range(n):
        t.forward(side_len)
        t.left(360.0/n)

t = turtle.Pen()

draw_reg_polygon(t,n,side_len)

stopper = input("Hit <enter> to quit.")

turtle.bye()
