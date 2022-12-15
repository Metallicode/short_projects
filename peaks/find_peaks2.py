
def closer(arr,prox):
    result = []
    result.append(arr[0])
    for i in range(1,len(arr)-1):
        if arr[i]-result[-1]>prox:
            result.append(arr[i])
    return result 

def find_peaks(signal, thd=0.005):
    signal = np.array(signal)
    diffs = signal[1:] - signal[:-1]
    peaks = np.where(np.abs(diffs) < thd)[0]
    return peaks



