import matplotlib.pyplot as plt
import numpy as np
import random


#parameters

max_speed = 3

size_coeff = 200

grid_size = max_speed*size_coeff

speed_multiplier = 0.6

complexity = 0.02

branch_probability = 0.005





#setting up grid that records particle path

grid = np.zeros((grid_size, grid_size))

centre = grid_size//2

grid[centre, centre] = 1

#calculates particle's random walk

def particle_journey():
    
    vel = [0, max_speed]
    
    x_pos = centre
    y_pos = centre
    
    points = []
    
    for i in range((size_coeff//2)-1):
        
        #changes particle direction if needed
        if random.random() < branch_probability:
            vel[0] = max(random.randint(0, max_speed-2), vel[0]-1)
            vel[1] = int(np.sqrt((max_speed*max_speed)-(vel[0]*vel[0])))
    
        x_pos = x_pos+vel[0]
        y_pos = y_pos+vel[1]
        
        
        #recording points particle has passed through
        points.append([x_pos, y_pos])
        points.append([x_pos+1, y_pos+1])
        points.append([x_pos-1, y_pos-1])
        
        
        #serves to make lines thicker so the snowflake pattern appears less wispy
        grid[-y_pos, -x_pos] = 1
        grid[-y_pos, x_pos] = 1
        grid[-y_pos+1, -(x_pos+1)] = 1
        grid[-y_pos+1, x_pos+1] = 1
        grid[-y_pos-1, -(x_pos-1)] = 1
        grid[-y_pos-1, x_pos-1] = 1
        
    return(points)
    

#this function takes a list of points (branch) and rotates it by a specified angle theta.
def rotate(points, theta):
    
    rotated_points = []
        
    rot_mat = np.array(([np.cos(theta), -1*np.sin(theta)], [np.sin(theta), np.cos(theta)]))
    
    for x, y in points:
        r_point = np.matmul(rot_mat ,[x - centre, y-centre])
        rotated_points.append([int(round(r_point[0]+centre)), int(round(r_point[1]+centre))])
    
    
    return rotated_points



branch_orig = []
for i in range(int(complexity*size_coeff)):
    branch_orig.extend(particle_journey())
    

#draws rotated branches

for i in [2, 5/3, 4/3, 2/3, 1/3]:
    rotated_branch = rotate(branch_orig, np.pi*i)
    for j in rotated_branch:
        grid[j[1], j[0]] = 1
        grid[j[1], -j[0]] = 1




#displays all points on a pyplot plot

plt.figure(figsize=(6, 6))


plt.axis('off')
plt.imshow(grid, cmap='Blues', interpolation='antialiased', vmin = 0, vmax = 1)


plt.title('Snowflake Simulation')
plt.show()