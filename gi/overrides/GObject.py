# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# Copyright (C) 2012 Canonical Ltd.
# Author: Martin Pitt <martin.pitt@ubuntu.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA

import gi.overrides
from gi.repository import GLib

__all__ = []

# API aliases for backwards compatibility
for name in ['markup_escape_text', 'get_application_name',
             'set_application_name', 'get_prgname', 'set_prgname',
             'main_depth', 'filename_display_basename',
             'filename_display_name', 'filename_from_utf8',
             'uri_list_extract_uris',
             'MainLoop', 'MainContext', 'main_context_default',
             'source_remove', 'Source', 'Idle', 'Timeout', 'PollFD',
             'idle_add', 'timeout_add', 'timeout_add_seconds',
             'io_add_watch', 'child_watch_add', 'get_current_time']:
    globals()[name] = gi.overrides.deprecated(getattr(GLib, name), 'GLib.' + name)
    __all__.append(name)

# constants are also deprecated, but cannot mark them as such
for name in ['PRIORITY_DEFAULT', 'PRIORITY_DEFAULT_IDLE', 'PRIORITY_HIGH',
             'PRIORITY_HIGH_IDLE', 'PRIORITY_LOW',
             'IO_IN', 'IO_OUT', 'IO_PRI', 'IO_ERR', 'IO_HUP', 'IO_NVAL',
             'IO_STATUS_ERROR', 'IO_STATUS_NORMAL', 'IO_STATUS_EOF',
             'IO_STATUS_AGAIN', 'IO_FLAG_APPEND', 'IO_FLAG_NONBLOCK',
             'IO_FLAG_IS_READABLE', 'IO_FLAG_IS_WRITEABLE',
             'IO_FLAG_IS_SEEKABLE', 'IO_FLAG_MASK', 'IO_FLAG_GET_MASK',
             'IO_FLAG_SET_MASK',
             'SPAWN_LEAVE_DESCRIPTORS_OPEN', 'SPAWN_DO_NOT_REAP_CHILD',
             'SPAWN_SEARCH_PATH', 'SPAWN_STDOUT_TO_DEV_NULL',
             'SPAWN_STDERR_TO_DEV_NULL', 'SPAWN_CHILD_INHERITS_STDIN',
             'SPAWN_FILE_AND_ARGV_ZERO',
             'glib_version']:
    globals()[name] = getattr(GLib, name)
    __all__.append(name)


G_MININT8 = GLib.MININT8
G_MAXINT8 = GLib.MAXINT8
G_MAXUINT8 = GLib.MAXUINT8
G_MININT16 = GLib.MININT16
G_MAXINT16 = GLib.MAXINT16
G_MAXUINT16 = GLib.MAXUINT16
G_MININT32 = GLib.MININT32
G_MAXINT32 = GLib.MAXINT32
G_MAXUINT32 = GLib.MAXUINT32
G_MININT64 = GLib.MININT64
G_MAXINT64 = GLib.MAXINT64
G_MAXUINT64 = GLib.MAXUINT64
__all__ += ['G_MININT8', 'G_MAXINT8', 'G_MAXUINT8', 'G_MININT16',
            'G_MAXINT16', 'G_MAXUINT16', 'G_MININT32', 'G_MAXINT32',
            'G_MAXUINT32', 'G_MININT64', 'G_MAXINT64', 'G_MAXUINT64']