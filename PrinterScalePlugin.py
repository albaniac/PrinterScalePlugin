from UM.Extension import Extension
from UM.Scene.Selection import Selection
from UM.Math.Vector import Vector

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("PrinterScalePlugin")


class PrinterScalePlugin(Extension):
    def __init__(self):
        super().__init__()
        self.addMenuItem(i18n_catalog.i18n("Scale for Printer"), self.scale)

    ##  Scales by specified ratio
    def scale(self):
        selected_nodes = Selection.getAllSelectedObjects()
        for node in selected_nodes:
            node.scale(Vector(1.025, 1.0, 1.025))
