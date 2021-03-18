a = "code"
b = "python"
c = "purwadhika"

def urai(str):
    result = ''
    for i in range(len(str)):
        result += str[:i+1]
    return result

urai(a)
urai(b)
urai(c)


