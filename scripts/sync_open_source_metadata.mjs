#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, "..");
const dataPath = path.join(rootDir, "data", "open-source.json");

function parseGitHubRepo(repoUrl) {
  try {
    const parsed = new URL(String(repoUrl || "").trim());
    if (parsed.hostname.toLowerCase() !== "github.com") return null;

    const parts = parsed.pathname.split("/").filter(Boolean);
    if (parts.length < 2) return null;

    return {
      owner: parts[0],
      repo: parts[1].replace(/\.git$/i, "")
    };
  } catch {
    return null;
  }
}

async function fetchRepoMeta(owner, repo) {
  const response = await fetch(`https://api.github.com/repos/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}`, {
    headers: {
      Accept: "application/vnd.github+json",
      "User-Agent": "yzhao062.github.io-open-source-sync/1.0",
      "X-GitHub-Api-Version": "2022-11-28"
    }
  });

  if (!response.ok) {
    throw new Error(`GitHub API HTTP ${response.status}`);
  }

  return response.json();
}

async function main() {
  const raw = await fs.readFile(dataPath, "utf8");
  const projects = JSON.parse(raw);
  let updated = 0;
  const skipped = [];

  for (const project of projects) {
    const parsed = parseGitHubRepo(project.repo_url);
    if (!parsed) {
      skipped.push(project.name || "Untitled Project");
      continue;
    }

    try {
      const meta = await fetchRepoMeta(parsed.owner, parsed.repo);
      project.stars = typeof meta.stargazers_count === "number" ? meta.stargazers_count : project.stars;
      project.last_updated_at = meta.pushed_at || project.last_updated_at || "";
      updated += 1;
    } catch (error) {
      console.warn(`[warn] ${project.name}: ${error.message}`);
    }
  }

  await fs.writeFile(dataPath, `${JSON.stringify(projects, null, 2)}\n`, "utf8");

  console.log(`Synced ${updated} GitHub repositories.`);
  if (skipped.length > 0) {
    console.log(`Skipped: ${skipped.join(", ")}`);
  }
}

await main();
