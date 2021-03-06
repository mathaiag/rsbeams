import numpy as np
import matplotlib.pyplot as plt

class RKSolver(object):

    def __init__( self, N, T=10. ):
        """Initialize the t and x arrays"""
        self.N = N
        self.dt = T/N
        self.t = np.arange(N) * self.dt # Vector operation
        x = np.empty(N)
        x[0] = 1.
        self.x = x

    def rk_integration( self ):
        """Integrate the differential equation, using Euler's method"""
        for i in range(1,self.N):
            k = self.x[i-1]*np.cos(self.t[i-1])*self.dt
            self.x[i] = self.x[i-1] + (self.x[i-1]+k/2)*np.cos(self.t[i-1]+self.dt/2)*self.dt

    def evaluate_result( self ):
        """Print the RMS error and plot the curve"""
    
        # Create the exact result
        x_exact = np.exp( np.sin(self.t) )
        # Print the RMS difference
        e_rms = np.sqrt( 1./self.N * ((self.x-x_exact)**2).sum() )
        print( e_rms )
        # Plot the result
        plt.plot( self.t, self.x, label="RK")
        plt.plot( self.t, x_exact, '--', label="Analytic Solution")
        plt.legend(loc=3)
        plt.show()

if __name__ == '__main__':

    solver = RKSolver( 100 )
    solver.rk_integration()
    solver.evaluate_result()
