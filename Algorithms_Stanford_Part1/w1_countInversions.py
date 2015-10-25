

def sort_and_count(a):
	if len(a) == 1:
		return (a, 0)
	else:
		b, x = sort_and_count(a[:len(a)/2])
		c, y = sort_and_count(a[len(a)/2:])
		d, z = merge_and_countSplitInv(b, c)
	return (d, x + y + z) # !!!


def merge_and_countSplitInv(a, b):
	count = 0
	k = len(a) + len(b)
	p = 0
	q = 0
	dest = range(k)
	for i in range(k):
		if p >= len(a):
			dest[i] = b[q]
			q += 1
		elif q >= len(b):
			dest[i] = a[p]
			p += 1
		elif a[p] < b[q]:
			dest[i] = a[p]
			p += 1
		else:
			dest[i] = b[q]
			count += len(a) - p
			q += 1
	return (dest, count)


def mergeSort(src):
	if len(src) <= 1:
		return src

	arrayLength = len(src)

	a = src[0:arrayLength/2]
	b = src[arrayLength/2:]

	n = mergeSort(a)
	m = mergeSort(b)
	return merge(n, m)

def merge(a, b):
	k = len(a) + len(b)
	p = 0
	q = 0
	dest = range(k)
	for i in range(k):
		if p >= len(a):
			dest[i] = b[q]
			q += 1
		elif q >= len(b):
			dest[i] = a[p]
			p += 1
		elif a[p] < b[q]:
			dest[i] = a[p]
			p += 1
		else:
			dest[i] = b[q]
			q += 1
	return dest

f = open('w1_IntegerArray.txt', 'r')
src = f.readlines()
for i in range(len(src)):
	src[i] = int(src[i].split()[0])

result = sort_and_count(src)
print result


