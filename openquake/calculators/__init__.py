# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2014-2016 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.

import os
from openquake.baselib.general import import_all, git_suffix

# version number follows the syntax <major>.<minor>.<patchlevel>[<suffix>]
# where major, minor and patchlevel are numbers.
# suffix follows the ubuntu versioning rules.
# for development version suffix is:
#  "-" + <pkg-version> + "+dev" + <secs_since_epoch> + "-" + <commit-id>
# NB: the next line is managed by packager.sh script (we retrieve the version
#     using sed and optionally replace it)
__version__ = '2.0.0'
__version__ += git_suffix(__file__)

# make sure the `base,calculators` dictionary is populated
import_all('openquake.calculators')

# import the development packages if any
extras = os.environ.get('OQLITEIMPORT', '')
for extra_pkg in extras.split(':'):
    if extra_pkg:
        import_all(extra_pkg)
