# JSON Email Generator

A lightweight Python tool for managing and generating JSON lists of email domains from text files.

## 🌟 Features

- **Batch Processing**: Process all txt files in input directory with a single command
- **Smart Processing**: 
  - Handles multiple input formats (quoted, unquoted, mixed)
  - Automatically removes duplicates
  - Maintains alphabetically sorted lists
  - Converts domains to lowercase for consistency
- **Dual Output Formats**:
  - Regular (indented) JSON for readability
  - Minified JSON for production use
- **Zero Dependencies**: Uses only Python standard library
- **Simple CLI**: One command to process everything: `python3 src/main.py make json`

## 📋 Installation

```bash
git clone https://github.com/yourusername/json-email-generator.git
cd json-email-generator
```

No additional dependencies required! Works with Python 3.x

## 🚀 Usage

### Generate JSON files:
```bash
python3 src/main.py make json
```

This command will:
1. Read all `.txt` files from `data/input/`
2. Generate corresponding JSON files in `data/output/`
3. Create both regular and minified versions
4. Skip any files that have no changes

## 📁 File Structure

```
json-email-generator/
├── data/
│   ├── input/                # Directory containing source txt files
│   │   ├── email-list.txt   # Any domain list file
│   │   └── emailist2.txt    # Another domain list file
│   └── output/              # Directory containing generated JSON files
│       ├── email-list.json       # Regular JSON output
│       ├── email-list.min.json   # Minified JSON output
│       ├── emailist2.json       # Regular JSON output
│       └── emailist2.min.json   # Minified JSON output
└── src/
    └── main.py             # Main script for processing files
```

## 📝 Input Format

The text files in `data/input/` support multiple formats in the same file:
```
# Plain text format
domain.com

# JSON-style format
"domain.com",

# Mixed format example
allmail.net
antichef.com
"0clickemail.com",
```

## 🔍 Output Format

For each input file `example.txt`, two files are generated:

### Regular JSON (example.json):
```json
{
    "domains": [
        "0clickemail.com",
        "allmail.net",
        "antichef.com"
    ]
}
```

### Minified JSON (example.min.json):
```json
{"domains":["0clickemail.com","allmail.net","antichef.com"]}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GNU General Public License v3.0 or later - see the [LICENSE](LICENSE) file for details. This means you can:

- Use this software for any purpose
- Study how the software works and modify it
- Redistribute copies of the software
- Distribute modified versions of the software

The only requirement is that if you distribute this software or any derivative works, you must also:
1. Make the source code available
2. License it under the GNU General Public License v3.0 or later
3. Preserve the copyright notices

For more details, see the [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) license terms.

## 🙏 Acknowledgments

- Thanks to all contributors who help maintain the email domain lists
- Inspired by the need for reliable email domain validation
