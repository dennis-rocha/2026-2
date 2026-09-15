# Requisitos Funcionais

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos

## Requisitos Funcionais

| Código     | Prioridade | Descrição                                                                                                                                                                                   |
| ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RF_001** | Alta       | O sistema deve permitir que os responsáveis realizem o cadastro e a manutenção das informações das empresas próprias e terceiras relacionadas à organização.                                |
| **RF_002** | Alta       | O sistema deve permitir que os responsáveis realizem o cadastro e a manutenção dos setores da organização.                                                                                  |
| **RF_003** | Alta       | O sistema deve permitir que os responsáveis realizem o cadastro e a manutenção dos cargos existentes na organização.                                                                        |
| **RF_004** | Alta       | O sistema deve permitir que os responsáveis realizem o cadastro e a manutenção dos colaboradores internos e terceirizados, associando cada colaborador à respectiva empresa, setor e cargo. |
| **RF_005** | Alta       | O sistema deve permitir que os responsáveis realizem o cadastro e a manutenção dos cursos de treinamentos obrigatórios de segurança (NRs).                                                  |
| **RF_006** | Alta       | O sistema deve permitir associar cursos obrigatórios aos respectivos cargos.                                                                                                                |
| **RF_007** | Alta       | O sistema deve permitir que os responsáveis registrem os treinamentos realizados, vinculando cada treinamento ao respectivo curso e professor responsável.                                  |
| **RF_008** | Alta       | O sistema deve permitir associar colaboradores aos treinamentos realizados.                                                                                                                 |
| **RF_009** | Alta       | O sistema deve permitir registrar a nota e a situação de aprovação de cada colaborador em um treinamento realizado.                                                                         |
| **RF_010** | Alta       | O sistema deve calcular a data de validade do treinamento realizado com base na data do treinamento e na validade definida para o curso.                                                    |
| **RF_011** | Alta       | O sistema deve permitir registrar e consultar os certificados relacionados aos treinamentos realizados pelos colaboradores.                                                                 |
| **RF_012** | Alta       | O sistema deve permitir armazenar o arquivo digital e a data de emissão do certificado relacionado ao treinamento realizado.                                                                |
| **RF_013** | Alta       | O sistema deve identificar os cursos obrigatórios aplicáveis a cada colaborador com base em seu cargo.                                                                                      |
| **RF_014** | Alta       | O sistema deve identificar o treinamento mais recente realizado pelo colaborador para cada curso obrigatório.                                                                               |
| **RF_015** | Alta       | O sistema deve identificar a situação dos treinamentos obrigatórios dos colaboradores com base na respectiva data de validade.                                                              |
| **RF_016** | Alta       | O sistema deve identificar os cursos obrigatórios que ainda não possuem treinamento registrado para o colaborador.                                                                          |
| **RF_017** | Alta       | O sistema deve permitir que gestores e responsáveis consultem a situação dos treinamentos obrigatórios dos colaboradores internos e terceirizados.                                          |
| **RF_018** | Média      | O sistema deve permitir consultar os treinamentos e certificados dos colaboradores organizados por empresa.                                                                                 |
| **RF_019** | Média      | O sistema deve permitir consultar os treinamentos e certificados dos colaboradores organizados por setor e cargo.                                                                           |
| **RF_020** | Média      | O sistema deve identificar os treinamentos dos colaboradores que estejam próximos do vencimento.                                                                                            |
| **RF_021** | Média      | O sistema deve permitir gerar relatórios sobre a situação dos treinamentos obrigatórios e das respectivas certificações dos colaboradores.                                                  |
| **RF_022** | Média      | O sistema deve permitir registrar a prestação de serviços entre empresas próprias e empresas terceiras.                                                                                     |
| **RF_023** | Média      | O sistema deve permitir consultar as prestações de serviços ativas e encerradas entre empresas.                                                                                             |
| **RF_024** | Média      | O sistema deve emitir alertas aos responsáveis sobre treinamentos próximos do vencimento ou já vencidos.                                                                                    |
| **RF_025** | Média      | O sistema deve permitir gerar relatórios periódicos sobre a situação dos treinamentos obrigatórios dos colaboradores.                                                                       |

## Observações

* A validade é uma característica do **curso**, definida em `validade_meses`.
* A data de validade de uma realização específica é armazenada em `treinamento_colaborador.data_validade`.
* O certificado representa o **documento comprobatório** da realização do treinamento e não é responsável por determinar sua validade.
* A situação do treinamento pode ser obtida comparando `data_validade` com a data atual.
* A obrigatoriedade de um curso para um colaborador é determinada pelo relacionamento entre `cargo` e `curso`, por meio da tabela `cargo_cursos`.
* O sistema deve considerar o treinamento mais recente do colaborador para cada curso obrigatório ao determinar sua situação atual.
* Treinamentos anteriores devem permanecer armazenados para preservação do histórico.
* A existência de um registro em `treinamento_colaborador` representa a participação do colaborador naquele treinamento.
* O colaborador pode ser próprio ou terceirizado, sendo essa informação determinada pela empresa à qual está vinculado.
* Os requisitos relacionados a alertas e relatórios periódicos podem demandar mecanismos de processamento automático e agendamento.

## Evoluções previstas

Algumas funcionalidades foram mantidas fora do escopo inicial para possibilitar sua utilização posteriormente como **mudanças de requisitos e evolução do software**, permitindo trabalhar conceitos relacionados à manutenção de software.

Entre as possíveis evoluções estão:

* Cadastro de coordenadores vinculados aos setores.
* Definição de líderes dos setores.
* Notificações automáticas por e-mail.
* Configuração do período de antecedência para alertas de vencimento.
* Dashboard gerencial de conformidade.
* Novos filtros e indicadores para relatórios.
* Integração com outros sistemas da organização.
* Automatização de rotinas de acompanhamento das certificações.
