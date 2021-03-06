# -*- coding: utf-8 -*-
# 程式 13-7 (Python 3 Version)

import matplotlib.pyplot as plt
import numpy as np

a = 1.5
b = 1
degree = np.linspace(0, 2*np.pi, 200)
x1 = a * (1 + np.cos(degree)) * np.cos(degree)
y1 = a * (1 + np.cos(degree)) * np.sin(degree)

x2 = a * np.sin(2*degree)
y2 = b * np.sin(degree)

plt.xlim(-2, 3.5)
plt.ylim(-2.5, 2.5)
plt.plot(x1, y1, color='red', lw=2)
plt.plot(x2, y2, color='blue', lw=2)
plt.title("數學函數圖形")
plt.show()
