def first_and_last(s):
	a = list(s)
	g = list(s)
	
	a.sort()
	g.sort(reverse=True)

	a = "".join(a)
	g = "".join(g)

	return [a, g]

b = first_and_last("hello")

print(b)


s = 'kushagra'
ls = list(s)
ls.sort()
ls = "".join(ls)
print(ls)


print(less_than_or_equal_to_zero(-12345))