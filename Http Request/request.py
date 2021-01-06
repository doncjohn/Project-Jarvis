from urllib import request
resp = request.urlopen("https://gridzybe.com/")
print(resp.code)
print(resp.length)
print(resp.peek())