import numpy as np
from scipy.interpolate import interp1d
import os

model='Spitzer'
# model='Lee-More'
T_ref = np.array([0.1, 1, 10,      20,      30,      50,      70,      100,     150,     200,      300,      500,      1000])
Z_ref = np.array([3,   3, 3.02048, 3.55294, 4.38492, 5.95555, 7.10874, 8.34575, 9.59144, 10.15816, 10.81922, 12.11186, 12.88516])

if __name__ == '__main__':
    logT = np.log10(T_ref)
    interp_func = interp1d(logT, Z_ref, kind='cubic')
    T_list = [1, 2, 3, 4, 6, 8, 12, 16, 25, 32, 50, 64, 100, 128, 200, 256, 384, 512, 750, 1000]
    density = '2.7'
    for T in T_list:
        Z = interp_func(np.log10(T))
        ele = 'al'+'_'+str(Z)
        with open('input','w') as f:
            f.write('3\n')
            f.write(ele+'\n')
            f.write(density+'\n')
            f.write(str(T)+'\n')
        os.system('../tool.exe < input > _tmp')
        with open('_tmp','r') as f:
            data = f.readlines()
            for line in data:
                if model in line:
                    parts = line.split()
                    sigma = parts[1]
                    kappa = parts[2]
                    Lorentz = parts[3]
                    break
        os.remove('_tmp')
        print(T, sigma, kappa, Lorentz)
    
    os.remove('input')
        

    