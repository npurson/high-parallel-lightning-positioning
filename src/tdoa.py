import numpy as np
import matlab
import gettdoa


def tdoa(trigger_time, data):
    """Computes Δtdoa by peak detection of waveform series.

    Args:
        trigger_time (Union[np.ndarray, list]): trigger_time with respect to each station
        data (Union[np.ndarray, list]):         wave datas with respect to each station

    Returns:
        tdoa (ndarray)
    """
    assert len(trigger_time) == len(data), 'Length of trigger_time and data must be equal!'
    engine = gettdoa.initialize()
    trigger_time = matlab.double(trigger_time, size=(len(trigger_time), 1))
    data = matlab.double(data)
    tdoa_ = engine.tdoa(trigger_time, data)
    engine.terminate()
    return np.unique((np.array(tdoa_).squeeze().round(7) * 1e7).astype(np.int32), axis=0)
