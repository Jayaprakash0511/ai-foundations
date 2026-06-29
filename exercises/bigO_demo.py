import timeit

n = 10000
data_list = list(range(n))
data_set = set(range(n))

target = n-1

list_time = timeit.timeit(lambda: target in data_list, number=1000)
set_time = timeit.timeit(lambda: target in data_set, number=1000)

print(f"list membership (O(n)): {list_time:.4f}s")
print(f"set membership (O(1)): {set_time:.4f}s")

print(f"set is ~{list_time / set_time:.2f}x faster than list for membership testing.")
