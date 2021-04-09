import os

password="asdf"
secret = "verysecret"

password: ${test}


def auth(user: "urandom",password = None):
    print(user,password)