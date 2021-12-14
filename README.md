not_covered_lines
=================

This module takes a path to a directory, where previously 
`coverage.py` was executed and thus now has the file `.coverage`
in it, which it reads. It outputs a list of missing lines in 
the form `[(filename, line_number)]`


## Usage Example

See `usage_example.py` as an example:
```
$ python3 usage_example.py example.coverage
```
Note: normally it is just `.coverage` but this file is used for testing 
and as long as it ends with `.coverge` the path is fine

Obviously you want to use this as library, not as script.