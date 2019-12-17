# 17-dec-2019

### 1 - barcode in python

https://pypi.org/project/python-barcode/

```python
>>> import barcode
>>> barcode.PROVIDED_BARCODES
['code39', 'code128', 'ean', 'ean13', 'ean8', 'gs1', 'gtin',
 'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca']
>>> EAN = barcode.get_barcode_class('ean13')
>>> EAN
<class 'barcode.ean.EuropeanArticleNumber13'>
>>> ean = EAN('5901234123457')
>>> ean
<barcode.ean.EuropeanArticleNumber13 object at 0x00BE98F0>
>>> fullname = ean.save('ean13_barcode')
>>> fullname
'ean13_barcode.svg'
```
