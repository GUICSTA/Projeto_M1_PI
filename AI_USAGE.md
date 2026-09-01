# Declaração de Uso de Inteligência Artificial Generativa

Conforme exigido pela seção 16 do enunciado do projeto aplicado (M1), declaramos abaixo o uso de IA generativa neste projeto.

## Ferramenta utilizada

Claude (Anthropic), via chat.

## Finalidade

Apoio na estruturação do repositório, implementação inicial do pipeline de PDI (pré-processamento, segmentação, extração de características e classificação por regras) e redação da documentação (README, proposta).

## Material produzido ou modificado com apoio de IA

- Estrutura de diretórios do repositório.
- Código-fonte inicial em `src/` (`preprocessing.py`, `segmentation.py`, `features.py`, `classify.py`, `main.py`, `generate_synthetic_cards.py`).
- Testes automatizados em `tests/test_pipeline.py`.
- Geração de um conjunto de **imagens sintéticas de desenvolvimento** (desenhos programáticos dos símbolos dos naipes), usado para validar o pipeline antes da sessão de fotos com o baralho físico real.
- Textos do `README.md` e `docs/proposta.md`.

## Forma como o grupo verificou a resposta obtida

- O código foi executado e os testes automatizados (`pytest`) foram rodados, confirmando que o pipeline processa as imagens e classifica corretamente as 20 imagens sintéticas de desenvolvimento (20/20 — ver `images/results/resultados_sinteticos.json`).
- O grupo revisou a lógica de cada módulo (binarização por Otsu, critério de cor dominante, descritores de forma e regras de classificação) e entende a justificativa geométrica de cada descritor.
- **Ainda pendentes:** validação com fotos reais do baralho físico. Os limiares de classificação foram calibrados apenas sobre as imagens sintéticas e **precisarão ser reajustados** — isso está documentado explicitamente como próximo passo em `docs/proposta.md`, e o grupo se responsabiliza por essa validação antes de reportar qualquer resultado como final.

## Responsabilidade

O grupo permanece responsável por todo o conteúdo do repositório e pelo entendimento técnico das decisões tomadas, e está apto a explicar qualquer parte do pipeline, incluindo suas limitações atuais (dependência de imagens sintéticas, necessidade de recalibração com dados reais).
