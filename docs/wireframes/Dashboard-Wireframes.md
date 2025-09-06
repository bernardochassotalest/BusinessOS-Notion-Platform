# Wireframes dos Dashboards Principais
## Business OS Integrado no Notion

**Versão:** 1.0  
**Data:** 06 de Setembro de 2025  
**Status:** Em Validação

---

## 1. Dashboard Principal: Pipeline de Entrega e Sucesso do Cliente

### 1.1 Layout Geral
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🏢 Business OS - Pipeline de Clientes                    [⚙️ Config] [👤 User] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ 📊 Métricas Rápidas                                                        │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│ │ Pré-venda   │ │ Implantação │ │ Ongoing CS  │ │ Concluído   │           │
│ │     12      │ │      8      │ │     45      │ │    123      │           │
│ │ clientes    │ │ projetos    │ │ clientes    │ │ clientes    │           │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ 🔄 Pipeline Visual (Board View)                                            │
│                                                                             │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│ │ PRÉ-VENDA   │ │ IMPLANTAÇÃO │ │ ONGOING CS  │ │ CONCLUÍDO   │           │
│ │             │ │             │ │             │ │             │           │
│ │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │           │
│ │ │Cliente A│ │ │ │Cliente D│ │ │ │Cliente G│ │ │ │Cliente J│ │           │
│ │ │Tech Co  │ │ │ │Startup X│ │ │ │BigCorp  │ │ │ │OldCorp  │ │           │
│ │ │👥 3 dias│ │ │ │🚀 15 dias│ │ │ │💚 Saudável│ │ │ │✅ Q2/25│ │           │
│ │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │           │
│ │             │ │             │ │             │ │             │           │
│ │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │           │
│ │ │Cliente B│ │ │ │Cliente E│ │ │ │Cliente H│ │ │ │Cliente K│ │           │
│ │ │New Biz  │ │ │ │Scale Up │ │ │ │MidSize  │ │ │ │Archived │ │           │
│ │ │⏰ 7 dias│ │ │ │⚠️ Atraso │ │ │ │🔄 Review│ │ │ │📁 Q1/25│ │           │
│ │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │           │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Card de Cliente - Detalhamento
```
┌─────────────────────────────────┐
│ 🏢 TechCorp Solutions           │
├─────────────────────────────────┤
│ 📊 Status: Pré-venda           │
│ 👥 Equipe: João, Maria, Pedro   │
│ 💰 Valor: R$ 150.000           │
│ 📅 Início: 01/09/2025          │
│ ⏰ Próxima: Reunião Discovery   │
│                                 │
│ 🎯 Produtos:                   │
│ • Notion Setup                  │
│ • Hubspot Integration          │
│ • Team Training                │
│                                 │
│ [📝 Editar] [👁️ Detalhes]      │
└─────────────────────────────────┘
```

## 2. Dashboard de Alocação de Talentos

### 2.1 Layout Principal
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 👥 Alocação de Talentos                              [🔍 Buscar] [+ Novo]    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ 📊 Visão Geral da Equipe                                                   │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│ │ Disponível  │ │ Ocupado     │ │ Férias      │ │ Total       │           │
│ │     8       │ │     15      │ │     2       │ │     25      │           │
│ │ pessoas     │ │ pessoas     │ │ pessoas     │ │ pessoas     │           │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ 🛠️ Mapa de Competências por Ferramenta                                     │
│                                                                             │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│ │    AWS      │ │   NOTION    │ │  HUBSPOT    │ │   ZOOM      │           │
│ │             │ │             │ │             │ │             │           │
│ │ 🟢 Avançado │ │ 🟢 Avançado │ │ 🟡 Interm.  │ │ 🟢 Avançado │           │
│ │ • João S.   │ │ • Maria L.  │ │ • Pedro M.  │ │ • Ana C.    │           │
│ │ • Carlos R. │ │ • João S.   │ │ • Sofia T.  │ │ • João S.   │           │
│ │             │ │             │ │             │ │             │           │
│ │ 🟡 Interm.  │ │ 🟡 Interm.  │ │ 🔴 Básico   │ │ 🟡 Interm.  │           │
│ │ • Ana C.    │ │ • Pedro M.  │ │ • Ana C.    │ │ • Maria L.  │           │
│ │ • Sofia T.  │ │ • Carlos R. │ │ • João S.   │ │ • Pedro M.  │           │
│ │             │ │             │ │             │ │             │           │
│ │ 🔴 Básico   │ │ 🔴 Básico   │ │             │ │ 🔴 Básico   │           │
│ │ • Maria L.  │ │ • Ana C.    │ │             │ │ • Carlos R. │           │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Card de Colaborador
```
┌─────────────────────────────────┐
│ 👤 João Silva                   │
│ 📧 joao@empresa.com             │
├─────────────────────────────────┤
│ 🎯 Cargo: Tech Lead             │
│ 📊 Status: 🟢 Disponível        │
│ ⭐ Senioridade: Sênior          │
│                                 │
│ 🛠️ Competências:               │
│ • AWS (Avançado) ⭐⭐⭐         │
│ • Notion (Avançado) ⭐⭐⭐      │
│ • Zoom (Avançado) ⭐⭐⭐        │
│ • Hubspot (Básico) ⭐           │
│                                 │
│ 📅 Projetos Atuais: 0          │
│ 🎯 Capacidade: 100%             │
│                                 │
│ [📝 Editar] [📊 Histórico]      │
└─────────────────────────────────┘
```

## 3. Dashboard de Projetos (Timeline View)

### 3.1 Visão Timeline
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 📅 Timeline de Projetos                                    [📊] [📋] [📅]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│     Set 2025        Out 2025        Nov 2025        Dez 2025               │
│ ────────────────────────────────────────────────────────────────────────── │
│                                                                             │
│ TechCorp Setup      ████████████                                           │
│ 👤 João S. | 🟡 Em Andamento                                               │
│                                                                             │
│ Startup X Migration      ██████████████████                                │
│ 👤 Maria L. | 🔴 Atrasado                                                  │
│                                                                             │
│ BigCorp Integration              ████████████████████                      │
│ 👤 Pedro M. | 🟢 No Prazo                                                  │
│                                                                             │
│ Scale Up Training                        ████████                          │
│ 👤 Ana C. | 🟢 Planejamento                                                │
│                                                                             │
│ MidSize Optimization                             ██████████                 │
│ 👤 Carlos R. | ⏸️ Pausado                                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 4. Dashboard de Atividades CS

### 4.1 Layout de Atividades
```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 📋 Customer Success Activities                          [+ Nova] [🔔 Alerts] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ 📊 Status das Atividades                                                   │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                           │
│ │ A Fazer     │ │ Em Execução │ │ Concluídas  │                           │
│ │     23      │ │      8      │ │     156     │                           │
│ │ atividades  │ │ atividades  │ │ atividades  │                           │
│ └─────────────┘ └─────────────┘ └─────────────┘                           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ 🔄 Atividades por Tipo                                                     │
│                                                                             │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│ │ REUNIÃO CS  │ │ HEALTH CHECK│ │  SUPORTE    │ │ TREINAMENTO │           │
│ │             │ │             │ │             │ │             │           │
│ │ ⏰ Hoje     │ │ 📅 Semanal  │ │ 🚨 Urgente  │ │ 📚 Agendado │           │
│ │ • BigCorp   │ │ • TechCorp  │ │ • Startup X │ │ • MidSize   │           │
│ │   15:00     │ │   Qua 10:00 │ │   ASAP      │ │   Sex 14:00 │           │
│ │             │ │             │ │             │ │             │           │
│ │ ⏰ Amanhã   │ │ 📅 Mensal   │ │ 💬 Normal   │ │ 📚 Pendente │           │
│ │ • Scale Up  │ │ • BigCorp   │ │ • MidSize   │ │ • TechCorp  │           │
│ │   09:30     │ │   15/10     │ │   2 dias    │ │   A definir │           │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 5. Navegação e Menu Principal

### 5.1 Sidebar Navigation
```
┌─────────────────┐
│ 🏢 Business OS  │
├─────────────────┤
│                 │
│ 📊 DASHBOARDS   │
│ • Pipeline      │
│ • Talentos      │
│ • Projetos      │
│ • Atividades    │
│                 │
│ 📋 BASES        │
│ • Clientes      │
│ • Projetos      │
│ • Colaboradores │
│ • Competências  │
│ • Atividades    │
│                 │
│ 📈 RELATÓRIOS   │
│ • Performance   │
│ • Utilização    │
│ • Métricas      │
│                 │
│ ⚙️ CONFIGURAÇÃO │
│ • Templates     │
│ • Automações    │
│ • Usuários      │
│                 │
└─────────────────┘
```

## 6. Especificações de Interação

### 6.1 Drag & Drop
- **Pipeline**: Arrastar clientes entre fases
- **Alocação**: Arrastar colaboradores para projetos
- **Atividades**: Mover entre status (A Fazer → Fazendo → Feito)

### 6.2 Filtros e Busca
- **Filtro por Status**: Dropdown com múltipla seleção
- **Filtro por Responsável**: Busca por nome do colaborador
- **Filtro por Data**: Range picker para períodos
- **Busca Global**: Campo de texto com autocomplete

### 6.3 Actions Rápidas
- **Quick Add**: Botão + para criação rápida
- **Bulk Actions**: Seleção múltipla com ações em lote
- **Context Menu**: Clique direito para ações contextuais
- **Keyboard Shortcuts**: Atalhos para ações frequentes

---

**Próximos Passos:**
1. Validar wireframes com usuários finais
2. Definir especificações de UX detalhadas
3. Criar protótipo interativo no Notion
