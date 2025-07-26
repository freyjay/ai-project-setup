# 🚀 AI-Powered Project Setup Automation

**Transform your development workflow with automated project creation and AI-driven blueprint discovery.**

This repository provides a complete solution for automated project setup with integrated Claude AI workflow that ensures every project starts with proper planning and vision.

## ✨ Features

- 🎯 **Automated Project Creation** - One-click project setup with templates
- 🤖 **AI Blueprint Discovery** - Claude automatically guides project planning
- 🎨 **Perfect UX** - Instant focus, clean interface, seamless workflow
- 🔒 **Security-First** - No unnecessary permissions, transparent operation
- 📁 **Template System** - Reusable project structures with best practices
- ⚡ **Developer Optimized** - Built for Claude Code + Cursor integration

## 🎥 Demo

*Coming soon: YouTube walkthrough and implementation guide*

## 📋 Prerequisites

### Required Tools
- **macOS** (tested on macOS 14+)
- **Python 3.8+** (usually pre-installed on macOS)
- **Git** (for version control)
- **Terminal** or **iTerm2**

### Recommended AI Tools
- **[Claude Code](https://claude.ai/code)** - AI coding assistant
- **[Cursor](https://cursor.sh/)** - AI-powered code editor
- **VS Code** or other preferred editor (fallback)

### Development Environment
- **Homebrew** (recommended for package management)
- **Node.js & npm** (for web projects)
- **Your preferred development stack**

## 🚀 Quick Start

### 1. Download the Application

```bash
# Clone this repository
git clone https://github.com/freyjay/ai-project-setup.git
cd ai-project-setup

# Copy the app to your desired location
cp -r app/* ~/Developer/project-setup-automation/
```

### 2. Setup Git Configuration

Create your Git accounts configuration:

```bash
cd ~/Developer/project-setup-automation
# Configure your Git accounts (see Configuration section below)
```

### 3. Launch the App

```bash
cd ~/Developer/project-setup-automation
python3 project-setup-app.py
```

### 4. Create Your First Project

1. **Enter project name** (cursor automatically focuses here)
2. **Select Git account** from dropdown
3. **Click "Create Project"**
4. **Success!** Project created with AI workflow integrated

## ⚙️ Configuration

### Git Accounts Setup

The app uses `git-accounts.json` for Git configuration:

```json
{
  "freyjay": {
    "name": "freyjay",
    "email": "francis@freyjay.dev",
    "ssh_host": "github-personal",
    "ssh_key": "~/.ssh/id_rsa_personal"
  }
}
```

### SSH Configuration

Add to your `~/.ssh/config`:

```
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_personal
```

### Project Template Location

Default template location: `~/Developer/project-template-minimal`

## 🎯 How It Works

### The AI Blueprint Workflow

1. **Project Creation** - App creates project from template
2. **Claude Integration** - AI reads CLAUDE.md workflow instructions
3. **Plan Mode Activation** - Claude automatically enters blueprint discovery
4. **5 Key Questions** - Systematic project vision development:
   - What type of application?
   - Core features needed?
   - Target users and problems?
   - Technical architecture?
   - Scope and timeline?
5. **Documentation** - Complete blueprint.md created
6. **Development** - Only proceeds after vision approval

### Project Structure Created

```
your-new-project/
├── CLAUDE.md              # AI workflow instructions
├── WORKFLOW.md            # Complete process documentation
├── README.md              # Project overview
├── tasks/
│   ├── todo.md           # Current work tracking
│   └── blueprint.md      # Project vision (AI creates this)
├── config/
│   ├── commands.md       # Development commands
│   ├── standards.md      # Coding standards
│   ├── stack.md          # Tech stack info
│   └── environment.md    # Setup requirements
└── src/                  # Your code goes here
```

## 💡 Usage Tips & Tricks

### 🎯 Best Practices

1. **Always Complete Blueprint First**
   - Don't skip the AI discovery process
   - Answer all 5 key questions thoroughly
   - Get stakeholder approval before coding

2. **Use the Workflow Commands**
   ```bash
   # Re-enter blueprint mode anytime
   "lets go back to plan mode and deeply understand what we are building"
   
   # Create project blueprint
   "create a blueprint for our project"
   
   # Solidify vision
   "solidify our project vision"
   ```

3. **Template Customization**
   - Modify project-template-minimal for your needs
   - Add your preferred tools and configurations
   - Update placeholder values for your workflow

### ⚡ Power User Features

- **Batch Project Creation** - Create multiple related projects
- **Template Variants** - Different templates for different project types
- **Integration Hooks** - Extend with additional automation
- **Custom Commands** - Add your development workflow commands

### 🔍 Validation Commands

```bash
# Check if blueprint is complete
grep "TO BE DETERMINED" tasks/blueprint.md

# Verify all discovery questions answered
grep "\[ \]" tasks/blueprint.md

# Review project status
cat tasks/todo.md
```

## 🛠️ Customization

### Modifying the Template

1. **Edit Template Files**
   ```bash
   cd ~/Developer/project-template-minimal
   # Modify files to match your preferences
   ```

2. **Update Placeholders**
   - `[PROJECT_NAME]` - Replaced with actual project name
   - `[PROJECT_DESCRIPTION]` - Replaced with description
   - `[REPOSITORY_URL]` - Replaced with Git URL

3. **Add Your Tools**
   - Package.json configurations
   - Docker setups
   - CI/CD configurations
   - Testing frameworks

### App Customization

- **Window Size**: Modify `geometry` in `project-setup-app.py`
- **Default Paths**: Update `developer_dir` and `template_dir`
- **Git Integration**: Customize Git initialization process
- **UI Elements**: Modify tkinter interface elements

## 🔧 Troubleshooting

### Common Issues

**App doesn't focus on project name field**
- Solution: Window focus fix is built-in (auto-retry mechanism)

**Git authentication fails**
- Check SSH key configuration
- Verify Git account settings in json file
- Test SSH connection: `ssh -T git@github.com`

**Template not found**
- Verify template directory exists
- Check file permissions
- Ensure all template files are present

**Claude doesn't enter plan mode**
- Check CLAUDE.md file exists in created project
- Verify blueprint workflow section is present
- Restart Claude Code session

### Advanced Troubleshooting

**Permission Issues**
```bash
# Fix file permissions
chmod +x project-setup-app.py
chmod -R 755 project-template-minimal/
```

**Python Issues**
```bash
# Check Python version
python3 --version

# Install/update tkinter if needed
# (Usually included with Python on macOS)
```

## 🎬 Video Tutorial

*Coming in v2: Complete YouTube walkthrough covering:*
- Installation and setup
- First project creation
- AI workflow demonstration
- Advanced customization
- Tips and best practices

## 🔮 Roadmap (v2 Features)

- 🎨 **Enhanced UI** - Modern interface with dark mode
- 📊 **Project Analytics** - Track project creation and success metrics
- 🔄 **Template Manager** - Easy template switching and management
- 🌐 **Multi-Platform** - Windows and Linux support
- 🔗 **IDE Integration** - Direct integration with more editors
- 📱 **Mobile Companion** - Project tracking on mobile
- 🤖 **Advanced AI Features** - More intelligent project suggestions

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
git clone https://github.com/freyjay/ai-project-setup.git
cd ai-project-setup
# Follow installation instructions above
```

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- **Claude AI** - For the brilliant blueprint workflow concept
- **Cursor** - For AI-powered development experience
- **Anthropic** - For providing Claude capabilities
- **Open Source Community** - For inspiration and best practices

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/freyjay/ai-project-setup/issues)
- **Discussions**: [GitHub Discussions](https://github.com/freyjay/ai-project-setup/discussions)
- **Email**: francis@freyjay.dev

---

**Built with ❤️ for developers who value both automation and thoughtful planning.**

⭐ **Star this repo** if it helps your development workflow!