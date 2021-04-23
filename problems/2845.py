n = (lambda l, p: l * p)(*map(int, input().split()))
print(*map(lambda x: int(x) - n, input().split()))
