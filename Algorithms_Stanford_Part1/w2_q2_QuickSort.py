'''
QuickSort - Q2

using the final element of the given array as the pivot element.
'''
import pdb

# number of comparisons
num = 0

def QuickSort(a):
	#print "======", a
	#pdb.set_trace()
	n = len(a)
	if n<=1:
		return a
	global num # global variable!!!
	num += n - 1
	#print a, n, num
	p = ChoosePivot(a)
	#swap
	a[0], a[n-1] = a[n-1], a[0]
	pos = Partition(a, p, 0, n-1)
	a[:pos] = QuickSort(a[:pos])
	a[pos+1:] = QuickSort(a[pos+1:])
	return a

def ChoosePivot(a):
	return a[len(a)-1]

def Partition(a, p, l ,r):
	i = l + 1
	for j in range(l+1, r+1):
		if a[j] < p:
			a[i], a[j] = a[j], a[i]
			i += 1
	a[l], a[i-1] = a[i-1], a[l]
	return i - 1

f = open('w2_QuickSort.txt', 'r')
src = f.readlines()
for i in range(len(src)):
	src[i] = int(src[i].split()[0])

out = QuickSort(src)
print "out: ", out
print "num", num

# q1: 162085
# q2: 164123