d, h, m = map(int, input().split())
r = d * 1440 + h * 60 + m - 16511
print(-1 if r < 0 else r)
