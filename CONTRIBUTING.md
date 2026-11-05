# Contributing to AeroTrade XAI

Thanks for your interest in improving AeroTrade XAI. This project is a prototype
for explainable supply-chain decision support, so changes should preserve both
the agent workflow and the transparency of the dashboard.

## Development setup

1. Fork the repository and clone your fork.
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows PowerShell
   venv\Scripts\Activate.ps1
   # macOS / Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a local `.env` with at least one provider key. Never commit this file
   or paste its contents into an issue.

5. Run the app:

   ```bash
   streamlit run app.py
   ```

## Branch naming

Use a short, descriptive prefix:

- `feat/<short-description>` for new functionality
- `fix/<short-description>` for bug fixes
- `docs/<short-description>` for documentation
- `refactor/<short-description>` for internal changes
- `chore/<short-description>` for tooling or maintenance

Keep each branch focused on one logical change.

## Commit messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

```text
feat(agent): add a maximum tool-call iteration limit
fix(ui): handle missing route scores in the matrix
docs(readme): clarify the simulated quote table
```

Use an imperative subject, keep it under about 72 characters, and explain the
reason for non-obvious changes in the body.

## Code guidelines

- Keep the Pydantic schemas in `models.py` as the contract between the agent and
  the UI. Update all call sites when a schema changes.
- Do not hide LLM failures behind successful-looking decisions. Surface errors
  in the UI or return an explicit failure state.
- Keep the weighted penalty calculation deterministic and independent of the
  LLM. If the formula changes, update the README and the UI caption.
- Avoid adding real credentials, generated audit logs, or large binary files.
- Match the existing Python style and keep functions small enough to review.

## Checks before opening a pull request

There is currently no automated test suite or linter configuration. Run these
smoke checks at minimum:

```bash
python -m compileall .
streamlit run app.py
```

Then verify:

- The app starts with each provider you changed.
- At least one built-in scenario completes and renders a decision.
- Tool traces, the trade-off matrix, rejection reasons, and the JSON download
  still work.
- No `.env`, API keys, or generated audit files are staged.

## Pull request checklist

- [ ] The change is scoped to one problem and has a clear description.
- [ ] `python -m compileall .` passes.
- [ ] The affected scenario or UI path was tested manually.
- [ ] Documentation was updated for user-visible behavior or configuration.
- [ ] No secrets, credentials, or large generated files are included.
- [ ] The PR follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## Reporting bugs and requesting features

Use the issue templates in `.github/ISSUE_TEMPLATE/`. Include the provider and
model in use, the selected corridor and scenario, and the relevant traceback.
Redact API keys and any sensitive data before posting.

Security vulnerabilities should be reported privately according to
[SECURITY.md](SECURITY.md).
