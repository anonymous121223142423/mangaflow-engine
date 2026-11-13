# MangaFlow Engine

An open-source, lightweight CLI and metadata automation toolkit designed for managing digital manga archives, optimizing image pipelines, and organizing local reading libraries.

## Features

- **Smart Archive Parser:** Automatically validates and extracts metadata from `.cbz` and `.zip` comic archives.
- **Image Optimization Pipeline:** Batch-processes high-resolution pages to reduce storage footprint without losing visual clarity.
- **Metadata Tagging:** Normalizes chapter numbering, volume grouping, and series indexing for self-hosted readers.
- **Zero-Bloat Architecture:** Built with minimal dependencies for fast execution on local machines and home servers.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com
cd For-Claude
pip install -r requirements.txt
```

## Quick Start

Run the library scanner on your target directory:

```bash
python main.py --scan ./library --optimize
```

## Roadmap

- [x] Core archive validation and chapter sorting
- [x] Automated JSON metadata generation
- [ ] Multi-threaded image compression worker
- [ ] Integration with public manga metadata APIs

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or submit an issue to help improve the project.

## License

Distributed under the MIT License. See `LICENSE` for more information.
