import numpy as np
import time


def GenSignal(power, freq, period, fs):
    omega = freq / fs * (2*np.pi)
    num_sample = period * fs
    sample = np.arange(num_sample).reshape(-1, 1)
    phase = np.dot(sample, omega.reshape(1, -1))
    phase_initial = np.random.randn(1, len(omega))
    phase_initial = np.tile(phase_initial, (num_sample, 1))
    s = np.exp(1j * (phase))
    y = np.dot(s, power)
    return y


def FreqSpectrum(s, OSR, fs, band):
    start_time = time.time()
    #
    num_s = s.shape[0]
    num_sensor = s.shape[1]
    osrnum_s = num_s * OSR
    num_pad = osrnum_s - num_s
    osr_s = np.concatenate([s, np.zeros((num_pad, num_sensor))], axis=0)
    sfft = np.fft.fft(osr_s, axis=0)
    sfft_abs = np.abs(sfft) / len(sfft)
    freq = np.fft.fftfreq(osrnum_s, 1/fs)
    idx = np.where((freq <= band[1]) & (freq >= band[0]))[0]
    #
    end_time = time.time()
    print('FFT running time = ', np.round((end_time-start_time), 2), '(sec.)')
    return sfft_abs, freq, idx


def MUSICspectrum(signal, OSR, fs, band):
    start_time = time.time()
    #
    N = signal.shape[0]
    M = 5  # Number of signal components
    DimCOV = N // 1
    # Create covariance matrix
    mean_signal = np.mean(signal, axis=0, keepdims=True)
    ac_signal = signal - mean_signal
    COV = np.matmul(ac_signal, np.conj(ac_signal.T))
    R = COV[0:DimCOV, 0:DimCOV]
    # Eigenvalue decomposition
    eigvals, eigvecs = np.linalg.eig(R)
    # Sort eigenvalues and eigenvectors
    eig_idx = np.argsort(eigvals)[::-1]  # ¤É§Ç ->­°§Ç
    eigvals = eigvals[eig_idx]
    eigvecs = eigvecs[:, eig_idx]
    # Frequency grid
    N_fft = N * OSR
    freq = np.fft.fftfreq(N_fft, 1/fs).reshape(-1, 1)
    idx = np.where((freq <= band[1]) & (freq >= band[0]))[0]
    omega = freq[idx] / fs * 2 * np.pi
    # Space
    noise_subspace = eigvecs[:, M-1:-1]
    sample = np.arange(DimCOV).reshape(1, -1)
    basis = np.exp(1j * np.dot(omega, sample))
    eV = np.matmul(np.conj(basis), noise_subspace)
    # MUSIC spectrum
    power = eV @ np.conj(eV.T)
    power_diag = np.diagonal(power)
    spectrum = 1 / np.real(power_diag)
    #
    end_time = time.time()
    print('MUSIC running time = ', np.round(
        (end_time-start_time), 2), '(sec.)')
    return spectrum, freq[idx], idx
