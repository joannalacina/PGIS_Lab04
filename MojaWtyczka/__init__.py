# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MojaWtyczka
                                 A QGIS plugin
 wtyczka
                             -------------------
        begin                : 2015-01-25
        copyright            : (C) 2015 by Asia
        email                : asialacina@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MojaWtyczka class from file MojaWtyczka.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .wtyczka import MojaWtyczka
    return MojaWtyczka(iface)
