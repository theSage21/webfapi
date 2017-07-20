import os
import bottle
from subprocess import run, PIPE

app = bottle.Bottle()
PWD = os.getcwd()


@app.post('/ls')
def ls():
    argv = bottle.request.json['argv']
    command = ' '.join(['cd', PWD, '&&', 'ls'] + argv)
    p = run(command, stderr=PIPE, stdout=PIPE, shell=True)
    data = {'return_code': p.returncode,
            'stdout': p.stdout.decode(),
            'stderr': p.stderr.decode()}
    return data


@app.post('/cd')
def cd():
    argv = bottle.request.json['argv']
    command = ' '.join(['cd', PWD, '&&', 'cd'] + argv)
    global PWD
    PWD = os.path.join(PWD, argv[0])
    print(PWD)
    p = run(command, stderr=PIPE, stdout=PIPE, shell=True)
    data = {'return_code': p.returncode,
            'stdout': p.stdout.decode(),
            'stderr': p.stderr.decode()}
    return data


if __name__ == '__main__':
    app.run(server='paste', debug=True)
