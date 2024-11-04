# Filtro_Wavelet
Atividade proposta para a materia de Computação Gráfica e Processamento de Imagens

O filtro de wavelet atua como uma ferramenta para decompor um sinal (como uma imagem, som ou qualquer série de dados) em diferentes escalas e frequências. No contexto de processamento de imagens, ele é usado para separar a imagem em componentes de baixa e alta frequência, o que é extremamente útil para várias aplicações, como compressão, redução de ruído e análise de características.

### Dentre as principais funções do filtro de wavelet temos:

Baixa Frequência (Aproximações): Este componente representa as partes mais suaves ou as estruturas gerais da imagem, sem muitos detalhes. Ele retém a maior parte das informações visuais, e é usado para reconstruir uma versão "simplificada" da imagem.
Alta Frequência (Detalhes): Os componentes de alta frequência capturam bordas, texturas e outros detalhes finos da imagem. Estes detalhes são essenciais para identificar contornos e pequenas variações.

### Na Prática:
O filtro wavelet age como uma "janela" móvel, semelhante a um zoom que observa as diferentes escalas (ou resoluções) do sinal. A transformação wavelet transforma a imagem em uma série de sub-bandas, e cada uma representa um nível específico de detalhe.

Para uma imagem, isso significa que o filtro wavelet aplica um conjunto de filtros passa-baixa e passa-alta, resultando nos componentes:

LL (baixa frequência, aproximação geral)
LH, HL, HH (detalhes em várias direções).

Atividade Prosposta: 

Objetivo: Utilizar a transformada Wavelet para realizar a compressão de uma imagem, removendo componentes de alta frequência (detalhes) e reconstruindo a imagem comprimida.

Instruções:
Carregue uma imagem em escala de cinza.
Aplique a transformada Wavelet (usando 'haar') para decompor a imagem em componentes: (LL, LH, HL, HH)
Descarte os componentes de detalhes  (LH, HL, HH) e mantenha apenas o componente de baixa frequência (LL)
Realize a reconstrução inversa usando apenas o componente LL e visualize a imagem reconstruída.
Desafio: Compare a imagem original com a imagem reconstruída. Avalie a qualidade da imagem comprimida.

![Uma capivara no filtro de wavelet: ](https://github.com/user-attachments/assets/15e0aa92-f1f1-4474-a59d-602c9268cfdc)


A imagem à direita mostra a versão reconstruída após aplicar a Transformada Wavelet, mantendo apenas o componente de baixa frequência (LL).
**Imagem Original (Esquerda):** Exibe todos os detalhes da imagem, incluindo bordas e texturas finas (como os pelos do animal).
**Imagem Reconstruída (Direita):** Perdeu alguns dos detalhes mais finos suavizando a imagem, mas mantém a estrutura geral da imagem. Essa suavização ocorre porque os componentes de alta frequência (LH, HL, HH), que carregam detalhes, foram descartados.

