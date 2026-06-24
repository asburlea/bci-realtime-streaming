"""
LSL EEG inlet wrapper
"""

from pylsl import StreamInlet, resolve_stream

def create_inlet(stream_type="EEG"):
    print("Looking for EEG stream...")
    streams = resolve_stream("type", stream_type)
    inlet = StreamInlet(streams[0])
    return inlet

