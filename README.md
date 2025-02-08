# USING PYTHON REQUESTS REST CLIENT
This project shows a very simple example of using a Python Rest client based on the [`requests` library](https://pypi.org/project/requests/).

## Project Overview
The project is so simple that we can summarise it here:

```python
import requests
import json
import time

list = [
    "a",
    "b",
    "f"
]
for item in list:
    try:
        response = requests.get(
            f"https://super-secret-api.com.br/v1/info/{item}/secure-key"
        )

        if response.status_code == 200:
            print(json.dumps(response.json()))
            print(", ")

        time.sleep(10)

    except Exception as e:
        print(e)
```

The point here is simplicity. Extracting some information is all we needed. So, no need for complex structures, design patterns, infinite variables. Just get the info - if something goes wrong, let me know!

_"Oh, but what if they need to change it in the future?"_, people say. Most likely they will - software is always changing. However, now, today, given resources, deadlines, and requirements we've got, this is all we need! If it needs to be updated in the future, well, so we can update it. If it needs to evolve to more complex structure _in the future_ to support extension and other scenarios, well, let's do it, but **in the future**, not now.

If this sounds infamous for you, perhaps you should have a look at:
- [The software architect elevator](https://a.co/d/a7ufuIC)
- [Clean architecture](https://a.co/d/0Shc2IJ)