from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

arr = np.zeros(1)

if rank == 1:
    arr[0] += rank
    comm.Send(arr, dest=2)

if rank == 2:
    comm.Recv(arr, source=1)
    arr[0] += rank
    comm.Send(arr, dest=3)

if rank == 3:
    comm.Recv(arr, source=2)
    arr[0] += rank
    comm.Send(arr, dest=4)

if rank == 4:
    comm.Recv(arr, source=3)
    arr[0] += rank
    comm.Send(arr, dest=0)

if rank == 0:
    comm.Recv(arr, source=4)
    print('This is the sum of the ranks', arr[0])