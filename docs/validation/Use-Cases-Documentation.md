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
8. **Se competência relacionada a PDI ativo:**
   - Atualiza progresso do PDI
   - Notifica gestor sobre evolução

**Regras de Negócio:**
- Apenas ferramentas da lista oficial podem ser adicionadas
- Níveis: Básico → Intermediário → Avançado
- Histórico de mudanças deve ser mantido
- Evolução de competência impacta avaliação de performance

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

### UC011: Monitorar Performance da Equipe
**Ator Principal:** Gestor  
**Objetivo:** Acompanhar produtividade e qualidade da equipe  

**Fluxo Principal:**
1. Gestor acessa Dashboard de Performance
2. Seleciona período de análise
3. Visualiza métricas por colaborador:
   - Atividades concluídas no prazo
   - Qualidade das entregas
   - Feedback dos clientes
4. Identifica colaboradores com performance abaixo do esperado
5. **Se necessário:** Agenda 1:1 para feedback
6. Define planos de ação individuais
7. Monitora evolução nas próximas semanas

**Regras de Negócio:**
- Métricas devem ser objetivas e mensuráveis
- Feedback deve ser construtivo e específico
- Planos de ação devem ter prazos definidos

## 5. Casos de Uso - Jornada do Colaborador

### UC012: Executar Onboarding de Novo Colaborador
**Ator Principal:** RH / Gestor  
**Objetivo:** Integrar novo colaborador de forma estruturada  

**Fluxo Principal:**
1. RH recebe confirmação de contratação
2. Sistema cria automaticamente checklist de onboarding
3. **Etapa 1 - Documentação:**
   - RH solicita documentos necessários
   - Colaborador envia via sistema
   - RH valida e aprova documentação
4. **Etapa 2 - Setup Técnico:**
   - TI cria acessos aos sistemas
   - Configura equipamentos
   - Testa conectividade
5. **Etapa 3 - Treinamentos:**
   - RH agenda treinamento institucional
   - Gestor agenda treinamento técnico
   - Colaborador completa módulos obrigatórios
6. **Etapa 4 - Mentoria:**
   - Sistema designa buddy automaticamente
   - Agenda primeira reunião
   - Define cronograma de acompanhamento
7. Sistema monitora progresso e envia lembretes
8. **Após 30 dias:** Avaliação de adaptação

**Regras de Negócio:**
- Cada etapa deve ser concluída antes da próxima
- Responsáveis recebem notificações automáticas
- Atrasos > 3 dias geram alertas para RH
- Buddy deve ser do mesmo time/área

### UC013: Conduzir Ciclo de Avaliação de Performance
**Ator Principal:** Gestor / RH  
**Objetivo:** Avaliar desempenho e definir desenvolvimento  

**Fluxo Principal:**
1. Sistema dispara início do ciclo automaticamente
2. **Auto-avaliação:**
   - Colaborador recebe formulário
   - Avalia próprio desempenho vs metas
   - Identifica pontos fortes e melhorias
3. **Avaliação do Gestor:**
   - Gestor acessa histórico do colaborador
   - Analisa entregas e feedback recebido
   - Preenche avaliação estruturada
4. **Reunião de Feedback:**
   - Sistema agenda reunião automaticamente
   - Gestor e colaborador discutem avaliações
   - Alinham expectativas e próximos passos
5. **Definição de Nota:**
   - Gestor define nota final consensual
   - Sistema registra justificativa
6. **Plano de Desenvolvimento:**
   - Identificam gaps de competência
   - Criam PDI para próximo período
   - Definem metas específicas
7. RH valida e aprova avaliação

**Regras de Negócio:**
- Ciclos trimestrais obrigatórios
- Auto-avaliação deve preceder avaliação do gestor
- Notas "Abaixo" requerem plano de melhoria
- PDI deve ter pelo menos 2 objetivos

### UC014: Gerenciar Plano de Desenvolvimento Individual (PDI)
**Ator Principal:** Colaborador / Gestor  
**Objetivo:** Estruturar e acompanhar crescimento profissional  

**Fluxo Principal:**
1. **Criação do PDI:**
   - Colaborador identifica competência a desenvolver
   - Define objetivo específico e mensurável
   - Propõe ações de desenvolvimento
   - Gestor revisa e aprova
2. **Execução:**
   - Colaborador executa ações planejadas
   - Atualiza progresso mensalmente
   - Documenta aprendizados e evidências
3. **Acompanhamento:**
   - Sistema envia lembretes automáticos
   - Gestor monitora evolução
   - Realiza check-ins regulares
4. **Avaliação Final:**
   - Colaborador apresenta resultados
   - Gestor valida competência desenvolvida
   - Sistema atualiza mapa de competências
5. **Próximos Passos:**
   - Avaliam oportunidades de aplicação
   - Definem novos objetivos se necessário

**Regras de Negócio:**
- PDI deve estar alinhado com trilha de carreira
- Progresso < 30% em 3 meses gera alerta
- Competência só é atualizada após validação
- Máximo 3 PDIs simultâneos por colaborador

### UC015: Processar Feedback 360 Graus
**Ator Principal:** RH / Colaborador  
**Objetivo:** Coletar e processar feedback multidirecional  

**Fluxo Principal:**
1. **Solicitação de Feedback:**
   - Colaborador ou gestor solicita feedback 360
   - Sistema identifica stakeholders relevantes
   - Envia convites automáticos
2. **Coleta de Feedback:**
   - Avaliadores recebem formulário estruturado
   - Preenchem feedback por categoria
   - Sistema garante anonimato quando solicitado
3. **Consolidação:**
   - Sistema compila feedbacks recebidos
   - Identifica padrões e tendências
   - Gera relatório consolidado
4. **Entrega e Discussão:**
   - RH agenda sessão de feedback
   - Apresenta resultados de forma construtiva
   - Colaborador e gestor discutem insights
5. **Plano de Ação:**
   - Definem ações baseadas no feedback
   - Criam cronograma de implementação
   - Agendam follow-up

**Regras de Negócio:**
- Mínimo 5 avaliadores para feedback válido
- Feedback confidencial apenas para RH
- Resultados ficam no histórico do colaborador
- Follow-up obrigatório em 90 dias

### UC016: Monitorar Clima Organizacional
**Ator Principal:** RH  
**Objetivo:** Acompanhar satisfação e engajamento da equipe  

**Fluxo Principal:**
1. **Pesquisa Pulse (Mensal):**
   - Sistema envia pesquisa curta automaticamente
   - Colaboradores respondem anonimamente
   - Foco em satisfação imediata
2. **Pesquisa Trimestral:**
   - Questionário mais abrangente
   - Inclui NPS interno e sugestões
   - Análise por área e cargo
3. **Análise de Resultados:**
   - Sistema gera dashboards automáticos
   - Identifica tendências e alertas
   - Compara com períodos anteriores
4. **Plano de Ação:**
   - RH identifica pontos críticos
   - Define ações de melhoria
   - Comunica resultados para liderança
5. **Acompanhamento:**
   - Monitora impacto das ações
   - Ajusta estratégias conforme necessário

**Regras de Negócio:**
- Participação mínima 80% para validade
- Resultados por área só se >5 respondentes
- Alertas automáticos para NPS <6
- Plano de ação obrigatório para scores baixos

### UC017: Executar Processo de Offboarding
**Ator Principal:** RH / Gestor  
**Objetivo:** Conduzir desligamento de forma estruturada  

**Fluxo Principal:**
1. **Comunicação de Saída:**
   - Gestor/RH registra decisão de desligamento
   - Sistema cria checklist de offboarding
   - Define responsabilidades e prazos
2. **Entrevista de Saída:**
   - RH agenda entrevista estruturada
   - Coleta feedback sobre experiência
   - Documenta motivos e sugestões
3. **Transferência de Conhecimento:**
   - Colaborador documenta processos
   - Transfere responsabilidades
   - Treina substituto quando aplicável
4. **Revogação de Acessos:**
   - TI remove acessos aos sistemas
   - Colaborador devolve equipamentos
   - Confirma segurança da informação
5. **Finalização:**
   - RH processa documentação final
   - Atualiza status no sistema
   - Arquiva informações relevantes

**Regras de Negócio:**
- Entrevista de saída obrigatória
- Revogação de acessos no último dia
- Transferência de conhecimento documentada

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
