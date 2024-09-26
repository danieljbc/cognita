from langchain.docstore.document import Document

from backend.logger import logger
from backend.modules.parsers.parser import BaseParser
from backend.settings import settings


class SourceCodeParser(BaseParser):
    """
    SourceCodeParser is a parser class for extracting text from source code files.
    """

    supported_file_extensions = [
        ".py",  # Python
        ".js",  # JavaScript
        ".ts",  # TypeScript
        ".java",  # Java
        ".c",  # C
        ".h",  # C header
        ".cpp",  # C++
        ".hpp",  # C++ header
        ".cc",  # C++ source file (alternative extension)
        ".m",  # Objective-C
        ".mm",  # Objective-C++
        ".cs",  # C#
        ".rs",  # Rust
        ".html",  # HTML
        ".htm",  # HTML (alternate extension)
        ".css",  # CSS
        ".scss",  # SASS
        ".less",  # LESS
        ".json",  # JSON
        ".xml",  # XML
        ".xhtml",  # XHTML
        ".xul",  # XUL (XML User Interface Language)
        ".xsl",  # XSLT
        ".xslt",  # XSLT (alternate)
        ".xbl",  # XML Binding Language
        ".svg",  # SVG (Scalable Vector Graphics)
        ".yml",  # YAML
        ".yaml",  # YAML (alternate extension)
        ".sh",  # Shell scripts
        ".bash",  # Bash scripts
        ".zsh",  # Zsh scripts
        ".bat",  # Batch scripts
        ".cmd",  # Windows Command script
        ".ps1",  # PowerShell scripts
        ".sql",  # SQL
        ".idl",  # Interface Definition Language (used in XPCOM)
        ".webidl",  # WebIDL (Web Interface Definition Language)
        ".properties",  # Java Properties files
        ".ini",  # INI files
        ".toml",  # TOML files
        ".cfg",  # Config files
        ".conf",  # Configuration files
        ".env",  # Environment variable files
        ".md",  # Markdown
        ".rst",  # reStructuredText
        ".tex",  # LaTeX
        ".bib",  # BibTeX
        ".jl",  # Julia
        ".cmake",  # CMake
        ".makefile",  # Makefile
        ".mk",  # Makefile (alternate)
        ".gradle",  # Gradle scripts
        ".dockerfile",  # Dockerfile
        ".vhd",  # VHDL
        ".vhdl",  # VHDL (alternate)
        ".verilog",  # Verilog
        ".asm",  # Assembly language
        ".s",  # Assembly language (alternate)
        ".rc",  # Resource files (Windows)
        ".rdata",  # R data files
        ".sav",  # SPSS data files
        ".dta",  # Stata data files
        ".tcl",  # Tcl scripts
        ".awk",  # AWK scripts
        ".sed",  # Sed scripts
        ".patch",  # Patch files
        ".diff",  # Diff files
        ".d",  # D programming language
        ".toml",  # TOML files
        ".log",  # Log files
        ".out",  # Output files
        ".ico",  # Icon files
        ".png",  # PNG image files
        ".jpg",  # JPEG image files
        ".jpeg",  # JPEG image files
        ".gif",  # GIF image files
        ".woff",  # Web Open Font Format
        ".woff2",  # Web Open Font Format 2
        ".ttf",  # TrueType Font
        ".otf",  # OpenType Font
        ".icns",  # Apple Icon Image format
        ".icns",  # Apple Icon Image format
        ".dtd",  # Document Type Definition
        ".properties",  # Java Properties files
        ".in",  # Input files for build systems
        ".mk",  # Makefiles
        ".mozbuild",  # Mozilla Build System files
        ".mozconfig",  # Mozilla Build Configuration files
        ".cfg",  # Config files
        ".prefs",  # Preference files (usually in Mozilla products)
        ".prefs.js",  # JavaScript-based preferences files
        ".whl",  # Python Wheel files
        ".ipynb",  # Jupyter Notebook
        ".eslintignore",  # ESLint ignore files
        ".eslintrc",  # ESLint configuration files
        ".prettierrc",  # Prettier configuration files
        ".gitignore",  # Git ignore files
        ".gitattributes",  # Git attributes files
        ".hgignore",  # Mercurial ignore files
        ".hgrc",  # Mercurial configuration files
        ".bazel",  # Bazel build files
        ".bzl",  # Bazel Starlark files
        ".gni",  # GN build configuration files
        ".gn",  # GN meta-build files
        ".go",  # Go
        ".groovy",  # Groovy
        ".java",  # Java
        ".jsp",  # JavaServer Pages
        ".class",  # Compiled Java class
        ".war",  # Web application archive
        ".ear",  # Enterprise application archive
        ".zip",  # ZIP archive
        ".tar",  # Tarball archive
        ".gz",  # Gzip compressed archive
        ".bz2",  # Bzip2 compressed archive
        ".7z",  # 7-Zip compressed archive
        ".rar",  # RAR archive
        ".jar",  # Java Archive
        ".apk",  # Android package file
        ".aab",  # Android App Bundle
        ".exe",  # Windows executable
        ".dll",  # Dynamic-link library
        ".so",  # Shared object
        ".dylib",  # Dynamic library (Mac)
        ".lib",  # Static library
        ".a",  # Static library
        ".ninja",  # Ninja build system files
        ".mk",  # Makefiles
        ".def",  # Module definition files
        ".vcproj",  # Visual C++ project files
        ".sln",  # Visual Studio solution
        ".vcxproj",  # Visual Studio project files
        ".jsonc",  # JSON with comments
        ".map",  # Source Map
        ".ts",  # TypeScript
        ".tsx",  # TypeScript JSX
        ".jsx",  # JavaScript JSX
    ]


    def __init__(self, *, max_chunk_size: int = 2000, **kwargs):
        """
        Initializes the SourceCodeParser object.
        """
        self.max_chunk_size = max_chunk_size

        super().__init__(**kwargs)

    async def get_chunks(self, filepath: str, metadata: dict, **kwargs):
        """
        Asynchronously extracts text from source code files and returns it in chunks.
        """
        final_texts = []
        try:
            with open(filepath, "r", errors="ignore") as f:
                if not metadata:
                    metadata = {}
                content = f.read()
                if not content:
                    return final_texts
                # Logic to split content into chunks
                chunks = [
                    content[i: i + self.max_chunk_size]
                    for i in range(0, len(content), self.max_chunk_size)
                ]
                metadata["filepath"] = filepath
                for chunk in chunks:
                    final_texts.append(Document(page_content=chunk, metadata=metadata))
            return final_texts
        except Exception as e:
            logger.exception(f"Final Exception: {e}")
            raise e
