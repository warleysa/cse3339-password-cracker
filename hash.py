import hashlib
import string
import time
import itertools
import threading
from multiprocessing import Process, Pipe, Pool
from functools import partial
import timeit

hashArray = []
hashArrayDict = []

lock = threading.Lock()
allCracked = {}
counter = 0

alphabet = string.uppercase + string.lowercase + string.digits
alphabetLower = string.lowercase
print(alphabet)

def bruteForce(loopValue):
	global allCracked
	pool = Pool()
	print("Entering Brute")
	for i in range(1,loopValue):
		for value in itertools.product(alphabet, repeat=i):
			if hashlib.sha256(''.join(value)).hexdigest() in hashArray:
				tempHash = hashlib.sha256(''.join(value).encode()).hexdigest()
				lock.acquire()
				allCracked.update({ tempHash: ''.join(value)})
				lock.release()
				print("Password", ''.join(value))

	print("Done with the Brute Force attack")



def bruteForce2():
	global allCracked
	pool = Pool()
	print("Entering Brute22")
	for i in range(6,7):
		for value in itertools.product(alphabetLower, repeat=i):
			if hashlib.sha256(''.join(value)).hexdigest() in hashArray:
				tempHash = hashlib.sha256(''.join(value).encode()).hexdigest()
				lock.acquire()
				allCracked.update({ tempHash: ''.join(value)})
				lock.release()
				print("Password", ''.join(value))

	print("Done with the Brute Force attack 2")


def dictAttack(fileName):
	pool = Pool()
	print("Thread Dict Starting")
	wordlist = []
	with open(fileName) as word_file:
		wordlist = set(word_file.read().split())

	total_successes = pool.imap_unordered(strComboCheck, wordlist, chunksize=19000)

	total_successes = [ent for sublist in total_successes for ent in sublist]

	lock.acquire()
	# print(total_successes)
	# print(allCracked)
	for value in total_successes:
		print(value.keys()[0])
		allCracked.update({ value.keys()[0]: value.values()[0]})
	lock.release()

	print("Done with the Dict attack with ", fileName)

def strComboCheck(value):
	successes = []
		# print(strIn)
		# l = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in strIn)))
		# for value in value:
	if hashlib.sha256(''.join(value)).hexdigest() in hashArray:
		tempHash = hashlib.sha256(''.join(value)).hexdigest()
		successes.append({tempHash: value })
	# time.sleep(.01)
	return successes


if __name__ == "__main__":
	with open("hashes.txt", "r") as f:
		for line in f:
			hashArray.append(line[:-1])
			allCracked.update({ line[:-1]: ''})


	threads = []
	t2 = threading.Thread(target=dictAttack, args=('words.txt',))
	threads.append(t2)
	t3 = threading.Thread(target=dictAttack, args=('words3.txt',))
	threads.append(t3)
	t4 = threading.Thread(target=dictAttack, args=('rockyou.txt',))
	threads.append(t4)
	t1 = threading.Thread(target=bruteForce, args=(6,))
	threads.append(t1)
	t5 = threading.Thread(target=bruteForce2)
	threads.append(t5)
	for t in threads:
		t.start()

	for u in range(len(threads)):
		threads[u].join()


	print(allCracked)
	with open("passwords.txt", "w") as f:
		for hash, password in allCracked.items():
			print(hash)
			print(password)
			if password:
				f.write(hash + ':' + password + '\n')
			else:
				f.write(hash + ':\n')
		f.close()

	print("Done!")
