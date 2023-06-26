# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spec.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='spec.proto',
    package='cabe.proto',
    syntax='proto3',
    serialized_pb=_b(
        '\n\nspec.proto\x12\ncabe.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa9\x01\n\tBuildSpec\x12\x31\n\x0egitiles_commit\x18\x01 \x01(\x0b\x32\x19.cabe.proto.GitilesCommit\x12\x30\n\x0egerrit_changes\x18\x02 \x03(\x0b\x32\x18.cabe.proto.GerritChange\x12\x37\n\x11installed_browser\x18\x03 \x01(\x0b\x32\x1c.cabe.proto.InstalledBrowser\"f\n\x0cGerritChange\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x0e\n\x06\x63hange\x18\x03 \x01(\x03\x12\x10\n\x08patchset\x18\x04 \x01(\x03\x12\x15\n\rpatchset_hash\x18\x05 \x01(\t\"Y\n\rGitilesCommit\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0b\n\x03ref\x18\x04 \x01(\t\x12\x10\n\x08position\x18\x05 \x01(\r\"1\n\x10InstalledBrowser\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"m\n\x0b\x46inchConfig\x12\x11\n\tseed_hash\x18\x01 \x01(\t\x12\x17\n\x0fseed_changelist\x18\x02 \x01(\x04\x12\x32\n\x0eseed_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"d\n\x07RunSpec\x12\n\n\x02os\x18\x01 \x01(\t\x12\x1e\n\x16synthetic_product_name\x18\x02 \x01(\t\x12-\n\x0c\x66inch_config\x18\x03 \x01(\x0b\x32\x17.cabe.proto.FinchConfig\"8\n\x0c\x41nalysisSpec\x12(\n\tbenchmark\x18\x01 \x03(\x0b\x32\x15.cabe.proto.Benchmark\"+\n\tBenchmark\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08workload\x18\x02 \x03(\t\"[\n\x07\x41rmSpec\x12)\n\nbuild_spec\x18\x01 \x03(\x0b\x32\x15.cabe.proto.BuildSpec\x12%\n\x08run_spec\x18\x02 \x03(\x0b\x32\x13.cabe.proto.RunSpec\"\xaf\x01\n\x0e\x45xperimentSpec\x12#\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x13.cabe.proto.ArmSpec\x12$\n\x07\x63ontrol\x18\x02 \x01(\x0b\x32\x13.cabe.proto.ArmSpec\x12&\n\ttreatment\x18\x03 \x01(\x0b\x32\x13.cabe.proto.ArmSpec\x12*\n\x08\x61nalysis\x18\x04 \x01(\x0b\x32\x18.cabe.proto.AnalysisSpecB!Z\x1fgo.skia.org/infra/cabe/go/protob\x06proto3'
    ),
    dependencies=[
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ])

_BUILDSPEC = _descriptor.Descriptor(
    name='BuildSpec',
    full_name='cabe.proto.BuildSpec',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='gitiles_commit',
            full_name='cabe.proto.BuildSpec.gitiles_commit',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='gerrit_changes',
            full_name='cabe.proto.BuildSpec.gerrit_changes',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='installed_browser',
            full_name='cabe.proto.BuildSpec.installed_browser',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=60,
    serialized_end=229,
)

_GERRITCHANGE = _descriptor.Descriptor(
    name='GerritChange',
    full_name='cabe.proto.GerritChange',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='host',
            full_name='cabe.proto.GerritChange.host',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='project',
            full_name='cabe.proto.GerritChange.project',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='change',
            full_name='cabe.proto.GerritChange.change',
            index=2,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='patchset',
            full_name='cabe.proto.GerritChange.patchset',
            index=3,
            number=4,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='patchset_hash',
            full_name='cabe.proto.GerritChange.patchset_hash',
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=231,
    serialized_end=333,
)

_GITILESCOMMIT = _descriptor.Descriptor(
    name='GitilesCommit',
    full_name='cabe.proto.GitilesCommit',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='host',
            full_name='cabe.proto.GitilesCommit.host',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='project',
            full_name='cabe.proto.GitilesCommit.project',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='id',
            full_name='cabe.proto.GitilesCommit.id',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='ref',
            full_name='cabe.proto.GitilesCommit.ref',
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='position',
            full_name='cabe.proto.GitilesCommit.position',
            index=4,
            number=5,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=335,
    serialized_end=424,
)

_INSTALLEDBROWSER = _descriptor.Descriptor(
    name='InstalledBrowser',
    full_name='cabe.proto.InstalledBrowser',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='cabe.proto.InstalledBrowser.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='version',
            full_name='cabe.proto.InstalledBrowser.version',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=426,
    serialized_end=475,
)

_FINCHCONFIG = _descriptor.Descriptor(
    name='FinchConfig',
    full_name='cabe.proto.FinchConfig',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='seed_hash',
            full_name='cabe.proto.FinchConfig.seed_hash',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='seed_changelist',
            full_name='cabe.proto.FinchConfig.seed_changelist',
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='seed_timestamp',
            full_name='cabe.proto.FinchConfig.seed_timestamp',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=477,
    serialized_end=586,
)

_RUNSPEC = _descriptor.Descriptor(
    name='RunSpec',
    full_name='cabe.proto.RunSpec',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='os',
            full_name='cabe.proto.RunSpec.os',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='synthetic_product_name',
            full_name='cabe.proto.RunSpec.synthetic_product_name',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='finch_config',
            full_name='cabe.proto.RunSpec.finch_config',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=588,
    serialized_end=688,
)

_ANALYSISSPEC = _descriptor.Descriptor(
    name='AnalysisSpec',
    full_name='cabe.proto.AnalysisSpec',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='benchmark',
            full_name='cabe.proto.AnalysisSpec.benchmark',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=690,
    serialized_end=746,
)

_BENCHMARK = _descriptor.Descriptor(
    name='Benchmark',
    full_name='cabe.proto.Benchmark',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='cabe.proto.Benchmark.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='workload',
            full_name='cabe.proto.Benchmark.workload',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=748,
    serialized_end=791,
)

_ARMSPEC = _descriptor.Descriptor(
    name='ArmSpec',
    full_name='cabe.proto.ArmSpec',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='build_spec',
            full_name='cabe.proto.ArmSpec.build_spec',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='run_spec',
            full_name='cabe.proto.ArmSpec.run_spec',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=793,
    serialized_end=884,
)

_EXPERIMENTSPEC = _descriptor.Descriptor(
    name='ExperimentSpec',
    full_name='cabe.proto.ExperimentSpec',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='common',
            full_name='cabe.proto.ExperimentSpec.common',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='control',
            full_name='cabe.proto.ExperimentSpec.control',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='treatment',
            full_name='cabe.proto.ExperimentSpec.treatment',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='analysis',
            full_name='cabe.proto.ExperimentSpec.analysis',
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=887,
    serialized_end=1062,
)

_BUILDSPEC.fields_by_name['gitiles_commit'].message_type = _GITILESCOMMIT
_BUILDSPEC.fields_by_name['gerrit_changes'].message_type = _GERRITCHANGE
_BUILDSPEC.fields_by_name['installed_browser'].message_type = _INSTALLEDBROWSER
_FINCHCONFIG.fields_by_name[
    'seed_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RUNSPEC.fields_by_name['finch_config'].message_type = _FINCHCONFIG
_ANALYSISSPEC.fields_by_name['benchmark'].message_type = _BENCHMARK
_ARMSPEC.fields_by_name['build_spec'].message_type = _BUILDSPEC
_ARMSPEC.fields_by_name['run_spec'].message_type = _RUNSPEC
_EXPERIMENTSPEC.fields_by_name['common'].message_type = _ARMSPEC
_EXPERIMENTSPEC.fields_by_name['control'].message_type = _ARMSPEC
_EXPERIMENTSPEC.fields_by_name['treatment'].message_type = _ARMSPEC
_EXPERIMENTSPEC.fields_by_name['analysis'].message_type = _ANALYSISSPEC
DESCRIPTOR.message_types_by_name['BuildSpec'] = _BUILDSPEC
DESCRIPTOR.message_types_by_name['GerritChange'] = _GERRITCHANGE
DESCRIPTOR.message_types_by_name['GitilesCommit'] = _GITILESCOMMIT
DESCRIPTOR.message_types_by_name['InstalledBrowser'] = _INSTALLEDBROWSER
DESCRIPTOR.message_types_by_name['FinchConfig'] = _FINCHCONFIG
DESCRIPTOR.message_types_by_name['RunSpec'] = _RUNSPEC
DESCRIPTOR.message_types_by_name['AnalysisSpec'] = _ANALYSISSPEC
DESCRIPTOR.message_types_by_name['Benchmark'] = _BENCHMARK
DESCRIPTOR.message_types_by_name['ArmSpec'] = _ARMSPEC
DESCRIPTOR.message_types_by_name['ExperimentSpec'] = _EXPERIMENTSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildSpec = _reflection.GeneratedProtocolMessageType(
    'BuildSpec',
    (_message.Message,),
    dict(
        DESCRIPTOR=_BUILDSPEC,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.BuildSpec)
    ))
_sym_db.RegisterMessage(BuildSpec)

GerritChange = _reflection.GeneratedProtocolMessageType(
    'GerritChange',
    (_message.Message,),
    dict(
        DESCRIPTOR=_GERRITCHANGE,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.GerritChange)
    ))
_sym_db.RegisterMessage(GerritChange)

GitilesCommit = _reflection.GeneratedProtocolMessageType(
    'GitilesCommit',
    (_message.Message,),
    dict(
        DESCRIPTOR=_GITILESCOMMIT,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.GitilesCommit)
    ))
_sym_db.RegisterMessage(GitilesCommit)

InstalledBrowser = _reflection.GeneratedProtocolMessageType(
    'InstalledBrowser',
    (_message.Message,),
    dict(
        DESCRIPTOR=_INSTALLEDBROWSER,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.InstalledBrowser)
    ))
_sym_db.RegisterMessage(InstalledBrowser)

FinchConfig = _reflection.GeneratedProtocolMessageType(
    'FinchConfig',
    (_message.Message,),
    dict(
        DESCRIPTOR=_FINCHCONFIG,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.FinchConfig)
    ))
_sym_db.RegisterMessage(FinchConfig)

RunSpec = _reflection.GeneratedProtocolMessageType(
    'RunSpec',
    (_message.Message,),
    dict(
        DESCRIPTOR=_RUNSPEC,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.RunSpec)
    ))
_sym_db.RegisterMessage(RunSpec)

AnalysisSpec = _reflection.GeneratedProtocolMessageType(
    'AnalysisSpec',
    (_message.Message,),
    dict(
        DESCRIPTOR=_ANALYSISSPEC,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.AnalysisSpec)
    ))
_sym_db.RegisterMessage(AnalysisSpec)

Benchmark = _reflection.GeneratedProtocolMessageType(
    'Benchmark',
    (_message.Message,),
    dict(
        DESCRIPTOR=_BENCHMARK,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.Benchmark)
    ))
_sym_db.RegisterMessage(Benchmark)

ArmSpec = _reflection.GeneratedProtocolMessageType(
    'ArmSpec',
    (_message.Message,),
    dict(
        DESCRIPTOR=_ARMSPEC,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.ArmSpec)
    ))
_sym_db.RegisterMessage(ArmSpec)

ExperimentSpec = _reflection.GeneratedProtocolMessageType(
    'ExperimentSpec',
    (_message.Message,),
    dict(
        DESCRIPTOR=_EXPERIMENTSPEC,
        __module__='spec_pb2'
        # @@protoc_insertion_point(class_scope:cabe.proto.ExperimentSpec)
    ))
_sym_db.RegisterMessage(ExperimentSpec)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(), _b('Z\037go.skia.org/infra/cabe/go/proto'))
# @@protoc_insertion_point(module_scope)