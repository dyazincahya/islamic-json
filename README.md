<p align="center">
  <img src="https://raw.githubusercontent.com/x-labs-myid/app-info/refs/heads/main/icons/muslimkit.png" alt="MuslimKit logo" width="160" />
</p>

<h1 align="center">Islamic JSON</h1>

<p align="center">All data json about Islam</p>

## Data Explorer

A Vue-based interface is included to browse the Qur'an, daily duas,
Asmaul Husna, the pillars of Islam, and the pillars of faith.

```bash
cd ui
npm install
npm run dev
```

The production site is built from the `ui` directory with `npm run build`
and deployed to GitHub
Pages automatically by `.github/workflows/deploy-pages.yml` whenever the
`main` branch is updated. In the repository settings, set **Pages → Source**
to **GitHub Actions**.

## Data Collections

- Qur'an, daily dua, dhikr, and Asmaul Husna
- Pillars of Islam and pillars of faith
- Obligatory and sunnah prayer guides
- Purification: wudu, tayammum, ritual bath, and impurities
- Angels, revealed books, and 25 prophets
- Hijri calendar and important Islamic occasions
- Major Islamic places
- Zakat and fasting references
- Daily manners for eating, sleeping, mosque, travel, visiting, and social life

Every domain includes a `README.md` describing its files, schema, and CDN
paths. The Vue explorer exposes these datasets under the **Library** and
**Developer API** navigation items.

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

## CDN

You can access _islamic json_ data free via CDN.

### 🚀 jsdelvr (Limit: Max 20 MB)

_Format_

`https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json/{_DIR_}/{_FILENAME_}.json`

_Example_

https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json/asmaul-husna/asmaul-husna.json

> 📝 asmaul-husna = `{_DIR_}` 📝 asmaul-husna.json = `{_FILENAME_}`.json

### 🚀 statically (Limit: Max 50 MB)

_Format_

`https://cdn.statically.io/gh/dyazincahya/islamic-json/{_BRANCH_}/{_DIR_}/{_FILENAME_}.json`

_Example_

https://cdn.statically.io/gh/dyazincahya/islamic-json/main/asmaul-husna/asmaul-husna.json

> 📝 main = `{_BRANCH_}` 📝 asmaul-husna = `{_DIR_}` 📝 asmaul-husna.json = `{_FILENAME_}`.json
