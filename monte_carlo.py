import random
import math
import matplotlib.pyplot as plt
import numpy as np


def pi_estimation(N):
    pi_values = []
    all_inside_x, all_inside_y = [], []
    all_outside_x, all_outside_y = [], []
    for n in N:
        #Wygenerujemy N par liczb xn,yn będących współrzędnymi punktów na kwadracie (0,0 ; 1,1)
        xn, yn = [], []
        for i in range(int(n)):
            xn.append(random.random())
            yn.append(random.random())

        #Skorzystamy z równania okręgu x2+y2=r2 dla r=1 - ograniczymy się do 1 ćwiartki..
        #Przekształcimy równanie na postać y=f(x)…
        r2 = [0] * int(n)
        y = [0] * int(n)
        for i in range(int(n)):
            r2[i] = xn[i] ** 2 + yn[i] ** 2
            y[i] = math.sqrt(1 - xn[i] ** 2)

        #Wielokrotnie, dla kolejnych n<N sprawdzimy, czy yn <= f(xn)
        inside = 0
        index_inside = []
        index_outside = []

        for i in range(int(n)):
            if yn[i] <= y[i]:
                inside += 1
                index_inside.append([xn[i], yn[i]])
            else:
                index_outside.append([xn[i], yn[i]])

        #Statystycznie obliczymy stosunek pola 
        #W ten sposób przybliżymy wartość pi
        pi = 4 * inside / int(n)
        pi_values.append(pi)


        inside_x, inside_y = zip(*index_inside) if index_inside else ([], [])
        outside_x, outside_y = zip(*index_outside) if index_outside else ([], [])

        all_inside_x.append(inside_x)
        all_inside_y.append(inside_y)
        all_outside_x.append(outside_x)
        all_outside_y.append(outside_y)

    return pi_values, all_inside_x, all_inside_y, all_outside_x, all_outside_y


def plot_points(N, inside_x, inside_y, outside_x, outside_y):
    plt.figure(figsize=(12, 8))
    for i, n in enumerate(N):
        plt.subplot(2, 3, i + 1)
        plt.scatter(inside_x[i], inside_y[i], color='pink', s=1)
        plt.scatter(outside_x[i], outside_y[i], color='purple', s=1)
        plt.title(f'N = {n}')
        plt.xlabel('X')
        plt.ylabel('Y')

        x_circle = np.cos(np.linspace(0, np.pi / 2, 100))
        y_circle = np.sin(np.linspace(0, np.pi / 2, 100))
        plt.plot(x_circle, y_circle, color='deeppink', linewidth=1.5)

    plt.tight_layout()
    plt.show()


def paths():
    N = [100, 1000, 5000, 10000, 50000, 100000]
    paths = [] 
    all_pi_values = {n: [] for n in N}
    
    for i in range(5):
        pi_values, inside_x, inside_y, outside_x, outside_y = pi_estimation(N)
        paths.append(pi_values)
        for i, n in enumerate(N):
            all_pi_values[n].append(pi_values[i])
        
    plot_points(N, inside_x, inside_y, outside_x, outside_y)


    plt.figure(figsize=(10, 6))
    for i, pi_values in enumerate(paths):
        plt.plot(N, pi_values, label=f'Path {i + 1}')
    
    plt.axhline(y = np.pi, color = 'black', linestyle = '--', label = 'PI value')
    plt.xlabel('N points')
    plt.ylabel('PI value')
    plt.legend()
    plt.title('Estimations for different paths')
    plt.show()


    plt.figure(figsize=(10, 6))
    plt.boxplot([all_pi_values[n] for n in N], labels = N, patch_artist= True)
    plt.axhline(y= np.pi, color='black', linestyle='--', label='PI value')
    plt.xlabel('N points')
    plt.ylabel('Estimated PI')
    plt.title('Boxplot of PI estimations for different N')
    plt.legend()
    plt.show()


paths()

