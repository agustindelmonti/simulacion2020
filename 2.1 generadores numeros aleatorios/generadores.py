from random import randint
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import interactive

def middle_square(seed,N=100):
    s = []
    num = seed
    for i in range(0,N):
        num = int(str(num * num).zfill(8)[2:6])
        s.append(num/10000)
    return s

#GCL
class LCG:
	def __init__(self,a,c,m):
		self.a = a
		self.c = c
		self.m = m

	def gen(self, seed, N=100):
		self.s = []
		self.seed = seed
		self.N = N

		num = seed
		for i in range(1,N):
			num = (self.a*num + self.c) % self.m
			self.s.append(num/self.m)
		return self.s

	def freq_analysis(self):
		plt.plot(self.s,'.',markersize=1.0)
		plt.xlim(0,len(self.s))
		plt.ylim(0,1)
		plt.show()

	def chi_squared(self, k=10, alpha=0.95):
		obs = pd.DataFrame(self.s, columns=['counts'])

		#Armo las categorias para test chi-cuadrado
		ranges = [i/k for i in range(k+1)]
		obs = obs.groupby(pd.cut(obs['counts'], ranges)).count()

		#Tabla de contingencia con valores uniformes de referencia
		cross = np.array([obs['counts'], [num//k]*k])

		chi2_stat, p_value, dof, expected_table = stats.chi2_contingency(cross)
		threshold = stats.chi2.ppf(alpha, dof)
		return chi2_stat, p_value, threshold, alpha


def spectral_test(G,seed,N=100):
	'''
		Test espectral en el plano: se trata de ver si  las secuencias generadas
		por la tupla (u_i,u_i+1) son independientes o si forman patrones
	'''
	x = G.gen(seed, N)
	y = G.gen(seed+1, N)	
	
	fig = plt.figure()
	plt.plot(x,y,'.g',markersize=1.0)

	plt.xlim(0,1)
	plt.ylim(0,1)	
	plt.show()

def cubic_spectral_test(G,seed,N=100):
	'''
		Test espectral en el cubo: se trata de ver si  las secuencias generadas
		por la tupla (u_i,u_i+1,u_i+2) son independientes o si forman patrones
	'''
	x = G.gen(3423,N)
	y = G.gen(23,N)	
	z = G.gen(1233,N)	
	
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	plt.plot(x,y,z,'.g',markersize=1.0)

	ax.view_init(70, 35)	
	plt.show()


if __name__ == "__main__":

	num = 20000
	seed = 1022
	a1 = 7**5
	c1 = 0
	m1 = 2**31 - 1

	G1 = LCG(a1,c1,m1)
	G1.gen(seed,num)
	G1.freq_analysis()
	chi2, p, _, alpha = G1.chi_squared()
	print(f'chi2: {chi2} \np: {p} \nalpha: {alpha}')

	spectral_test(G1,seed,num)
	cubic_spectral_test(G1,seed,num)
	