# Matriz de Controle de Acesso - BusinessOS
**Versão:** 1.0  
**Data:** 07 de Setembro de 2025  
**Autor:** Bernardo Chassot, CVO  
**Status:** Especificação Técnica Aprovada

---

## 📋 **VISÃO GERAL**

### Objetivo
Definir níveis de acesso e permissões para informações individuais de colaboradores no BusinessOS, garantindo transparência operacional mantendo privacidade de dados sensíveis.

### Princípios de Segurança
- **Transparência Operacional:** Informações necessárias para colaboração são públicas
- **Privacidade Individual:** Dados pessoais e financeiros são restritos
- **Hierarquia de Acesso:** Permissões baseadas em função e responsabilidade
- **Compliance LGPD:** Conformidade com legislação de proteção de dados

---

## 🔐 **NÍVEIS DE ACESSO DEFINIDOS**

### **Nível 1: Colaborador Individual**
**Escopo:** Próprios dados + Informações públicas do time

```
✅ PODE ACESSAR:
- Próprio perfil completo (incluindo dados pessoais)
- Dados públicos de todos os colaboradores
- Competências e disponibilidade do time
- Projetos e atividades em que participa

❌ NÃO PODE ACESSAR:
- Dados confidenciais de outros colaboradores
- Informações salariais de terceiros
- Avaliações de performance de outros
- Dados pessoais de outros (CPF, endereço, telefone)
```

### **Nível 2: Liderança (Gestores)**
**Escopo:** Equipe direta + Dados públicos gerais

```
✅ PODE ACESSAR:
- Dados completos da própria equipe
- Avaliações de performance dos subordinados
- PDIs e planos de desenvolvimento da equipe
- Feedback 360 relacionado à sua gestão
- Dados públicos de toda a organização

❌ NÃO PODE ACESSAR:
- Dados confidenciais de outras equipes
- Informações salariais fora de sua alçada
- Avaliações de performance de outros gestores
- Dados pessoais de colaboradores de outras áreas
```

### **Nível 3: RH + CVO (Administradores)**
**Escopo:** Acesso total e irrestrito

```
✅ PODE ACESSAR:
- TODOS os dados de TODOS os colaboradores
- Todas as bases de dados do sistema
- Relatórios consolidados e análises
- Configurações de sistema e permissões
- Dados históricos e arquivos
```

---

## 📊 **MATRIZ DE INFORMAÇÕES POR NÍVEL**

### **🌐 INFORMAÇÕES PÚBLICAS (Todos os Níveis)**

| Campo | Tipo | Visibilidade | Justificativa |
|-------|------|--------------|---------------|
| Nome Completo | Title | 🌐 Público | Identificação para colaboração |
| Email Corporativo | Email | 🌐 Público | Contato profissional |
| Cargo | Select | 🌐 Público | Função e responsabilidades |
| Departamento | Select | 🌐 Público | Organização e estrutura |
| Nível Senioridade | Select | 🌐 Público | Experiência e capacidade |
| Data Admissão | Date | 🌐 Público | Tempo de casa (público) |
| Status | Select | 🌐 Público | Disponibilidade operacional |
| Disponibilidade | Select | 🌐 Público | Alocação e planejamento |
| Competências Técnicas | Relation | 🌐 Público | Expertise para projetos |
| Projetos Atuais | Relation | 🌐 Público | Alocação atual |
| Observações Profissionais | Text | 🌐 Público | Contexto de trabalho |

### **🔒 INFORMAÇÕES RESTRITAS (RH + Liderança)**

| Campo | Tipo | Visibilidade | Justificativa |
|-------|------|--------------|---------------|
| Salário | Number | 🔒 Restrito | Informação confidencial |
| CPF | Text | 🔒 Restrito | Documento pessoal |
| Telefone Pessoal | Phone | 🔒 Restrito | Contato privado |
| Endereço Completo | Text | 🔒 Restrito | Informação pessoal |
| Data Nascimento | Date | 🔒 Restrito | Dado pessoal sensível |
| Risco Turnover | Select | 🔒 Restrito | Análise estratégica |
| NPS Individual | Number | 🔒 Restrito | Satisfação pessoal |
| Avaliações Performance | Relation | 🔒 Restrito | Dados de performance |
| Feedback 360 Detalhado | Relation | 🔒 Restrito | Comentários pessoais |
| PDI Completo | Relation | 🔒 Restrito | Planos de carreira |

### **👥 INFORMAÇÕES DE EQUIPE (Gestor + RH)**

| Campo | Tipo | Visibilidade | Justificativa |
|-------|------|--------------|---------------|
| Gestor Direto | Relation | 👥 Equipe | Hierarquia organizacional |
| Metas Individuais | Text | 👥 Equipe | Gestão de performance |
| Histórico Avaliações | Relation | 👥 Equipe | Acompanhamento desenvolvimento |
| Planos Desenvolvimento | Relation | 👥 Equipe | Gestão de carreira |
| Feedback Recebido | Relation | 👥 Equipe | Acompanhamento evolução |

---

## 🛠️ **IMPLEMENTAÇÃO TÉCNICA NO NOTION**

### **Configuração de Permissões por Base**

#### **Base COLABORADORES - Configuração de Views**

```
📋 View "Equipe Completa" (Público)
├── Campos Visíveis: Nome, Email, Cargo, Departamento, Senioridade
├── Campos Visíveis: Status, Disponibilidade, Competências
├── Filtros: Status = "Ativo"
└── Permissão: Todos os membros

🔒 View "Gestão RH" (Restrito)
├── Campos Visíveis: TODOS os campos
├── Campos Sensíveis: Salário, CPF, Dados Pessoais
├── Filtros: Sem restrições
└── Permissão: Apenas RH + CVO

👥 View "Minha Equipe" (Gestores)
├── Campos Visíveis: Dados da equipe + Avaliações
├── Filtros: Gestor Direto = @Usuário Atual
└── Permissão: Gestores + RH + CVO
```

#### **Bases Restritas (Fase 2)**

```
🔒 AVALIACOES_PERFORMANCE
├── Acesso: RH + Gestor Direto + Próprio Colaborador
├── Restrição: Não pode ver avaliações de outros
└── Exceção: CVO vê todas

🔒 FEEDBACK_360
├── Acesso: RH + Destinatário do Feedback
├── Restrição: Anonimato dos avaliadores
└── Exceção: CVO vê origem dos feedbacks

🔒 PLANO_QUARTER
├── Acesso: RH + Gestor + Próprio Colaborador
├── Restrição: Planos são individuais
└── Compartilhamento: Apenas com autorização

🔒 PESQUISAS_CLIMA
├── Acesso: Apenas RH + CVO
├── Dados: Agregados e anônimos
└── Individual: Apenas para análises internas
```

---

## 📋 **CONFIGURAÇÃO DE GRUPOS DE USUÁRIOS**

### **Grupo 1: Colaboradores**
```
👤 Membros: Todos os funcionários
🔑 Permissões Base:
- Leitura: Dados públicos de todos
- Escrita: Apenas próprios dados não-sensíveis
- Relações: Pode se vincular a projetos/atividades

📊 Acesso a Bases:
✅ COLABORADORES (view pública)
✅ PROJETOS (projetos próprios)
✅ ATIVIDADES (atividades próprias)
✅ MAPA_COMPETENCIAS (próprias competências)
❌ Bases de RH (restritas)
```

### **Grupo 2: Gestores**
```
👥 Membros: Líderes de equipe, PMs, Tech Leads
🔑 Permissões Expandidas:
- Leitura: Dados da equipe + públicos gerais
- Escrita: Avaliações e feedback da equipe
- Gestão: Alocação e planejamento da equipe

📊 Acesso a Bases:
✅ COLABORADORES (view equipe)
✅ PROJETOS (projetos da equipe)
✅ ATIVIDADES (atividades da equipe)
✅ AVALIACOES_PERFORMANCE (equipe)
✅ PLANO_QUARTER (equipe)
❌ Dados financeiros e pessoais
```

### **Grupo 3: RH + CVO**
```
🔑 Membros: RH, CVO, Administradores
🔑 Permissões Totais:
- Leitura: TODOS os dados
- Escrita: TODAS as bases
- Administração: Configurações e permissões

📊 Acesso a Bases:
✅ TODAS as bases sem restrição
✅ Views administrativas
✅ Relatórios consolidados
✅ Configurações de sistema
```

---

## 🎯 **CASOS DE USO PRÁTICOS**

### **Cenário 1: Alocação de Projeto**
```
🎯 Necessidade: PM precisa alocar desenvolvedor React
👀 Pode ver: Competências técnicas, disponibilidade, senioridade
❌ Não vê: Salário, dados pessoais, avaliações detalhadas
✅ Resultado: Alocação baseada em competência e disponibilidade
```

### **Cenário 2: Avaliação de Performance**
```
🎯 Necessidade: Gestor avalia colaborador da equipe
👀 Pode ver: Histórico, metas, feedback anterior da equipe
❌ Não vê: Avaliações de outros gestores, dados salariais
✅ Resultado: Avaliação contextualizada e justa
```

### **Cenário 3: Planejamento de Carreira**
```
🎯 Necessidade: RH planeja promoções e aumentos
👀 Pode ver: TODOS os dados, performance, competências
✅ Acesso total: Salários, avaliações, potencial
✅ Resultado: Decisões estratégicas embasadas
```

---

## 🔍 **AUDITORIA E COMPLIANCE**

### **Log de Acessos**
- ✅ Registro de quem acessou quais dados
- ✅ Timestamp de todas as operações
- ✅ Identificação de acessos não autorizados
- ✅ Relatórios de compliance LGPD

### **Revisão Periódica**
- 📅 **Mensal:** Revisão de permissões ativas
- 📅 **Trimestral:** Auditoria de acessos sensíveis
- 📅 **Semestral:** Validação de grupos e níveis
- 📅 **Anual:** Revisão completa da matriz

### **Controles de Segurança**
- 🔐 **Autenticação:** Login único corporativo
- 🛡️ **Autorização:** Baseada em grupos e funções
- 📊 **Monitoramento:** Alertas de acessos suspeitos
- 🔄 **Backup:** Dados críticos protegidos

---

## 📈 **BENEFÍCIOS DA IMPLEMENTAÇÃO**

### **Para Colaboradores**
- ✅ Transparência nas competências e oportunidades
- ✅ Visibilidade de especialistas para colaboração
- ✅ Proteção de dados pessoais e sensíveis
- ✅ Clareza sobre informações públicas vs privadas

### **Para Gestores**
- ✅ Informações necessárias para gestão da equipe
- ✅ Dados para tomada de decisão de alocação
- ✅ Ferramentas para desenvolvimento de talentos
- ✅ Compliance automático com políticas

### **Para RH e Liderança**
- ✅ Visão completa para gestão estratégica
- ✅ Dados para análises de people analytics
- ✅ Controle total sobre informações sensíveis
- ✅ Compliance com LGPD e regulamentações

---

## 🚀 **CRONOGRAMA DE IMPLEMENTAÇÃO**

### **Fase 1: Configuração Base (Semana 1)**
- ✅ Estrutura de permissões básica
- ✅ Views públicas configuradas
- ✅ Grupos de usuários definidos

### **Fase 2: Bases Restritas (Semana 2-3)**
- 📅 Implementação das bases de RH
- 📅 Configuração de permissões avançadas
- 📅 Testes de acesso e segurança

### **Fase 3: Validação e Treinamento (Semana 4)**
- 📅 Testes com usuários reais
- 📅 Treinamento da equipe
- 📅 Ajustes finais e go-live

---

**Esta matriz garante o equilíbrio perfeito entre transparência operacional e proteção de dados sensíveis! 🛡️**
