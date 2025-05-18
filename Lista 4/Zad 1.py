import numpy
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sys

def epidemia(y,t,N,beta,sigma,gamma):
	S,E,I,R = y
	dydt = [ -beta*S*I/N , beta*S*I/N-sigma*E , sigma*E-gamma*I , gamma*I]
	return dydt


def wykres(N=1000,S=999,E=1,I=0,R=0,beta=1.2,sigma=0.6,gamma=0.5):

	N=int(N)
	S=int(S)
	E=int(E)
	I=int(I)
	R=int(R)
	beta=float(beta)
	sigma=float(sigma)
	gamma=float(gamma)
	y0=[S,E,I,R]
	time = numpy.linspace(0,200,200)

	solution = odeint(epidemia, y0, time, (N, beta, sigma, gamma))

	S=solution[:,0]
	E=solution[:,1]
	I=solution[:,2]
	R=solution[:,3]

	# plt.plot(time, N, label="populacja")
	plt.plot(time, S, label="podatny")
	plt.plot(time, E, label="narażony")
	plt.plot(time, I, label="zarażający")
	plt.plot(time, R, label="ozdrowieniec")
	plt.title("Symulacja epidemiczna")
	plt.xlabel("Czas")
	plt.ylabel("populacja")
	plt.legend(loc="best")
	plt.grid
	plt.show()

wykres(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])