# -*- coding: utf-8 -*-
#
#  Copyright 2017 Ramil Nugmanov <stsouko@live.ru>
#  This file is part of FNS.
#
#  FNS is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
from pony.orm import db_session
from .. import Loader


def add_core(**kwargs):
    Loader.load_schemas()
    seller = Loader.get_database(kwargs['database'])[0]
    fn, fd, fs = kwargs['fn'], kwargs['fd'], kwargs['fs']
    with db_session:
        try:
            print('Added. total sum:', seller.add_sale(fn, fd, fs))
        except Exception as e:
            print(e)
