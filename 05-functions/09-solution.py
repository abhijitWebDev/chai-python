# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    li = []
    for i in range(2, limit+1, 2):
        # li.append(i)
        # return li
        yield i

for num in even_generator(12):
    print(num)