import matplotlib.pyplot as plt
import numpy as np
import func as fn
# Setup ####################################################################
period = 20
fs = 100
band = np.array([0, 0.6]).reshape(-1, 1)
freq = np.array([0.1, 0.15]).reshape(-1, 1)
power = np.array([100, 100]).reshape(-1, 1)
# Generate Data ############################################################
signal = fn.GenSignal(power, freq, period, fs)
print('Size of Data = ', signal.shape)
# Algorithm ################################################################
OSRfft = 16  # oversampling
fft_abs, freq, idx = fn.FreqSpectrum(signal, OSRfft, fs, band)

OSRmusic = 16  # oversampling
music_abs, mfreq, midx = fn.MUSICspectrum(signal, OSRmusic, fs, band)
# Plot results #############################################################
stime = [i for i in range(len(signal))]
stime = np.array(stime) / fs
fig, [ax1, ax2, ax3] = plt.subplots(nrows=3, ncols=1)
ax1.plot(stime, signal.real, label='Real')
ax1.plot(stime, signal.imag, label='Imag')
ax1.legend(loc='upper right', shadow=True)
ax1.set_xlabel('Time (sec.)')
ax1.set_ylabel('Amplitude')
ax1.set_xlim(0, period)
ax1.set_title('Signal')
ax1.grid()

ax2.plot(freq[idx], fft_abs[idx])
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Amplitude')
ax2.set_xlim(band[0], band[1])
ax2.set_ylim(0, np.max(fft_abs))
ax2.set_title('FFT')
ax2.grid()

ax3.plot(mfreq, music_abs)
ax3.set_xlabel('Frequency (Hz)')
ax3.set_ylabel('Amplitude')
ax3.set_xlim(band[0], band[1])
ax3.set_title('MUSIC')
ax3.grid()

plt.tight_layout()
plt.savefig('results.png',
            transparent=True,
            bbox_inches='tight',
            pad_inches=1)
plt.show()
