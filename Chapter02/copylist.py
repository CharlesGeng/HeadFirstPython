first = list(range(5))
second = first
third = first.copy()

# Both list FIRST and SECOND will turn to [0, 1, 2, 3, 4, 121]
# But third will remain [0, 1, 2, 3, 4]
second.append(121)

print(first)
print(second)
print(third)
