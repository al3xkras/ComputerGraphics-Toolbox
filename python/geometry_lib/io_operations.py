"""@package docstring
Documentation for this module.

More details.
"""
from parser import *

class TestOutputWriter:
    def __init__(self, filename, testdata):
        self.testdata=testdata
        self.filename=filename

    def run_intersection_test(self):
        _type='intersections'
        _tests=self.testdata[_type]
        test_results=[]
        for i in range(0,len(_tests)):
            _t=_tests[i]
            p=_t.intersection_point
            _t=_t.segment1,_t.segment2
            if len(_t)<2: break
            test_results.append([_t[0],_t[1],p,Intersection(*_t)])
        for x in test_results:
            for y in x:
                print(y)
            print()


if __name__ == '__main__':
    tests=test_cases()
    print(tests)
    t=TestOutputWriter("",tests)
    t.run_intersection_test()
