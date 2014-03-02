#!/usr/bin/env python3
# coding: utf-8
# see : https://en.wikipedia.org/wiki/HSL_and_HSV

"""
r,g,b : [0,1]
h : hue : [0,360)
s,v,l : [0,1]
"""

def rgb_to_hue(r,g,b):
    M = max(r,g,b)
    m = min(r,g,b)
    c = M - m  # chroma.
    
    if c == 0:
        return None  # undefined.
    elif r == M:
        h2 = (g-b)/c % 6
    elif g == M:
        h2 = (b-r)/c + 2
    else:
        h2 = (r-g)/c + 4
    
    return 60*h2

def rgb_to_hsv(r,g,b):
    hue = rgb_to_hue(r,g,b)
    c = max(r,g,b) - min(r,g,b)
    val = max(r,g,b)
    sat = 0 if c == 0 else c/val
    return(hue,sat,val)


def hsv_to_rgb(h,s,v):
    """
    h <- [0,360), s <- [0,1], v <- [0,1]
    => (r,g,b) <- [0,1]**3
    """
    c = v*s  # chroma
    m = v-c
    if h is None:
        return(m,m,m)
    h2 = h/60
    x = c*(1-abs(h2 % 2 -1))
    h2 = int(h2)
    
    if h2 == 0:
        (r1,g1,b1) = (c,x,0)
    elif h2 == 1:
        (r1,g1,b1) = (x,c,0)
    elif h2 == 2:
        (r1,g1,b1) = (0,c,x)
    elif h2 == 3:
        (r1,g1,b1) = (0,x,c)
    elif h2 == 4:
        (r1,g1,b1) = (x,0,c)
    elif h2 == 5:
        (r1,g1,b1) = (c,0,x)
    
    return (r1+m, g1+m, b1+m)

def test(n,m):
    import random
    import PIL.Image as Img
    import numpy as np
    imgarray = np.zeros((n*3,m,3), dtype=np.uint8)
    for i in range(n):
        r,g,b = [random.random() for i in range(3)]
        imgarray[3*i:3*i+3,:m//2] = [int(x*255) for x in (r,g,b)]
        h,s,v = rgb_to_hsv(r,g,b)
        imgarray[3*i:3*i+3,m//2:] = [int(x*255) for x in hsv_to_rgb(h,s,v)]
    img = Img.fromarray(imgarray)
    img.show()
    img.save("foo.png")



# test(250,100) ok!

