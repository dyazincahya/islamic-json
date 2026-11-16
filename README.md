<p align="center">
  <img src="https://raw.githubusercontent.com/x-labs-myid/app-info/refs/heads/main/icons/muslimkit.png" alt="MuslimKit logo" width="160" />
</p>

<h1 align="center">Islamic JSON</h1>

<p align="center">All data json about Islam</p>

## Data Explorer

This branch contains the Vue-based interface for browsing the Islamic JSON
collections. The JSON data remains on the `main` branch and is checked out
into `data/` only during the GitHub Pages build.

```bash
# Run locally after checking out the data branch into ./data
cd ui
npm install
npm run dev
```

The production site is built from `ui/` with `npm run build` and deployed by
`.github/workflows/deploy-pages.yml` whenever `docs` is updated. The workflow
checks out `main` into `data/`, builds `ui/`, and publishes `ui/dist` as the
Pages artifact. In repository settings, set **Pages → Source** to **GitHub
Actions**.

## Data Branch

All JSON data, guides, catalog metadata, and schemas are maintained on the
`main` branch. The `docs` branch intentionally does not contain a copy of the
data. The Pages workflow checks out `main` as `data/` only for compilation.

## Machine-readable Catalog

The data catalog and JSON Schema are available from the `main` branch:
`catalog.json` and `catalog.schema.json`.

[`catalog.schema.json`](./catalog.schema.json) uses JSON Schema Draft 2020-12
to validate the catalog. After adding or moving a collection, update the
metadata in `scripts/generate_catalog.py` and regenerate the catalog:

```bash
python scripts/generate_catalog.py
```

### Path migration

Collections formerly stored at the repository root now live under `library/`;
procedural datasets live under `guides/`. This changes raw and CDN URLs that
used the old paths. Update consumers to the paths listed in `catalog.json` (for
example, `dhikr/data/morning-dhikr.json` is now
`library/dhikr/data/morning-dhikr.json`).

## Data Sources

The Qur'an data is sourced from the official [AL Qur'an Kemenag](https://quran.kemenag.go.id)
website. The source code used to retrieve and convert the data is available in
the [quran-json-kemenag](https://github.com/dyazincahya/quran-json-kemenag)
repository.

## Data Relationships

The following diagram shows how primary sources, pillars, worship guides,
knowledge collections, and developer access relate to each other. An
interactive version is available on the **Data Relations** page in the UI.

```mermaid
flowchart TD
    Q[Al-Qur'an] -->|verse references| FAI[Pillars of Faith]
    Q -->|verse references| FIS[Pillars of Islam]
    Q -->|accounts and mentions| PRO[Prophets]
    Q -->|mentions| ANG[Angels]
    Q -->|earlier revelation| BKS[Revealed Books]
    Q -->|months and occasions| CAL[Islamic Calendar]
    Q -->|places and history| PLC[Islamic Places]
    Q -->|prayer and protection| DKR[Dhikr]

    FAI --> ANG
    FAI --> BKS
    FAI --> PRO
    FAI --> AKH[Last Day]
    FAI --> QDR[Divine Decree]

    FIS --> SYH[Shahada]
    FIS --> SAL[Prayer]
    FIS --> ZKT[Zakat]
    FIS --> PUA[Fasting]
    FIS --> HJJ[Hajj]

    SAL --> PG[Prayer Guide]
    SAL --> SP[Sunnah Prayers]
    SAL --> PUR[Purification]
    SAL --> DKR
    ZKT --> ZD[Zakat Data]
    PUA --> FD[Fasting Data]
    HJJ --> PLC
    HJJ --> CAL

    DUA[Daily Dua] --> DKR
    DUA --> MNR[Manners]
    MNR --> PUR
    MNR --> SAL
    MNR --> DUA

    API[Developer API] -.->|GitCDN Generator| Q
    API -.-> FAI
    API -.-> FIS
    API -.-> LIB[Islamic Library]
    LIB --> DKR
    LIB --> PG
    LIB --> SP
    LIB --> PUR
    LIB --> ANG
    LIB --> BKS
    LIB --> PRO
    LIB --> CAL
    LIB --> PLC
    LIB --> ZD
    LIB --> FD
    LIB --> MNR
```
