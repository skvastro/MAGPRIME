import numpy as np
import pandas as pd
import pkg_resources

def load_michibiki_data():
    "Import the magnetometer data from the file"
    file_path = pkg_resources.resource_filename('magprime.utility.SPACE_DATA', 'michibiki.dat')
    qzs_1 = np.loadtxt(file_path, dtype=float, usecols=(0, 4, 5, 6, 7, 8, 9))
    B_qzs = qzs_1.T

    "Subtract the bias from the magnetometer data"
    B_qzs[1] -= 60 # MAM-S1 X-Axis
    B_qzs[2] -= 410 # MAM-S1 Y-Axis
    B_qzs[3] -= -202 # MAM-S1 Z-Axis
    B_qzs[4] -= -528 # MAM-S2 X-Axis
    B_qzs[5] -= -200 # MAM-S2 Y-Axis
    B_qzs[6] -= 478 # MAM-S2 Z-Axis

    B1 = np.vstack((B_qzs[1], B_qzs[2], B_qzs[3]))
    B2 = np.vstack((B_qzs[4], B_qzs[5], B_qzs[6]))
    michibiki = np.stack((B1, B2))
    return(michibiki)


def load_swarm_data(start = 160000, stop = 169736):
    "Import 50 Hz magnetometer residual data"
    file_path = pkg_resources.resource_filename('magprime.utility.SPACE_DATA', 'Swarm_MAGA_HR_20150317_0900.csv')
    df=pd.read_csv(file_path, sep=',',header=None)
    r = df[10]
    swarm = np.array([np.fromstring(r[i][1:-1], dtype=float, sep=' ') for i in range(1, r.shape[0])]).T[:,start:stop]
    return(swarm)

def load_quadmag_data():
    start = 160000
    stop = 169736
    file_path = pkg_resources.resource_filename('magprime.utility.SPACE_DATA', 'Swarm_MAGA_HR_20150317_0900.csv')
    df=pd.read_csv(file_path, sep=',',header=None)
    r = df[10]
    swarm = np.array([np.fromstring(r[i][1:-1], dtype=float, sep=' ') for i in range(1, r.shape[0])]).T[:,start:stop]
        
    file_path = pkg_resources.resource_filename('magprime.utility.SPACE_DATA', 'quadmag_data.txt')
    S = np.loadtxt(file_path, dtype=float, delimiter=',' , usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13))
    S1 = S.T
    B1 = np.vstack((S1[0], S1[1], S1[2])) + swarm
    B2 = np.vstack((S1[3], S1[4], S1[5])) + swarm
    B3 = np.vstack((S1[6], S1[7], S1[8])) + swarm
    B4 = np.vstack((S1[9], S1[10], S1[11])) +swarm
    quadmag = np.stack((B1, B2, B3, B4))
    return(quadmag)
    

