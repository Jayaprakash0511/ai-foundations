# 1. Dedup, keep order: given [3, 1, 3, 5, 1, 9], return [3, 1, 5, 9] (duplicates removed, first-seen order preserved). Hint: a set to track "seen," a list for the output.
# 2. Word frequency: given "the cat sat on the mat the cat", return {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}. Hint: a dict.
# 3. Common elements: given two lists, return the values present in both, efficiently. Hint: set intersection.
# 4. Two-sum: given nums = [2, 7, 11, 15] and target = 9, return the indices [0, 1] of the two numbers that add to the target — in a single pass. Hint: a dict mapping value → index as you go.
# 5. Anagram check: return True if two strings use the same letters with the same counts ("listen", "silent" → True). Hint: compare letter-count dicts, or sorted characters.

from collections import Counter

nums = [3,1,3,5,1,9]
ans = []
seen = set()
for num in nums:
    if num not in seen:
        ans.append(num)
        seen.add(num)
print(ans)


text = "the cat sat on the mat the cat"
count = {}
for word in text.split():
    count[word] = count.get(word, 0) + 1
print(count)

def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return (list(set1&set2))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if (target-num) in seen:
            return (seen[target-num], i)
        seen[num] = i

print(two_sum([2,7,11,15], 9))

def check_anagram(str1, str2):
    return Counter(str1)==Counter(str2)

print(check_anagram("listen", "silent"))
