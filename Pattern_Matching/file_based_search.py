import time

def function1(txt, pat, m, n):
    for i in range(m - n + 1):
        if txt[i:n+i] == pat:
            return i
    return -1

# Open text file
f = open("input1.txt", "r")

# Open pattern file
f2 = open("pattern.txt", "r")

# Read contents
txt = f.read().strip()
pat = f2.read().strip()

# Start time
stime = time.time()

# Search pattern
print("Pattern found at index:",
      function1(txt, pat, len(txt), len(pat)))

# End time
etime = time.time()

print("Length of Text:", len(txt))
print("Length of Pattern:", len(pat))
print("Execution Time:", etime - stime)

# Close files
f.close()
f2.close()