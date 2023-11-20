from horoscope.converters import UpperConvertor


my_converter = UpperConvertor()
assert my_converter.to_python('python') == 'PYTHON'
assert my_converter.to_url('PYTHON') == 'python'