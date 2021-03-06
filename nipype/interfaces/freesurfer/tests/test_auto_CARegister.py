# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import CARegister


def test_CARegister_inputs():
    input_map = dict(A=dict(argstr='-A %d',
    ),
    align=dict(argstr='-align-%s',
    mandatory=False,
    ),
    args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-3,
    ),
    invert_and_save=dict(argstr='-invert-and-save',
    mandatory=False,
    position=-4,
    ),
    l_files=dict(argstr='-l %s',
    ),
    levels=dict(argstr='-levels %d',
    ),
    mask=dict(argstr='-mask %s',
    mandatory=False,
    ),
    no_big_ventricles=dict(argstr='-nobigventricles',
    mandatory=False,
    ),
    num_threads=dict(),
    out_file=dict(argstr='%s',
    genfile=True,
    mandatory=False,
    position=-1,
    ),
    subjects_dir=dict(),
    template=dict(argstr='%s',
    mandatory=False,
    position=-2,
    ),
    terminal_output=dict(nohash=True,
    ),
    transform=dict(argstr='-T %s',
    mandatory=False,
    ),
    )
    inputs = CARegister.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_CARegister_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = CARegister.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
