#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   enums.py   
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time          @Author      @Version    @Description
-----------------     ---------    --------    -----------
2019-04-15 21:50      RaistlinD    1.0         None
"""

# import lib
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    USER_MINA = 200
    USER_WX = 201
