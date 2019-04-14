#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   user.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Description
-----------------    ---------    --------    -----------
2019-04-07 21:33      RaistlinD    1.0         None
"""

# import lib

from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'RaistlinD'
