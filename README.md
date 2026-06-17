# Cars API

API REST simples em FastAPI para testes de frontend. Armazena dados em memória — tudo some quando a API é reiniciada.

## Pré-requisitos

- Python 3.9 ou superior

## Primeira execução

Na primeira vez, crie um ambiente virtual (venv) e instale as dependências.

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> Caso o PowerShell bloqueie a ativação do venv, libere a execução de scripts para a sessão atual com `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` e tente novamente.

Nas próximas vezes, basta ativar o venv (`source .venv/bin/activate` ou `.venv\Scripts\Activate.ps1`) antes de rodar a API.

## Como rodar

Com o venv ativado:

```bash
fastapi dev main.py
```

A API sobe em `http://localhost:8000`. Documentação interativa disponível em `http://localhost:8000/docs`.

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/cars` | Lista todos os carros |
| GET | `/cars/{id}` | Busca um carro pelo ID |
| POST | `/cars` | Cria um novo carro |
| PUT | `/cars/{id}` | Substitui um carro por completo |
| PATCH | `/cars/{id}` | Atualiza campos específicos de um carro |
| DELETE | `/cars/{id}` | Remove um carro |

## Modelo de Carro

```json
{
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2023,
  "estado": "Novo",
  "motor": "2.0 16V",
  "combustivel": "Flex",
  "transmissao": "Automático",
  "cor": "Prata",
  "quilometragem": 0,
  "preco": 120000.00
}
```

### Valores aceitos

- **estado**: `Novo`, `Seminovo`
- **combustivel**: `Gasolina`, `Etanol`, `Flex`, `Diesel`, `Elétrico`, `Híbrido`
- **transmissao**: `Manual`, `Automático`, `CVT`

## Tipos TypeScript

Com a API rodando, gere os tipos automaticamente a partir do schema OpenAPI:

```bash
npx openapi-typescript http://localhost:8000/openapi.json -o src/types/api.ts
```
