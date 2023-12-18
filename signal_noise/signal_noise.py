import numpy as np

class signal_noise:
    def __init__(self,derivative_rang:list[int]=[2],norm_func:list[str]=['evklid']):
        """
        derivative_rang - you can give n from 1 to infinity
        norm_func - you can use evklid norm, manhattan norm, chebyshev norm
        """
        self.derivative_rang=derivative_rang
        self.norm_func=norm_func

    def evklid(self,vector):
        # return np.sqrt(np.sum(np.square(vector)))
        return np.linalg.norm(vector)
    
    def manhattan(self,vector):
        return np.linalg.norm(vector,ord=1)
    
    def chebyshev(self,vector):
        return np.linalg.norm(vector,ord=np.inf)
    
    def derivative_n_rang(self,signal,x,rang:int):
        derivative = np.gradient(signal, x)
        for i in range(1,rang):
            derivative = np.gradient(derivative, x)
        return derivative
    
    def main(self,signal,x):
        values = [[] for i in range(len(self.norm_func))]
        dictionary = dict(zip(self.norm_func, values))
        for i in self.derivative_rang:
            derivative=self.derivative_n_rang(signal.copy(),x,i)
            for j in self.norm_func:
                match j:
                    case 'evklid': 
                        norm_signal=self.evklid(signal.copy())
                        norm_deriv=self.evklid(derivative.copy())
                        dictionary['evklid'].append(norm_signal/norm_deriv)
                    case 'manhattan': 
                        norm_signal=self.manhattan(signal.copy())
                        norm_deriv=self.manhattan(derivative.copy())
                        dictionary['manhattan'].append(norm_signal/norm_deriv)
                    case 'chebyshev': 
                        norm_signal=self.chebyshev(signal.copy())
                        norm_deriv=self.chebyshev(derivative.copy())
                        dictionary['chebyshev'].append(norm_signal/norm_deriv)
        return dictionary
    