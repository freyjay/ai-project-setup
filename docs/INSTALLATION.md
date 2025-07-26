# 📦 Installation Guide

Complete step-by-step installation guide for the AI-Powered Project Setup Automation.

## 🎯 Overview

This guide will walk you through setting up the entire system including:
- Project Setup application
- Git configuration
- Template setup
- AI tool integration

## 📋 Prerequisites Check

Before starting, verify you have these installed:

```bash
# Check Python version (3.8+ required)
python3 --version

# Check Git installation
git --version

# Check if you have a Developer directory
ls ~/Developer
```

## 🚀 Step-by-Step Installation

### Step 1: Download and Setup Application

1. **Download the repository**
   ```bash
   # Option A: Clone from GitHub
   git clone https://github.com/your-username/ai-project-setup.git
   cd ai-project-setup
   
   # Option B: Download ZIP and extract
   # Download from GitHub releases page
   ```

2. **Create project setup directory**
   ```bash
   mkdir -p ~/Developer/project-setup-automation
   ```

3. **Copy application files**
   ```bash
   cp app/* ~/Developer/project-setup-automation/
   cd ~/Developer/project-setup-automation
   ```

4. **Make app executable**
   ```bash
   chmod +x project-setup-app.py
   ```

### Step 2: Configure Git Accounts

1. **Create Git configuration file**
   ```bash
   cd ~/Developer/project-setup-automation
   nano git-accounts.json
   ```

2. **Add your Git account(s)**
   ```json
   {
     "your-github-username": {
       "name": "your-github-username",
       "email": "your-email@example.com",
       "ssh_host": "github-personal",
       "ssh_key": "~/.ssh/id_rsa_personal"
     },
     "work-account": {
       "name": "work-username",
       "email": "work-email@company.com",
       "ssh_host": "github-work",
       "ssh_key": "~/.ssh/id_rsa_work"
     }
   }
   ```

3. **Setup SSH configuration** (if not already done)
   ```bash
   # Edit SSH config
   nano ~/.ssh/config
   
   # Add entries for each account:
   Host github-personal
     HostName github.com
     User git
     IdentityFile ~/.ssh/id_rsa_personal
   
   Host github-work
     HostName github.com
     User git
     IdentityFile ~/.ssh/id_rsa_work
   ```

4. **Generate SSH keys** (if needed)
   ```bash
   # Generate personal key
   ssh-keygen -t rsa -b 4096 -C "your-email@example.com" -f ~/.ssh/id_rsa_personal
   
   # Generate work key (if needed)
   ssh-keygen -t rsa -b 4096 -C "work-email@company.com" -f ~/.ssh/id_rsa_work
   
   # Add public keys to GitHub accounts
   cat ~/.ssh/id_rsa_personal.pub
   # Copy output and add to GitHub SSH keys
   ```

### Step 3: Setup Project Template

1. **Copy template directory**
   ```bash
   cp -r templates/project-template-minimal ~/Developer/
   ```

2. **Verify template structure**
   ```bash
   ls -la ~/Developer/project-template-minimal
   # Should show: CLAUDE.md, README.md, config/, tasks/, etc.
   ```

3. **Customize template** (optional)
   ```bash
   cd ~/Developer/project-template-minimal
   # Edit files to match your preferences
   # Modify config/commands.md for your workflow
   # Update config/stack.md for your preferred technologies
   ```

### Step 4: Test Installation

1. **Launch the application**
   ```bash
   cd ~/Developer/project-setup-automation
   python3 project-setup-app.py
   ```

2. **Create test project**
   - Enter "test-installation" as project name
   - Select your Git account
   - Click "Create Project"
   - Verify success message appears

3. **Verify project creation**
   ```bash
   ls ~/Developer/test-installation
   # Should show complete project structure
   
   # Check if Git is initialized
   cd ~/Developer/test-installation
   git status
   ```

4. **Test Claude integration**
   ```bash
   cd ~/Developer/test-installation
   claude
   # Claude should automatically recognize blueprint workflow
   ```

5. **Clean up test project**
   ```bash
   rm -rf ~/Developer/test-installation
   ```

### Step 5: Install AI Tools (Optional but Recommended)

1. **Install Claude Code**
   ```bash
   # Follow instructions at: https://claude.ai/code
   # Or use curl installer (check official docs)
   ```

2. **Install Cursor**
   ```bash
   # Download from: https://cursor.sh/
   # Or use Homebrew:
   brew install cursor
   ```

3. **Verify AI tools**
   ```bash
   # Test Claude Code
   claude --version
   
   # Test Cursor (if installed via CLI)
   cursor --version
   ```

## ⚙️ Advanced Configuration

### Custom Application Settings

Edit `project-setup-app.py` for customization:

```python
# Custom window size (current: 400x408)
self.root.geometry("450x450")  # Make it larger

# Custom default directory
self.developer_dir = "/path/to/your/projects"

# Custom template location
self.template_dir = "/path/to/your/custom/template"
```

### Environment Variables

Optional environment setup:

```bash
# Add to ~/.zshrc or ~/.bash_profile
export PROJECT_SETUP_DIR="$HOME/Developer/project-setup-automation"
export PROJECT_TEMPLATE_DIR="$HOME/Developer/project-template-minimal"

# Create alias for easy launching
alias project-setup="cd $PROJECT_SETUP_DIR && python3 project-setup-app.py"
```

### Dock Integration (macOS)

Create desktop application:

1. **Create app bundle**
   ```bash
   mkdir -p ~/Applications/ProjectSetup.app/Contents/MacOS
   mkdir -p ~/Applications/ProjectSetup.app/Contents/Resources
   ```

2. **Create launcher script**
   ```bash
   cat > ~/Applications/ProjectSetup.app/Contents/MacOS/ProjectSetup << 'EOF'
   #!/bin/bash
   cd ~/Developer/project-setup-automation
   python3 project-setup-app.py
   EOF
   
   chmod +x ~/Applications/ProjectSetup.app/Contents/MacOS/ProjectSetup
   ```

3. **Create Info.plist**
   ```bash
   cat > ~/Applications/ProjectSetup.app/Contents/Info.plist << 'EOF'
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>CFBundleExecutable</key>
       <string>ProjectSetup</string>
       <key>CFBundleIdentifier</key>
       <string>com.yourname.projectsetup</string>
       <key>CFBundleName</key>
       <string>Project Setup</string>
       <key>CFBundleVersion</key>
       <string>1.0</string>
   </dict>
   </plist>
   EOF
   ```

## 🔍 Verification Checklist

After installation, verify everything works:

- [ ] Application launches without errors
- [ ] Git accounts appear in dropdown
- [ ] Can create test project successfully
- [ ] Project has proper file structure
- [ ] Git repository is initialized correctly
- [ ] Claude recognizes blueprint workflow
- [ ] CLAUDE.md contains workflow instructions
- [ ] Template files have correct placeholders replaced

## 🚨 Common Installation Issues

### Permission Denied Errors
```bash
# Fix file permissions
chmod +x ~/Developer/project-setup-automation/project-setup-app.py
chmod -R 755 ~/Developer/project-template-minimal/
```

### Python Not Found
```bash
# Check if Python 3 is installed
which python3

# Install Python 3 if missing (using Homebrew)
brew install python@3.11
```

### Git SSH Issues
```bash
# Test SSH connection
ssh -T git@github.com

# If fails, check SSH key is added to ssh-agent
ssh-add ~/.ssh/id_rsa_personal
```

### Template Not Found
```bash
# Verify template directory exists and has content
ls -la ~/Developer/project-template-minimal/

# Re-copy template if missing
cp -r templates/project-template-minimal ~/Developer/
```

## 🔄 Updating

To update to a new version:

```bash
# Backup current setup
cp -r ~/Developer/project-setup-automation ~/Developer/project-setup-automation.backup

# Download new version
git pull origin main  # If cloned from Git
# Or download new ZIP file

# Copy new files
cp app/* ~/Developer/project-setup-automation/

# Preserve your git-accounts.json file
# Update template if needed
```

## ✅ Installation Complete!

You're now ready to use the AI-Powered Project Setup system!

**Next steps:**
1. Read the [Usage Guide](USAGE.md)
2. Check out [Best Practices](BEST_PRACTICES.md)
3. Create your first real project
4. Explore advanced features

**Need help?** Check the [Troubleshooting Guide](TROUBLESHOOTING.md) or open an issue on GitHub.