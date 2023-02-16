from multiprocessing import Process, current_process, Value, Lock

N = 8
def task(common, lock):
	tid = current_process().name
	for i in range(100):
		print(f'{tid}−{i}: Non−critical Section')
		print(f'{tid}−{i}: End of non−critical Section')
		while not lock.acquire(False):
			print(f'{tid}−{i}: Giving up')
		print(f'{tid}−{i}: Critical section')
		v = common.value + 1
		print(f'{tid}−{i}: Inside critical section')
		common.value = v
		print(f'{tid}−{i}: End of critical section')
		lock.release()
def main():
	lp = []
	common = Value('i', 0)
	lock = Lock()
	for tid in range(N):
		lp.append(Process(target=task, name=tid, args=(common, lock)))
	print (f"Valor inicial del contador {common.value}")
	for p in lp:
		p.start()
	for p in lp:
		p.join()
	print (f"Valor final del contador {common.value}")
	print ("fin")
	
if __name__ == "__main__":
	main()

