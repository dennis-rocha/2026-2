# Tabela: `certificado`

**Projeto:** SafeIndustry - Sistema de Gerenciamento de Treinamentos
**Descrição:** Armazena o certificado emitido para o colaborador como comprovação da realização do treinamento.

## Atributos

| Atributo                     | Tipo de dado | Restrições           | Descrição                                                                       |
| ---------------------------- | ------------ | -------------------- | ------------------------------------------------------------------------------- |
| `id`                         | INT          | PK, AUTO_INCREMENT   | Identificador único do certificado.                                             |
| `treinamento_colaborador_id` | INT          | FK, NOT NULL, UNIQUE | Identifica o registro de participação/conclusão ao qual o certificado pertence. |
| `arquivo`                    | VARCHAR(255) | NOT NULL             | Caminho ou referência para o arquivo digital do certificado.                    |
| `data_emissao`               | DATE         | NOT NULL             | Data em que o certificado foi emitido.                                          |

## Regras e observações

* Um registro de `treinamento_colaborador` pode possuir nenhum ou um certificado.
* Cada certificado pertence a exatamente um registro de `treinamento_colaborador`.
* `treinamento_colaborador_id` deve ser único para garantir a relação 1:0..1.
* O certificado não precisa armazenar diretamente o `curso` ou o `colaborador`, pois essas informações podem ser obtidas por meio de `treinamento_colaborador`.
* O arquivo representa o documento digital emitido como comprovação da capacitação.

## Relacionamento

```text id="m74xqk"
TREINAMENTO_COLABORADOR
           │
           │ 1:0..1
           ▼
      CERTIFICADO
```
