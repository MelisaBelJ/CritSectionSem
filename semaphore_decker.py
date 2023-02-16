from multiprocessing import Process, current_process, Value, BoundedSemaphore
from time import sleep
from random import random

N = 8
def task(common, semaforo):
	tid = current_process().name
	for i in range(20):
		print(f'{tid}−{i}: Non−critical Section', flush = True)
		print(f'{tid}−{i}: End of non−critical Section', flush = True)		
		sleep(random())
		with semaforo:
			print(f'{tid}−{i}: Critical section', flush = True)
			v = common.value + 1
			print(f'{tid}−{i}: Inside critical section', flush = True)
			sleep(random())
			common.value = v
			print(f'{tid}−{i}: End of critical section', flush = True)
def main():
	lp = []
	common = Value('i', 0)
	semaforo = BoundedSemaphore()
	for tid in range(N):
		lp.append(Process(target=task, name=f'{tid}', args=(common, semaforo)))
	print (f"Valor inicial del contador {common.value}")
	for p in lp:
		p.start()
	for p in lp:
		p.join()
	print (f"Valor final del contador {common.value}")
	print ("fin")
if __name__ == "__main__":
	main()
