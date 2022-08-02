number = [200,400,600]
out = map(str, number)
print(list(out))

out = map(lambda i: i/10, number)
print(list(out))




# map = make changes to every element
# filter = apply condition on everything