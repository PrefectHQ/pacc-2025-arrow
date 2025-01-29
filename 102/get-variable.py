from prefect.variables import Variable

var = Variable.get(
    "answer"
)  # answer is a variable on the server, set in the UI or code
print(var)
