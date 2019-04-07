#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ginger.py    
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time         @Author      @Version    @Description
-----------------    ---------    --------    -----------
2019-04-06 23:38      RaistlinD    1.0         None
"""

# import lib
from app.app import create_app

app = create_app()


@app.route('/v1/user/get')
def get_user():
    return 'RaistlinD'


@app.route('/v1/book/get')
def get_book():
    return 'get book'


if __name__ == '__main__':
    app.run(debug=True)
