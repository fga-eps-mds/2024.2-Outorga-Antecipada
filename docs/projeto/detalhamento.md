# Mapeamento de Alterações Necessárias para Implementação de Indicadores

## 1. Introdução  

Para avaliar as modificações requeridas, foi conduzido um estudo inicial para identificar os requisitos necessários à implementação dos indicadores, incluindo as métricas essenciais para sua correta aplicação. Em seguida, foi realizada uma análise do código-fonte do projeto, visando compreender sua estrutura e viabilizar a implementação das métricas identificadas.  

## 2. Indicadores Necessários  

Os seguintes indicadores foram definidos para a implementação do projeto:  

- **Bug Density LOC**  
- **Bug Density Feature**  
- **Fulfillment of Critical/Blocker Quality Rules**  

A tabela abaixo apresenta a descrição detalhada de cada indicador:  

![Tabela de Indicadores](assets/tabela_indicadores.png)  

## 3. Análise do Código-Fonte  

### **parser_template.py**  

O arquivo `parser_template.py` é responsável por extrair métricas do SonarQube e do Git, armazenando-as em arquivos JSON.  

As seguintes alterações são necessárias para viabilizar a coleta das métricas:  

- Ajuste no caminho do arquivo JSON de saída.  
- Configuração do arquivo `.env`. 

### **internal_quality_analysis-sonarqube.ipynb**  

O arquivo `internal_quality_analysis-sonarqube.ipynb` tem como função processar as métricas extraídas pelo parser e convertê-las em indicadores.  

As seguintes modificações são necessárias para a derivação dos indicadores:  

- Configuração dos repositórios que serão analisados, incluindo a especificação de suas linguagens.  
- Ajuste no caminho do arquivo JSON de entrada.  
- Correção na extração das linguagens dos repositórios: `repos_language[base_name.split("-")[6]]`.  
- Implementação dos cálculos dos indicadores.  
- Geração e visualização dos gráficos dos indicadores.  

### **Alterações recomendadas para o repositório de analytics**  

- Configuração do arquivo `.env.example`.  
- Adição de configurações ao `.gitignore`.  

## 4. Dúvidas sobre a Implementação

* No repositório de analytics exisite o notebook internal_quality_analysis-github.ipynb que não foi mencionado no documento. Para o indicador que envolve apenas o repositório do GitHub, esse notebook deve ser utilizado?

* Para os indicadores que mesclam métricas do SonarQube e do GitHub, como deve ser feita a integração dessas métricas? Um novo notebook deve ser criado para essa finalidade?

* Deve ser gerado uma nova release para cada consulta do parser sobre o GitHub e o SonarQube?


## 5. Conclusão

Com a implementação das alterações mencionadas, será possível extrair, processar e visualizar os indicadores de qualidade do projeto de forma eficiente. As adaptações sugeridas garantem a compatibilidade das métricas com a estrutura existente, facilitando a análise da qualidade do código.

