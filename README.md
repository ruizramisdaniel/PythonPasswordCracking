# PythonPasswordCracking

Python script that cracks any MD5 hash against a given password wordlist. This tool was created to solve one of the NCL Password Cracking challenges.

## Installation

Use the package manager [pip](https://pypi.org/project/pip/) to install *Hashlib* and *Argparse* modules.

```bash
pip install hashlib argparse
```

## Usage

For basic usage:
```python
md5hashcracker.py -hashes hashes.txt -p passwordlist.txt
```
To obtain txt file with output:
```python
md5hashcracker.py -hashes hashes.txt -p passwordlist.txt -o
```
## Author
https://www.linkedin.com/in/danielruizramis/

## Note
Use this script only for Educational Purposes.