#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bez nazwy.py
#  
#  Copyright 2015 Uczeń - instalacyjny <uczen@uczen-G31M-ES2L>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import pyjsonrpc

http_client = pyjsonrpc.HttpClient(
    url = "http://localhost:8080",
    username = "Username",
    password = "Password"
)
print http_client.call("add", 1, 2)
# Result: 3

# It is also possible to use the *method* name as *attribute* name.
print http_client.add(1, 2)
# Result: 3

# Notifications send messages to the server, without response.
http_client.notify("add", 3, 4)
