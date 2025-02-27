# 🎶 Geração de Sinal com Controle de SNR em Arquivo WAV

Este repositório contém um código em **Python** para gerar um sinal acústico sintético, adicionar ruído branco controlado e exportar o resultado para um arquivo **.wav** com um SNR (Signal-to-Noise Ratio) especificado.

## 📌 Funcionalidades
✅ Gera sinais senoidais ou chirp (variação de frequência no tempo).  
✅ Adiciona ruído branco com um SNR ajustável.  
✅ Exporta o sinal final como um arquivo **.wav** com nome dinâmico.  
✅ Permite alterar frequência, duração, taxa de amostragem e nível de ruído.  
✅ Código modular para fácil adaptação a diferentes aplicações.

---

## 📂 Estrutura do Código

- **`generate_sine_wave(freq, duration, sample_rate, amplitude)`** → Gera um tom senoidal puro.  
- **`generate_chirp_signal(f_start, f_end, duration, sample_rate, amplitude)`** → Gera um sinal chirp variando a frequência entre `f_start` e `f_end`.  
- **`generate_white_noise(duration, sample_rate, amplitude)`** → Cria ruído branco para mistura com o sinal.  
- **`adjust_snr(signal_wave, noise_wave, snr_db)`** → Ajusta a potência do ruído para obter o SNR desejado.  
- **`export_wav(signal_wave, noise_wave, sample_rate, freq, duration, snr_db, signal_type)`** → Salva o áudio final em um arquivo `.wav`.

---

## ⚙️ Como Usar
### 1️⃣ Instalar Dependências
```bash
pip install numpy soundfile scipy
```
### 2️⃣ Configurar Parâmetros no Código
No arquivo principal, defina:
```python
signal_type = "chirp"  # Opções: "sine" ou "chirp"
freq = 1000  # Frequência do sinal (Hz)
f_start, f_end = 500, 2000  # Faixa do chirp
duration = 2  # Duração do sinal (s)
sample_rate = 44100  # Frequência de amostragem (Hz)
snr_db = 10  # Relação SNR desejada (dB)
```
### 3️⃣ Executar o Script
```bash
python nome_do_arquivo.py
```
O arquivo `.wav` será salvo no diretório do projeto.

---

## 🔬 Entendendo o SNR (Signal-to-Noise Ratio)
SNR (Relação Sinal-Ruído) mede a relação entre a potência do sinal e a potência do ruído, sendo expressa em **decibéis (dB)**:

\[ SNR (dB) = 10 \cdot \log_{10} (P_{sinal} / P_{ruído}) \]

| **SNR (dB)** | **Interpretação** |
|-------------|------------------|
| **+30 dB** | Sinal muito mais forte que o ruído (excelente qualidade) |
| **+20 dB** | Sinal claramente audível sobre o ruído |
| **+10 dB** | Sinal perceptível, mas com ruído significativo |
| **0 dB** | Sinal e ruído têm a mesma potência |
| **-10 dB** | O ruído domina o sinal |

---

## 📊 Aplicações
🔹 Simulação de sinais acústicos subaquáticos com diferentes condições de ruído.  
🔹 Testes de algoritmos de filtragem e detecção de sinais.  
🔹 Treinamento de modelos de machine learning para classificação de áudio.  
🔹 Geração de dados sintéticos para análise acústica.

---

## 🚀 Melhorias Futuras
✅ Adicionar ruídos submarinos reais além do ruído branco.  
✅ Implementar diferentes formas de onda (exemplo: pulsos e onda quadrada).  

---

## 📜 Licença
Este projeto está sob a licença **MIT**. Sinta-se à vontade para modificar e utilizar!  

---

Desenvolvido por [Isabela Assis Cardoso](https://www.linkedin.com/in/isabelaassiscardoso/) 🚀

