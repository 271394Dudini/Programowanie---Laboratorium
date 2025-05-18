import numpy
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import argparse

def epidemia(y,t,N,beta,sigma,gamma):
	S,E,I,R = y
	dydt = [ -beta*S*I/N , beta*S*I/N-sigma*E , sigma*E-gamma*I , gamma*I]
	return dydt

parser=argparse.ArgumentParser()
parser.add_argument('-N',type=int,default=1000)
parser.add_argument('-S',type=int,default=999)
parser.add_argument('-E',type=int,default=1)
parser.add_argument('-I',type=int,default=0)
parser.add_argument('-R',type=int,default=0)
parser.add_argument('--beta',type=float,default=1.34)
parser.add_argument('--sigma',type=float,default=0.19)
parser.add_argument('--gamma',type=float,default=0.34)
args = parser.parse_args()

S = args.S if args.S is not None else args.N-args.E-args.I-args.R
E = args.E if args.E is not None else args.N-args.S-args.I-args.R
I = args.I if args.I is not None else args.N-args.E-args.S-args.R
R = args.R if args.R is not None else args.N-args.E-args.I-args.S
N = args.N if args.N is not None else args.S+args.E+args.I+args.R

def wykres(N,S,E,I,R,beta,sigma,gamma):

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

wykres(N,S,E,I,R,args.beta,args.sigma,args.gamma)