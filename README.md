<p align="center">
  <img src="https://raw.githubusercontent.com/x-labs-myid/app-info/refs/heads/main/icons/muslimkit.png" alt="MuslimKit logo" width="160" />
</p>

<h1 align="center">Islamic JSON</h1>

<p align="center">All data json about Islam</p>

## Data Explorer

A Vue-based interface is included to browse the Qur'an, daily duas,
Asmaul Husna, and the pillars of Islam.

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
