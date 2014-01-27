# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.freesurfer.preprocess import UnpackSDICOMDir

def test_UnpackSDICOMDir_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    config=dict(argstr='-cfg %s',
    mandatory=True,
    xor=('run_info', 'config', 'seq_config'),
    ),
    dir_structure=dict(argstr='-%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    log_file=dict(argstr='-log %s',
    ),
    no_info_dump=dict(argstr='-noinfodump',
    ),
    no_unpack_err=dict(argstr='-no-unpackerr',
    ),
    output_dir=dict(argstr='-targ %s',
    ),
    run_info=dict(argstr='-run %d %s %s %s',
    mandatory=True,
    xor=('run_info', 'config', 'seq_config'),
    ),
    scan_only=dict(argstr='-scanonly %s',
    ),
    seq_config=dict(argstr='-seqcfg %s',
    mandatory=True,
    xor=('run_info', 'config', 'seq_config'),
    ),
    source_dir=dict(argstr='-src %s',
    mandatory=True,
    ),
    spm_zeropad=dict(argstr='-nspmzeropad %d',
    ),
    subjects_dir=dict(),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = UnpackSDICOMDir.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
