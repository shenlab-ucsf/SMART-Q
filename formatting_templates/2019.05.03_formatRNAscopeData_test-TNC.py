import argparse
import os
from typing import Mapping, Tuple, Union

import numpy as np
from skimage.io import imread
from slicedimage import ImageFormat

from starfish import Codebook
from starfish.experiment.builder import FetchedTile, TileFetcher, write_experiment_json
from starfish.types import Axes, Coordinates, Number
from starfish.util.argparse import FsExistsType

class RNAScopeTile(FetchedTile):
    def __init__(self, file_path):
        self.file_path = file_path

    @property
    def shape(self) -> Tuple[int, ...]:
        return 1024, 1024

    ##### FIX THIS by referring to format_osmfish.py; you'll have to get it from the metadata somehow
    @property
    def coordinates(self) -> Mapping[Union[str, Coordinates], Union[Number, Tuple[Number, Number]]]:
        # FIXME: (dganguli) please provide proper coordinates here.
        return {
            Coordinates.X: (0.0, 0.0001),
            Coordinates.Y: (0.0, 0.0001),
            Coordinates.Z: (0.0, 0.0001),
        }

    '''@staticmethod
    def crop(img):
        crp = img[40:1084, 20:1410]
        return crp

    def tile_data(self) -> np.ndarray:
        return self.crop(imread(self.file_path))
    '''

    def tile_data(self) -> np.ndarray:
        return imread(self.file_path)

class RNAScopePrimaryTileFetcher(TileFetcher):
    def __init__(self, input_dir, root_dir_name, nameBeforeDot, fileType, seriesName, num_zplanes):
        self.input_dir = input_dir
        self.num_zplanes = num_zplanes
        self.root_dir_name = root_dir_name
        self.nameBeforeDot = nameBeforeDot
        self.fileType = fileType
        self.seriesName = seriesName

    @property
    def ch_dict(self):
        #ch_dict = {0: 'DAPI', 1: 'mCherry', 2: 'GFP', 3: 'Cy5'}
        ch_names = ['0', '1', '2', '3']
        ch_dict = dict(enumerate(ch_names))
        return ch_dict

    @property
    def zplane_dict(self):
        zplane_str = []
        for i in range(1,self.num_zplanes+1):
            zplane_str.append(str(i))
        zplane_dict = dict(enumerate(zplane_str))
        return zplane_dict

    def get_tile(self, fov: int, r: int, ch: int, z: int) -> FetchedTile:
        filename = '{}.{} - {} - C=1--{}.tif'.format(self.nameBeforeDot, self.fileType, self.seriesName, self.zplane_dict[z])
        file_path = os.path.join(self.input_dir, filename)
        return RNAScopeTile(file_path)

class RNAScopeAuxTileFetcher:
    """
    This is the contract for providing the image data for constructing a
    :class:`slicedimage.Collection`.
    """
    def __init__(self, input_dir, aux_type, root_dir_name, nameBeforeDot, fileType, seriesName, num_zplanes):
        self.input_dir = input_dir
        self.aux_type = aux_type
        ####### Add this to the parameters that you have to give in the beginning
        self.num_zplanes = num_zplanes
        self.root_dir_name = root_dir_name
        self.nameBeforeDot = nameBeforeDot
        self.fileType = fileType
        self.seriesName = seriesName

    @property
    def zplane_dict(self):
        zplane_str = []
        for i in range(1,self.num_zplanes+1):
            zplane_str.append(str(i))
        zplane_dict = dict(enumerate(zplane_str))
        return zplane_dict

    def get_tile(self, fov: int, r: int, ch: int, z: int) -> FetchedTile:
        if self.aux_type == 'nuclei':
            filename = '{}.{} - {} - C=0--{}.tif'.format(self.nameBeforeDot, self.fileType, self.seriesName, self.zplane_dict[z])
        elif self.aux_type == 'channel2':
            filename = '{}.{} - {} - C=2--{}.tif'.format(self.nameBeforeDot, self.fileType, self.seriesName, self.zplane_dict[z])
        elif self.aux_type == 'channel4':
            filename = '{}.{} - {} - C=4--{}.tif'.format(self.nameBeforeDot, self.fileType, self.seriesName, self.zplane_dict[z])
        elif self.aux_type == 'dots':
            filename = '{}.{} - {} - C=3--{}.tif'.format(self.nameBeforeDot, self.fileType, self.seriesName, self.zplane_dict[z])
        else:
            msg = 'invalid aux type: {}'.format(self.aux_type)
            msg += ' expected either nuclei or dots'
            raise ValueError(msg)

        file_path = os.path.join(self.input_dir, filename)

        return RNAScopeTile(file_path)

        """
        Given fov, r, ch, and z, return an instance of a :class:`.FetchedImage` that can be
        queried for the image data.
        """

def format_data(input_dir, output_dir, root_dir_name, nameBeforeDot, fileType, seriesName, num_zplanes):
    def add_codebook(experiment_json_doc):
        experiment_json_doc['codebook'] = "codebook.json"
        return experiment_json_doc

    primary_image_dimensions = {
        Axes.ROUND: 1,
        Axes.CH: 1,
        Axes.ZPLANE: num_zplanes,
    }

    aux_name_to_dimensions = {
        'nuclei': {
            Axes.ROUND: 1,
            Axes.CH: 1,
            Axes.ZPLANE: num_zplanes,
        },
        'channel2': {
            Axes.ROUND: 1,
            Axes.CH: 1,
            Axes.ZPLANE: num_zplanes,
        },
        'channel4': {
            Axes.ROUND: 1,
            Axes.CH: 1,
            Axes.ZPLANE: num_zplanes,
        },
        'dots': {
            Axes.ROUND: 1,
            Axes.CH: 1,
            Axes.ZPLANE: num_zplanes,
        }
    }

    write_experiment_json(
        path=output_dir,
        fov_count=1,
        tile_format=ImageFormat.TIFF,
        primary_image_dimensions=primary_image_dimensions,
        aux_name_to_dimensions=aux_name_to_dimensions,
        primary_tile_fetcher=RNAScopePrimaryTileFetcher(input_dir, root_dir_name, nameBeforeDot, fileType, seriesName, num_zplanes),
        aux_tile_fetcher={
            'nuclei': RNAScopeAuxTileFetcher(input_dir, 'nuclei', root_dir_name, nameBeforeDot, fileType, seriesName, num_zplanes),
            'channel2': RNAScopeAuxTileFetcher(input_dir, 'channel2', root_dir_name, nameBeforeDot, fileType, seriesName, num_zplanes),
            'channel4': RNAScopeAuxTileFetcher(input_dir, 'channel4', root_dir_name, nameBeforeDot, fileType, seriesName, num_zplanes),
            'dots': RNAScopeAuxTileFetcher(input_dir, 'dots', root_dir_name, nameBeforeDot, fileType, seriesName, num_zplanes),
        },
        postprocess_func=add_codebook,
        default_shape=(1024, 1024)
    )

    # mappings_array = [
    #     {
    #         "codeword": [
    #             {"r": 0, "c": 0, "v": 1},
    #         ],
    #         "target": "GFP"
    #     },
    # ]

    # codebook = {
    #     "version": "0.0.0",
    #     "mappings": mappings_array
    # }

    # codebook = Codebook.from_code_array(codebook)
    # codebook_json_filename = "codebook.json"
    # codebook.to_json(os.path.join(output_dir, codebook_json_filename))

    # At some point, somebody might need to make a more copmlex codebook (with all the target genes, called Features.TARGET here, 
    #   and what round and channel they're in). When that time comes, model your codebook according to below, 
    #   based on what ROUND and CH (channel) your target gene was imaged in
    """
    codebook_array = [
        {
            Features.CODEWORD: [
                {Axes.ROUND.value: 0, Axes.CH.value: 3, Features.CODE_VALUE: 1},
                {Axes.ROUND.value: 1, Axes.CH.value: 3, Features.CODE_VALUE: 1},
                {Axes.ROUND.value: 2, Axes.CH.value: 1, Features.CODE_VALUE: 1},
                {Axes.ROUND.value: 3, Axes.CH.value: 2, Features.CODE_VALUE: 1}
            ],
            Features.TARGET: "ACTB_human"
        },
        {
            Features.CODEWORD: [
                {Axes.ROUND.value: 0, Axes.CH.value: 3, Features.CODE_VALUE: 1},
                {Axes.ROUND.value: 1, Axes.CH.value: 1, Features.CODE_VALUE: 1},
                {Axes.ROUND.value: 2, Axes.CH.value: 1, Features.CODE_VALUE: 1},
                {Axes.ROUND.value: 3, Axes.CH.value: 2, Features.CODE_VALUE: 1}
            ],
            Features.TARGET: "ACTB_mouse"
        },
    ]
    codebook = Codebook.from_code_array(codebook_array)
    codebook_json_filename = "codebook.json"
    codebook.to_json(os.path.join(output_dir, codebook_json_filename))
    """

if __name__ == "__main__":
    input_help_msg = "Path to raw data"
    output_help_msg = "Path to output experment.json and all formatted images it references"
    zplanes_help_msg = "The number of stacks (on the Z plane) in your TIF images"
    root_dir_help_msg = "The name of the root dir that is also in the names of your TIF files"
    nameBeforeDot_help_msg = "The name on the file before the first . in the filename"
    fileType_help_msg = "The file type that the images were processed from"
    seriesName_help_msg = "The name of that series in the filename in between the dashes"
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=FsExistsType(), help=input_help_msg)
    parser.add_argument("output_dir", type=FsExistsType(), help=output_help_msg)
    parser.add_argument("root_dir_name", type=str, help=root_dir_help_msg)
    parser.add_argument("nameBeforeDot", type=str, help=nameBeforeDot_help_msg)
    parser.add_argument("fileType", type=str, help=fileType_help_msg)
    parser.add_argument("seriesName", type=str, help=seriesName_help_msg)
    parser.add_argument("num_zplanes", type=int, help=zplanes_help_msg)

    args = parser.parse_args()
    format_data(args.input_dir, args.output_dir, args.root_dir_name, args.nameBeforeDot, args.fileType, args.seriesName, args.num_zplanes)
