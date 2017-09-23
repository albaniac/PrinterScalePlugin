# Copyright (c) 2017 Nirav Patel
# The PrinterScalePlugin is released under the terms of the AGPLv3 or higher.

from . import PrinterScalePlugin
from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("PrinterScalePlugin")


def getMetaData():
    return {}


def register(app):
    return {"extension": PrinterScalePlugin.PrinterScalePlugin()}
