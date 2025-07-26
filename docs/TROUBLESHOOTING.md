# 🔧 Troubleshooting Guide

Solutions for common issues with the AI-Powered Project Setup system.

## 🚨 Common Issues & Solutions

### Application Launch Issues

#### Issue: Python not found
```
python3: command not found
```

**Solutions:**
```bash
# Check if Python 3 is installed
which python3

# Install Python 3 via Homebrew
brew install python@3.11

# Or use official installer from python.org
# Download from: https://www.python.org/downloads/macos/

# Verify installation
python3 --version
```

#### Issue: Permission denied when running app
```
Permission denied: ./project-setup-app.py
```

**Solutions:**
```bash
# Make file executable
chmod +x ~/Developer/project-setup-automation/project-setup-app.py

# Alternative: run with python3 directly
python3 ~/Developer/project-setup-automation/project-setup-app.py

# Fix directory permissions if needed
chmod 755 ~/Developer/project-setup-automation/
```

#### Issue: tkinter module not found
```
ModuleNotFoundError: No module named 'tkinter'
```

**Solutions:**
```bash
# On macOS, tkinter is usually included with Python
# Reinstall Python to ensure tkinter is included
brew reinstall python@3.11

# Or install python-tk specifically
brew install python-tk

# Verify tkinter works
python3 -c "import tkinter; print('tkinter working')"
```

### GUI Issues

#### Issue: Window doesn't come to front
The application launches but stays behind Terminal.

**Solutions:**
- **Built-in fix:** The app includes automatic focus handling
- **Manual workaround:** Click on the app icon in Dock
- **Check system preferences:** System Preferences > Dock & Menu Bar > "Prefer tabs when opening documents" set to "Manual"

#### Issue: Cursor not in project name field
Project name field doesn't have focus on launch.

**Solutions:**
```python
# This is already implemented in the app, but if issues persist:
# 1. Check if any other apps are stealing focus
# 2. Disable app nap for Python:
# System Preferences > Battery > App Nap (disable for Python)

# 3. Alternative launch method:
open -a Terminal ~/Developer/project-setup-automation/project-setup-app.py
```

#### Issue: App window too small/large
The window size doesn't fit your screen or preferences.

**Solutions:**
```python
# Edit project-setup-app.py, line ~19:
# Change from:
self.root.geometry("400x408")

# To your preferred size:
self.root.geometry("500x500")  # width x height
```

### Git Configuration Issues

#### Issue: Git accounts not loading
Dropdown is empty or shows "No accounts found".

**Solutions:**
```bash
# Check if git-accounts.json exists
ls ~/Developer/project-setup-automation/git-accounts.json

# Verify JSON format is valid
python3 -c "import json; print(json.load(open('git-accounts.json')))"

# Create default configuration if missing
cat > git-accounts.json << 'EOF'
{
  "default": {
    "name": "your-username",
    "email": "your-email@example.com",
    "ssh_host": "github.com",
    "ssh_key": "~/.ssh/id_rsa"
  }
}
EOF
```

#### Issue: SSH authentication fails
```
Permission denied (publickey)
```

**Solutions:**
```bash
# Test SSH connection
ssh -T git@github.com

# Check if SSH key exists
ls ~/.ssh/

# Generate new SSH key if needed
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"

# Add key to SSH agent
ssh-add ~/.ssh/id_rsa

# Add public key to GitHub
cat ~/.ssh/id_rsa.pub
# Copy output and add to GitHub Settings > SSH Keys
```

#### Issue: Wrong Git account used
Project created with incorrect Git identity.

**Solutions:**
```bash
# Check current Git config in project
cd ~/Developer/your-project
git config user.name
git config user.email

# Fix Git config manually
git config user.name "correct-username"
git config user.email "correct-email@example.com"

# Update remote if needed
git remote set-url origin git@correct-host:username/repo.git
```

### Template Issues

#### Issue: Template not found
```
Template directory not found: ~/Developer/project-template-minimal
```

**Solutions:**
```bash
# Check if template exists
ls ~/Developer/project-template-minimal/

# Copy template from repository
cp -r path/to/downloaded/templates/project-template-minimal ~/Developer/

# Verify template structure
ls ~/Developer/project-template-minimal/
# Should show: CLAUDE.md, README.md, config/, tasks/, etc.

# Fix permissions if needed
chmod -R 755 ~/Developer/project-template-minimal/
```

#### Issue: Placeholders not replaced
Created project still shows `[PROJECT_NAME]` in files.

**Solutions:**
```bash
# Check if sed command works
echo "[PROJECT_NAME]" | sed 's/\[PROJECT_NAME\]/test-project/g'

# Manual replacement if needed
cd ~/Developer/your-project
find . -name "*.md" -exec sed -i '' 's/\[PROJECT_NAME\]/your-project/g' {} \;
find . -name "*.md" -exec sed -i '' 's/\[PROJECT_DESCRIPTION\]/your description/g' {} \;
```

#### Issue: Missing files in created project
Project created but missing expected files or directories.

**Solutions:**
```bash
# Verify template completeness
ls -la ~/Developer/project-template-minimal/

# Re-copy template files
cd ~/Developer/project-template-minimal
cp -r * ~/Developer/your-project/

# Check for hidden files
ls -la ~/Developer/project-template-minimal/
cp .* ~/Developer/your-project/ 2>/dev/null || true
```

### Claude AI Integration Issues

#### Issue: Claude doesn't recognize blueprint workflow
Claude starts normally without entering plan mode.

**Solutions:**
```bash
# Check if CLAUDE.md exists in project
ls ~/Developer/your-project/CLAUDE.md

# Verify CLAUDE.md contains blueprint workflow
grep "BLUEPRINT WORKFLOW" ~/Developer/your-project/CLAUDE.md

# Re-copy enhanced CLAUDE.md if needed
cp ~/Developer/project-template-minimal/CLAUDE.md ~/Developer/your-project/

# Restart Claude session
claude --restart
```

#### Issue: Blueprint workflow incomplete
Claude enters plan mode but doesn't ask all 5 questions.

**Solutions:**
```bash
# Check tasks/blueprint.md exists
ls ~/Developer/your-project/tasks/blueprint.md

# Verify blueprint template is complete
grep "5 Key Discovery Questions" ~/Developer/your-project/tasks/blueprint.md

# Use workflow commands manually
"lets go back to plan mode and deeply understand what we are building"
```

#### Issue: Plan mode doesn't exit
Claude stays in plan mode even after blueprint completion.

**Solutions:**
- Manually approve the plan when Claude presents it
- Use command: "exit plan mode and start development"
- Check that all "TO BE DETERMINED" placeholders are filled in blueprint.md

### Project Creation Issues

#### Issue: Project already exists error
```
Project 'my-project' already exists!
```

**Solutions:**
```bash
# Check if directory exists
ls ~/Developer/my-project

# Remove existing directory if safe to do so
rm -rf ~/Developer/my-project

# Or choose a different project name
```

#### Issue: Directory permission errors
```
Permission denied: cannot create directory
```

**Solutions:**
```bash
# Check Developer directory permissions
ls -ld ~/Developer/

# Create Developer directory if missing
mkdir -p ~/Developer
chmod 755 ~/Developer

# Fix ownership if needed
sudo chown -R $(whoami) ~/Developer
```

#### Issue: Git initialization fails
Project created but Git repository not initialized.

**Solutions:**
```bash
# Navigate to project and initialize manually
cd ~/Developer/your-project
git init
git config user.name "your-username"
git config user.email "your-email@example.com"
git remote add origin git@github.com:username/repo.git
git add .
git commit -m "Initial commit"
```

## 🔍 Diagnostic Commands

### System Health Check
```bash
# Check all prerequisites
echo "=== System Check ==="
python3 --version
git --version
ls ~/Developer/ | head -5
ls ~/Developer/project-setup-automation/
ls ~/Developer/project-template-minimal/

echo "=== Git Configuration ==="
git config --global user.name
git config --global user.email

echo "=== SSH Keys ==="
ls ~/.ssh/id_rsa* 2>/dev/null || echo "No SSH keys found"

echo "=== Claude Installation ==="
which claude || echo "Claude not found in PATH"
```

### Application Diagnostics
```bash
# Test Python imports
python3 -c "
import tkinter
import json
import subprocess
import os
import shutil
print('All imports successful')
"

# Test Git accounts file
python3 -c "
import json
try:
    with open('git-accounts.json', 'r') as f:
        accounts = json.load(f)
    print(f'Found {len(accounts)} Git accounts')
    for name in accounts.keys():
        print(f'  - {name}')
except Exception as e:
    print(f'Error reading git-accounts.json: {e}')
"
```

### Template Validation
```bash
# Check template structure
echo "=== Template Structure ==="
ls -la ~/Developer/project-template-minimal/

echo "=== Required Files ==="
for file in CLAUDE.md README.md tasks/blueprint.md tasks/todo.md config/commands.md; do
    if [ -f ~/Developer/project-template-minimal/$file ]; then
        echo "✅ $file"
    else
        echo "❌ $file (missing)"
    fi
done

echo "=== Blueprint Workflow Check ==="
grep -q "BLUEPRINT WORKFLOW" ~/Developer/project-template-minimal/CLAUDE.md && echo "✅ Blueprint workflow found" || echo "❌ Blueprint workflow missing"
```

## 🆘 Getting Help

### Log Collection
When reporting issues, include these logs:

```bash
# Create diagnostic report
echo "=== AI Project Setup Diagnostics ===" > diagnostic_report.txt
echo "Date: $(date)" >> diagnostic_report.txt
echo "macOS Version: $(sw_vers -productVersion)" >> diagnostic_report.txt
echo "Python Version: $(python3 --version)" >> diagnostic_report.txt
echo "" >> diagnostic_report.txt

# Add system info
echo "=== System Info ===" >> diagnostic_report.txt
ls -la ~/Developer/ >> diagnostic_report.txt
echo "" >> diagnostic_report.txt

# Add error details
echo "=== Error Details ===" >> diagnostic_report.txt
echo "Describe your issue here" >> diagnostic_report.txt

# Share this file when seeking help
```

### Community Support
- **GitHub Issues**: Report bugs and feature requests
- **Discussions**: Ask questions and share tips
- **Discord/Slack**: Real-time community help (if available)

### Professional Support
For business use cases:
- Custom template development
- Team onboarding assistance
- Integration with enterprise tools

## 🔄 Recovery Procedures

### Complete Reset
If everything is broken and you want to start fresh:

```bash
# Backup current setup (optional)
cp -r ~/Developer/project-setup-automation ~/Desktop/project-setup-backup

# Remove and reinstall
rm -rf ~/Developer/project-setup-automation
rm -rf ~/Developer/project-template-minimal

# Re-download and install
# Follow installation guide from scratch
```

### Selective Reset
If only specific components are broken:

```bash
# Reset just the application
rm -rf ~/Developer/project-setup-automation
# Re-copy app files from repository

# Reset just the template
rm -rf ~/Developer/project-template-minimal  
# Re-copy template from repository

# Reset Git configuration
rm ~/Developer/project-setup-automation/git-accounts.json
# Reconfigure Git accounts
```

---

**Still having issues?** Open a [GitHub issue](https://github.com/your-username/ai-project-setup/issues) with your diagnostic report! 🛠️