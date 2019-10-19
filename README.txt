
# How to crack passwords with brute force & dictionaries (0.5 hours to 1 hour)?
## This is a 34/50 of the passwords on hashes.txt

	- Simply run the 2 commands below in the folder you downloaded it in...
```sh
$ wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
$ python hash.py
```
or run (if 'wget' command does not run)
```sh
$ curl 'https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt' > rockyou.txt
$ python hash.py
```
  - This will take about 30 minutes to 1 hour on a normal server (tested on SMU Gen-Use Server)
  - The normal dictionary functions only takes about 2 minutes to run with "rockyou.txt", "words.txt", "words3.txt"

# How to crack passwords with just dictionaries (5-10 minutes)?
- Simply run the 2 commands below in the folder you downloaded it in...
```sh
$ wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
$ python hashDict.py
```
or run (if 'wget' command does not run)
```sh
$ curl 'https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt' > rockyou.txt
$ python hashDict.py
```
- This will take about 30 minutes to 1 hour on a normal server (tested on SMU Gen-Use Server)
- The normal dictionary functions only takes about 2 minutes to run with "rockyou.txt", "words.txt", "words3.txt"
