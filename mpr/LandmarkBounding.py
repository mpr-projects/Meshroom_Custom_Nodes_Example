__version__ = "2.0"

import sys

from meshroom.core import desc
from meshroom.core.utils import VERBOSE_LEVEL

import os.path


class LandmarkBounding(desc.AVCommandLineNode):
    commandLine = 'aliceVision_landmarkBounding {allParams}'
    size = desc.DynamicNodeSize('input')

    category = 'mpr'
    documentation = '''
This node removes all landmarks that are not within the bounding box described by corners
(xmin, ymin, zmin) and (xmax, ymax, zmax).
'''

    inputs = [
        desc.File(
            name="input",
            label="Input",
            description="Input SfMData file .",
            value="",
            uid=[0],
        ),
        desc.BoolParam(
            name="useXmin",
            label="Set Minimum x-value",
            description="Set x-value below which all landmarks will be removed.",
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name="xmin",
            label="  Minimum x-value [dm].",
            description="The x-coordinate of the lower corner of the bounding box.",
            value=0.0,
            range=(sys.float_info.min, sys.float_info.max, 0.001),
            enabled=lambda node: node.useXmin.value is True,
            uid=[0],
        ),
        desc.BoolParam(
            name="useXmax",
            label="Set Maximum x-value",
            description="Set x-value above which all landmarks will be removed.",
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name="xmax",
            label="  Maximum x-value [dm].",
            description="The x-coordinate of the second corner of the bounding box.",
            value=1.0,
            range=(sys.float_info.min, sys.float_info.max, 0.001),
            enabled=lambda node: node.useXmax.value is True,
            uid=[0],
        ),
        desc.BoolParam(
            name="useYmin",
            label="Set Minimum y-value",
            description="Set y-value below which all landmarks will be removed.",
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name="ymin",
            label="  Minimum y-value [dm].",
            description="The y-coordinate of the first corner of the bounding box.",
            value=0.0,
            range=(sys.float_info.min, sys.float_info.max, 0.001),
            enabled=lambda node: node.useYmin.value is True,
            uid=[0],
        ),
        desc.BoolParam(
            name="useYmax",
            label="Set Maximum y-value",
            description="Set y-value above which all landmarks will be removed.",
            value=True,
            uid=[0],
        ),
        desc.FloatParam(
            name="ymax",
            label="  Maximum y-value [dm].",
            description="The y-coordinate of the second corner of the bounding box.",
            value=-0.1,
            range=(sys.float_info.min, sys.float_info.max, 0.001),
            enabled=lambda node: node.useYmax.value is True,
            uid=[0],
        ),
        desc.BoolParam(
            name="useZmin",
            label="Set Minimum z-value",
            description="Set z-value below which all landmarks will be removed.",
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name="zmin",
            label="  Minimum z-value [dm].",
            description="The z-coordinate of the first corner of the bounding box.",
            value=0.0,
            range=(sys.float_info.min, sys.float_info.max, 0.001),
            enabled=lambda node: node.useZmin.value is True,
            uid=[0],
        ),
        desc.BoolParam(
            name="useZmax",
            label="Set Maximum z-value",
            description="Set z-value above which all landmarks will be removed.",
            value=False,
            uid=[0],
        ),
        desc.FloatParam(
            name="zmax",
            label="  Maximum z-value [dm].",
            description="The z-coordinate of the second corner of the bounding box.",
            value=1.0,
            range=(sys.float_info.min, sys.float_info.max, 0.001),
            enabled=lambda node: node.useZmax.value is True,
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name="output",
            label="SfMData File",
            description="Output SfMData file.",
            value=lambda attr: desc.Node.internalFolder + (os.path.splitext(os.path.basename(attr.node.input.value))[0] or "sfmData") + ".abc",
            uid=[],
        ),
    ]
