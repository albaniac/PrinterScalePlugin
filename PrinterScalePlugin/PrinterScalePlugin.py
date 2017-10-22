from UM.Extension import Extension
from UM.Scene.Selection import Selection
from UM.Math.Vector import Vector
from UM.Application import Application
from UM.Scene.Iterator.BreadthFirstIterator import BreadthFirstIterator
from UM.Logger import Logger

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("PrinterScalePlugin")

class PrinterScalePlugin(Extension):
    def __init__(self):
        super().__init__()

        self._scene_objects = set()
        self._scene = Application.getInstance().getController().getScene()
        self._scene.sceneChanged.connect(self.onSceneChanged)

    def onSceneChanged(self, node):
        root = Application.getInstance().getController().getScene().getRoot()
        new_scene_objects = set(node for node in BreadthFirstIterator(root) if node.callDecoration("isSliceable"))
        if new_scene_objects != self._scene_objects:
            to_scale = new_scene_objects - self._scene_objects
            self._scene_objects = new_scene_objects

            for node in to_scale:
                # Scale up by 2.5% on X and Y.  Modify as needed.
                node.scale(Vector(1.025, 1.0, 1.025))
