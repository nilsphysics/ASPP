from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
#randNum = np.zeros(1)

print('hello world from process', rank)
