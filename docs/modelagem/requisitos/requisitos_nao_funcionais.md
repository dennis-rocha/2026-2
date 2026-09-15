# Requisitos Não Funcionais

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos

## Requisitos Não Funcionais

| Código      | Categoria        | Prioridade | Descrição                                                                                                                                                                                |
| ----------- | ---------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RNF_001** | Segurança        | Alta       | O sistema deve restringir o acesso às informações e funcionalidades de acordo com o perfil e as permissões de cada usuário.                                                              |
| **RNF_002** | Segurança        | Alta       | O sistema deve proteger os dados de colaboradores, empresas, treinamentos e certificados contra acesso, alteração ou exclusão não autorizada.                                            |
| **RNF_003** | Segurança        | Alta       | O sistema deve registrar as operações relevantes realizadas pelos usuários sobre os dados do sistema, permitindo identificar o usuário e a data da operação.                             |
| **RNF_004** | Confiabilidade   | Alta       | O sistema deve manter os registros de colaboradores, treinamentos e certificados de forma consistente, evitando perda ou inconsistência dos dados armazenados.                           |
| **RNF_005** | Confiabilidade   | Alta       | O sistema deve garantir a integridade dos relacionamentos entre empresas, colaboradores, setores, cargos, cursos, treinamentos e certificados.                                           |
| **RNF_006** | Confiabilidade   | Alta       | O sistema deve preservar o histórico dos treinamentos realizados pelos colaboradores, mesmo quando novos treinamentos do mesmo curso forem registrados.                                  |
| **RNF_007** | Confiabilidade   | Alta       | O sistema deve possuir mecanismo de backup dos dados armazenados, permitindo sua recuperação em caso de falhas.                                                                          |
| **RNF_008** | Usabilidade      | Alta       | O sistema deve apresentar as informações relacionadas à situação dos treinamentos de forma clara e organizada, facilitando o acompanhamento pelos usuários responsáveis.                 |
| **RNF_009** | Usabilidade      | Média      | O sistema deve apresentar mensagens claras aos usuários durante operações de cadastro, alteração, exclusão e consulta de informações.                                                    |
| **RNF_010** | Desempenho       | Média      | O sistema deve apresentar as consultas e informações solicitadas pelos usuários em tempo adequado para a operação normal, sem atrasos que prejudiquem o acompanhamento dos treinamentos. |
| **RNF_011** | Disponibilidade  | Média      | O sistema deve permanecer disponível durante os períodos de utilização definidos pela organização, permitindo o acesso às informações e funcionalidades necessárias à operação.          |
| **RNF_012** | Manutenibilidade | Média      | O sistema deve possuir estrutura organizada e modular, facilitando a manutenção, correção de falhas e inclusão de novas funcionalidades.                                                 |
| **RNF_013** | Manutenibilidade | Média      | O sistema deve permitir a evolução das regras relacionadas aos treinamentos obrigatórios sem exigir alterações desnecessárias em funcionalidades não relacionadas.                       |
| **RNF_014** | Escalabilidade   | Média      | O sistema deve permitir o crescimento da quantidade de empresas, colaboradores, treinamentos e certificados cadastrados sem comprometer sua operação normal.                             |
| **RNF_015** | Compatibilidade  | Média      | O sistema deve permitir sua utilização nos principais navegadores web utilizados pelos usuários da organização.                                                                          |

## Observações

* Os requisitos relacionados à segurança devem considerar diferentes perfis e permissões de acesso às funcionalidades do sistema.
* A integridade dos dados deve ser garantida tanto pela aplicação quanto pelas regras definidas no banco de dados.
* O histórico dos treinamentos deve ser preservado para possibilitar consultas e comprovação das realizações anteriores.
* A validade dos treinamentos é determinada a partir das regras definidas para cada curso e das datas registradas nas realizações dos treinamentos.
* O certificado representa o documento comprobatório da realização do treinamento e não é responsável por determinar sua validade.
* Os requisitos de desempenho e disponibilidade devem ser posteriormente associados a métricas mensuráveis quando forem definidos os critérios de infraestrutura e implantação.
* O mecanismo de backup deve considerar a necessidade de recuperação dos dados em caso de falha ou perda de informações.

## Evoluções previstas

Alguns requisitos podem receber critérios mais específicos durante a evolução do projeto, especialmente aqueles relacionados a desempenho, disponibilidade, segurança e infraestrutura.

Possíveis evoluções incluem:

* Definição de tempo máximo de resposta para consultas.
* Definição de percentual mínimo de disponibilidade.
* Política de retenção e periodicidade dos backups.
* Recuperação automatizada de dados.
* Registro detalhado de auditoria.
* Autenticação com mecanismos adicionais de segurança.
* Notificações e alertas automáticos.
* Monitoramento da aplicação e da infraestrutura.
* Adequação para novos ambientes de implantação.
