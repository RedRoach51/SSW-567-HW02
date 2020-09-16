# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # "I added in a print line to each test so I could see what was actually being printed."

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(3,5,1),'Scalene','3,5,1 should be scalene')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(3,2,2),'Isoceles','3,2,2 should be Isoceles');

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 should be Isoceles');

    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be Isoceles');

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

