from horoscope.converters import SplitConvertor
my_converter = SplitConvertor()

assert my_converter.to_python('apple,banana,orange') == ['apple', 'banana', 'orange']
assert my_converter.to_url(['apple', 'banana', 'orange']) == 'apple,banana,orange'
