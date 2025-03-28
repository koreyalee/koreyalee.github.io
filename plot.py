import matplotlib.pyplot as plt
import numpy as np

def create_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Sine Wave')
    plt.title('Beautiful Sine Wave')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('plot.png')
    plt.close()

if __name__ == '__main__':
    create_plot()