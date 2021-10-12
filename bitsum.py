from sys import stdin

def bit(x, n):
	return x & 1 << n != 0

inp = stdin.buffer.read()

acc = 0

for b in inp:
	for i in range(8):
		if bit(b, i):
			acc = acc + 1
		else:
			continue

print("HASH: %x" % acc)