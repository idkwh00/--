import os
import math
import csv

A = 1
x_start = -15
x_end = 5
step = 0.1  

if not os.path.exists('results'):
    os.makedirs('results')

results = []
x_values = []
y_values = []
x = x_start
while x <= x_end:
    try:
        y = 100 * math.sqrt(abs(A - 0.01 * x**2)) + 0.01 * x + 10
        results.append((x, y))
        x_values.append(x)
        y_values.append(y)
    except ValueError:
        pass
    x = round(x + step, 10) 

with open('results/result_v11.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['index', 'x', 'f(x)']) 
    for i, (x_val, y_val) in enumerate(results, start=1):
        writer.writerow([i, x_val, y_val])


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, 'b-', linewidth=2)
plt.title('График функции f(x) = 100 * sqrt(1 - 0.01x^2) + 0.01x + 10')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.savefig('results/function_plot_v11.png')
plt.show()
