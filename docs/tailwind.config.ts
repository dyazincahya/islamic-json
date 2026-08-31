import type { Config } from "tailwindcss";

export default {
  content: [
    "./components/**/*.vue",
    "./index.md",
    "./guide/**/*.md",
    "./reference/**/*.md",
    "./explorer/**/*.md",
    "./api/**/*.md",
    "./migration/**/*.md",
    "./contributing/**/*.md",
    "./.vitepress/**/*.ts",
  ],
  theme: {
    extend: {
      colors: {
        canvas: "var(--oe-canvas)",
        surface: "var(--oe-surface)",
        "surface-muted": "var(--oe-surface-muted)",
        border: "var(--oe-border)",
        foreground: "var(--oe-fg)",
        muted: "var(--oe-muted)",
        accent: "var(--oe-accent)",
        link: "var(--oe-link)",
        success: "var(--oe-success)",
        warning: "var(--oe-warning)",
        danger: "var(--oe-danger)",
      },
    },
  },
  plugins: [],
} satisfies Config;
