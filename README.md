# Nitrogen
---

Nitrogen is a Python module designed to make desktop app development in Python easier. It utilizes [Flask](), [Jinja2](), and [web technologies]() to create the Python equivalent of [Electron]().

### Installation

To install from PyPi **(recommended)**:
```sh
pip install nitrogenfw
```
or, to install from source:
```sh
git clone https://github.com/ii-Python/nitrogen
cd nitrogen
python3 setup.py install  # or pip install .
```

### Module usage

To begin developing using Nitrogen, create a `src` folder and a file named `app.py`. The `src` folder is where all your web files will be stored, this includes your HTML, CSS, etc. The `app.py` file will be the entrypoint to your application.  

Inside `app.py`, put the following template:
```py
from nitrogen import Nitrogen
app = Nitrogen(source_dir = "src", use_jinja = True)
app.start()
```

Now, inside `src/index.html`, put any HTML that you want to render. In my case, I put the following:
```html
<div style = "text-align: center; padding-top: 45px">
    <h3>Hello, world!</h3>
</div>
```

To start your app, simply run `app.py`. You should see your HTML file render!

### Configuration

By default, Nitrogen does not need passed any kwargs at runtime. However they can be useful if Nitrogen does not do what you are trying to accomplish.  

When creating a `Nitrogen` object, you can pass the following kwargs:
+ `source_dir`; default: "src"; This is where Nitrogen + Jinja will look for files
+ `use_jinja`; default: True; Indicates if Nitrogen should use Jinja to render templates

After you make the `Nitrogen` object, and you use `app.start()`, you can pass the following:
+ `start_location`; default: "index.html"; This is the first page Nitrogen will render upon start
