import cv2
import pywt
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem em escala de cinza
imagem = cv2.imread('capivara.png', cv2.IMREAD_GRAYSCALE)

# Aplicar a Transformada Wavelet Discreta 2D (usando a wavelet 'haar')
coeffs2 = pywt.dwt2(imagem, 'haar')
LL, (LH, HL, HH) = coeffs2  # LL: baixa frequência, LH, HL, HH: alta frequência

# Descartar os componentes de detalhes (LH, HL, HH), mantendo apenas LL
coeffs2_comprimido = (LL, (np.zeros_like(LH), np.zeros_like(HL), np.zeros_like(HH)))

# Realizar a Transformada Inversa Wavelet Discreta 2D para reconstruir a imagem
imagem_reconstruida = pywt.idwt2(coeffs2_comprimido, 'haar')

# Visualizar a imagem original e a imagem reconstruída
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Imagem Original
ax[0].imshow(imagem, cmap='gray')
ax[0].set_title('Imagem Original')
ax[0].axis('off')

# Imagem Reconstruída
ax[1].imshow(imagem_reconstruida, cmap='gray')
ax[1].set_title('Imagem Reconstruída (Apenas LL)')
ax[1].axis('off')

plt.tight_layout()
plt.show()

# Calcular a diferença entre a imagem original e a reconstruída
diferença = np.abs(imagem - imagem_reconstruida)
erro_medio = np.mean(diferença)

print(f"Erro Médio Absoluto entre a imagem original e a reconstruída: {erro_medio:.2f}")