import turtle

n_inp = input("Enter number of sides")
n = int(n_inp)
side_len_inp = input("Enter side length")
side_len = int(side_len_inp)

def draw_star(t,n,side_len):
    for i in range(n):
        t.forward(side_len)
        t.right((360.0+180*(n-3))/n)

bob = turtle.Pen()

for j in range(1):
    bob.up()
    bob.backward(side_len/2.0)
    bob.down()
    draw_star(bob,n,side_len)

stopper = input("Hit <enter> to quit.")

turtle.bye()
