import requests


def url(x):
    return 'http://localhost:8080/'+x


def test_ls():
    resp = requests.get(url('ls'))
    json = resp.json()
    assert json['return_code'] == 0
    assert json['stderr'].strip() == ''
    assert json['stdout'].strip() != ''


def test_cd():
    data = {'path': '..'}
    resp = requests.post(url('cd'), json=data)
    json = resp.json()
    assert json['return_code'] == 0
    assert json['stderr'].strip() == ''
    assert json['stdout'].strip() != ''
