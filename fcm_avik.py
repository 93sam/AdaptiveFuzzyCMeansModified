import numpy as np
import math
from reader import Reader
np.seterr(divide='ignore', invalid='ignore')


class FCM():
	def __init__(self,n_clusters,epsilon=0.05,max_iter=-1):
		self.m = 2
		self.n_clusters = n_clusters

		read = Reader('irisdata2.txt')
		self.X,self.y = read.get_data()
		self.data_shape = self.X.shape
		rows , cols = self.data_shape
		
		self.U = []
		for i in range(rows):
			index = i % n_clusters
			l = [ 0 for j in range(n_clusters) ]
			l[index] = 1
			self.U.append(l)
		self.U = np.array(self.U).astype(np.float)
		
		self.C = []
		l = [ 0 for j in range(cols) ]
		for i in range(n_clusters):
			self.C.append(l)
		self.C = np.array(self.C).astype(np.float)


	def cost_function(self):
		J = 0
		for i in range(self.data_shape[0]):
			for j in range(self.n_clusters):
				J += (self.U[i][j] ** self.m) * (np.sum(np.subtract(self.X[i],self.C[j])))
		return J

	def Update_C(self):
		for j in range(self.n_clusters):
			num_sum = 0
			den_sum = 0
			for i in range(self.data_shape[0]):
				num_sum += np.dot((self.U[i][j] ** self.m),self.X[i])
				den_sum += self.U[i][j] ** self.m
		
				self.C[j] = np.divide(num_sum,den_sum)
		
		print  self.C


	def update_U(self):
		for i in range(self.X.shape[0]):
			for j in range(self.n_clusters):
				sumation = 0
				for k in range(self.n_clusters):
					sumation += ( np.sum(np.subtract(self.X[i],self.C[j])) / np.sum(np.subtract(self.X[i],self.C[k])) ) ** (2 / (self.m-1) )
				self.U[i][j] = 1 / sumation

a = FCM(4)
#a.Update_C()
