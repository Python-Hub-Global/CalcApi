from flask import Flask, request

app = Flask(__name__)


@app.route('/calc', methods=["GET", "POST"])
def calc():

    value1 = int(request.args['value1'])
    value2 = int(request.args['value2'])
    # operation = request.args['operation']
    st = request.query_string.decode()
    # print(type(operation))
    list = []
    for i in range(len(st)):
        if st[i] == '=':
            list.append(st[i+1])
    op = list[-1]

    if op == '+':
        ans = value1 + value2
        return str(ans)
    elif op == '-':
        ans = value1 - value2
        return str(ans)
    else:
        ans = value1 * value2
        return str(ans)


if __name__ == '__main__':
    app.run()
