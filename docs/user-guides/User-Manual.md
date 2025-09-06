# Manual do Usuário
## Business OS Integrado no Notion

**Versão:** 1.0  
**Data:** 06 de Setembro de 2025  
**Status:** Em Validação  
**Público-Alvo:** Toda a equipe

---

## 🚀 Guia de Início Rápido

### Primeiro Acesso
1. **Acesse o workspace**: [Business OS Workspace](# "Link será fornecido")
2. **Faça login** com sua conta corporativa
3. **Complete seu perfil** na base Colaboradores
4. **Explore os dashboards** principais

### Navegação Principal
```
📊 DASHBOARDS          📋 BASES DE DADOS
├── Pipeline           ├── Clientes
├── Talentos           ├── Projetos  
├── Projetos           ├── Colaboradores
└── Atividades CS      ├── Competências
                       └── Atividades
```

---

## 👥 Por Função - Guias Específicos

## 📈 Account Manager

### Gerenciar Pipeline de Clientes

#### ✅ **Cadastrar Novo Cliente**
1. Acesse **Dashboard Pipeline**
2. Clique **[+ Novo Cliente]**
3. Preencha campos obrigatórios:
   ```
   📝 Nome da Empresa: [Nome completo]
   📊 Fase: Pré-venda
   👥 Equipe Responsável: [Selecionar da lista]
   💰 Valor Contrato: [Se conhecido]
   📅 Data Início: [Data do primeiro contato]
   ```
4. **Salvar** - Cliente aparece na coluna Pré-venda

#### 🔄 **Mover Cliente Entre Fases**
1. Localize o **card do cliente** no pipeline
2. **Arraste** para a nova coluna:
   - **Pré-venda** → **Implantação**: Auto-cria projeto
   - **Implantação** → **Ongoing CS**: Auto-cria atividades CS
3. **Confirme** a mudança quando solicitado

#### 📊 **Acompanhar Métricas**
- **Tempo na fase**: Visível no card do cliente
- **Conversão**: Relatório semanal automático
- **Pipeline value**: Total por coluna

### Integração com Hubspot
- **Sincronização automática**: Dados fluem bidirecionalmente
- **Status mapping**: Fases Notion ↔ Stages Hubspot
- **Conflitos**: Notion prevalece (source of truth)

---

## 🎯 Project Manager

### Gestão de Projetos

#### ⚡ **Projeto Auto-Criado**
Quando cliente move para "Implantação":
1. **Projeto criado automaticamente**
2. **Equipe sugerida** baseada em competências
3. **Template aplicado** conforme produtos contratados
4. **Você é notificado** para revisar e ajustar

#### 👥 **Alocar Equipe Manualmente**
1. Acesse **Dashboard de Talentos**
2. **Filtre por competência** necessária:
   ```
   🔍 Ferramenta: AWS
   ⭐ Nível: Avançado
   📊 Status: Disponível
   ```
3. **Visualize colaboradores** que atendem critério
4. **Arraste colaborador** para o projeto
5. **Defina papel** (Líder, Membro, Consultor)

#### 📅 **Acompanhar Timeline**
1. Acesse **Dashboard Projetos (Timeline)**
2. **Visualize** todos os projetos cronologicamente
3. **Identifique** conflitos de recursos
4. **Ajuste prazos** conforme necessário

#### ⚠️ **Gerenciar Alertas**
- **🔴 Vermelho**: Projeto atrasado
- **🟡 Amarelo**: Prazo em 7 dias
- **🟢 Verde**: No prazo
- **⏸️ Cinza**: Pausado/Bloqueado

### Relatórios de Projeto
```
📊 Métricas Disponíveis:
├── Projetos por status
├── Utilização da equipe
├── Tempo médio por fase
├── Taxa de sucesso
└── Previsão de entregas
```

---

## 💚 Customer Success Manager

### Gestão de Atividades CS

#### 🔄 **Atividades Recorrentes**
Quando projeto é concluído:
1. **Atividades CS criadas automaticamente**:
   - Health Check (mensal)
   - Reunião de acompanhamento (quinzenal)
   - Check-in rápido (semanal)
2. **Você é designado** como responsável
3. **Calendário sincronizado** automaticamente

#### 📋 **Executar Health Check**
1. Acesse **Dashboard Atividades CS**
2. Localize **Health Check agendado**
3. **Prepare-se** revisando:
   - Histórico do cliente
   - Atividades recentes
   - Métricas de uso
4. **Execute a reunião**
5. **Registre resultado**:
   ```
   🟢 Saudável: Cliente satisfeito, usando bem
   🟡 Atenção: Alguns pontos de melhoria
   🔴 Risco: Problemas sérios, ação necessária
   ```
6. **Crie ações** se necessário

#### 🎯 **Identificar Oportunidades**
Durante atividades CS:
1. **Documente necessidades** do cliente
2. **Avalie fit** com nosso catálogo
3. **Registre oportunidade**:
   ```
   💡 Tipo: Expansão de serviços
   💰 Valor estimado: R$ XX.XXX
   📅 Timeline: Próximos 3 meses
   🎯 Produtos: [Lista de produtos]
   ```
4. **Notifique equipe comercial**

### Dashboard CS
```
📊 Visão Geral:
├── 🟢 Clientes saudáveis: XX
├── 🟡 Clientes atenção: XX  
├── 🔴 Clientes risco: XX
├── 📅 Atividades hoje: XX
└── 💡 Oportunidades: XX
```

---

## 👤 RH / Gestão de Pessoas

### Gestão de Colaboradores

#### ✏️ **Atualizar Perfil Colaborador**
1. Acesse **Base Colaboradores**
2. **Localize** o colaborador
3. **Atualize informações**:
   ```
   👤 Dados Básicos:
   ├── Nome completo
   ├── Email corporativo
   ├── Cargo atual
   ├── Foto do perfil
   └── Senioridade
   
   📊 Status:
   ├── Disponível
   ├── Ocupado  
   ├── Férias
   └── Licença
   ```

#### 🛠️ **Gerenciar Competências**
1. **Acesse perfil** do colaborador
2. **Adicione competência**:
   ```
   🔧 Ferramenta: [Selecionar das 12 oficiais]
   ⭐ Nível: Básico | Intermediário | Avançado
   📅 Certificação: [Data se houver]
   📝 Observações: [Contexto adicional]
   ```
3. **Salve** - Dashboard Talentos atualiza automaticamente

#### 📊 **Relatórios RH**
- **Mapa de competências**: Gaps e fortalezas
- **Utilização da equipe**: Quem está sobrecarregado
- **Desenvolvimento**: Necessidades de treinamento
- **Alocação**: Histórico de projetos por pessoa

### Dashboard de Talentos
```
🎯 Competências por Ferramenta:
├── AWS: 8 pessoas (3 avançado, 3 intermediário, 2 básico)
├── Notion: 12 pessoas (5 avançado, 4 intermediário, 3 básico)
├── Hubspot: 6 pessoas (2 avançado, 2 intermediário, 2 básico)
└── [Outras ferramentas...]
```

---

## ⚙️ Funcionalidades Avançadas

### 🔍 Busca e Filtros

#### **Busca Global**
- **Atalho**: `Ctrl + K` (Windows) ou `Cmd + K` (Mac)
- **Busque por**: Nome cliente, projeto, colaborador, atividade
- **Resultados**: Links diretos para registros

#### **Filtros Avançados**
```
📊 Dashboard Pipeline:
├── Por fase da jornada
├── Por equipe responsável  
├── Por valor do contrato
├── Por data de início
└── Por produtos contratados

👥 Dashboard Talentos:
├── Por disponibilidade
├── Por competência
├── Por nível de proficiência
├── Por senioridade
└── Por projetos atuais
```

### 🔄 Automações Disponíveis

#### **Triggers Automáticos**
1. **Cliente → Implantação**: Cria projeto automaticamente
2. **Projeto concluído**: Move cliente para CS + cria atividades
3. **Prazo próximo**: Notifica responsáveis (7, 3, 1 dia)
4. **Dados incompletos**: Lembra responsável diariamente

#### **Notificações**
- **Email**: Mudanças importantes
- **Slack**: Alertas urgentes (se configurado)
- **Notion**: Notificações in-app

### 📱 Uso Mobile

#### **Funcionalidades Mobile**
- ✅ Visualizar dashboards
- ✅ Atualizar status
- ✅ Adicionar comentários
- ✅ Receber notificações
- ❌ Criar novos registros (desktop recomendado)

#### **Dicas Mobile**
- **Instale o app Notion** para melhor experiência
- **Ative notificações push** para alertas importantes
- **Use modo offline** - sincroniza quando conectar

---

## 🆘 Troubleshooting

### Problemas Comuns

#### **❌ "Não consigo ver alguns clientes"**
**Causa**: Filtros ativos ou permissões
**Solução**: 
1. Verifique filtros no topo da página
2. Clique "Limpar filtros"
3. Se persistir, contate admin

#### **❌ "Automação não funcionou"**
**Causa**: Campos obrigatórios não preenchidos
**Solução**:
1. Verifique se todos os campos obrigatórios estão preenchidos
2. Aguarde 30 segundos para processamento
3. Atualize a página

#### **❌ "Dados não sincronizaram"**
**Causa**: Problema de conectividade ou API
**Solução**:
1. Verifique conexão com internet
2. Atualize a página
3. Se persistir por >5 minutos, reporte

#### **❌ "Performance lenta"**
**Causa**: Muitos filtros ou dados carregados
**Solução**:
1. Simplifique filtros
2. Use views específicas em vez de "All"
3. Feche abas desnecessárias

### 📞 Suporte

#### **Canais de Suporte**
- **🚨 Urgente**: WhatsApp Tech Lead
- **❓ Dúvidas**: Canal #business-os (Slack)
- **🐛 Bugs**: Email suporte@empresa.com
- **💡 Sugestões**: Formulário de feedback

#### **Horários de Suporte**
- **Segunda a Sexta**: 8h às 18h
- **Urgências**: 24/7 (apenas problemas críticos)
- **Tempo resposta**: <2h em horário comercial

---

## 📚 Recursos Adicionais

### 🎥 Vídeos Tutoriais
1. **Introdução ao Business OS** (5 min)
2. **Gerenciando Clientes** (8 min)
3. **Alocação de Equipe** (6 min)
4. **Customer Success** (10 min)
5. **Relatórios e Métricas** (7 min)

### 📖 Documentação Técnica
- **[Arquitetura do Sistema](../architecture/TAD-Technical-Architecture-Document.md)**
- **[Fluxos de Processo](../flows/Customer-Journey-Flowcharts.md)**
- **[Casos de Uso](../validation/Use-Cases-Documentation.md)**

### 🔗 Links Úteis
- **Workspace Principal**: [Business OS](# "Link será fornecido")
- **Templates**: [Pasta Templates](# "Link será fornecido")
- **Backup Manual**: [Export Data](# "Link será fornecido")
- **Status Page**: [System Status](# "Link será fornecido")

---

## 📋 Checklist de Onboarding

### ✅ Primeiro Dia
- [ ] Acesso ao workspace confirmado
- [ ] Perfil pessoal completado
- [ ] Competências mapeadas
- [ ] Dashboards principais explorados
- [ ] Primeiro cliente/projeto criado (teste)

### ✅ Primeira Semana
- [ ] Participou de treinamento da função
- [ ] Executou fluxo completo da sua área
- [ ] Identificou e reportou dúvidas
- [ ] Configurou notificações preferidas
- [ ] Integrou com ferramentas pessoais (calendário)

### ✅ Primeiro Mês
- [ ] Usando sistema para 100% das atividades
- [ ] Contribuiu com feedback/sugestões
- [ ] Ajudou colegas com dúvidas
- [ ] Participou de sessão de otimização
- [ ] NPS do sistema > 8

---

**💡 Dica Final**: O Business OS foi criado para tornar seu trabalho mais eficiente e transparente. Quanto mais você usar, mais valor vai extrair. Não hesite em dar feedback para melhorarmos continuamente!

**🎯 Lembre-se**: Dados atualizados = Decisões melhores = Resultados superiores
