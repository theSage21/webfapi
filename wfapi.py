import os
import bottle
from subprocess import run, PIPE

PWD = os.getcwd()
app = bottle.Bottle()


@app.post('/ls')
def ls():
    global PWD
    argv = bottle.request.json['argv']
    command = ' '.join(['cd', PWD, '&&', 'ls'] + argv)
    p = run(command, stderr=PIPE, stdout=PIPE, shell=True)
    data = {'return_code': p.returncode,
            'stdout': p.stdout.decode(),
            'stderr': p.stderr.decode()}
    return data


@app.post('/cd')
def cd():
    global PWD
    argv = bottle.request.json['argv']
    command = ' '.join(['cd', PWD, '&&', 'cd'] + argv + ['&&', 'ls'])
    PWD = os.path.join(PWD, argv[0])
    print(PWD, command)
    p = run(command, stderr=PIPE, stdout=PIPE, shell=True)
    data = {'return_code': p.returncode,
            'stdout': p.stdout.decode(),
            'stderr': p.stderr.decode()}
    print(data)
    return data


@app.get('/<path:path>')
def callback(path):
    return bottle.static_file(path, '/home/arjoonn/webfapi')


if __name__ == '__main__':
    app.run(debug=True)
