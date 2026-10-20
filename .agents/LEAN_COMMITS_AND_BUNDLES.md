# ⚖️ LEAN COMMITS & BUNDLES LAW (`.agents/LEAN_COMMITS_AND_BUNDLES.md`)

## Non-Negotiable Repository Hygiene Rules

1. **Zero Raw Dumps or Binary Blobs**:
   - Never commit `.sql` dumps, `.tar.gz` archives, `.zip` bundles, `.mp4`/`.wav` raw media, or base64-encoded assets into Git.
2. **File Size Hard Cap**:
   - Any single file > **2 MB** (or code file > **500 lines** without an explicit legacy exemption) is blocked from commit by `./scripts/review.sh` and `./scripts/sync-brain.sh`.
3. **Secret & Token Scrubbing**:
   - Never write raw API keys, Supabase service-role JWTs, Stripe secret keys, or GitHub PATs into `.agents/` markdown files or source files.
4. **Clean Memory Diffs**:
   - `.agents/CHECKPOINTS.md` and `.agents/memory/*.md` must contain high-signal architectural state, decisions, and audit trails—never raw multi-megabyte terminal stdout dumps.
