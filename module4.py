# Уровень 1 бинарный поиск в отсортированном массиве
# Сделал итеративно, так как рекурсия в Python как правило работает медленее

def binary_search(num_list, search_item):
    low = 0
    high = len(num_list)
    search_res = False

    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = num_list[middle]
        if guess == search_item:
            search_res = True
            break
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    return search_res

num_list = sorted([3, 6, 8, 1, 12, 56, 78, 96, 34, 112, 156, 2, 456])
value = 1

result = binary_search(num_list, value)
if result:
    print(f'Цифра {value} найдена')
else:
    print(f'Цифра {value} в списке отсутствует')


# Уровень 2 сортировка списка вставками
num_list2 = [3, 6, 8, 1, 12, 56, 78, 96, 34, 112, 156, 2, 456]

def insertion_sort(num_list):
    len_list = len(num_list)

    for i in range(1, len_list):
        for j in range(i, 0, -1):
            if num_list2[j] < num_list2[j - 1]:
                num_list2[j], num_list2[j - 1] = num_list2[j - 1], num_list2[j]
            else:
                break
    return num_list2
print(insertion_sort(num_list2))


# Уровень 3 (Очень сложно к пониманию, нужно еще разбираться)
adj = [
    [1,3], # 0
    [0,3,4,5], # 1
    [4,5], # 2
    [0,1,5], # 3
    [1,2], # 4
    [1,2,3] # 5
]

level = [-1] * len(adj)

def bfs(s):
    global level
    level[s] = 0
    queue = [s]
    while queue:
        v = queue.pop(0)
        for w in adj[v]:
            if level[w] == -1:
                queue.append(w)
                level[w] = level[v] + 1

for i in range(len(adj)):
    if level[i] == -1:
        bfs(i)

print(level[2])