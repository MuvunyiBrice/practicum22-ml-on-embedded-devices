from cmath import sin
import math
import numpy as np


def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    dx = x1 - x0
    dy = y1 - y0

    d=math.sqrt((dx)**2 + (dy)**2)
    # d = math.hypot(dx, dy)
    # print(d)
    
    # non intersecting
    if d > (r0 + r1) :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)

        # breakpoint()
        x2= x0 + (dx*(a/d))   
        y2= y0 + (dy*(a/d))

        # print(f"x2: {x2}, y2: {y2}")
        rx = -dy * (h/d)
        ry = dx * (h/d)

        x3=x2+rx
        x4=x2-rx 

        y3=y2+ry
        y4=y2-ry
        
        return (x3, y3, x4, y4)

#origin coordinates
origx, origy = 0.0, 0.0

# open file with coordinates and angles
with open('dummy_input.txt') as f:
    for l in f:
        field = l.strip().split(" ") # retrieve elements separated by spaces
        field=[float(x) for x in field if x] # remove space
        x1, y1, x2, y2, x3, y3 = field[0], field[1], field[2], field[3], field[4], field[5]
        a1, a2 = field[6], field[7]
        
        d1 = math.dist([x1,y1], [x2,y2]) #calculate distance between l1 & l2
        d2 = math.dist([x2,y2], [x3,y3]) #calculate distance between l2 & l3

        print(f"distance 1: {d1},\ndistance 2: {d2}")
        r1 = (d1/2)/np.sin(np.deg2rad(a1))
        r2 = (d2/2)/np.sin(np.deg2rad(a2))
        print(f"radius 1: {r1},\nradius 2: {r2}")
        h1 = (d1/2)/np.tan(np.deg2rad(a1))
        h2 = (d2/2)/np.tan(np.deg2rad(a2))
        print(f"height 1: {h1},\nheight 2: {h2}")

        x_mid1 = (x1 + x2)/2
        y_mid1 = (y1 + y2)/2
        
        x_mid2 = (x2 + x3)/2
        y_mid2 = (y2 + y3)/2

        xc1,yc1,xc2,yc2 =  get_intersections(x1, y1, r1, x_mid1, y_mid1, h1)
        xC1, yC1 = 0.0, 0.0
        
        # check for the coordinates closest to the origin to be considered as
        # center coordinates of circle 1
        if math.dist([xc1,yc1], [0.0, 0.0]) > math.dist([xc2,yc2], [0.0, 0.0]):
            xC1, yC1 = xc2,yc2
        elif math.dist([xc1,yc1], [0.0, 0.0]) < math.dist([xc2,yc2], [0.0, 0.0]):
            xC1, yC1 = xc1,yc1
        else:
            xC1, yC1 = xc2,yc2
        
        print(xC1, yC1)
        

        xc2,yc2,xc3,yc3 =  get_intersections(x2, y2, r2, x_mid2, y_mid2, h2)
        xC2, yC2 = 0.0, 0.0
        
        # check for the coordinates closest to the origin to be considered as
        # center coordinates of circle 2
        if math.dist([xc2,yc2], [0.0, 0.0]) > math.dist([xc3,yc3], [0.0, 0.0]):
            xC2, yC2 = xc3,yc3
        elif math.dist([x1,y1], [0.0, 0.0]) < math.dist([xc3,yc3], [0.0, 0.0]):
            xC2, yC2 = xc2,yc2
        else:
            xC2, yC2 = xc2,yc2

        print(xC2, yC2)

        
        print(get_intersections(xC1, yC1, r1, xC2, yC2, r2)) # return robot coordinates
        



