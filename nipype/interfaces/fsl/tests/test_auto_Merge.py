# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.utils import Merge

def test_Merge_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    dimension=dict(argstr='-%s',
    mandatory=True,
    position=0,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_files=dict(argstr='%s',
    mandatory=True,
    position=2,
    ),
    merged_file=dict(argstr='%s',
    hash_files=False,
    name_source='in_files',
    name_template='%s_merged',
    position=1,
    ),
    output_type=dict(),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    tr=dict(argstr='%.2f',
    position=-1,
    ),
    )
    inputs = Merge.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Merge_outputs():
    output_map = dict(merged_file=dict(),
    )
    outputs = Merge.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
