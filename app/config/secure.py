#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   secure.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Description
-----------------    ---------    --------    -----------
2019-04-07 20:07      RaistlinD    1.0         None
"""

# import lib

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:8889/ginger'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

SECRET_KEY = 'adedfefdgrgdw'
