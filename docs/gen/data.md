# Internals: Data utils


## SourcePrefix
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L51)
```python 
SourcePrefix()
```


---
Represents a source using a file-like prefix. WB://<id> means the id points to a World Bank id, etc.


**Args**

* **str** (_type_) : Inherits from `str`, just a glorified prefix string.


**Returns**

* **SourcePrefix**  : A prefixed string class 



**Methods:**


### .WB
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L67)
```python
.WB(
   cls
)
```

---
Adds the World Bank Prefix to the object


**Returns**

* **Self**  : A `SourcePrefix` instance with Prefix set to `WB://`


### .GDIM
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L78)
```python
.GDIM(
   cls
)
```

---
Adds the World Bank's GDIM Prefix to the object


**Returns**

* **Self**  : A `SourcePrefix` instance with Prefix set to `GDIM://`


### .__matmul__
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L89)
```python
.__matmul__(
   cls, route: str
)
```

---
Equivalent of `at`, bases the route at the previously set prefix value.


**Args**

* **route** (str) : A route / id that points to a subset within the prefix


**Returns**

* **Self**  : A `SourcePrefix` instance with Prefix & route set.


### .at
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L120)
```python
.at(
   cls, route: str
)
```

---
Equivalent of `Self @ route`, bases the route at the previously set prefix value.


**Args**

* **route** (str) : A route / id that points to a subset within the prefix


**Returns**

* **Self**  : A `SourcePrefix` instance with Prefix & route set.


### .eval
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L133)
```python
.eval(
   cls
)
```

---
Evaluates the SourcePrefix to yield the entire identifier `<prefix><route>` or `<ID>://<route>`


**Returns**

* **str**  : the full identifier


### .prefix
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L142)
```python
.prefix(
   cls
)
```

---
A simple getter to retrieve the underlying prefix.


**Returns**

* **str**  : the prefix used by the class


### .from_pair
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L151)
```python
.from_pair(
   prefix: str, route: str
)
```

---
Creates immediately the built object from the `prefix` & `source` pair


**Args**

* **prefix** (str) : prefix as string, case insensitive.
* **route** (str) : route to be used from the prefix.


**Returns**

* **Self**  : A `SourcePrefix` instance with Prefix & route set.


### .eval_pair
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L164)
```python
.eval_pair(
   prefix: str, route: str
)
```

---
Creates and immediately evaluates the built object from the `prefix` & `source` pair


**Args**

* **prefix** (str) : prefix as string, case insensitive.
* **route** (str) : route to be used from the prefix.


**Returns**

* **str**  : A full identifier in string form `<ID>://<route>` 


### .normalize
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L177)
```python
.normalize(
   cls, full_name: str
)
```

---
Sets the route from a full identifier


**Args**

* **full_name** (str) :  A full identifier in string form `<ID>://<route>` 


**Returns**

* **Self**  : A `SourcePrefix` instance with Prefix & route set.


### .from_identifier
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L190)
```python
.from_identifier(
   cls, full_name: str
)
```

---
End to end setter from full identifier.


**Args**

* **full_name** (str) : A full identifier in string form `<ID>://<route>` 


**Returns**

* **Self**  : A `SourcePrefix` instance with Prefix & route set.


### .route
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L207)
```python
.route(
   cls
)
```

---
Simple getter for the `route` value


**Returns**

* **str**  : The route from prefix


----


## DataSource
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L279)
```python 
DataSource()
```


---
Represents a data source, as identified by a `SourcePrefix`.
The `DataSource` is able to check and fetch remote data based on the prefixes.


**Methods:**


### .as_gdim
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L291)
```python
.as_gdim(
   cls
)
```


### .as_wb
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L297)
```python
.as_wb(
   cls
)
```


### .is_wb
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L303)
```python
.is_wb(
   cls
)
```


### .is_gdim
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L307)
```python
.is_gdim(
   cls
)
```


### .from_identifier
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L311)
```python
.from_identifier(
   full_name: str
)
```


### .fetch
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L316)
```python
.fetch(
   cls
)
```


### .__str__
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L323)
```python
.__str__(
   cls
)
```


----


## Dimensions
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L269)
```python 
Dimensions()
```


---
A class regrouping all different statistics and dimensions across which a country should be ranked.


----


## Wages
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L251)
```python 
Wages()
```


---
Statistics pertaining to wages


**Args**

* **Enum** (_type_) : Types of statistics


----


## Immigration
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L225)
```python 
Immigration()
```


---
Statistics pertaining to immigration or population


**Args**

* **Enum** (_type_) : Types of statistics


----


## Business
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L261)
```python 
Business()
```


---
Statistics pertaining to ease of doing business


**Args**

* **Enum** (_type_) : Types of statistics


----


## Education
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L243)
```python 
Education()
```


---
Statistics pertaining to education


**Args**

* **Enum** (_type_) : Types of statistics


----


## MobilityMetrics
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L215)
```python 
MobilityMetrics()
```


---
All the social mobility metrics from the World Bank's GDIM database.


**Args**

* **Enum** (_type_) : Types of metrics (rank / yos / category)


----


## Labor
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/data.py\#L235)
```python 
Labor()
```


---
Statistics pertaining to labour and labour quality

**Args**

* **Enum** (_type_) : Types of statistics

