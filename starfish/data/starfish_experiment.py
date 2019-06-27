from starfish import Experiment
from starfish.util.argparse import FsExistsType

def RNAscope(input_json: FsExistsType()):
	return Experiment.from_json(input_json)

if __name__ == "__main__":
    ###### Change s3_bucket, 
    path_help_msg = "Path to experiment.json file for the field of view of interest."
    output_help_msg = "Path to output directory"
    #series_help_msg = "The two-digit number found in the file name directly after \"Series0\""
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=FsExistsType(), help=path_help_msg)
    parser.add_argument("output_dir", type=FsExistsType(), help=output_help_msg)

    args = parser.parse_args()
    experiment = RNAscope(args.input_json)
    # Ex: experiment = RNAscope("/Users/sbergenholtz/Applications/starfish/rnascope/formatted/experiment.json")
    
