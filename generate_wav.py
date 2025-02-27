import numpy as np
import soundfile as sf
import scipy.signal as signal

def generate_sine_wave(freq=1000, duration=2, sample_rate=44100, amplitude=0.8):
    """ Gera um sinal senoidal puro audível ao ouvido humano. """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal_wave = amplitude * np.sin(2 * np.pi * freq * t)
    return signal_wave

def generate_chirp_signal(f_start=500, f_end=2000, duration=2, sample_rate=44100, amplitude=0.8):
    """ Gera um sinal chirp (sweep de frequência) dentro da faixa audível. """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    chirp_wave = amplitude * signal.chirp(t, f0=f_start, f1=f_end, t1=duration, method='linear')
    return chirp_wave

def generate_white_noise(duration=2, sample_rate=44100, amplitude=0.5):
    """ Gera ruído branco audível. """
    num_samples = int(sample_rate * duration)
    noise = amplitude * np.random.normal(0, 1, num_samples)
    return noise

def adjust_snr(signal_wave, noise_wave, snr_db):
    """ Ajusta o ruído para obter a relação SNR desejada. """
    signal_power = np.mean(signal_wave**2)
    noise_power = np.mean(noise_wave**2)
    
    target_noise_power = signal_power / (10**(snr_db / 10))
    noise_wave = noise_wave * np.sqrt(target_noise_power / noise_power)
    
    return noise_wave

def export_wav(signal_wave, noise_wave, sample_rate, freq, duration, snr_db, signal_type="sine"):
    """ Exporta o sinal combinado para um arquivo .wav com nome dinâmico. """
    filename = f"sinal_{signal_type}_{freq}Hz_{duration}s_SNR{snr_db}dB_{sample_rate}Hz.wav"
    combined_wave = signal_wave + noise_wave
    combined_wave /= np.max(np.abs(combined_wave))  # Normalização para evitar distorção
    sf.write(filename, combined_wave, sample_rate)
    print(f"Arquivo salvo: {filename}")

# Parâmetros ajustados para audibilidade
signal_type = "chirp"  # Opções: "sine" ou "chirp"
freq = 350  # Frequência do sinal (Hz) para senóide fixa
f_start, f_end = 200, 350  # Faixa de variação de frequência para chirp
duration = 5  # Duração em segundos
sample_rate = 44100  # Frequência de amostragem (Hz)
snr_db = 0.5 # Relação SNR desejada (dB)

# Escolher tipo de sinal
if signal_type == "sine":
    signal_wave = generate_sine_wave(freq, duration, sample_rate)
elif signal_type == "chirp":
    signal_wave = generate_chirp_signal(f_start, f_end, duration, sample_rate)

# Gerar ruído
noise_wave = generate_white_noise(duration, sample_rate)

# Ajustar SNR
noise_wave = adjust_snr(signal_wave, noise_wave, snr_db)

# Exportar WAV com nome dinâmico
export_wav(signal_wave, noise_wave, sample_rate, freq if signal_type == "sine" else f"{f_start}-{f_end}", duration, snr_db, signal_type)
