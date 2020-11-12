

import pytest

from cleancode import dataclass3 



class PersonTest:
    
    @pytest.mark.customdataclass
    def test_dataclass(self):
        d = dataclass3.Person()
        assert isinstance(d, object) == True

    @pytest.mark.classfunctioncall
    def test_class_call(self):
        d = dataclass3.Person(name='samman', age=22)
        assert d.__post_init__() == True

    def test_input_value(self):
        d = dataclass3.Person(name= 'johncena', age= 21)
        assert hasattr(d, 'height') == True

    