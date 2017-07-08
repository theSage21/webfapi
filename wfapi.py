import os
import bottle
from subprocess import run, PIPE

app = bottle.Bottle()
PWD = os.getcwd()


@app.get('/ls')
def ls():
    p = run('ls {}'.format(PWD), stderr=PIPE, stdout=PIPE, shell=True)
    data = {'return_code': p.returncode,
            'stdout': p.stdout.decode(),
            'stderr': p.stderr.decode()}
    return data


@app.post('/cd')
def cd():
    path = bottle.request.json['path']
    p = run('cd {} && pwd'.format(path), stderr=PIPE, stdout=PIPE, shell=True)
    data = {'return_code': p.returncode,
            'stdout': p.stdout.decode(),
            'stderr': p.stderr.decode()}
    global PWD
    PWD = data['stdout'].strip()
    return data


if __name__ == '__main__':
    app.run(server='paste')
