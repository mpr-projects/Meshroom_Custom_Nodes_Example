import os
import json
from meshroom.core import desc


def swap_yz(d):
    i, j = 1, 2
    for e in ['pose', 'forward', 'up']:
        d[e][i], d[e][j] = d[e][j], d[e][i]
    return d

def flip_y(d):
    i = 1
    for e in ['pose', 'forward', 'up']:
        d[e][i] *= -1
    return d



class LocalKnownPosesData(desc.Node):

    category = 'mpr'
    documentation = """
    Converts local camera_poses.json file to Meshroom's format and provides a
    link to the file as output (to use in the ImportKnownPoses node).
    """

    inputs = [
        desc.File(
            name="sfmData",
            label="SfMData",
            description="Input SfMData file.",
            value="",
            uid=[0],
        ),
        desc.StringParam(
            name="rel_path",
            label="Relative Path",
            description="Enter the path where the file camera_poses.json is saved, relative to the location of the .mg file.",
            value='.',
            uid=[0],
        )
    ]

    outputs = [
        desc.File(
            name="knownPosesData",
            label="Known Poses Data",
            description="Known poses data in JSON format.",
            value=desc.Node.internalFolder + "knownPoses.json",
            uid=[],
        )
    ]

    def processChunk(self, chunk):
        attr = chunk.node.attribute
        mg_file = chunk.node.graph._filepath

        output_file = attr('knownPosesData').value
        sfmFile = attr('sfmData').value

        rel_path = attr('rel_path').value
        input_folder = os.path.join(os.path.dirname(mg_file), rel_path)

        # read filenames of photos
        with open(sfmFile, 'r') as f:
            sfmData = json.load(f)

        mapping = dict()

        for view in sfmData['views']:
            filename = os.path.basename(view['path'])
            mapping[filename] = None

        # map filenames of photos
        fnames = os.listdir(input_folder)
        input_files = [os.path.join(input_folder, fname)
                       for fname in fnames
                       if fname[-17:] == 'camera_poses.json']

        for input_file in input_files:
            with open(input_file, 'r') as f:
                for line in f.readlines():
                    line = json.loads(line)
                    fname = line['filename']

                    if fname not in mapping:
                        continue

                    line = swap_yz(line)
                    line = flip_y(line)
                    mapping[fname] = line
                    # output.append(line)

        output = [mapping[k] for k in sorted(mapping.keys())]

        with open(output_file, 'w') as f:
            for line in output:
                json.dump(line, f)

                if line is not output[-1]:
                    f.write('\n')
