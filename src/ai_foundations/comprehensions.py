# 1) collect the uppercase version of each word 
words = ["ai", "ml", "llm"]
uppercase_words = [x.upper() for x in words]
print(uppercase_words)

# 2) keep only positive numbers 
nums = [-2, 5, -1, 8, 0, 3]
pos_nums = [x for x in nums if x>0]
print(pos_nums)

# 3) build a {number: its square} mapping for 1...5
squares = {x:x*x for x in range(1,6)}
print(squares)
