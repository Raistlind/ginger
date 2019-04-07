#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   app.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Description
-----------------    ---------    --------    -----------
2019-04-06 23:39      RaistlinD    1.0         None
"""

# import lib
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    return app