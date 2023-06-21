# Internals: Index Utils


## DataIndex
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/indices.py\#L62)
```python 
DataIndex()
```


---
A data Index, represents the actual collection of every row for each dimension used to create the overall metric.


**Returns**

* **DataIndex**  : A class that interfaces between the raw cached data and formats such as pandas' `pd.DataFrame`. 



**Methods:**


### .wipe
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/indices.py\#L110)
```python
.wipe(
   cls
)
```

---
Truncates the underlying cache, emptying all memory of downloaded content.


### .to_rich_table
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/indices.py\#L116)
```python
.to_rich_table(
   cls, name: str = None, ind_id: str = None
)
```

---
Renders the database to a rich table using `rich.table.Table`. Very expensive, low-use overall.


**Args**

* **name** (str, optional) : Indicator on which to filter before rendering. Defaults to None.
* **ind_id** (str, optional) : Indicator identifier on which to filter, of the form <ID>://<route>. Defaults to None.


**Returns**

* **Table**  : Rich object to display the cached data in the terminal. 


### .to_df
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/indices.py\#L137)
```python
.to_df(
   cls, name: str = None, ind_id: str = None
)
```

---
Merges every metric and its rows into a single consolidated dataframe.


**Args**

* **name** (str, optional) : Indicator on which to filter before rendering. Defaults to None.
* **ind_id** (str, optional) : Indicator identifier on which to filter, of the form <ID>://<route>. Defaults to None.


**Returns**

* **DataFrame**  : A dataframe of several hundred thousand rows containing every metric.


### .preprocess
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/indices.py\#L175)
```python
.preprocess(
   cls, dropna: bool = True, list_indicators: bool = False, indicator: str = None,
   normalize: bool = True, year_gt: int = 1980, debug: bool = False
)
```

---
Preprocesses the merged dataframe by grouping the metrics per batches of 5 years,
and normalizes the values across countries on that time period.


**Args**

* **dropna** (bool, optional) : Whether to drop NA rows. Defaults to True.
* **list_indicators** (bool, optional) : Whether to just list indicators instead of pre-processing. Defaults to False.
* **indicator** (str, optional) : Whether to filter on a specific indicator before pre-processing. Defaults to None.
* **normalize** (bool, optional) : Whether to perform cross-country normalization of the metrics. Defaults to True.
* **year_gt** (int, optional) : Whether to drop years before a certain date. Defaults to 1980, dropping all years before that date.
* **debug** (bool, optional) : Whether to log additionnal information, verbosity level. Defaults to False.


**Returns**

* **str**  : A preprocessed `pd.DataFrame` ready for use (storage | plotting | ranking)


----


### isCacheComplete
[source](https://github.com/arnos-stuff/open-borders-index\blob\master\openborders/indices.py\#L46)
```python
.isCacheComplete(
   db: TinyDB
)
```

---
Checks if cache is complete given the analysis dimensions provided by `openborders.data.Dimensions.All`


**Args**

* **db** (TinyDB) : The local cache data, stored in a `.json` TinyDB instance of a few MBs.


**Returns**

* **bool**  : Whether one dimension misses. False if one is not present.

