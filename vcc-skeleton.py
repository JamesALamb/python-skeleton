# DO NOT EDIT THIS FILE
from multiprocessing import Manager, Process
from flask import Flask, request, jsonify
import json
from time import clock
import os
from q1 import question01
from q2 import question02
from q3 import question03
from q4 import question04
from q5 import question05
from q6 import question06

app = Flask(__name__)

teamname = "Python"


# IMPORTANT: DO NOT CHANGE THIS FUNCTION
@app.route('/runq1', methods=['POST'])
def runq1_main():
    q1 = json.loads(request.data)
    q1tests = q1["tests"]
    response = []
    for testnumber in range(0, len(q1tests)):
        try:
            return_dict = Manager().dict()
            q1test = q1tests[testnumber]
            q1input = q1test["input"]
            p = Process(target=runq1, args=(q1input, return_dict))
            p.start()

            # Wait for 1 seconds or until process finishes
            p.join(1)

            # If thread is still active
            if p.is_alive():
                # Terminate
                print("A question 1 test has timed out. Each individual test has a maximum of one second to run.")
                p.terminate()
                p.join()
            else:
                correct = return_dict['output'] == q1test["output"]
                response.append({
                        "teamName": teamname,
                        "questionNumber": 1,
                        "testNumber": testnumber,
                        "correct": correct,
                        "speed": return_dict['diff'] * 1000000000
                    })
        except Exception as e:
            print(e)

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# DO NOT CHANGE THIS FUNCTION EITHER
def runq1(q1input, return_dict):
    start = clock()
    output = question01(q1input)
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# IMPORTANT: DO NOT CHANGE THIS FUNCTION
@app.route('/runq2', methods=['POST'])
def runq2_main():
    q2 = json.loads(request.data)
    q2tests = q2["tests"]
    response = []
    for testnumber in range(0, len(q2tests)):
        try:
            return_dict = Manager().dict()
            q2test = q2tests[testnumber]
            q2input = q2test["input"]
            p = Process(target=runq2, args=(q2input, return_dict))
            p.start()

            # Wait for 1 second or until process finishes
            p.join(1)

            # If thread is still active
            if p.is_alive():
                # Terminate
                print("A question 2 test has timed out. Each individual test has a maximum of one second to run.")
                print(q2input["numNodes"], q2input["edges"], return_dict['output'], q2test["output"])
                p.terminate()
                p.join()
            else:
                correct = return_dict['output'] == q2test["output"]
                if not correct:
                    print(q2input["numNodes"], q2input["edges"], return_dict['output'], q2test["output"])
                response.append({
                        "teamName": teamname,
                        "questionNumber": 2,
                        "testNumber": testnumber,
                        "correct": correct,
                        "speed": return_dict['diff'] * 1000000000
                    })
        except:
            print("An exception occurred")

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# DO NOT CHANGE THIS FUNCTION EITHER
def runq2(q2input, return_dict):
    start = clock()
    output = question02(q2input["cashFlowIn"], q2input["cashFlowOut"])
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# IMPORTANT: DO NOT CHANGE THIS FUNCTION
@app.route('/runq3', methods=['POST'])
def runq3_main():
    q3 = json.loads(request.data)
    q3tests = q3["tests"]
    response = []
    for testnumber in range(0, len(q3tests)):
        try:
            return_dict = Manager().dict()
            q3test = q3tests[testnumber]
            q3input = q3test["input"]
            p = Process(target=runq3, args=(q3input, return_dict))
            p.start()

            # Wait for 1 second or until process finishes
            p.join(1)

            # If thread is still active
            if p.is_alive():
                # Terminate
                print("A question 3 test has timed out. Each individual test has a maximum of one second to run.")
                p.terminate()
                p.join()
            else:
                correct = return_dict['output'] == q3test["output"]
                response.append({
                        "teamName": teamname,
                        "questionNumber": 3,
                        "testNumber": testnumber,
                        "correct": correct,
                        "speed": return_dict['diff'] * 1000000000
                    })
        except:
            print("An exception occurred")

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# DO NOT CHANGE THIS FUNCTION EITHER
def runq3(q3input, return_dict):
    start = clock()
    output = question03(q3input["numNodes"], q3input["edges"])
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# IMPORTANT: DO NOT CHANGE THIS FUNCTION
@app.route('/runq4', methods=['POST'])
def runq4_main():
    q4 = json.loads(request.data)
    q4tests = q4["tests"]
    response = []
    for testnumber in range(0, len(q4tests)):
        try:
            return_dict = Manager().dict()
            q4test = q4tests[testnumber]
            q4input = q4test["input"]
            p = Process(target=runq4, args=(q4input, return_dict))
            p.start()

            # Wait for 1 second or until process finishes
            p.join(1)

            # If thread is still active
            if p.is_alive():
                # Terminate
                print("A question 4 test has timed out. Each individual test has a maximum of one second to run.")
                p.terminate()
                p.join()
            else:
                correct = return_dict['output'] == q4test["output"]
                response.append({
                    "teamName": teamname,
                    "questionNumber": 4,
                    "testNumber": testnumber,
                    "correct": correct,
                    "speed": return_dict['diff'] * 1000000000
                })
        except:
            print("An exception occurred")

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# DO NOT CHANGE THIS FUNCTION EITHER
def runq4(q4input, return_dict):
    start = clock()
    output = question04(q4input["rows"], q4input["numberMachines"])
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# IMPORTANT: DO NOT CHANGE THIS FUNCTION
@app.route('/runq5', methods=['POST'])
def runq5_main():
    q5 = json.loads(request.data)
    q5tests = q5["tests"]
    response = []
    for testnumber in range(0, len(q5tests)):
        try:
            return_dict = Manager().dict()
            q5test = q5tests[testnumber]
            q5input = q5test["input"]
            p = Process(target=runq5, args=(q5input, return_dict))
            p.start()

            # Wait for 1 second or until process finishes
            p.join(1)

            # If thread is still active
            if p.is_alive():
                # Terminate
                print("A question 5 test has timed out. Each individual test has a maximum of one second to run.")
                p.terminate()
                p.join()
            else:
                correct = return_dict['output'] == q5test["output"]
                if not correct:
                    print(q5input["numNodes"], q5input["edges"], return_dict['output'], q5test["output"])

                response.append({
                    "teamName": teamname,
                    "questionNumber": 5,
                    "testNumber": testnumber,
                    "correct": correct,
                    "speed": return_dict['diff'] * 1000000000
                })
        except:
            print("An exception occurred")

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# DO NOT CHANGE THIS FUNCTION EITHER
def runq5(q5input, return_dict):
    start = clock()
    output = question05(q5input["allowedAllocations"], q5input["totalValue"])
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# IMPORTANT: DO NOT CHANGE THIS FUNCTION
@app.route('/runq6', methods=['POST'])
def runq6_main():
    q6 = json.loads(request.data)
    q6tests = q6["tests"]
    response = []
    for testnumber in range(0, len(q6tests)):
        try:
            return_dict = Manager().dict()
            q6test = q6tests[testnumber]
            q6input = q6test["input"]
            p = Process(target=runq6, args=(q6input, return_dict))
            p.start()

            # Wait for 1 second or until process finishes
            p.join(1)

            # If thread is still active
            if p.is_alive():
                # Terminate
                print("A question 6 test has timed out. Each individual test has a maximum of one second to run.")
                p.terminate()
                p.join()
            else:
                correct = return_dict['output'] == q6test["output"]
                if not correct:
                    print(q6input["numNodes"], q6input["edges"], return_dict['output'], q6test["output"])
                response.append({
                    "teamName": teamname,
                    "questionNumber": 6,
                    "testNumber": testnumber,
                    "correct": correct,
                    "speed": return_dict['diff'] * 1000000000
                })
        except:
            print("An exception occurred")

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# DO NOT CHANGE THIS FUNCTION EITHER
def runq6(q6input, return_dict):
    start = clock()
    output = question06(q6input["numServers"], q6input["targetNode"], q6input["arcs"])
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8182))
    app.run(host='0.0.0.0', port=port)
