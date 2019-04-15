#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Description
-----------------    ---------    --------    -----------
2019-04-07 21:32      RaistlinD    1.0         None
"""

# import lib
from flask import Blueprint
from app.api.v1 import user, book, client


def create_blueprint_v1():
    # from app.api.v1.book import api as user
    # from app.api.v1.user import api as book
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1
