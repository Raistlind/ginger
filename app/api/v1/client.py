#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   client.py   
@Contact :   Johnd0712@hotmail.com
@License :   (C)Copyright 2017-2018, Krynn.cn

@Modify Time          @Author      @Version    @Description
-----------------     ---------    --------    -----------
2019-04-15 21:46      RaistlinD    1.0         None
"""

# import lib
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error import APIException
from app.libs.error_code import ClientTypeError
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        }
        promise[form.type.data]()
    else:
        raise ClientTypeError()
    return 'success'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
