x = 42
print("id: ", id(x), " | type:", type(x))

a = [1,2,3]
b = a
b.append(4)
print("a is now ", a)

p = [1,2,3]
q = [1,2,3]
print("p is q: ", p is q)
print("p == q: ", p == q)

def add_itme(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_itme("a"))
print(add_itme("b"))

def add_item_fixed(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(add_item_fixed("a"))
print(add_item_fixed("b"))
