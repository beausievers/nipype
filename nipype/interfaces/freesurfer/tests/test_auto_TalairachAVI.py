# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..utils import TalairachAVI


def test_TalairachAVI_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    atlas=dict(argstr='--atlas %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='--i %s',
    mandatory=True,
    ),
    out_file=dict(argstr='--xfm %s',
    mandatory=True,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = TalairachAVI.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_TalairachAVI_outputs():
    output_map = dict(out_file=dict(),
    out_log=dict(),
    out_txt=dict(),
    )
    outputs = TalairachAVI.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
