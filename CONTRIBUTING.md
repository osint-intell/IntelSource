# Contributing to IntelSource

Thank you for your interest in contributing to IntelSource! We welcome contributions from developers of all skill levels.

## 🎯 How to Contribute

### Reporting Bugs
1. Check the [issues page](https://github.com/osint-intell/IntelSource/issues) to ensure the bug hasn't been reported
2. If it's new, [open a new issue](https://github.com/osint-intell/IntelSource/issues/new?template=bug_report.md)
3. Provide:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)

### Suggesting Features
1. Check [discussions](https://github.com/osint-intell/IntelSource/discussions) for similar ideas
2. [Open a new discussion](https://github.com/osint-intell/IntelSource/discussions) with your feature request
3. Explain:
   - What problem it solves
   - Why it's useful
   - Potential implementation approach

### Submitting Code

#### Setup Your Local Environment
```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/osint-intell/IntelSource.git
cd IntelSource

# 3. Add upstream remote
git remote add upstream https://github.com/osint-intell/IntelSource.git

# 4. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt
```

#### Make Your Changes
```bash
# 1. Create a feature branch
git checkout -b feature/my-feature

# 2. Make your changes
# - Write clean, readable code
# - Include docstrings and type hints
# - Add comments for complex logic
# - Keep functions small and focused

# 3. Test your changes
python3 main.py

# 4. Commit with clear messages
git commit -m "Add my feature: brief description"
git commit -m "Fix bug: description of the fix"

# 5. Push to your fork
git push origin feature/my-feature
```

#### Open a Pull Request
1. Go to the original repository on GitHub
2. Click "Pull requests" → "New Pull Request"
3. Select your branch and write a detailed description:
   - What does this PR do?
   - Why is this change needed?
   - How did you test it?
   - Any breaking changes?

4. Link related issues: `Closes #123`
5. Wait for review and feedback

## 📝 Code Standards

### Python Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for function parameters and returns
- Write docstrings for all functions and classes:
  ```python
  def my_function(target: str) -> Dict[str, Any]:
      """
      Brief description of what this function does.
      
      Args:
          target: Description of the parameter
          
      Returns:
          Description of the return value
      """
      pass
  ```

### Error Handling
- Use try/except blocks for external API calls
- Log errors with appropriate severity levels
- Provide user-friendly error messages
- Never silently fail

### Comments
- Only comment complex logic that isn't obvious
- Keep comments accurate and up-to-date
- Use clear, concise language

### Testing
- Test your changes before submitting
- Ensure existing functionality still works
- Add test cases for new features
- Test both success and error scenarios

## 🚀 Development Workflow

### Branch Naming
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

### Commit Messages
```
# Good commit message format:
# [type]: brief description

# Types: feature, fix, docs, style, refactor, test, chore

# Examples:
git commit -m "feature: add Shodan API integration"
git commit -m "fix: resolve DNS timeout issue"
git commit -m "docs: update installation instructions"
```

### Pull Request Process
1. Update documentation if needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Request review from maintainers
5. Address feedback and suggestions
6. Maintainers will merge when approved

## 📚 Documentation

When adding features, please update:
- `README.md` - Add feature to features list and usage examples
- `config.json` - Add any new configuration options
- Code docstrings - Full documentation of new functions
- Inline comments - For complex logic

## 🐛 Common Issues & Solutions

### "Import errors when testing"
```bash
# Make sure you're in the virtual environment
source venv/bin/activate  # Unix/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### "Changes aren't reflected when running"
```bash
# Make sure you're running from the IntelSource directory
cd /path/to/IntelSource
python3 main.py
```

### "My PR has conflicts"
```bash
# Update your branch with latest upstream
git fetch upstream
git rebase upstream/main
# Resolve conflicts in your editor
git add .
git rebase --continue
git push -f origin feature/my-feature
```

## 🎓 Learning Resources

- [Python Documentation](https://docs.python.org/3/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [OWASP Security Guidelines](https://owasp.org/)

## 💡 Areas We Need Help With

- 🔲 **New Collectors** - Add Shodan, Censys, or other data sources
- 🔲 **Performance** - Parallelize bulk queries
- 🔲 **Output Formats** - CSV, HTML, PDF export
- 🔲 **Testing** - Unit and integration tests
- 🔲 **Documentation** - Examples, guides, tutorials
- 🔲 **Bug Fixes** - Check open issues
- 🔲 **UI/UX** - Improve user experience

## ❓ Questions?

- 📖 Check the [README](README.md)
- 🐛 Search [existing issues](https://github.com/osint-intell/IntelSource/issues)
- 💬 Ask in [discussions](https://github.com/osint-intell/IntelSource/discussions)
- 📧 Contact maintainers on GitHub

## ✨ Thank You!

Your contributions make IntelSource better for everyone. We appreciate your time and effort! 🙏

---

**Happy Contributing!** 🚀
