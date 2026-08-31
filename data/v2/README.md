# Islamic JSON v2

`data/v2/` is the current structured contract for multilingual non-Quran, non-hadith learning content. Start with [`manifest.json`](manifest.json), then load its stage catalog, registries, and collection indexes.

- Default locale: Indonesian (`id`)
- Additional locale: English (`en`)
- Content: typed JSON documents with semantic IDs, review state, source references, and structured blocks
- Assets: optional SVG icons under `assets/icons/`

Run the repository tools from the project root:

```sh
python scripts/build_v2_indexes.py
python scripts/validate_v2.py
python -m unittest discover -s scripts/tests -v
```

For a public release, consumers should pin an immutable Git tag and use paths beginning with `data/v2/`.
