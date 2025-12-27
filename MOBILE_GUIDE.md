# TriKind Mobile Anti-Friction Guide

This document provides high-velocity commands for managing the **triyl** pipeline from mobile devices where physical keyboard shortcuts (like Ctrl keys) are unavailable.

## 🚀 Daily Workflow Commands
| Action | Mobile-Safe Command |
| :--- | :--- |
| **Step 1: Safe Sync** | `git pull origin main --no-edit` |
| **Step 2: Log Update** | `echo "Triyl Log: $(date)" >> trikind_srb_pipeline/sync_log.txt` |
| **Step 3: Auto-Push** | `python3 trikind_srb_pipeline/auto_push.py` |

## 🛠️ Permanent Anti-Friction Configuration
Run these once to permanently disable interactive prompts:
```bash
git config --global core.editor "true"
git config --global pull.rebase false
git config --global credential.helper store
```

## 🆘 Emergency Recovery
If the terminal is "stuck" or divergent:
- **Abort Merge:** `git merge --abort`
- **Abort Rebase:** `git rebase --abort`

