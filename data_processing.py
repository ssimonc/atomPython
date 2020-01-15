import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

def extract_prices(filename):
	Prices = dict()
	with open(filename, 'r') as file:
		for line in file:
			l = line.split(';')
			if l[0] == "Price":
				if l[1] in Prices.keys():
					T, P = Prices[l[1]]
					T.append(int(l[6]))
					P.append(int(l[4]))
				else:
					Prices[l[1]] = [int(l[6])], [int(l[4])]
	return Prices

def extract_qties(filename):
	T = []
	Q = []
	with open(filename, 'r') as file:
		qty = 0
		tick = 0
		for line in file:
			l = line.split(';')
			if l[0] == "Tick":
				tick += 1
				T.append(tick)
				Q.append(qty)
				qty = 0
			if l[0] == "Price" and l[5] != "None":
				qty += int(l[5])
	return T, Q

def extract_wealths(filename):
	Wealths = dict()
	with open(filename, 'r') as file:
		for line in file:
			l = line.split(';')
			if l[0] == "AgentWealth":
				if l[1] in Wealths.keys():
					T, W = Wealths[l[1]]
					T.append(int(l[3]))
					W.append(int(l[2]))
				else:
					Wealths[l[1]] = [int(l[3])], [int(l[2])]
	return Wealths

def extract_cash(filename):
        Cash = dict()
        with open(filename, 'r') as file:
                for line in file:
                        l = line.split(';')
                        if l[0] == "Agent":
                                if l[1] in Cash.keys():
                                        T, C = Cash[l[1]]
                                        T.append(int(l[-1]))
                                        C.append(int(l[2]))
                                else:
                                        Cash[l[1]] = [int(l[-1])], [int(l[2])]
        return Cash

def extract_limit_orders(filename):
        LimitOrder = dict()
        with open(filename, 'r') as file:
                for line in file:
                        l = line.split(';')
                        if l[0] == "LimitOrder":
                                if l[2] in LimitOrder.keys():
                                        T, L = LimitOrder[l[2]]
                                        T.append(int(l[-1]))
                                        L.append(l[3])
                                else:
                                        LimitOrder[l[2]] = [int(l[-1])], [l[3]]
        return LimitOrder


def draw_returns_hist(filename, asset, nb_pts, tau=1):
	Prices = np.array(extract_prices(filename)[asset][1])
	Returns = np.log(Prices[tau:])-np.log(Prices[:-tau])
	Y, X, _ = plt.hist(Returns, nb_pts) # Y contains the number of occurrences and X the nb_pts+1 points separating the different bars of the histogram.
	plt.clf() # We do not want the plt.hist to be displayed
	R = (X[1:]+X[:-1])/2 # R contains the list of the centers of the abscissae of the bars of the histogram.
	r = np.max(np.abs(R))
	R2 = np.linspace(-r, r, nb_pts*2)
	Y = np.array(Y)
	D = Y*R.size/(max(R)-min(R))/np.sum(Y) # D contains the density of returns
	mu = np.mean(Returns)
	sigma = np.sqrt(np.mean((Returns-mu)**2))
	N = scipy.stats.norm.pdf(R2, mu, sigma) # Normal law of the same expectation and standard deviation as profitability
	X = ((R-mu)/sigma)**4
	plt.semilogy(R, D, 'o', label='Returns for tau = %i. Kurtosis = %.2f' % (tau, 3+scipy.stats.kurtosis(Returns)))
	plt.semilogy(R2, N, '--', label='Normal PDF')
	plt.xlabel('Returns')
	plt.ylabel('Density')
	plt.legend(loc='best')
	plt.title('Distribution of returns')
	r = np.max(np.abs(R))*1.05
	plt.axis([-r, r, 10**-3, max(D)*2])
	plt.grid()
	plt.show()

def smooth(lst, p):
	lst_out = []
	n = len(lst)
	for i in range(n):
		x_inf = max(0, i-p)
		x_sup = min(n, i+p+1)
		lst_out.append(sum(lst[x_inf:x_sup])/(x_sup - x_inf))
	return lst_out
