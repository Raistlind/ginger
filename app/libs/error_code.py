#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   error_code.py   
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time          @Author      @Version    @Description
-----------------     ---------    --------    -----------
2019-05-24 21:30      RaistlinD    1.0         None
"""

# import lib

from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006
