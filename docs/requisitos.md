# Requisitos de Software

## Introdução

Requisitos de software são as especificações que definem o que um sistema deve fazer (requisitos funcionais) e como ele deve se comportar (requisitos não funcionais). Eles são fundamentais para orientar o desenvolvimento, garantindo que o produto final atenda às necessidades dos usuários e stakeholders. A engenharia de requisitos envolve atividades como elicitação, análise, documentação e gestão de requisitos ao longo do ciclo de vida do projeto.

A gestão eficaz dos requisitos é essencial para o sucesso do projeto, incluindo a identificação e resolução de ambiguidades, conflitos e mudanças. Além disso, a comunicação clara entre todos os envolvidos é crucial para traduzir as necessidades dos usuários em requisitos claros e viáveis.

Tendo em vista a execução previa do projeto, foi possível realizar um refinamento nos requisitos de software, a fim de torná-los mais claros e completos. Abaixo estão listados os requisitos funcionais e não funcionais, com suas respectivas descrições detalhadas. 

---

## Requisitos Funcionais

|   ID   | Requisito                                                                                       | Detalhamento                                                                                                   |
| :----: | :--------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------   |
| RFSO01 | O sistema deve permitir que os usuários cadastrem kits                                          | O cadastro de kits deve incluir nome, lista de componentes associados, e um anexo do kit                       |
| RFSO02 | O sistema deve permitir que os usuários editem os kits                                          | A edição deve permitir a modificação de todos os campos cadastrados, exceto o ID do kit.                       |
| RFSO03 | O sistema deve permitir que os usuários listem os kits                                          | A listagem deve informar a lista de componentes com nome e anexo, além da opção de produzir                    |
| RFSO04 | O sistema deve permitir que os usuários excluam os kits                                         | A exclusão deve eliminar o registro da base                                                                    |
| RFSO05 | O sistema deve permitir que usuários sejam cadastrados                                          | O cadastro de usuários deve incluir nome, e-mail, senha, papel (administrador/operador)                        |
| RFSO06 | O sistema deve permitir que usuários sejam editados                                             | A edição deve permitir a modificação de todos os campos, exceto o ID do usuário.                               |
| RFSO07 | O sistema deve permitir que usuários sejam listados                                             |                                                                                                                |
| RFSO08 | O sistema deve permitir que usuários sejam excluídos                                            | A exclusão deve eliminar o registro da base                                                                    |
| RFSO09 | O sistema deve permitir que os usuários cadastrem os componentes                                | O cadastro de componentes deve incluir nome, descrição, quantidade mínima em estoque e tipo.                   |
| RFSO10 | O sistema deve permitir que os usuários editem os componentes                                   | A edição deve permitir a modificação de todos os campos cadastrados, exceto o ID do componente.                |
| RFSO11 | O sistema deve permitir que os usuários listem os componentes                                   |                                                                                                                |
| RFSO12 | O sistema deve permitir que os usuários excluam os componentes                                  | A exclusão deve eliminar o registro da base                                                                    |
| RFSO13 | O sistema deve ser capaz de reconhecer as imagens dos elementos dos kits                        | O reconhecimento de imagens deve utilizar o modelo yolo v8  para identificar componentes.                      |
| RFSO14 | O sistema deve ser capaz de comparar os dados da balança e das imagens dos componentes do kit   | A comparação deve validar a quantidade e o tipo de componente com base nos dados da balança e das imagens.     |
| RFSO15 | O sistema deve ser capaz de realizar controle de estoque                                        | Armazenar a quantidade de cada componente disponível no estoque, atualizando automaticamente após a montagem.  |
| RFSO16 | O sistema deve ser capaz de informar quantos e quais componentes ao concluir a montagem do kit  | O sistema deve gerar um relatório detalhado dos componentes utilizados e seu status após a montagem.           |
| RFSO17 | O sistema deve permitir que os usuários selecionem kits para produção                           | A seleção deve incluir a verificação da disponibilidade de componentes no estoque.                             |
| RFSO18 | O sistema deve permitir que os usuários se autentiquem no sistema com seu devido papel          | A autenticação deve ser feita via login e senha, com restrições de acesso baseadas no papel do usuário.        |
| RFSO19 | O sistema deve permitir a configuração de permissões de acesso por papel                        | As permissões devem ser configuráveis para cada funcionalidade do sistema, com base no papel do usuário.       |

---

## Requisitos Não Funcionais

|   ID    | Requisito                                                                                       | Detalhamento                                                                                                 |
| :-----: | :--------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| RNFSO01 | Os usuários do sistema serão separados por administrador e operador                            | O administrador terá acesso total ao sistema, enquanto o operador terá acesso restrito a funcionalidades específicas. |
| RNFSO02 | A detecção e reconhecimento de componentes devem ocorrer em tempo real                         | O tempo de resposta para reconhecimento de imagens deve ser inferior a 2 segundos.                            |
| RNFSO03 | O sistema deve ser capaz de lidar com múltiplas solicitações de CRUD simultaneamente           | O sistema deve suportar pelo menos 10 requisições simultâneas sem degradação de desempenho.                   |
| RNFSO04 | O sistema deve suportar a adição de novos tipos de componentes sem interromper operações       |                                                                                                               |
| RNFSO05 | O sistema deve ser robusto o suficiente para lidar com possíveis falhas de hardware            | O sistema deve ser capaz de se recuperar automaticamente de falhas de hardware em até 5 minutos.              |
| RNFSO06 | A interface do usuário deve ser intuitiva e fácil de usar                                      | A interface deve seguir princípios de UX/UI, com navegação simplificada e feedback visual claro.              |
| RNFSO07 | Mensagens de erro devem ser claras e informativas                                              | As mensagens devem incluir código de erro, descrição e sugestões para resolução.                              |
| RNFSO08 | Deve ser implementado um sistema de registro de logs abrangente                                | Os logs devem incluir informações como data, hora, usuário, ação realizada e status (sucesso/erro).           |
| RNFSO09 | O backend será desenvolvido em Python/Django                                                   | O uso de Django deve garantir modularidade, segurança e escalabilidade.                                       |
| RNFSO10 | O frontend será desenvolvido em TypeScript/React                                               | O uso de React deve garantir uma interface dinâmica e responsiva.                                             |
| RNFSO11 | O sistema deve ser uma aplicação web acessível via navegadores padrão                          | A aplicação deve ser compatível com Chrome, Firefox, Edge e Safari.                                           |
| RNFSO12 | O banco de dados será desenvolvido em MySQL                                                    | O banco de dados deve ser normalizado                                                                         |

---

Refinamento sobre requisitos funcionais e não funcionais:

## Requisitos Funcionais

|   ID   | Requisito                                                                                       | Detalhamento                                                                                                              |
| :-----: | :--------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| RFSO01 | O sistema deve permitir que os usuários cadastrem kits                                          | O cadastro de kits deve incluir nome, lista de componentes associados, e um anexo do kit, alem do status (ativo, inativo) |
| RFSO04 | O sistema deve permitir que os usuários excluam os kits                                         | Ao inves de excluir o registro a exclusão deve ser lógica (marcação como inativo)                                         |
| RFSO08 | O sistema deve permitir que usuários sejam excluídos                                            | Ao inves de excluir o registro a exclusão deve ser lógica (marcação como inativo)                                         |
| RFSO12 | O sistema deve permitir que os usuários excluam os componentes                                  | Ao inves de excluir o registro a exclusão deve ser lógica (marcação como inativo)                                         |
| RFSO15 | O sistema deve ser capaz de realizar controle de estoque                                        | O controle de estoque deve incluir alertas de reposição quando a quantidade mínima for atingida.                          |
| RFSO20 | O sistema deve gerar relatórios de produção e estoque                                           | Os relatórios devem ser exportáveis em formatos como PDF e CSV                                                            |

## Requisitos Não Funcionais

|   ID   | Requisito                                                                                       | Detalhamento                                                                                                       |
| :-----: | :--------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| RNFSO13 | O sistema deve garantir a segurança dos dados                                                  | Os dados devem ser criptografados, com controle de acesso baseado em permissões e autenticação de dois fatores.    |
| RNFSO14 | O sistema deve ser escalável para suportar crescimento futuro                                  | A arquitetura deve permitir a adição de novos servidores e balanceamento de carga.                                 |
| RNFSO15 | O tempo de resposta médio do sistema deve ser inferior a 500ms                                 | O desempenho deve ser monitorado e otimizado continuamente.                                                        |
| RNFSO16 | O sistema deve ser compatível com dispositivos móveis                                          | A interface deve ser responsiva e adaptável a diferentes tamanhos de tela.                                         |
