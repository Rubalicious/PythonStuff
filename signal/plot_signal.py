#
#   Author: Ruby Abrams
#   Description:
#           This will plot data saved in the data file
#           I will do some signal processing in this file too
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# this will select sample points uniformly
# from the signal
def sampling(data, rate):
    step = int(len(data)*rate)
    return data[::step][data.columns[1]]

def main():
    data = pd.read_csv('data')
    # plt.plot(data[data.columns[0]], data[data.columns[1]])
    # plt.show()

    # angle of rotation in randians
    theta = np.pi/6         # 30 degrees
    # defines the rotation matrix
    def R(theta): return np.matrix([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
    rotated = np.array([R(theta).dot((x,y)) for x,y in zip(data[data.columns[0]], data[data.columns[1]]) ])

    x_coord = np.array([rotated[i][0][0] for i in xrange(len(rotated))])
    y_coord = np.array([rotated[i][0][1] for i in xrange(len(rotated))])
    m = (rotated[-1][0][1]-rotated[0][0][1])/(rotated[-1][0][0]-rotated[0][0][0])
    average_line = np.array(m*data[data.columns[0]])

    # ROTATED SINE GRAPH
    plt.axis([-0.5, 1.5, -1, 1.5])
    plt.plot(x_coord, y_coord, data[data.columns[0]], average_line, data[data.columns[0]], [0 for i in rotated])
    plt.show()

    # SAMPLING SUBGRAPH
    # plt.plot(sampling(data, 0.01))
    plt.plot(sampling(data, 0.005), '*')
    # plt.plot(sampling(data, 0.02))
    # plt.plot(sampling(data, 0.03))
    # plt.plot(sampling(data, 0.04))
    # plt.plot(sampling(data, 0.05))

    # plt.plot(sampling(data, 0.1))
    # plt.plot(sampling(data, 0.15))

    # plt.legend({'0.05','0.1','0.15', '0.3'})
    plt.show()

if __name__ == '__main__':
    main()
