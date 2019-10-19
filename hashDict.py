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

alphabet = string.uppercase + string.lowercase + string.digits
alphabetLower = string.lowercase

def dictAttack(fileName):
	pool = Pool()
	print("Thread Dict Starting")
	wordlist = []
	with open(fileName) as word_file:
		wordlist = set(word_file.read().split())

	total_successes = pool.imap_unordered(strComboCheck, wordlist, chunksize=19000)

	total_successes = [ent for sublist in total_successes for ent in sublist]

	lock.acquire()
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
	t1 = threading.Thread(target=dictAttack, args=('rockyou.txt',))
	threads.append(t1)

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
