def append(list1, list2):
	return list1+list2


def concat(lists):
	return [item for list1 in lists for item in list1]


def filter(function, list):
	return [item for item in list if function(item)]


def length(list1):
	return len(list1)


def map(function, list1):
	return [function(item) for item in list1]


def foldl(function, list1, initial):
	print(initial)
	for f in list1:
		initial=function(initial, f)
	return initial


def foldr(function, list1, initial):
	for f in list1[::-1]:
		initial=function(f,initial)
	return initial


def reverse(list1):
	return list1[::-1]
