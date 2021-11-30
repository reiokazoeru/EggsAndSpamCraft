import numpy as np
import matplotlib
from matplotlib import pyplot

def sphere_intersection(center,radius,ray_origin,ray_direction):
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) **2 - radius **2 
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 >0:
            return min(t1,t2)
        return None

def nearest_intersected_object(objects,ray_origin,ray_direction):
    distances =  [sphere_intersection(obj.center,obj.radius,ray_origin,ray_direction) for obj in objects]
    nearest_object = None
    min_distance = np.inf
    for index, distance in enumerate(distances):
        if distance and distance < min_distance:
            min_distance = distances
            nearest_object = objects[index]
    return nearest_object, min_distance
width = 300
height = 200

camera = np.array([0,0,1])
ratio = float(width)/height
screen = (-1,1/ratio,1,-1/ratio) #left, top, right, bottom

objects = {
    {'center':np.array([-0.2,0,-1]), 'radius':0.7},
    {'center':np.array([0.1,-0.3,0]), 'radius':0.1},
    {'center':np.array([-0.3,0,0]), 'radius':0.15}
}

image = np.zeros((height,width,3))
for i, y in enumerate(np.linspace(screen[1],screen[3],height)):
    for j, x in enumerate(np.linspace(screen[0],screen[2],width)):
        pixel = np.array([x,y,0])
        origin = camera
        direction = np.linalg.norm(pixel-origin)

        # image[i-j] = ...
        print("progress: %d/%d" % (i+1, height))
pyplot.imsave('image.png',image)