# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Clnt

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Group(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Group()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGroup(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Group
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Group
    def AvgAge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Group
    def AvgWeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Group
    def ParticipantNamelist(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Group
    def ParticipantNamelistLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Group
    def ParticipantNamelistIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def GroupStart(builder):
    builder.StartObject(3)

def Start(builder):
    GroupStart(builder)

def GroupAddAvgAge(builder, avgAge):
    builder.PrependFloat32Slot(0, avgAge, 0.0)

def AddAvgAge(builder, avgAge):
    GroupAddAvgAge(builder, avgAge)

def GroupAddAvgWeight(builder, avgWeight):
    builder.PrependFloat32Slot(1, avgWeight, 0.0)

def AddAvgWeight(builder, avgWeight):
    GroupAddAvgWeight(builder, avgWeight)

def GroupAddParticipantNamelist(builder, participantNamelist):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(participantNamelist), 0)

def AddParticipantNamelist(builder, participantNamelist):
    GroupAddParticipantNamelist(builder, participantNamelist)

def GroupStartParticipantNamelistVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartParticipantNamelistVector(builder, numElems: int) -> int:
    return GroupStartParticipantNamelistVector(builder, numElems)

def GroupEnd(builder):
    return builder.EndObject()

def End(builder):
    return GroupEnd(builder)