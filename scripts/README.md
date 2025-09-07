# Scripts de População do BusinessOS Notion Platform

Este diretório contém scripts Python para automatizar a criação e população das bases de dados do BusinessOS no Notion.

## 📋 Scripts Disponíveis

### 1. `populate-colaboradores.py`
**Objetivo**: Popular a base de Colaboradores com 50 colaboradores realistas

**Funcionalidades**:
- Cria 50 colaboradores com dados realistas
- Distribui por departamentos (Executivo, Tecnologia, RH, Comercial, Operações)
- Gera emails automáticos baseados nos nomes
- Define cargos apropriados por departamento
- Calcula performance e NPS interno aleatórios
- Status distribuído realisticamente (95% ativo)

**Uso**:
```bash
python3 populate-colaboradores.py
```

### 2. `populate-atividades.py`
**Objetivo**: Popular a base de Atividades do Projeto com 30 atividades detalhadas

**Funcionalidades**:
- Cria 30 atividades específicas do projeto BusinessOS
- Organiza por 4 fases: Fundação, Integrações, Otimização, Produção
- Define responsáveis, prioridades e estimativas realistas
- Cronograma completo de 09/09 a 18/10/2025
- Categorias: Arquitetura, Database, Integração, Dashboard, etc.

**Uso**:
```bash
python3 populate-atividades.py
```

### 3. `create-additional-databases.py`
**Objetivo**: Criar bases adicionais da jornada do colaborador

**Databases Criadas**:
- **Checklist Onboarding**: Tarefas de integração por etapa
- **Avaliações Performance**: Sistema de avaliação trimestral/anual
- **Feedback 360°**: Coleta de feedback multi-fonte
- **Pesquisa Clima Organizacional**: NPS interno e satisfação

**Uso**:
```bash
python3 create-additional-databases.py
```

## ⚙️ Configuração

### Pré-requisitos
```bash
pip install requests
```

### Token do Notion
1. Acesse [Notion Integrations](https://www.notion.so/my-integrations)
2. Crie uma nova integração
3. Copie o token e substitua `ntn_****` nos scripts
4. Compartilhe as páginas/databases com a integração

### IDs das Databases
- **Colaboradores**: `267d6174-4f45-81d8-8bd3-d3c27e224e1d`
- **Atividades do Projeto**: `267d6174-4f45-8138-9b4e-c8b5b8b9b8b8`
- **Página Gestão de Pessoas**: `267d6174-4f45-8198-aba2-f0f91e396274`

## 🚀 Execução Recomendada

### Ordem de Execução:
1. **Primeiro**: `create-additional-databases.py`
2. **Segundo**: `populate-colaboradores.py`
3. **Terceiro**: `populate-atividades.py`

### Validação:
- Verificar se todas as databases foram criadas
- Confirmar se os dados foram populados corretamente
- Testar relações entre databases
- Validar permissões e acessos

## 📊 Dados Gerados

### Colaboradores (50 registros)
- **Distribuição por Departamento**:
  - Executivo: 5% (2-3 pessoas)
  - Tecnologia: 35% (17-18 pessoas)
  - RH: 15% (7-8 pessoas)
  - Comercial: 25% (12-13 pessoas)
  - Operações: 20% (10 pessoas)

### Atividades (30 registros)
- **Distribuição por Fase**:
  - Fase 1 - Fundação: 8 atividades
  - Fase 2 - Integrações: 10 atividades
  - Fase 3 - Otimização: 7 atividades
  - Fase 4 - Produção: 5 atividades

### Databases Adicionais (4 bases)
- Checklist Onboarding (6 etapas)
- Avaliações Performance (5 tipos)
- Feedback 360° (5 competências)
- Clima Organizacional (8 dimensões)

## 🔧 Troubleshooting

### Erros Comuns:
1. **Token inválido**: Verificar se o token está correto e ativo
2. **Permissões**: Confirmar se a integração tem acesso às páginas
3. **IDs incorretos**: Validar se os IDs das databases estão atualizados
4. **Rate limiting**: Aguardar alguns segundos entre execuções

### Logs:
- Todos os scripts geram logs detalhados de execução
- Contadores de sucesso/falha para monitoramento
- Mensagens específicas para cada erro

## 📈 Próximos Passos

Após executar os scripts:
1. Configurar views personalizadas nas databases
2. Criar dashboards de RH e gestão
3. Implementar automações entre bases
4. Popular dados de exemplo nas novas databases
5. Configurar relatórios executivos

## 🛡️ Segurança

- **Nunca commitar tokens** nos scripts
- Usar variáveis de ambiente em produção
- Validar permissões antes da execução
- Fazer backup antes de executar scripts de população
