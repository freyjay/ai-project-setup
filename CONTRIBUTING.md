# 🤝 Contributing to AI-Powered Project Setup

Thank you for your interest in contributing! This project aims to make AI-powered development workflows accessible to everyone.

## 🎯 Ways to Contribute

### 1. 🐛 Bug Reports
- Use GitHub Issues with clear reproduction steps
- Include diagnostic information (see Troubleshooting guide)
- Test on fresh installation when possible

### 2. 💡 Feature Requests  
- Describe the use case and problem it solves
- Consider backward compatibility
- Provide mockups or examples if applicable

### 3. 📝 Documentation
- Improve existing guides
- Add new examples and workflows
- Translate to other languages
- Create video tutorials

### 4. 🔧 Code Contributions
- Bug fixes
- New features
- Performance improvements
- Template enhancements

### 5. 🎨 Templates
- Create specialized project templates
- Share workflow configurations
- Document best practices

## 🚀 Getting Started

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/your-username/ai-project-setup.git
   cd ai-project-setup
   ```

2. **Install Dependencies**
   ```bash
   # Python dependencies are minimal (built-in modules)
   python3 --version  # Ensure 3.8+
   ```

3. **Setup Development Environment**
   ```bash
   # Copy app to development location
   cp -r app/* ~/Developer/project-setup-automation-dev/
   
   # Test the application
   cd ~/Developer/project-setup-automation-dev
   python3 project-setup-app.py
   ```

### Code Style

**Python Code:**
- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

**Documentation:**
- Use clear, concise language
- Include examples for complex concepts
- Test all code examples
- Update table of contents when adding sections

## 📋 Contribution Guidelines

### Pull Request Process

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Make Changes**
   - Follow existing code patterns
   - Test thoroughly on macOS
   - Update documentation as needed
   - Add examples if applicable

3. **Test Your Changes**
   ```bash
   # Test app functionality
   python3 project-setup-app.py
   
   # Test template creation
   # Create test project and verify:
   # - All files present
   # - Placeholders replaced
   # - Git initialization works
   # - Claude integration works
   ```

4. **Commit Guidelines**
   ```bash
   # Use conventional commit format
   git commit -m "feat: add multi-template support"
   git commit -m "fix: resolve SSH key permission issue"
   git commit -m "docs: improve installation guide"
   ```

5. **Submit Pull Request**
   - Clear title and description
   - Reference related issues
   - Include testing steps
   - Add screenshots for UI changes

### Code Review Process

**What We Look For:**
- ✅ Functionality works as intended
- ✅ Code follows project patterns
- ✅ Documentation is updated
- ✅ No breaking changes (unless major version)
- ✅ Appropriate error handling
- ✅ Security considerations addressed

**Review Timeline:**
- Initial response: within 48 hours
- Full review: within 1 week
- We may request changes or improvements

## 🏗️ Development Areas

### High Priority
- **Cross-platform support** (Windows, Linux)
- **Template management system** (multiple templates, easy switching)
- **Enhanced error handling** (better user feedback)
- **Automated testing** (CI/CD pipeline)

### Medium Priority
- **UI improvements** (dark mode, better styling)
- **Configuration management** (settings file, preferences)
- **Plugin system** (extensible functionality)
- **Performance optimization** (faster startup, memory usage)

### Low Priority
- **Mobile companion app** (project tracking)
- **Web interface** (browser-based version)
- **Advanced analytics** (project success metrics)
- **Team collaboration features** (shared templates, workflows)

## 🎨 Template Contributions

### Creating New Templates

1. **Base Structure**
   ```bash
   # Copy minimal template as starting point
   cp -r templates/project-template-minimal templates/project-template-your-type
   cd templates/project-template-your-type
   ```

2. **Customize Template**
   - Update file structure for your use case
   - Modify package.json, dependencies, configurations
   - Update CLAUDE.md with relevant instructions
   - Customize config/ files for your stack

3. **Documentation**
   - Add README explaining template purpose
   - Document required tools and dependencies
   - Provide usage examples
   - Include best practices

4. **Testing**
   - Test template with Project Setup app
   - Verify all placeholders work correctly
   - Ensure Claude integration functions properly
   - Test with different project names and configurations

### Template Guidelines

**File Structure:**
```
project-template-name/
├── README.md              # Template description and usage
├── CLAUDE.md              # AI workflow (keep blueprint workflow)
├── package.json.template  # Dependencies and scripts
├── src/                   # Source code structure
├── config/                # Development configurations
├── tasks/                 # Task management files
└── docs/                  # Template-specific documentation
```

**Naming Conventions:**
- Template directories: `project-template-{type}`
- Clear, descriptive names: `project-template-react-spa`, `project-template-node-api`
- Avoid abbreviations: `project-template-js-framework` not `project-template-jsfw`

## 🔍 Testing Guidelines

### Manual Testing Checklist

**Application Testing:**
- [ ] App launches without errors
- [ ] Window focuses correctly
- [ ] Git accounts load from configuration
- [ ] Project creation works with various names
- [ ] Success dialog appears and closes properly
- [ ] Git repository initialized correctly

**Template Testing:**
- [ ] All placeholder replacements work
- [ ] File structure created correctly
- [ ] CLAUDE.md contains blueprint workflow
- [ ] Claude enters plan mode automatically
- [ ] Blueprint.md template is complete

**Integration Testing:**
- [ ] Claude recognizes project setup
- [ ] Blueprint workflow executes completely
- [ ] All 5 discovery questions are asked
- [ ] Development phase begins after approval

### Automated Testing (Future)

We're working on:
- Unit tests for core functions
- Integration tests for full workflow
- Template validation scripts
- Cross-platform compatibility tests

## 🐛 Bug Report Template

When reporting bugs, please use this template:

```markdown
## Bug Description
Clear description of what went wrong.

## Steps to Reproduce
1. Step one
2. Step two
3. Step three

## Expected Behavior
What should have happened.

## Actual Behavior
What actually happened.

## Environment
- macOS version: 
- Python version: 
- App version/commit: 

## Additional Context
- Error messages
- Screenshots
- Diagnostic output
```

## 💡 Feature Request Template

```markdown
## Problem Description
What problem does this solve?

## Proposed Solution
Describe your proposed feature.

## Alternatives Considered
Other approaches you've thought about.

## Use Cases
How would this be used in real scenarios?

## Implementation Notes
Technical considerations (optional).
```

## 🏆 Recognition

### Contributors
All contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation they help create

### Special Recognition
- **Template Creators**: Featured in template gallery
- **Documentation Writers**: Credited in guides they improve
- **Bug Reporters**: Thanked in fix commit messages
- **Feature Contributors**: Named in feature announcements

## 📞 Getting Help

### Development Questions
- **GitHub Discussions**: For development questions
- **Issues**: For bugs and feature requests
- **Email**: maintainer@example.com for sensitive issues

### Real-time Chat
- **Discord**: [Coming soon]
- **Slack**: [Coming soon]

## 📜 Code of Conduct

### Our Standards
- **Be respectful** and inclusive
- **Be constructive** in feedback
- **Be patient** with new contributors
- **Be professional** in all interactions

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or inflammatory comments
- Personal attacks
- Publishing private information

### Enforcement
Issues will be addressed by maintainers. Serious violations may result in temporary or permanent bans.

## 🎉 Thank You!

Every contribution, no matter how small, helps make this project better for everyone. Whether you're:

- 🐛 Reporting a bug
- 💡 Suggesting a feature  
- 📝 Improving documentation
- 🔧 Contributing code
- 🎨 Creating templates

**You're making AI-powered development more accessible to developers everywhere!**

---

**Ready to contribute?** Check out our [good first issues](https://github.com/your-username/ai-project-setup/labels/good%20first%20issue) to get started! 🚀