# pyDBCollect
pyDBCollect is a python package with drop-in replacements for 
built-in python collections that persist to a database.

## DBSet
Create a DBSet in memory
```python
from pydbcollect import DBSet as set

a = set('stuffintheset')
a -= set('toremove')
print(a)
```

Create a DBSet
## Set Tests
As a drop-in replacement, DBSet should pass all reasonable
tests for the standard set in python stdlib

Suite | Test | DBSet Passes? | Explanation
---|------|---|--- 
