# -*- coding: utf-8 -*-
import base64
raw_b64 = "Pz8/Pz8gKFNQRUNJQUwgUE9XRVIgT0YgQVRUT1JORVkp"
decoded = base64.b64decode(raw_b64.encode('ascii')).decode('utf-8')
with open('d:/promotion/.agents/worker_m4/test_out.txt', 'w', encoding='utf-8') as out:
    out.write(decoded)
