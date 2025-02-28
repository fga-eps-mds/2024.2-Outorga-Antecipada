# Arquitetura do Projeto Esteira Inteligente

## Visão Geral
O projeto [Esteira  inteligente]() utiliza uma **Raspberry Pi 4** como unidade central para gerenciar a operação de montagem e distribuição de kits de peças. A identificação das peças ocorre por meio de **Inteligência Artificial (IA)**, enquanto a movimentação das esteiras é controlada por **Arduino Uno R3**.

O sistema permite que o usuário solicite kits de peças por meio de um cliente web. A IA processa imagens para identificar as peças presentes na esteira e garantir que o kit solicitado seja corretamente montado e entregue ao usuário.

![Arquitetura do Projeto](https://github.com/fga-eps-mds/2024.2-Outorga-Antecipada/blob/main/docs/assets/EI.jpg?raw=true)

## Componentes Principais

### 1. Hardware
- **Raspberry Pi 4**: Unidade central de processamento do sistema.
- **Arduino Uno R3 (x2)**: Controlam os módulos eletrônicos, motores das esteiras e outros atuadores.
- **Câmeras (x2)**:
  - **Câmera 1**: Identifica as peças posicionadas na esteira.
  - **Câmera 2**: Confirma quais peças foram entregues ao usuário ao final do processo.
- **Motores e Sensores**: Utilizados para movimentação da esteira e detecção da presença de peças.

### 2. Software
- **Modelo de IA**:
  - Processa as imagens capturadas pela Câmera 1 para identificar as peças na esteira.
  - Verifica, por meio da Câmera 2, se as peças corretas foram entregues ao usuário.
- **Backend (Django)**:
  - Gerencia solicitações de kits de peças.
  - Controla a comunicação entre a interface web e os microcontroladores.
- **Frontend (Next.js)**:
  - Interface gráfica para o usuário solicitar kits de peças e acompanhar a operação da esteira.
- **Comunicação**:
  - A Raspberry Pi se comunica com os Arduinos via **Serial/USB**.
  - O frontend se comunica com o backend via **HTTP**.

## Fluxo de Operação
1. O usuário acessa a interface web e solicita um kit de peças.
2. O backend recebe a solicitação e a envia para a Raspberry Pi.
3. A Câmera 1 captura uma imagem da esteira.
4. O modelo de IA processa a imagem e identifica as peças disponíveis.
5. O sistema decide como movimentar as esteiras para montar o kit.
6. Os comandos são enviados para os Arduinos para acionar os motores e deslocar as peças.
7. Ao final do processo, a Câmera 2 verifica se o kit correto foi montado e entregue.
8. O backend atualiza o status da solicitação na interface web.

## Tecnologias Utilizadas
- **Hardware**: Raspberry Pi 4, Arduino Uno R3, Câmeras, Motores, Sensores.
- **Inteligência Artificial**: YOLOv8.
- **Backend**: Django.
- **Frontend**: Next.js, React.
- **Comunicação**: HTTP, Serial/USB.

## 

## Conclusão
Este sistema permite a montagem automatizada de kits de peças utilizando visão computacional e controle de esteiras via microcontroladores. A Raspberry Pi atua como o núcleo do sistema, processando imagens com IA e coordenando as ações dos Arduinos. O backend em Django e o frontend em Next.js proporcionam uma interface eficiente para a solicitação e acompanhamento da operação pelo usuário.
