# NeoEdit

**NeoEdit** is a powerful, feature-rich text editor built with Python and Tkinter. It combines essential text editing capabilities with advanced features like encryption, PDF export, and find/replace functionality—all within an intuitive graphical interface.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-GPL_v3-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

## ✨ Features:

### 📝 Core Text Editing:
- **New File**: Create new documents with a single click
- **Open File**: Support for .txt, .py, and all file types
- **Save/Save As**: Quick save with keyboard shortcuts
- **Cut/Copy/Paste**: Standard clipboard operations
- **Undo/Redo**: Full history support with Ctrl+Z and Ctrl+Y

### 🔧 Advanced Tools:
- **Encryption/Decryption**: Secure your text using Base64 encoding
- **Export to PDF**: Convert your documents to PDF format instantly
- **Find and Replace**: Search and replace text throughout your document
- **Status Bar**: Real-time feedback on all operations

### ⌨️ Keyboard Shortcuts:
| Shortcut | Action |
|----------|--------|
| `Ctrl + N` | New File |
| `Ctrl + O` | Open File |
| `Ctrl + S` | Save File |
| `Ctrl + Shift + S` | Save As |
| `Ctrl + Q` | Exit |
| `Ctrl + X` | Cut |
| `Ctrl + C` | Copy |
| `Ctrl + V` | Paste |
| `Ctrl + Z` | Undo |
| `Ctrl + Y` | Redo |
| `Ctrl + F` | Find/Replace |

## 🚀 Installation:

### Prerequisites:
- Python 3.7 or higher
- pip (Python package installer)

### Required Dependencies:

Install the required Python packages:

```bash
pip install fpdf
```

**Note**: `tkinter` comes pre-installed with most Python distributions. If you encounter issues, install it using:

**On Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**On Fedora:**
```bash
sudo dnf install python3-tkinter
```

**On macOS:**
Tkinter is included with Python from python.org

## 📦 Quick Start:

1. **Clone the repository:**
```bash
git clone https://github.com/Nullkernel/NeoEdit.git
cd NeoEdit
```

2. **Install dependencies:**
```bash
pip install fpdf
```

3. **Run NeoEdit:**
```bash
python NeoEdit.py
```

## 💻 Usage:

### Basic Operations:
1. **Creating a New File**: Click `File > New` or press `Ctrl+N`
2. **Opening Files**: Click `File > Open` or press `Ctrl+O` to browse and select a file
3. **Saving Work**: Click `File > Save` or press `Ctrl+S`

### Advanced Features:

#### Encryption/Decryption:
1. Write or paste your text in the editor
2. Go to `Tools > Encrypt` to encode your text
3. Use `Tools > Decrypt` to decode encrypted text

#### Export to PDF:
1. Create or open your document
2. Go to `File > Export as PDF`
3. Choose the save location and filename

#### Find and Replace:
1. Press `Ctrl+F` or go to `Edit > Find/Replace`
2. Enter the text to find and the replacement text
3. Click "Replace" to replace all instances

## 🛠️ Development:

### Project Structure:
```
NeoEdit/
│
├── NeoEdit.py          # Main application file
├── README.md           # Project documentation
└── LICENSE            # License file
```

### Building from Source:
```bash
# Clone the repository
git clone https://github.com/Nullkernel/NeoEdit.git

# Navigate to directory
cd NeoEdit

# Install dependencies
pip install fpdf

# Run the application
python NeoEdit.py
```

## 🎯 Roadmap:

Future enhancements planned for NeoEdit:

- [ ] Syntax highlighting for multiple programming languages
- [ ] Dark mode/Theme customization
- [ ] Line numbers
- [ ] Auto-save functionality
- [ ] Multiple file tabs
- [ ] Enhanced encryption with password protection
- [ ] Word count and statistics
- [ ] Search highlighting
- [ ] Regular expression support in Find/Replace
- [ ] Plugin system for extensibility

## 🤝 Contributing:

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows Python best practices and includes appropriate comments.

## 📝 License:

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author:

**Amal Bijoy**
- GitHub: [@Nullkernel](https://github.com/Nullkernel)

## 🙏 Acknowledgments:

- Built with [Python](https://www.python.org/) and [Tkinter](https://docs.python.org/3/library/tkinter.html)
- PDF generation powered by [FPDF](https://pyfpdf.readthedocs.io/)
- Inspired by classic text editors and modern development tools

## 📧 Contact:

For questions, suggestions, or issues, please open an issue on GitHub or contact [amalbijoy2007@gmail.com](mailto:amalbijoy2007@gmail.com)

---

⭐ If you find NeoEdit useful, please consider giving it a star on GitHub!
