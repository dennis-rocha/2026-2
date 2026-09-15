# Regras de Negócio

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos

## Regras de Negócio

| Código     | Descrição                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **RN_001** | Cada colaborador deve estar vinculado a uma única empresa.                                                                            |
| **RN_002** | Uma empresa deve ser classificada como própria ou terceira.                                                                           |
| **RN_003** | Cada colaborador deve pertencer a um único setor.                                                                                     |
| **RN_004** | Cada colaborador deve ocupar um único cargo.                                                                                          |
| **RN_005** | Uma empresa própria pode possuir colaboradores próprios e colaboradores vinculados a empresas terceiras relacionadas à organização.   |
| **RN_006** | Uma prestação de serviço deve relacionar uma empresa própria a uma empresa terceira.                                                  |
| **RN_007** | Uma prestação de serviço deve possuir uma data de início e pode possuir uma data de encerramento.                                     |
| **RN_008** | Um cargo pode possuir vários cursos obrigatórios, e um curso pode ser obrigatório para vários cargos.                                 |
| **RN_009** | O mesmo curso não pode ser associado mais de uma vez ao mesmo cargo.                                                                  |
| **RN_010** | A obrigatoriedade de um curso para um colaborador deve ser determinada a partir do cargo ocupado pelo colaborador.                    |
| **RN_011** | Um treinamento deve estar associado a um único curso e possuir um professor responsável.                                              |
| **RN_012** | Um professor responsável por um treinamento deve estar cadastrado como colaborador no sistema.                                        |
| **RN_013** | Um colaborador pode participar de vários treinamentos, e um treinamento pode possuir vários colaboradores.                            |
| **RN_014** | Um colaborador não pode ser associado mais de uma vez ao mesmo treinamento.                                                           |
| **RN_015** | A participação do colaborador em um treinamento deve possuir uma nota e uma situação de aprovação.                                    |
| **RN_016** | A data de validade de um treinamento realizado deve ser calculada com base na data de realização e na validade definida para o curso. |
| **RN_017** | A data de validade calculada para um treinamento realizado deve ser armazenada para preservar o histórico da realização.              |
| **RN_018** | A alteração da validade definida para um curso não deve alterar a validade dos treinamentos realizados anteriormente.                 |
| **RN_019** | A situação atual do colaborador em relação a um curso deve considerar o treinamento mais recente realizado para aquele curso.         |
| **RN_020** | Um treinamento realizado deve permanecer registrado no histórico mesmo quando existir uma realização posterior do mesmo curso.        |
| **RN_021** | Um registro de participação em treinamento pode possuir, no máximo, um certificado associado.                                         |
| **RN_022** | Um certificado deve estar associado a um único registro de participação em treinamento.                                               |
| **RN_023** | O certificado representa o documento comprobatório da realização do treinamento e não determina a validade do treinamento.            |
| **RN_024** | A situação de um treinamento deve ser determinada pela comparação entre sua data de validade e a data atual.                          |
| **RN_025** | Um treinamento obrigatório sem registro de realização para o colaborador deve ser considerado pendente de realização.                 |
| **RN_026** | Os treinamentos anteriores de um colaborador devem permanecer disponíveis para consulta e preservação do histórico.                   |

## Regras relacionadas à conformidade

A situação de conformidade de um colaborador deve considerar os cursos obrigatórios definidos para seu cargo e os respectivos treinamentos realizados.

Para cada curso obrigatório, o sistema poderá identificar uma das seguintes situações:

* **Pendente:** não existe registro de realização do curso para o colaborador.
* **Vigente:** existe treinamento realizado e sua data de validade é igual ou posterior à data atual.
* **Vencido:** existe treinamento realizado, porém sua data de validade é anterior à data atual.

A situação deve considerar sempre o **treinamento mais recente do colaborador para o respectivo curso**, preservando os registros anteriores como histórico.

## Observações

* As regras de negócio representam as condições que devem ser respeitadas independentemente da tecnologia utilizada para implementação.
* Algumas regras poderão ser implementadas por restrições do banco de dados, enquanto outras deverão ser tratadas pela aplicação.
* As regras relacionadas à validade dos treinamentos deverão ser consideradas durante a implementação dos modelos e das funcionalidades do sistema.
* As regras de negócio também servirão como base para a definição dos testes do sistema.

## Evoluções previstas

As seguintes regras podem ser incorporadas futuramente como parte da evolução do sistema:

* Definição de um ou mais coordenadores responsáveis por cada setor.
* Definição de um líder para cada setor.
* Regras específicas para colaboradores vinculados a diferentes prestações de serviço.
* Regras para alertas de vencimento configuráveis.
* Regras para notificações automáticas aos responsáveis.
* Regras adicionais de conformidade de acordo com novas necessidades da organização.
