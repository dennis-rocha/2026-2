# Tabela: `treinamento`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos
**Descrição:** Registra cada realização de um curso, identificando quando o treinamento ocorreu e qual colaborador foi responsável por ministrá-lo.

## Atributos

| Atributo       | Tipo de dado | Restrições         | Descrição                                                         |
| -------------- | ------------ | ------------------ | ----------------------------------------------------------------- |
| `id`           | INT          | PK, AUTO_INCREMENT | Identificador único do treinamento.                               |
| `curso_id`     | INT          | FK, NOT NULL       | Identifica o curso que está sendo realizado.                      |
| `data`         | DATE         | NOT NULL           | Data em que o treinamento foi realizado.                          |
| `professor_id` | INT          | FK, NOT NULL       | Identifica o colaborador responsável por ministrar o treinamento. |

## Regras e observações

* Cada treinamento deve estar associado a um único `curso`.
* Um `curso` pode possuir vários registros de `treinamento`.
* O `professor_id` referencia a tabela `colaborador`, pois o professor/instrutor é considerado um colaborador do sistema.
* O professor pode ser um colaborador próprio ou terceiro.
* Um treinamento pode possuir vários colaboradores participantes por meio da tabela `treinamento_colaborador`.
* A data do treinamento será utilizada como referência para o cálculo da validade da capacitação do colaborador.

## Relacionamentos

```text id="h81qz4"
CURSO
  │
  │ 1:N
  ▼
TREINAMENTO
  │
  │ N:N
  ▼
TREINAMENTO_COLABORADOR
```
