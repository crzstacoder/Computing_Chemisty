import matplotlib.pyplot as plt
import numpy as np

V = np.arange(10,50,5) 
n = 1
R = 0.08
T = 273.15

#압력에 대한 식
#PV=nRT 꼴
P = n*R*T/V

plt.plot(V,P,'mo',label='T = 273.15K')

plt.xlabel('boopee (L)') #x축에는 부피!
plt.ylabel("ap_ryeok (atm)") #y축에는 압력!
plt.title('Isang giche bangjeongsik') #그래프 제목 ( 이상기체방정식 )

plt.legend()
plt.show()