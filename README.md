
# SEO Reporting pipeline using Screaming Frog CLI, PageSpeed API, duckdb & evidence.dev
This repository is based on the Evidence Template Project and includes python scripts for:
- Getting emails from Gmail with specific label to local duckdb database
- Crawling all the extracted domains with Screaming Frog CLI and loading to duckdb
- Running lighthouse test with PageSpeed Insights API and loading to duckdb
- And finally evidence.dev handles the data into a dynamic reporting template.

Currently I use it for prospect SEO audits so that I swap the index.md file in the pages folder for every prospect and change the runtime variable domain in the .env file. I build the static site and upload to netlify, which I will eventually also include into the automated workflow.

Here some resulting audit reports:
- imagegroup.netlify.app

Reach out if you would like your own audit or custom implementation of this reporting pipeline

## Evidence Template Project

### Using Codespaces

If you are using this template in Codespaces, click the `Start Evidence` button in the bottom status bar. This will install dependencies and open a preview of your project in your browser - you should get a popup prompting you to open in browser.

Or you can use the following commands to get started:

```bash
npm install
npm run sources
npm run dev -- --host 0.0.0.0
```

See [the CLI docs](https://docs.evidence.dev/cli/) for more command information.

**Note:** Codespaces is much faster on the Desktop app. After the Codespace has booted, select the hamburger menu → Open in VS Code Desktop.

### Get Started from VS Code

The easiest way to get started is using the [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=evidence-dev.evidence):

1. Install the extension from the VS Code Marketplace
2. Open the Command Palette (Ctrl/Cmd + Shift + P) and enter `Evidence: New Evidence Project`
3. Click `Start Evidence` in the bottom status bar

### Get Started using the CLI

```bash
npx degit evidence-dev/template my-project
cd my-project 
npm install 
npm run sources
npm run dev 
```

Check out the docs for [alternative install methods](https://docs.evidence.dev/getting-started/install-evidence) including Docker, Github Codespaces, and alongside dbt.

### Learning More

- [Docs](https://docs.evidence.dev/)
- [Github](https://github.com/evidence-dev/evidence)
- [Slack Community](https://slack.evidence.dev/)
- [Evidence Home Page](https://www.evidence.dev)