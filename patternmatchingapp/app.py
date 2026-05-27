from flask import Flask, render_template, request
import time

app = Flask(__name__)

# -------------------------------------------------------
# Naive Algorithm
# -------------------------------------------------------
def naive_search(txt, pat):

    m = len(txt)
    n = len(pat)

    steps = []

    for i in range(m - n + 1):

        current = txt[i:n+i]
        match = current == pat

        steps.append({
            'window': current,
            'index': i,
            'match': match
        })

        if match:
            return i, steps

    return -1, steps


# -------------------------------------------------------
# Rabin Karp
# -------------------------------------------------------
def rabin_karp(text, pattern, d=256, q=101):

    n = len(text)
    m = len(pattern)

    h = pow(d, m-1) % q

    p = 0
    t = 0

    result = []

    for i in range(m):

        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):

        if p == t:

            if text[s:s+m] == pattern:
                result.append(s)

        if s < n - m:

            t = (d * (t - ord(text[s]) * h)
                 + ord(text[s + m])) % q

            if t < 0:
                t += q

    return result


# -------------------------------------------------------
# KMP
# -------------------------------------------------------
def compute_lps(pattern):

    m = len(pattern)

    lps = [0] * m

    length = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[length]:

            length += 1
            lps[i] = length
            i += 1

        else:

            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(pattern, text):

    m = len(pattern)
    n = len(text)

    lps = compute_lps(pattern)

    i = 0
    j = 0

    matches = []

    while i < n:

        if pattern[j] == text[i]:

            i += 1
            j += 1

        if j == m:

            matches.append(i-j)
            j = lps[j-1]

        elif i < n and pattern[j] != text[i]:

            if j != 0:
                j = lps[j-1]

            else:
                i += 1

    return matches, lps


# -------------------------------------------------------
# Home Route
# -------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])

def home():

    result = None

    if request.method == 'POST':

        text = request.form['text']
        pattern = request.form['pattern']
        algorithm = request.form['algorithm']

        # Naive
        start = time.time()
        naive_index, naive_steps = naive_search(text, pattern)
        naive_time = time.time() - start

        # Rabin-Karp
        start = time.time()
        rk_result = rabin_karp(text, pattern)
        rk_time = time.time() - start

        # KMP
        start = time.time()
        kmp_result, lps = kmp_search(pattern, text)
        kmp_time = time.time() - start

        result = {

            'algorithm': algorithm,

            'naive_index': naive_index,
            'naive_time': naive_time,

            'rk_result': rk_result,
            'rk_time': rk_time,

            'kmp_result': kmp_result,
            'kmp_time': kmp_time,

            'lps': lps
        }

    return render_template(
        'index.html',
        result=result
    )


if __name__ == '__main__':
    app.run()