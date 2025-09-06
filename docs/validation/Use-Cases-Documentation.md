# Casos de Uso Detalhados
## Business OS Integrado no Notion

**Versão:** 1.0  
**Data:** 06 de Setembro de 2025  
**Status:** Em Validação

---

## 1. Casos de Uso - Gestão de Clientes

### UC001: Cadastrar Novo Cliente
**Ator Principal:** Account Manager  
**Objetivo:** Registrar novo cliente qualificado no sistema  
**Pré-condições:** Lead foi qualificado tecnicamente  

**Fluxo Principal:**
1. Account Manager acessa base "Clientes"
2. Clica em "Novo Cliente"
3. Preenche dados obrigatórios:
   - Nome da Empresa
   - Fase da Jornada: "Pré-venda"
   - Data de Início
4. Define equipe técnica responsável
5. Adiciona produtos/serviços de interesse
6. Salva registro
7. Sistema notifica equipe alocada

**Fluxos Alternativos:**
- **3a.** Se dados incompletos: Sistema exibe erros de validação
- **4a.** Se equipe indisponível: Sistema sugere alternativas
- **6a.** Se erro ao salvar: Sistema mantém dados e exibe mensagem

**Pós-condições:**
- Cliente registrado na fase "Pré-venda"
- Equipe notificada
- Atividades iniciais criadas automaticamente

### UC002: Mover Cliente Entre Fases
**Ator Principal:** Account Manager / Project Manager  
**Objetivo:** Atualizar fase da jornada do cliente  
**Pré-condições:** Cliente existe no sistema  

**Fluxo Principal:**
1. Usuário acessa Dashboard Pipeline
2. Localiza card do cliente
3. Arrasta card para nova coluna de fase
4. Sistema confirma mudança
5. **Se movendo para "Implantação":**
   - Sistema auto-cria projeto de onboarding
   - Aplica template padrão
   - Aloca equipe baseada em competências
6. **Se movendo para "Ongoing CS":**
   - Sistema cria atividades recorrentes
   - Designa CS Manager
   - Agenda primeiro Health Check
7. Sistema atualiza histórico

**Critérios de Aceite:**
- Movimento deve ser fluido (drag & drop)
- Automações devem executar em < 5 segundos
- Notificações enviadas para stakeholders relevantes

## 2. Casos de Uso - Gestão de Projetos

### UC003: Criar Projeto de Implantação
**Ator Principal:** Sistema (Automação)  
**Ator Secundário:** Project Manager  
**Objetivo:** Auto-criar projeto quando cliente move para implantação  

**Fluxo Principal:**
1. **Trigger:** Cliente movido para "Implantação"
2. Sistema consulta template de onboarding
3. Cria novo registro na base "Projetos"
4. Define propriedades:
   - Nome: "Implantação - [Nome Cliente]"
   - Status: "Planejamento"
   - Cliente: Vincula automaticamente
   - Prazo: +30 dias da data atual
5. Analisa produtos contratados
6. Identifica competências necessárias
7. Consulta mapa de competências
8. Aloca equipe disponível com skills adequados
9. Define líder do projeto (maior senioridade)
10. Notifica equipe alocada
11. Cria atividades iniciais do projeto

**Regras de Negócio:**
- Projeto deve ter pelo menos 1 colaborador
- Líder deve ter competência "Avançada" em pelo menos 2 ferramentas
- Prazo padrão: 30 dias (ajustável)

### UC004: Alocar Equipe para Projeto
**Ator Principal:** Project Manager  
**Objetivo:** Definir equipe ideal para execução do projeto  

**Fluxo Principal:**
1. PM acessa projeto criado
2. Analisa escopo e produtos contratados
3. Identifica competências necessárias
4. Acessa Dashboard de Talentos
5. Filtra por ferramenta necessária
6. Filtra por nível de proficiência
7. Verifica disponibilidade dos colaboradores
8. Seleciona equipe ideal
9. Vincula colaboradores ao projeto
10. Define papéis e responsabilidades
11. Comunica alocação para a equipe

**Fluxos Alternativos:**
- **7a.** Se nenhum colaborador disponível:
  - Sistema sugere realocação de outros projetos
  - Ou sugere contratação externa
  - Ou sugere ajuste de prazo
- **8a.** Se competência não disponível:
  - Escalar para liderança
  - Buscar recursos externos
  - Replanejar escopo

## 3. Casos de Uso - Customer Success

### UC005: Executar Health Check
**Ator Principal:** CS Manager  
**Objetivo:** Avaliar saúde da conta do cliente  

**Fluxo Principal:**
1. CS Manager recebe notificação de Health Check agendado
2. Acessa registro do cliente
3. Revisa histórico de atividades
4. Prepara agenda da reunião
5. Executa reunião com cliente
6. Avalia indicadores:
   - Utilização da solução
   - Satisfação da equipe
   - Resultados obtidos
   - Desafios enfrentados
7. Registra resultado na atividade
8. Define status da conta:
   - 🟢 Saudável
   - 🟡 Atenção
   - 🔴 Risco
9. **Se status "Atenção" ou "Risco":**
   - Cria plano de ação
   - Define atividades corretivas
   - Agenda follow-ups
10. Agenda próximo Health Check

**Critérios de Aceite:**
- Health Check deve ser executado conforme cadência definida
- Status da conta deve ser visível no dashboard
- Planos de ação devem ter responsáveis e prazos

### UC006: Identificar Oportunidade de Expansão
**Ator Principal:** CS Manager  
**Objetivo:** Detectar potencial para venda adicional  

**Fluxo Principal:**
1. Durante atividade de CS, manager identifica necessidade
2. Documenta oportunidade na atividade
3. Avalia fit com catálogo de produtos
4. Estima valor da oportunidade
5. Cria registro de oportunidade
6. Notifica equipe comercial
7. Agenda reunião de discovery
8. **Se oportunidade aprovada pelo cliente:**
   - Cria novo projeto
   - Retorna cliente para fase "Implantação"
   - Inicia novo ciclo de entrega

## 4. Casos de Uso - Gestão de Competências

### UC007: Atualizar Competências de Colaborador
**Ator Principal:** RH / Colaborador  
**Objetivo:** Manter mapa de competências atualizado  

**Fluxo Principal:**
1. Ator acessa perfil do colaborador
2. Navega para seção "Competências"
3. **Para nova competência:**
   - Seleciona ferramenta da lista oficial
   - Define nível de proficiência
   - Adiciona data de certificação (se houver)
   - Inclui observações relevantes
4. **Para competência existente:**
   - Atualiza nível de proficiência
   - Adiciona nova certificação
   - Atualiza observações
5. Salva alterações
6. Sistema atualiza dashboard de talentos
7. Recalcula disponibilidade para novos projetos

**Regras de Negócio:**
- Apenas ferramentas da lista oficial podem ser adicionadas
- Níveis: Básico → Intermediário → Avançado
- Histórico de mudanças deve ser mantido

### UC008: Buscar Colaborador por Competência
**Ator Principal:** Project Manager  
**Objetivo:** Encontrar colaborador com skill específico  

**Fluxo Principal:**
1. PM acessa Dashboard de Talentos
2. Seleciona ferramenta necessária
3. Filtra por nível mínimo de proficiência
4. Sistema exibe colaboradores que atendem critério
5. PM verifica disponibilidade de cada um
6. Analisa outros projetos em andamento
7. Seleciona colaborador ideal
8. Verifica capacidade atual
9. Aloca para novo projeto

## 5. Casos de Uso - Automações

### UC009: Notificar Prazo Próximo
**Ator Principal:** Sistema (Automação)  
**Objetivo:** Alertar sobre deadlines próximos  

**Fluxo Principal:**
1. Sistema executa verificação diária (00:00)
2. Consulta todos os projetos ativos
3. Identifica projetos com prazo em 7, 3 e 1 dia
4. Para cada projeto identificado:
   - Cria notificação para líder do projeto
   - Cria notificação para equipe
   - Registra alerta no dashboard
5. **Se prazo vencido:**
   - Marca projeto como "Atrasado"
   - Notifica liderança
   - Cria task de revisão de prazo

### UC010: Sincronizar Status Entre Bases
**Ator Principal:** Sistema (Automação)  
**Objetivo:** Manter consistência de dados  

**Fluxo Principal:**
1. **Trigger:** Alteração em qualquer base
2. Sistema identifica registros relacionados
3. Verifica se alteração impacta outros registros
4. **Exemplos de sincronização:**
   - Projeto concluído → Cliente move para "Ongoing CS"
   - Colaborador indisponível → Realoca atividades
   - Cliente inativo → Arquiva projetos relacionados
5. Executa alterações em cascata
6. Registra log das alterações
7. Notifica usuários impactados

## 6. Casos de Uso - Relatórios e Analytics

### UC011: Gerar Relatório de Performance
**Ator Principal:** Liderança  
**Objetivo:** Analisar métricas de performance da operação  

**Fluxo Principal:**
1. Líder acessa seção de Relatórios
2. Seleciona período de análise
3. Define métricas de interesse:
   - Tempo médio por fase
   - Taxa de conversão entre fases
   - Utilização da equipe
   - Satisfação do cliente
4. Sistema coleta dados das bases
5. Calcula métricas solicitadas
6. Gera visualizações (gráficos/tabelas)
7. Exibe relatório interativo
8. Permite export em PDF/Excel

**Métricas Chave:**
- **Tempo médio na pré-venda:** < 7 dias
- **Taxa de conversão pré-venda → implantação:** > 80%
- **Tempo médio de implantação:** < 30 dias
- **Taxa de sucesso em implantação:** > 95%
- **NPS médio:** > 8

---

## 7. Matriz de Rastreabilidade

| Caso de Uso | Requisito Funcional | Base de Dados | Dashboard | Automação |
|-------------|-------------------|---------------|-----------|-----------|
| UC001 | Cadastrar Cliente | CLIENTES | Pipeline | ✓ |
| UC002 | Mover Fase | CLIENTES, PROJETOS | Pipeline | ✓ |
| UC003 | Criar Projeto | PROJETOS | Pipeline | ✓ |
| UC004 | Alocar Equipe | COLABORADORES, COMPETENCIAS | Talentos | - |
| UC005 | Health Check | ATIVIDADES | CS Activities | ✓ |
| UC006 | Oportunidade | CLIENTES, PROJETOS | Pipeline | - |
| UC007 | Atualizar Competência | COMPETENCIAS | Talentos | - |
| UC008 | Buscar Colaborador | COMPETENCIAS | Talentos | - |
| UC009 | Notificar Prazo | PROJETOS | Todos | ✓ |
| UC010 | Sincronizar Status | Todas | Todos | ✓ |
| UC011 | Relatório Performance | Todas | Relatórios | - |

---

**Próximos Passos:**
1. Validar casos de uso com usuários finais
2. Definir cenários de teste para cada UC
3. Priorizar desenvolvimento por criticidade
