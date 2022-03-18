
* Create & activate a virtual env, upgrade pip and install modules required by the project and the packaging process
```
>python -m venv venv
[...]
>.\venv\Scripts\activate
(venv) >python -m pip install --upgrade pip
[...]
(venv) >pip install -r requirements\package.requirements.txt
[...]
(venv) >pip install -r requirements\development.requirements.txt
``` 

* Build the Python package
```
(venv) >python setup.py bdist_wheel --universal
```

* The package shouild have been created under the dist folder : 
```
> dir dist
[...]
03/18/2022  04:26 PM             1,051 hello_pyspark-1.0-py2.py3-none-any.whl
[...]          
```