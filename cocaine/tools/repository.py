#
# Copyright (c) 2013+ Evgeny Safronov <division494@gmail.com>
# Copyright (c) 2011-2014 Other contributors as noted in the AUTHORS file.
#
# This file is part of Cocaine-tools.
#
# Cocaine is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Cocaine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import subprocess
import os

__author__ = 'EvgenySafronov <division494@gmail.com>'


class RepositoryDownloadError(Exception):
    pass


class RepositoryDownloader(object):
    def download(self, url, destination):  # pragma: no cover
        raise NotImplementedError


class GitRepositoryDownloader(RepositoryDownloader):
    def __init__(self, stream=None):
        self.stream = stream or open(os.devnull, 'w')

    def download(self, url, destination):
        process = subprocess.Popen(['git', 'clone', url, destination],
                                   stdout=self.stream,
                                   stderr=self.stream)
        process.wait()
        if process.returncode != 0:
            raise RepositoryDownloadError('Cannot download repository from "{0}"'.format(url))
