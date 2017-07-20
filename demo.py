import requests


def url(x):
    return 'http://localhost:8080/'+x


def demo(command, argv=[]):
    data = {'argv': argv}
    resp = requests.post(url(command), json=data)
    json = resp.json()
    print('='*20)
    print(command, argv)
    print('='*20)
    print(json['stdout'])
    print('#'*20)


demo('ls')
demo('cd', ['..'])
demo('ls')
