#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test.py   
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time          @Author      @Version    @Description
-----------------     ---------    --------    -----------
2019-04-23 19:55      RaistlinD    1.0         None
"""

# import lib
import re

if __name__ == '__main__':
    d = {'a': 'A', 'b': 'B'}

    str = "1 [2.2 3.3 4.4 5.5] 0.2 ".strip()

    # r = re.search('([\d*])\s\[([\.\d\s]*)\]\s([\d\.]*)', str)
    r = re.search('(\d+)\s\[([\d\.]*)\s([\d\.]*)\s([\d\.]*)\s([\d\.]*)\]\s([\d\.]*)', str)

    print(r.groups())
    print(str)
