export const dataRelationshipDiagram = `flowchart TD
    Q[Al-Qur'an] -->|referensi ayat| FAI[Rukun Iman]
    Q -->|referensi ayat| FIS[Rukun Islam]
    Q -->|kisah dan penyebutan| PRO[Nabi dan Rasul]
    Q -->|penyebutan| ANG[Malaikat]
    Q -->|wahyu terdahulu| BKS[Kitab Allah]
    Q -->|bulan dan peristiwa| CAL[Kalender Islam]
    Q -->|tempat dan sejarah| PLC[Tempat Islam]
    Q -->|doa dan perlindungan| DKR[Dzikir]

    FAI --> ANG
    FAI --> BKS
    FAI --> PRO
    FAI --> AKH[Hari Akhir]
    FAI --> QDR[Qada dan Qadar]

    FIS --> SYH[Syahadat]
    FIS --> SAL[Salat]
    FIS --> ZKT[Zakat]
    FIS --> PUA[Puasa]
    FIS --> HJJ[Haji]

    SAL --> PG[Panduan Salat]
    SAL --> SP[Salat Sunah]
    SAL --> PUR[Bersuci]
    SAL --> DKR
    ZKT --> ZD[Data Zakat]
    PUA --> FD[Data Puasa]
    HJJ --> PLC
    HJJ --> CAL

    DUA[Doa Harian] --> DKR
    DUA --> MNR[Adab]
    MNR --> PUR
    MNR --> SAL
    MNR --> DUA

    API[Developer API] -.->|GitCDN Generator| Q
    API -.-> FAI
    API -.-> FIS
    API -.-> LIB[Pustaka Islam]
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
    LIB --> MNR`
