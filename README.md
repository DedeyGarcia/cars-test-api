# Cars API

API REST simples em FastAPI para testes de frontend. Armazena dados em memória — tudo some quando a API é reiniciada.

## Como rodar

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

## Instalação

```bash
pip install -r requirements.txt
```
