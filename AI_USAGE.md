Declaração de Uso de Inteligência Artificial Generativa
Ferramenta: Claude (Anthropic), via chat

Finalidade: Apoio na estruturação do repositório, implementação inicial do pipeline de Processamento Digital de Imagens (pré-processamento, segmentação, extração de características e classificação por regras) e redação da documentação.

Partes Afetadas:

Estrutura de diretórios do repositório.

Arquivos em src/ (preprocessing.py, segmentation.py, features.py, classify.py, main.py, generate_synthetic_cards.py).

Testes automatizados em tests/test_pipeline.py.

Documentação em README.md e docs/proposta.md.

Forma de Validação:

Execução dos testes automatizados via pytest, confirmando o processamento e classificação das 20 imagens sintéticas de desenvolvimento (20/20 — images/results/resultados_sinteticos.json).

Revisão técnica da lógica de cada módulo (binarização por Otsu, critério de cor dominante, descritores de forma e regras de classificação) e validação da justificativa geométrica de cada descritor.

Pendente: Validação e recalibração com fotos reais do baralho físico (o grupo se responsabiliza por esta etapa antes da entrega final).

Modificações Realizadas:

Definição e criação da estrutura arquitetural do repositório.

Escrita e refinamento do código-fonte dos módulos de PDI em src/.

Construção dos cenários de teste em test_pipeline.py.

Redação dos textos descritivos do README.md e proposta.md.

Registro:

Pergunta: Como estruturar um pipeline modularizado de PDI em Python para classificação de objetos?

Orientação: Separe o fluxo em etapas independentes: pré-processamento (preprocessing.py), segmentação (segmentation.py), extração de características (features.py) e regras de decisão (classify.py).

Uso: Aplicado na criação da arquitetura do repositório na pasta src/.

Pergunta: Como gerar imagens sintéticas programaticamente para testar o pipeline antes da etapa de captura real?

Orientação: Utilize bibliotecas como OpenCV e NumPy para desenhar programmaticamente as formas dos naipes e simular cartas com variações controladas.

Uso: Implementado no script src/generate_synthetic_cards.py para gerar o conjunto inicial de testes.

Pergunta: Como estruturar os testes automatizados utilizando pytest para validar o pipeline?

Orientação: Crie funções iniciadas com test_ no diretório tests/ que iteram sobre as imagens sintéticas, executam a função principal de classificação e verificam o resultado com assert.

Uso: Estruturação do arquivo tests/test_pipeline.py.

Pergunta: Como aplicar binarização adaptativa/Otsu e extrair descritores de forma para segmentação?

Orientação: Converta para escala de cinza, aplique cv2.threshold com a flag THRESH_OTSU e utilize cv2.findContours para obter métricas geométricas (área, perímetro, excentricidade).

Uso: Implementado em preprocessing.py, segmentation.py e features.py.
