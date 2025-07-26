# 🔄 Example Workflows & Best Practices

Real-world examples of how to use the AI-Powered Project Setup system effectively.

## 🏢 Multi-Account Git Management

### Scenario: Freelance Developer

You work on personal projects, client work, and contribute to open source.

**Git Accounts Configuration:**
```json
{
  "personal": {
    "name": "john-doe",
    "email": "john@personal.com",
    "ssh_host": "github-personal",
    "ssh_key": "~/.ssh/id_rsa_personal"
  },
  "freelance": {
    "name": "johndoe-dev",
    "email": "john@freelance.com", 
    "ssh_host": "github-freelance",
    "ssh_key": "~/.ssh/id_rsa_freelance"
  },
  "client-acme": {
    "name": "john-contractor",
    "email": "john@acmecorp.com",
    "ssh_host": "github-acme",
    "ssh_key": "~/.ssh/id_rsa_acme"
  },
  "opensource": {
    "name": "johndoe",
    "email": "john@gmail.com",
    "ssh_host": "github.com",
    "ssh_key": "~/.ssh/id_rsa"
  }
}
```

**SSH Configuration (~/.ssh/config):**
```
# Personal projects
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_personal

# Freelance business
Host github-freelance  
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_freelance

# Client work
Host github-acme
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_acme

# Open source (default)
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa
```

**Usage Pattern:**
- **Personal Projects** → Select "personal" account
- **Client Deliverables** → Select "client-acme" account  
- **Freelance Portfolio** → Select "freelance" account
- **Open Source Contributions** → Select "opensource" account

### Scenario: Enterprise Developer

You work for a company with multiple teams and client projects.

**Git Accounts Configuration:**
```json
{
  "company-main": {
    "name": "jane-smith",
    "email": "jane.smith@company.com",
    "ssh_host": "github-company",
    "ssh_key": "~/.ssh/id_rsa_company"
  },
  "company-client-a": {
    "name": "jane-smith-contractor",
    "email": "contractor@clienta.com",
    "ssh_host": "github-clienta", 
    "ssh_key": "~/.ssh/id_rsa_clienta"
  },
  "company-internal": {
    "name": "jane.smith",
    "email": "jane.smith@company.com",
    "ssh_host": "gitlab-internal",
    "ssh_key": "~/.ssh/id_rsa_internal"
  },
  "personal": {
    "name": "jane-dev",
    "email": "jane@personal.com",
    "ssh_host": "github-personal", 
    "ssh_key": "~/.ssh/id_rsa_personal"
  }
}
```

**Project Organization:**
```
~/Developer/
├── company/
│   ├── main-product/      # company-main account
│   ├── client-a-project/  # company-client-a account
│   └── internal-tools/    # company-internal account  
└── personal/
    ├── side-project/      # personal account
    └── learning-react/    # personal account
```

## 🎯 Project Type Examples

### Example 1: E-commerce Platform

**Blueprint Discovery Session:**

**Q1: Project Type**
- **Decision:** E-commerce Platform
- **Reasoning:** Need full shopping cart, payment processing, inventory management

**Q2: Core Features**
- **Primary:**
  - Product catalog with search/filter
  - Shopping cart and checkout
  - User authentication and profiles
  - Payment processing (Stripe)
  - Order management
- **Secondary:**
  - Admin dashboard
  - Inventory tracking
  - Email notifications
  - Reviews and ratings
- **MVP:**
  - Product listing
  - Basic cart functionality
  - Simple checkout process

**Q3: Users & Problems**
- **Target Users:** Small business owners selling physical products
- **Pain Points:** Complex existing solutions, high fees, poor user experience
- **Value Proposition:** Simple, affordable e-commerce with great UX

**Q4: Technical Architecture**
- **Frontend:** React with TypeScript
- **Backend:** Node.js with Express
- **Database:** PostgreSQL
- **Authentication:** JWT with refresh tokens
- **Payments:** Stripe API
- **Hosting:** Vercel (frontend), Railway (backend)

**Q5: Scope & Timeline**
- **Type:** MVP for client project
- **Timeline:** 8 weeks
- **Success Criteria:** Process orders, handle payments, admin can manage products

**Generated Project Structure:**
```
ecommerce-platform/
├── CLAUDE.md                    # AI workflow
├── tasks/
│   ├── blueprint.md            # Complete project vision
│   └── todo.md                # Development roadmap
├── frontend/
│   ├── src/components/
│   ├── src/pages/
│   └── package.json
├── backend/
│   ├── src/routes/
│   ├── src/models/
│   └── package.json
└── docs/
    ├── api.md
    └── deployment.md
```

### Example 2: Personal Portfolio

**Blueprint Discovery Session:**

**Q1: Project Type**
- **Decision:** Portfolio/Personal Site
- **Reasoning:** Showcase development skills and projects

**Q2: Core Features**
- **Primary:**
  - Project showcase
  - About me section
  - Contact form
  - Blog (optional)
- **MVP:**
  - Landing page
  - Projects section
  - Contact information

**Q3: Users & Problems**
- **Target Users:** Potential employers, clients, collaborators
- **Pain Points:** Need to see my work and skills quickly
- **Value Proposition:** Clean, fast showcase of abilities

**Q4: Technical Architecture**
- **Frontend:** Next.js with TypeScript
- **Styling:** Tailwind CSS
- **Content:** Markdown files
- **Hosting:** Vercel
- **Analytics:** Google Analytics

**Q5: Scope & Timeline**
- **Type:** Personal project
- **Timeline:** 2 weeks
- **Success Criteria:** Professional appearance, fast loading, mobile responsive

### Example 3: Internal Business Tool

**Blueprint Discovery Session:**

**Q1: Project Type**
- **Decision:** Business Application  
- **Reasoning:** Internal team needs project management and reporting

**Q2: Core Features**
- **Primary:**
  - Project tracking
  - Team collaboration
  - Time tracking
  - Reporting dashboard
- **MVP:**
  - Basic project creation
  - Task assignment
  - Simple time logging

**Q3: Users & Problems**
- **Target Users:** Internal development team (8 people)
- **Pain Points:** Scattered tools, no central visibility, manual reporting
- **Value Proposition:** Unified tool for project visibility and reporting

**Q4: Technical Architecture**
- **Frontend:** Vue.js 3 with Composition API
- **Backend:** Python FastAPI
- **Database:** PostgreSQL
- **Authentication:** Company SSO integration
- **Hosting:** Company AWS account

**Q5: Scope & Timeline**
- **Type:** Internal MVP, iterate based on feedback
- **Timeline:** 6 weeks initial, ongoing improvements
- **Success Criteria:** Team adopts tool, reduces reporting overhead by 50%

## 🔄 Development Workflow Patterns

### Pattern 1: Rapid Prototyping

**Use Case:** Validating ideas quickly

**Workflow:**
1. **Quick Setup** (2 minutes)
   ```bash
   # Launch app, create "idea-validation-app"
   # Select personal Git account
   ```

2. **Focused Blueprint** (10 minutes)
   ```
   - Type: Tool/Utility
   - Features: Core functionality only
   - Users: Early adopters/testers
   - Tech: Fastest to implement
   - Scope: Prove concept in 1 week
   ```

3. **MVP Development** (1 week)
   - Build only core feature
   - Minimal styling
   - Focus on functionality

4. **Validation** 
   - User testing
   - Feedback collection
   - Decision: continue or pivot

### Pattern 2: Client Project

**Use Case:** Delivering professional projects

**Workflow:**
1. **Requirements Gathering**
   - Client consultation
   - Detailed feature discussion
   - Technical constraints review

2. **Collaborative Blueprint**
   ```bash
   # Create project with client account
   # Include client in blueprint review
   # Document all decisions with reasoning
   ```

3. **Phased Development**
   - Phase 1: Core MVP
   - Phase 2: Enhanced features  
   - Phase 3: Polish and optimization

4. **Client Handoff**
   - Documentation transfer
   - Training session
   - Support transition

### Pattern 3: Learning Project

**Use Case:** Exploring new technologies

**Workflow:**
1. **Technology-Focused Creation**
   ```bash
   # Project name: "learning-nextjs-13"
   # Personal account
   ```

2. **Experiment-Oriented Blueprint**
   ```
   - Type: Learning/Experimental
   - Features: Test specific capabilities
   - Users: Self (learning goals)
   - Tech: New technology to explore
   - Scope: Complete tutorial, build sample app
   ```

3. **Iterative Learning**
   - Small experiments
   - Document learnings
   - Build progressively complex features

### Pattern 4: Open Source Contribution

**Use Case:** Contributing to existing projects

**Workflow:**
1. **Fork-Based Setup**
   ```bash
   # Project name: "opensource-contribution-fixes"
   # Use opensource Git account
   ```

2. **Contribution-Focused Blueprint**
   ```
   - Type: Bug fixes/Feature additions
   - Features: Specific issues from GitHub
   - Users: Existing project users
   - Tech: Match existing project stack
   - Scope: Specific issues, follow project guidelines
   ```

## 🏗️ Template Customization Examples

### Custom React Template

**Directory Structure:**
```
project-template-react/
├── CLAUDE.md
├── README.md
├── package.json.template
├── tsconfig.json
├── tailwind.config.js
├── src/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   └── utils/
├── public/
└── docs/
```

**package.json.template:**
```json
{
  "name": "[PROJECT_NAME]",
  "description": "[PROJECT_DESCRIPTION]",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "test": "vitest",
    "lint": "eslint src/"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.8.0"
  },
  "devDependencies": {
    "vite": "^4.0.0",
    "@vitejs/plugin-react": "^3.0.0",
    "typescript": "^4.9.0",
    "tailwindcss": "^3.2.0"
  }
}
```

### API Template

**Directory Structure:**
```
project-template-api/
├── CLAUDE.md
├── README.md
├── package.json.template
├── src/
│   ├── routes/
│   ├── models/
│   ├── middleware/
│   ├── services/
│   └── utils/
├── tests/
├── docs/
└── config/
```

**Includes:**
- Express.js setup
- Database configuration options
- Authentication middleware
- API documentation structure
- Testing framework setup

## 📊 Success Metrics & KPIs

### Project Creation Metrics
- **Setup Time:** < 5 minutes from idea to first code
- **Blueprint Completion:** 100% of projects have complete blueprints
- **Technical Decision Documentation:** All choices have recorded reasoning

### Development Efficiency  
- **Reduced Scope Creep:** Clear vision prevents feature drift
- **Faster Onboarding:** New team members understand project quickly
- **Better Planning:** Issues identified early in blueprint phase

### Quality Indicators
- **Project Success Rate:** Higher completion rate for planned projects
- **Client Satisfaction:** Better alignment between expectations and delivery
- **Code Quality:** Consistent architecture decisions

## 🎯 Advanced Use Cases

### Multi-Service Architecture

**Scenario:** Building microservices application

**Approach:**
1. **Create Related Projects**
   ```
   my-app-auth-service
   my-app-user-service  
   my-app-payment-service
   my-app-frontend
   my-app-admin-dashboard
   ```

2. **Consistent Architecture**
   - Use same Git account
   - Similar technical stack
   - Shared coding standards
   - Unified documentation approach

3. **Service Communication**
   - Document API contracts in each blueprint
   - Plan integration points
   - Define shared data models

### Team Onboarding

**Scenario:** New developer joining team

**Process:**
1. **Share Template Standards**
   - Team-specific templates
   - Coding conventions
   - Git workflow patterns

2. **Guided First Project**
   - Pair on blueprint session
   - Review technical decisions
   - Demonstrate workflow tools

3. **Independent Creation**
   - Solo project setup
   - Review and feedback
   - Iterative improvement

---

**These workflows demonstrate the flexibility and power of combining automated setup with AI-driven planning!** 🚀