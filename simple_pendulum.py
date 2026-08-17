import scipy,matplotlib
import matplotlib.pyplot as plt
import numpy as np
class SimplePendulum:
    def __init__(self, l:float=1.0, g:float=9.81):
        self.l = l
        self.g = g
        self.x0:np.ndarray = np.array([np.pi/4, 0.0]) 
    def simple_pendulum(self,t,x:np.ndarray):
        '''
        t is dt
        '''
        dx=np.zeros(2)
        dx[0]=x[1]
        dx[1]=-(self.g/self.l)*np.sin(x[0])
        return dx
def main():
    pendulum = SimplePendulum()
    sol=scipy.integrate.solve_ivp(pendulum.simple_pendulum, [0, 15], pendulum.x0,dense_output=True)
    
    t = np.linspace(0, 15, 300)
    z=sol.sol(t)

    # 等价于
    sol2=scipy.integrate.solve_ivp(pendulum.simple_pendulum, [0, 15], pendulum.x0,t_eval=t)
    #将每列的第一个元素取出来，作为角度theta
    
    theta=z[0,:]
    print(theta.shape,t.shape)
    plt.plot(t,theta)
    plt.show()
if __name__ == "__main__":
    main()
