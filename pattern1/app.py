from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Pattern Matching Function
def function1(txt, pat, m, n):

    for i in range(m - n + 1):

        if txt[i:n+i] == pat:
            return i

    return -1


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    txt_len = None
    pat_len = None
    execution_time = None

    if request.method == "POST":

        f = open("input1.txt", "r")
        f2 = open("pattern.txt", "r")

        txt = f.read().strip()
        pat = f2.read().strip()

        f.close()
        f2.close()

        stime = time.time()

        time.sleep(1)

        result = function1(txt, pat, len(txt), len(pat))

        etime = time.time()

        txt_len = len(txt)
        pat_len = len(pat)

        execution_time = round(etime - stime - 1, 6)

    return render_template(
        "index.html",
        result=result,
        txt_len=txt_len,
        pat_len=pat_len,
        execution_time=execution_time
    )


if __name__ == "__main__":
    app.run()