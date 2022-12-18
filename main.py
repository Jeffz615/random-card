# -*- coding:utf-8 -*-
import numpy as np
import time
import hashlib
from flask import Flask, render_template
import json
import sys
import os
import threading
import webbrowser

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)
with open('song.json', 'r', encoding="utf-8") as f:
    jdata = json.load(f)

np.random.seed(int(hashlib.md5(time.time().hex().encode()).hexdigest(), 16) & 0xffffffff)
arrays = []
for lang_group in jdata.get('langs_group'):
    tmp_arr = {"title": lang_group.get('title'), "label": lang_group.get('label')}
    tmp_items = []
    for lang in lang_group.get('langs'):
        for x in jdata['items'][lang[0]]:
            tmp_items.append([lang[1], x[0], x[1]])
    np.random.shuffle(tmp_items)
    tmp_arr["items"] = tmp_items
    arrays.append(tmp_arr)


@app.route('/')
def get_random_pool():
    np.random.seed(int(hashlib.md5(time.time().hex().encode()).hexdigest(), 16) & 0xffffffff)
    rt_arrays = []
    for arr in arrays:
        my_items = arr["items"].copy()
        np.random.shuffle(my_items)
        my_rt = {"title": str(arr.get('title') or ""), "label": str(arr.get('label') or "")}

        index = 1
        num_length = len(str(len(my_items)))
        rt_items = []
        for x in my_items:
            rt_items.append(
                {'no': str(arr.get('label')) + str(index).zfill(num_length), 'lang': x[0], 'song': x[1], 'singer': x[2]}
            )
            index += 1
        my_rt["rand_items"] = rt_items
        rt_arrays.append(my_rt)
    return render_template('index.html', data=rt_arrays)


def start_web():
    time.sleep(1)
    webbrowser.open(f"http://127.0.0.1:{jdata.get('port')}", new=0, autoraise=True)


if __name__ == '__main__':
    t = threading.Thread(target=start_web)
    t.start()
    app.run(port=jdata.get('port'), debug=False)
    t.join()
