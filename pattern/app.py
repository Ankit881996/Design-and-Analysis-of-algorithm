from flask import Flask, render_template_string, request
import time

app = Flask(__name__)

# Pattern searching function
def function(txt, pat, m, n):
    for i in range(m - n + 1):
        if txt[i:n+i] == pat:
            return i
    return -1

# HTML Page
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Pattern Matching</title>
    <style>
        body{
            font-family: Arial;
            background:#f4f4f4;
            padding:40px;
        }
        .container{
            width:400px;
            margin:auto;
            background:white;
            padding:20px;
            border-radius:10px;
            box-shadow:0 0 10px gray;
        }
        input{
            width:100%;
            padding:10px;
            margin-top:10px;
        }
        button{
            margin-top:15px;
            padding:10px;
            width:100%;
            background:blue;
            color:white;
            border:none;
            cursor:pointer;
        }
        h2{
            text-align:center;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Pattern Matching</h2>

    <form method="POST">
        <input type="text" name="text" placeholder="Enter Text" required>

        <input type="text" name="pattern" placeholder="Enter Pattern" required>

        <button type="submit">Search</button>
    </form>

    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
        <h3>Execution Time: {{ execution_time }} seconds</h3>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    execution_time = None

    if request.method == "POST":
        txt = request.form["text"]
        pat = request.form["pattern"]

        stime = time.time()
        time.sleep(1)

        result = function(txt, pat, len(txt), len(pat))

        etime = time.time()
        execution_time = round(etime - stime - 1, 6)

    return render_template_string(
        HTML,
        result=result,
        execution_time=execution_time
    )

if __name__ == "__main__":
    app.run(debug=True)