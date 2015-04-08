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
#  

import pyjsonrpc
import sys, time, datetime

# importing special library for Galielo Project
galileo_path = "/opt/";
if galileo_path not in sys.path:
    sys.path.append(galileo_path);
from coderdojo_library import *
####


class RequestHandler(pyjsonrpc.HttpRequestHandler):

  @pyjsonrpc.rpcmethod
  def getTemperature(self):
      """getting temperature"""
      GalileoBoard = CoderDojoGalileo()
      temp = GalileoBoard.getTemperature()
      return temp


# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = ('localhost', 8080),
    RequestHandlerClass = RequestHandler
)
print "Starting HTTP server ..."
print "URL: http://localhost:8080"
http_server.serve_forever()
