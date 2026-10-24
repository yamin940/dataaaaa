def unique_in_order(values):
    seen = set()
    result = []
    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(unique_in_order([1, 2, 2, 3, 1, 4]))

def word_frequencies(text):
    words = text.split()
    frequencies = {}
    for word in words:
        cleaned_word = word.strip('.,!?":;()[]{}')
        if cleaned_word:
            frequencies[cleaned_word] = frequencies.get(cleaned_word, 0) + 1
    return frequencies
print(word_frequencies("hello world hello"))

def top_k(frequencies, k):
    return sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))[:k]
freqs = {"apple": 5, "banana": 2, "cherry": 5} 
print(top_k(freqs, 2))

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(transpose([[1, 2, 3], [4, 5, 6]]))

def invert(mapping):
    inverted = {}
    for k, v in mapping.items():
        inverted.setdefault(v, []).append(k)
    for v in inverted:
        inverted[v].sort()
    return inverted
print(invert({'a': 1, 'b': 2, 'a': 3}))

def common_elements(first, second):
    return list(set(first) & set(second))

print(common_elements([1, 2, 3], [2, 3, 4]))

def group_by_length(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        if word not in groups[length]:
            groups[length].append(word)
    return groups
print(group_by_length(["cat", "dog", "elephant", "bat"]))

class Bag:
     def init(self):
         self.data = {}
def add(self, item):
        self.data[item] = self.data.get(item, 0) + 1

def remove(self, item):
    if item in self.data:
        self.data[item] -= 1
        if self.data[item] <= 0:
            del self.data[item]

def count(self, item):
    return self.data.get(item, 0)

def __len__(self):
    return sum(self.data.values())

def distinct_items(self):
    return list(self.data.keys())

def clear(self):
    self.data.clear()

def is_empty(self):
    return len(self.data) == 0

def union(self, other):
    result = Bag()
    for item, count in self.data.items():
        result.data[item] = count
    for item, count in other.data.items():
        result.data[item] = max(result.data.get(item, 0), count)
    return result

def intersection(self, other):
    result = Bag()
    for item, count in self.data.items():
        if item in other.data:
            result.data[item] = min(count, other.data[item])
    return result

def difference(self, other):
    result = Bag()
    for item, count in self.data.items():
        diff = count - other.data.get(item, 0)
        if diff > 0:
            result.data[item] = diff
    return result
my_bag = Bag() 
my_bag.add("apple") 
print(my_bag.count("apple"))

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(3): print(num)

def chunks(values, size):
    for i in range(0, len(values), size):
        yield values[i:i + size]

for chunk in chunks([1, 2, 3, 4, 5], 2): print(chunk)