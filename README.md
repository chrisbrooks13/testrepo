<!-- README.md -->
<!-- Overview of the full stack template. -->
<!-- Explains the directory layout and setup. -->

# AI SaaS Template

This repository contains a minimal full stack template. It aims to stay small and easy to read. The code is kept simple on purpose.

## Tech Stack

- **Frontend**: Next.js with TypeScript and Lucide React icons.
- **Backend**: Python FastAPI.
- **Database**: Supabase.
- **Auth**: not configured.
- **Payments**: not configured.
- **Hosting**: run locally or deploy as you prefer.
- **CI/CD**: none included.

## Structure

```
frontend/    Next.js project
backend/     FastAPI server code
README.md    Overview and instructions
agents.md    Contributor guidelines
```

You can start the frontend with `npm install && npm run dev` inside the `frontend` folder. The backend runs with `pip install -r requirements.txt` and `uvicorn backend.main:app`.

## Project tree

If the `tree` command is missing, run the helper script:

```bash
python3 show_structure.py
```

This prints the directory layout up to three levels deep.

## Troubleshooting

`npm install lucide-react` may fail in restricted environments. Ensure your machine can reach the npm registry.

`brew install tree` or `apt-get install tree` might fail if those package managers are unavailable. Use the `show_structure.py` script instead.
