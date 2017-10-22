# PrinterScalePlugin
A plugin that automatically scales models on loading, allowing X, Y, and Z axis scaling for printers that can't adjust those in firmware.

## Installation
For Cura 2.x, put the PrinterScalePlugin into your Cura user plugins folder:
    Windows: %AppData%/cura/plugins
    Mac: ~/Library/Application Support/cura/plugins
    Linux: ~/.cura/plugins

For Cura 3.x, install PrinterScalePlugin.curaplugin through the
Plugins->Installed Plugins menu.

## Configuration
Defaults to scaling the X and Y axes up by 2.5%.  Edit PrinterScalePlugin.py
to adjust this.

At some point the future I'll make a configuration menu for this, maybe...
