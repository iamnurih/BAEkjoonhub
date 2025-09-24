def reverse_words(text):
    return " ".join(text.split()[::-1])

N=int(input())
cases = []
for i in range(N):
    cases.append(reverse_words(input()))

for idx, result in enumerate(cases):
    print(f"Case #{idx +1}: {result}")
    