import numpy as np
import math
from reader import Reader

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
		self.C = np.dot(np.transpose(self.U),self.X)
		self.C = np.divide()
		print  self.C
	

a = FCM(4)
