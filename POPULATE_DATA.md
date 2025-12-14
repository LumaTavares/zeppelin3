# 📊 Guia: Populando o Banco de Dados

## 🎯 O que foi feito

Criei um sistema automático para popular o banco de dados com dados iniciais. As tabelas não estarão mais vazias!

## 🚀 Como funciona

### Método 1: Automático (Recomendado)
Quando você sobe o container com `docker-compose up`, o banco é automaticamente populado com:

✅ **Estágios STH** (5 estágios)
- Initial
- Managed  
- Defined
- Quantitatively Managed
- Optimizing

✅ **Fases Contínuas** (5 fases)
- Planning
- Development
- Testing
- Deployment
- Monitoring

✅ **Níveis de Adoção** (4 níveis)
- Not Adopted (0%)
- Partially Adopted (25%)
- Mostly Adopted (75%)
- Fully Adopted (100%)

✅ **Organização Padrão**
- Default Organization

## 📝 Arquivos criados/modificados

| Arquivo | Descrição |
|---------|-----------|
| `src/apps/core/management/commands/populate_data.py` | Comando Django que popula os dados |
| `entrypoint.sh` | Atualizado para executar o populate_data |
| `populate_data.sh` | Script bash alternativo |

## 🔧 Como usar

### Opção 1: Subir tudo do zero
```bash
docker-compose down -v
docker-compose up --build
```

### Opção 2: Apenas popular novamente (sem reconstruir)
```bash
docker exec zeppelin python manage.py populate_data
```

### Opção 3: Fazer dentro do container
```bash
docker exec -it zeppelin bash
python manage.py populate_data
```

## 📊 Verificar dados

Dentro do container:
```bash
docker exec zeppelin python manage.py shell
```

Depois no Python shell:
```python
from sth.models import Stage
Stage.objects.all()  # Ver todos os estágios

from questionnaire.models import AdoptedLevel
AdoptedLevel.objects.all()  # Ver todos os níveis
```

## 🎨 Estender com mais dados

Edite o arquivo `src/apps/core/management/commands/populate_data.py` para adicionar:
- Mais estágios
- Mais processos
- Dados de exemplo de empregados
- Dados de questionários
- Etc.

Exemplo para adicionar mais dados:
```python
# Em populate_data.py, adicione no método handle():

self.stdout.write(self.style.WARNING('➤ Criando CSE Processes...'))
processes = [
    {'name': 'Continuous Planning', 'description': 'Planning processes'},
    {'name': 'Continuous Development', 'description': 'Development processes'},
]

from cseframework.models import Process
for proc_data in processes:
    proc, created = Process.objects.get_or_create(**proc_data)
    status = '✓ Criado' if created else '→ Existente'
    self.stdout.write(f'  {status}: {proc.name}')
```

## 🛑 Se algo quebrar

Se as migrações não executarem corretamente:

```bash
# Resetar o banco e tentar novamente
docker-compose down -v
docker volume rm zeppelin_postgres_data
docker-compose up --build
```

## ✅ Status

Pronto! Agora suas tabelas sobem **com dados iniciais** 🎉
