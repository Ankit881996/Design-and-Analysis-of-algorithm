import time

def rabin_karp(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)

    h = pow(d, m - 1) % q

    p = 0
    t = 0

    result = []

    # Calculate hash value
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide pattern over text
    for s in range(n - m + 1):

        # If hash values match
        if p == t:

            # Check characters one by one
            if text[s:s + m] == pattern:
                result.append(s)

        # Calculate next window hash
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) +
                 ord(text[s + m])) % q

            if t < 0:
                t += q

    return result


# -------- MAIN PROGRAM --------

text = input("Enter Text : ")
pattern = input("Enter Pattern : ")

stime = time.time()

result = rabin_karp(text, pattern)

etime = time.time()

if result:
    print("Pattern found at positions:", result)
else:
    print("Pattern not found")

print("Execution Time:", etime - stime)