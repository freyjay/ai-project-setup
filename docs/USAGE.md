# 🎯 Usage Guide

Complete guide for using the AI-Powered Project Setup system effectively.

## 🚀 Quick Start Workflow

### The 30-Second Project Creation

1. **Launch app**: `python3 project-setup-app.py`
2. **Type project name** (cursor auto-focuses)
3. **Select Git account** from dropdown
4. **Click "Create Project"**
5. **Done!** ✅ Project ready with AI workflow

## 🎬 Step-by-Step Walkthrough

### Phase 1: Project Creation

#### 1. Launch the Application
```bash
cd ~/Developer/project-setup-automation
python3 project-setup-app.py
```

**What happens:**
- GUI window opens with focus on project name field
- Available Git accounts loaded from configuration
- Ready for immediate typing

#### 2. Enter Project Details
- **Project Name**: Type your project name (e.g., "my-awesome-app")
  - Use lowercase, hyphens for spaces
  - No special characters or spaces
  - Will become your directory name

- **Git Account**: Select from dropdown
  - Shows all configured accounts
  - Displays account info (name, email, SSH host)

#### 3. Create Project
- **Click "Create Project"** or press Enter
- **Success dialog** appears with next steps
- **Both windows close** automatically (GUI + Terminal remain as designed)

### Phase 2: AI Blueprint Discovery

#### 4. Open in Claude Code
```bash
cd ~/Developer/your-project-name
claude
```

**What happens automatically:**
- Claude reads `CLAUDE.md` with blueprint workflow
- **Enters plan mode automatically**
- Displays blueprint discovery checklist
- Ready to guide you through 5 key questions

#### 5. Complete Project Discovery

Claude will systematically ask:

**Question 1: Project Type**
```
What type of web application are we building?
Options: Portfolio, Business App, E-commerce, CMS, Social Platform, Tool/Utility, Other
```

**Question 2: Core Features**
```
What are the core features you envision?
- List primary functionality
- Categorize as Primary/Secondary/MVP
```

**Question 3: Users & Problems**
```
Who are the users and what problems does this solve?
- Target audience definition
- Pain points addressed
- Value proposition
```

**Question 4: Technical Architecture**
```
Technical preferences:
- Frontend: React, Vue, vanilla JS, server-rendered?
- Database: SQLite, PostgreSQL, MongoDB, none?
- Authentication: Simple, OAuth, JWT, none?
- APIs: REST, GraphQL, third-party integrations?
```

**Question 5: Scope & Timeline**
```
Scope and timeline:
- Learning project, MVP, or full application?
- Expected timeline
- Success criteria
```

#### 6. Blueprint Documentation

Claude will:
- **Create `tasks/blueprint.md`** with all decisions
- **Update project overview** with findings
- **Define technical architecture**
- **Identify MVP features**
- **Present plan for approval**

#### 7. Development Phase

Only after approval:
- **Exit plan mode**
- **Create development todos**
- **Begin implementation**
- **Follow systematic development process**

## 🎨 Advanced Usage

### Creating Multiple Projects

**Batch Creation Workflow:**
1. Create related projects with consistent naming
2. Use similar technical stacks for efficiency
3. Share components between projects

Example for a multi-service application:
```
my-app-frontend
my-app-backend
my-app-mobile
my-app-admin
```

### Template Customization

**Modify Default Template:**
```bash
cd ~/Developer/project-template-minimal

# Add your preferred tools
echo "vite" >> package.json.template
echo "tailwindcss" >> package.json.template

# Update default configurations
nano config/commands.md  # Add your build commands
nano config/stack.md     # Update tech stack preferences
```

**Create Specialized Templates:**
```bash
# Copy base template
cp -r project-template-minimal project-template-react
cp -r project-template-minimal project-template-node-api

# Customize each for specific use cases
cd project-template-react
# Add React-specific configurations

cd project-template-node-api  
# Add API-specific structure
```

### Git Workflow Integration

**Multiple Account Management:**
```json
{
  "personal": {
    "name": "personal-username",
    "email": "personal@example.com",
    "ssh_host": "github-personal",
    "ssh_key": "~/.ssh/id_rsa_personal"
  },
  "work": {
    "name": "work-username", 
    "email": "work@company.com",
    "ssh_host": "github-work",
    "ssh_key": "~/.ssh/id_rsa_work"
  },
  "client": {
    "name": "client-username",
    "email": "contractor@client.com", 
    "ssh_host": "github-client",
    "ssh_key": "~/.ssh/id_rsa_client"
  }
}
```

## 💡 Tips & Tricks

### 🚀 Productivity Tips

**1. Use Keyboard Shortcuts**
- Enter key creates project (no mouse needed)
- Tab to navigate between fields
- Arrow keys in Git account dropdown

**2. Naming Conventions**
```bash
# Good project names
my-portfolio-site
e-commerce-platform
task-management-app
client-dashboard

# Avoid
My Portfolio Site  # (spaces)
e_commerce_platform  # (underscores, preference)
TaskMgmt  # (unclear abbreviations)
```

**3. Quick Launch Setup**
```bash
# Add alias to ~/.zshrc
alias newproject="cd ~/Developer/project-setup-automation && python3 project-setup-app.py"

# Usage
newproject
```

**4. Template Preparation**
```bash
# Pre-configure your most-used settings in template
cd ~/Developer/project-template-minimal/config

# Update commands.md with your typical workflow
# Update stack.md with your preferred technologies
# Add any standard dependencies or configurations
```

### 🤖 AI Workflow Tips

**1. Effective Blueprint Sessions**
- **Be specific**: "User authentication with OAuth" vs "login stuff"
- **Think long-term**: Consider scaling and maintenance
- **Document decisions**: Why you chose specific technologies

**2. Blueprint Quality Indicators**
```bash
# Check blueprint completeness
grep "TO BE DETERMINED" tasks/blueprint.md  # Should be empty
grep "\[.*\]" tasks/blueprint.md           # Should be minimal placeholders
```

**3. Claude Interaction Best Practices**
- **Answer questions thoroughly** during discovery
- **Ask for clarification** when requirements are unclear
- **Reference the blueprint** throughout development
- **Update blueprint** when requirements change

**4. Development Phase Commands**
```bash
# Re-enter blueprint mode anytime
"lets go back to plan mode and deeply understand what we are building"

# Review project vision
cat tasks/blueprint.md

# Check current status
cat tasks/todo.md
```

### 🔧 Customization Tips

**1. Window Preferences**
```python
# In project-setup-app.py, modify:
self.root.geometry("450x500")  # Larger window
self.root.resizable(True, True)  # Allow resizing
```

**2. Default Selections**
```python
# Auto-select first Git account
if self.git_accounts:
    self.git_combo.set(list(self.git_accounts.keys())[0])
```

**3. Custom Success Messages**
```python
# Modify success message in create_project()
messagebox.showinfo("Success", 
    f"🎉 {project_name} is ready!\n\n"
    f"📁 Location: {project_path}\n\n"
    f"⚡ Next: cd {project_name} && claude")
```

### 📁 Organization Tips

**1. Project Grouping**
```bash
# Organize projects by type/client
~/Developer/
├── personal/
│   ├── my-portfolio/
│   └── side-project/
├── work/
│   ├── company-dashboard/
│   └── internal-tool/
└── clients/
    ├── client-a-website/
    └── client-b-app/
```

**2. Template Organization**
```bash
# Multiple templates for different needs
~/Developer/
├── project-template-minimal/     # Basic template
├── project-template-react/       # React applications  
├── project-template-api/         # Backend APIs
├── project-template-mobile/      # Mobile apps
└── project-template-fullstack/   # Complete stack
```

## 🔄 Workflow Patterns

### Pattern 1: Rapid Prototyping
1. **Quick project creation** (under 1 minute)
2. **Focused blueprint** (10-15 minutes max)
3. **MVP identification** (what to build first)
4. **Immediate development** start

### Pattern 2: Client Projects
1. **Detailed discovery session** with client input
2. **Comprehensive blueprint** with stakeholder approval
3. **Milestone-based development** following blueprint
4. **Documentation handoff** using generated docs

### Pattern 3: Learning Projects
1. **Technology-focused** project creation
2. **Experiment-oriented** blueprint
3. **Iterative development** with frequent blueprint updates
4. **Knowledge documentation** in project files

### Pattern 4: Team Projects
1. **Collaborative blueprint** session
2. **Shared vision** documented in blueprint.md
3. **Role assignment** based on technical decisions
4. **Consistent development** following standards

## 📊 Success Metrics

Track your project success with these indicators:

**Project Creation Efficiency:**
- Time from idea to first code: < 20 minutes
- Blueprint completion rate: 100%
- Setup issues: Minimal

**Project Quality:**
- Clear vision documentation: Always
- Technical decision rationale: Documented
- MVP definition: Clear and achievable

**Development Velocity:**
- Faster initial setup
- Reduced scope creep
- Better planning leads to faster execution

## 🎯 Next Steps

After mastering basic usage:

1. **Explore Advanced Features**
   - Custom templates
   - Multiple Git accounts
   - Workflow automation

2. **Integrate with Your Tools**
   - IDE configurations
   - CI/CD pipelines
   - Deployment workflows

3. **Share with Your Team**
   - Team template standards
   - Shared blueprint processes
   - Collaborative development workflows

4. **Contribute Back**
   - Share useful templates
   - Suggest improvements
   - Create tutorials

---

**Ready to create amazing projects with AI-powered planning!** 🚀