import numpy as np
import matplotlib.pyplot as plt
MOON_PERIOD = 60*60*24*27.3

def analyse(dt):
    journey = np.genfromtxt('one_second.txt')
    x = journey[:,0]
    y = journey[:,1]
    distance = np.sqrt(x**2+y**2)
    maximums = find_maximums(distance, dt)
    plt.plot(distance)
    plt.xlabel('Time (s)')
    plt.ylabel('Absolute distance (m) from Earth')
    plt.title('Absolute radial distance from Earth as a function of time')
    plt.show()
    print(maximums)
    for time_s, point in maximums:
        print(f'Maximum at {np.round(time_s/MOON_PERIOD, 5)}% of value {point}')

        
    


def find_maximums(p, dt):
    maximums = []
    for i,point in enumerate(np.abs(p)):
        if i==len(p)-1:
            break
        if point>p[i-1] and point>p[i+1]:
            maximums.append([i*dt, point])
    return maximums

analyse(1)
