#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: yangyangyang
"""

# Source: https://github.com/rahulbot/Programming-Style-Examples/blob/master/test-driven.py

import unittest
from HW2_Yang import media_cloud

class media_cloud_test(unittest.TestCase):
    
    def test_handle_request(self):
        self.response = media_cloud().handle_request(('Trump'),(2016,9,1),(2016,9,30))
        assert self.response['count']>0

if __name__ == '__main__':
    unittest.main()
