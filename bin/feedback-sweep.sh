#!/bin/bash
# Audit's hourly sweep of visitors' feedback (Website #3, 2026-11-17 13:13 UTC; Udi's yes to Audit #2).
# Copies each file feedback/<name>.md of GLP's branch feedback, unchanged, to a branch feedback/<name>
# of udi-shapiro/Grassroots-Audit based on its main, and prints "OPEN <branch> <name>" for each that
# still needs its pull request.  It never reads the posts' text.
set -u
GLP=${GLP_URL:-https://github.com/EShapiro2/GLP}
AUD=/home/user/grassroots-audit
REC=/home/user/audit-tools/feedback-opened.txt
W=$(mktemp -d)
touch "$REC"
if ! git ls-remote --exit-code "$GLP" refs/heads/feedback >/dev/null 2>&1; then echo "NONE: no branch feedback in GLP"; exit 0; fi
git -C "$W" init -q && git -C "$W" fetch -q --depth 1 "$GLP" feedback || { echo "ERROR: fetch of GLP feedback failed"; exit 1; }
git -C "$AUD" fetch -q --depth 5 origin main || { echo "ERROR: fetch of audit main failed"; exit 1; }
for f in $(git -C "$W" ls-tree --name-only FETCH_HEAD feedback/ | grep -E '^feedback/[A-Za-z0-9._-]+\.md$'); do
  name=$(basename "$f" .md); br="feedback/$name"
  grep -qx "$name" "$REC" && continue
  git -C "$AUD" cat-file -e "origin/main:$f" 2>/dev/null && { echo "$name" >> "$REC"; continue; }
  n=$(gh api -X GET search/issues -f q="repo:udi-shapiro/Grassroots-Audit is:pr in:title \"Feedback from a visitor, $name\"" --jq .total_count 2>/dev/null || echo 0)
  [ "$n" != "0" ] && { echo "$name" >> "$REC"; continue; }
  if ! git -C "$AUD" ls-remote --exit-code origin "refs/heads/$br" >/dev/null 2>&1; then
    T=$(mktemp -d)
    git -C "$AUD" worktree add -q --detach "$T" origin/main || { echo "ERROR: worktree for $name"; continue; }
    mkdir -p "$T/feedback" && git -C "$W" show "FETCH_HEAD:$f" > "$T/$f"
    git -C "$T" add -- "$f" && git -C "$T" -c user.name="Ehud Shapiro" -c user.email="ehud.shapiro@weizmann.ac.il" commit -q -m "Feedback from a visitor, $name" -- "$f" \
      && git -C "$T" -c push.negotiate=true push -q ${DRY:+--dry-run} origin "HEAD:refs/heads/$br" 2>/dev/null || { echo "ERROR: push of $br"; }
    git -C "$AUD" worktree remove --force "$T"
  fi
  echo "OPEN $br $name"
done
rm -rf "$W"
