# Documentation of WifiScannerPro
## import
```python
>>> from WifiScanner.scanner import Scanner
```
### WifiScanner.Scanner(username=None, password=None, urls=None, range=None)
Base: `object`

#### \__init__(username, password, urls, range)

Initialize self. See help(type(self)) for accurate signature.

#### wifi_hack()
Returns a list of wifi name, password, location

```python
>>> scanner = Scanner(username=[], password=[], urls=[])
>>> print(scanner.wifi_hack())
Output
---------
[{"WifiName": wifiName, "Password": Password, "Location": Location, "URL": url}]
```

* **Returns**
    Python dictionary inside a list

* **Parameters**

    **urls**     – A list of ip address like([10.0.1.1, 10.0.0.2]etc)
    **username** – A list of username. Note the list will only contain 2
                   user name for this version
    **password** – A list of username. Note the list will only contain 2
                   user name for this version

#### is_http_running()
Return if any http server running on this host or ip

```python
>>> scanner = Scanner()
>>> print(scanner.is_http_running(host))
Output
---------
True or False # Based on running or not
```

* **Returns**
    Python bool 

* **Parameters**

    **host** – An Ip address
    **port** – By default 80(It is the default port for http). For any
               other server give the valid port  

#### scan_ip()
Returns a list of ip address those are running http server on port 80 based on given ip range 

```python
>>> scanner = Scanner(range="10.0.0.1-10.0.0.10") # like this
>>> print(scanner.scan_ip())
Output
---------
[10.0.0.1, 10.0.0.6, 10.0.0.8] #etc
```

* **Returns**
    Python list of ip address

* **Parameters**

    **range** – A range of ip like("10.0.0.1-10.0.0.10")

#### save_as_html()
Save the return data of wifi_hack method as html format

```python
>>> scanner = Scanner() # like this
>>> scanner.save_as_html(data, dir="the location", name="fileName.html")
Output
---------

```

* **Returns**
    Saves the the return data of wifi_hack method as html

* **Parameters**

    **data** – A list of dictionary with the keys 'WifiName','URL','Password', 'Location'
    **dir** – The location of the file file where you want to save the file
    **name** – The name of the file with extension

#### open_htmlfile()
Opens the the given html file in web browser

```python
>>> scanner = Scanner() # like this
>>> scanner.open_htmlfile(dir="the location", name="fileName.html")
Output
---------

```

* **Returns**
    Opens the html file in web browser

* **Parameters**

    **dir** – The location of the file file where you want to save the file
    **name** – The name of the file with extension

#### save_as_json()
Save the return data of wifi_hack method as json format

```python
>>> scanner = Scanner() # like this
>>> print(scanner.save_as_json(data, dir="the location", name="fileName.json"))
Output
---------

```

* **Returns**
    Saves the the return data of wifi_hack method as html

* **Parameters**

    **data** – A list of dictionary with the keys 'WifiName','URL','Password', 'Location'
    **dir** – The location of the file file where you want to save the file
    **name** – The name of the file with extension

#### load_json()
Returns the data of a json file as a dict

```python
>>> scanner = Scanner() # like this
>>> print(scanner.save_as_json(data, dir="the location", name="fileName.json"))
Output
---------

```

* **Returns**
    The data of a json file as a python dict

* **Parameters**

    **location** – The location of the json file