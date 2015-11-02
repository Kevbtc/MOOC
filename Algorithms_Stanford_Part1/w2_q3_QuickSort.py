'''
QuickSort - Q3

using the "median-of-three" pivot rule
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
	p, index = ChoosePivot(a)
	#swap
	a[0], a[index] = a[index], a[0]

	pos = Partition(a, p, 0, n-1)
	a[:pos] = QuickSort(a[:pos])
	a[pos+1:] = QuickSort(a[pos+1:])
	return a

def ChoosePivot(a):
	print "ChoosePivot", a
	if(len(a)<3):
		return (a[0], 0)
	three = (a[0], a[(len(a)+1)/2-1], a[len(a)-1])
	maxNum = max(three)
	minNum = min(three)
	print "max", maxNum, "min", minNum
	for i in range(3):
		if (three[i] != maxNum and three[i] != minNum):
			middle = three[i]
			if (middle == three[0]):
				index = 0
			elif (middle == three[2]):
				index = len(a)-1
			else:
				index = (len(a)+1)/2-1
			print (middle, index)
			return (middle, index)


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

#src = [4, 65436,2132,123,12313]

out = QuickSort(src)
print "out: ", out
print "num", num

# q1: 162085
# q3: 138382
