#!/usr/bin/env python3
"""
Issue and Progress Tracker for Basics of Mathematics Student Workbook 2026.

Features:
- Pulls open issues and review comments directly from GitHub API.
- Highlights exercises needing revision with reviewer comments.
- Scans local workspace for completed and empty exercise solution files.
- Updates repository-status.html with real-time local completion status.
"""

import argparse
import datetime
import json
import os
import re
import sys
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding="utf-8")

REPO_OWNER = "ndahirwaIneza"
REPO_NAME = "Basics_of_Mathematics_Student_Workbook_2026"
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=open&per_page=100"

ALL_SECTIONS = [
    "1_Algebra/01_matrices_and_operations",
    "1_Algebra/02_determinants",
    "1_Algebra/03_matrix_inversion",
    "1_Algebra/04_systems_of_equations",
    "2_Geometry/01_vectors",
    "2_Geometry/02_lines_and_planes",
    "2_Geometry/03_second_degree_curves_and_surfaces",
    "3_Calculus/01_limits",
    "3_Calculus/02_derivatives",
    "3_Calculus/03_function_analysis",
    "3_Calculus/04_integrals",
    "3_Calculus/05_applications",
]


def fetch_open_issues(token=None):
    headers = {
        "User-Agent": "Mathematics-Workbook-Sync/1.0",
        "Accept": "application/vnd.github+json",
    }
    auth_token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"

    req = urllib.request.Request(API_URL, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return [i for i in data if not i.get("pull_request")]
    except urllib.error.HTTPError as e:
        print(f"Error fetching issues from GitHub: HTTP {e.code} {e.reason}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Failed to fetch issues: {e}", file=sys.stderr)
        return []


def scan_local_completion(root_dir="."):
    results = []
    solutions_dir = os.path.join(root_dir, "solutions")

    for section in ALL_SECTIONS:
        sec_dir = os.path.join(solutions_dir, section.replace("/", os.sep))
        max_exercises = 12 if section == "3_Calculus/05_applications" else 15
        completed = 0
        incomplete = 0

        for i in range(1, max_exercises + 1):
            name_v1 = f"problem_{i:02d}_solution.md"
            name_v2 = f"ex_{i:02d}.md"
            p1 = os.path.join(sec_dir, name_v1)
            p2 = os.path.join(sec_dir, name_v2)

            is_done = False
            for p in (p1, p2):
                if os.path.isfile(p) and os.path.getsize(p) > 50:
                    is_done = True
                    break

            if is_done:
                completed += 1
            else:
                incomplete += 1

        results.append([section, completed, incomplete])

    return results


def print_issues_report(issues):
    print("=" * 70)
    print(f" GitHub Open Issues Report ({len(issues)} open issues found)")
    print("=" * 70)

    if not issues:
        print("No open issues.")
        return

    for issue in issues:
        num = issue["number"]
        title = issue["title"]
        body = issue.get("body", "")
        url = issue.get("html_url", "")
        updated_at = issue.get("updated_at", "")

        print(f"\n▶ Issue #{num}: {title}")
        print(f"  URL: {url}")
        print(f"  Updated: {updated_at}")

        revisions = re.findall(r"### Exercise (\d+) — Needs revision", body)
        if revisions:
            print(f"  ⚠️  Exercises needing revision: {', '.join(revisions)}")
            for rev in revisions:
                pattern = rf"(### Exercise {rev} — Needs revision[\s\S]*?)(?=### Exercise \d+|$)"
                m = re.search(pattern, body)
                if m:
                    print("\n    " + m.group(1).strip().replace("\n", "\n    "))
        else:
            first_lines = [l.strip() for l in body.splitlines() if l.strip()][:3]
            if first_lines:
                print("  Summary: " + " | ".join(first_lines))


def update_repository_status_html(local_completion, html_path="repository-status.html"):
    if not os.path.isfile(html_path):
        print(f"HTML file {html_path} not found.")
        return False

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    now_iso = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat()
    lines = ["    const completionSnapshot = {", f'      checkedAt: "{now_iso}",', "      sections: ["]
    for idx, (sec, comp, incomp) in enumerate(local_completion):
        comma = "," if idx < len(local_completion) - 1 else ""
        lines.append(f'        ["{sec}", {comp}, {incomp}]{comma}')
    lines.append("      ]")
    lines.append("    };")
    replacement_block = "\n".join(lines)

    new_content = re.sub(
        r"    const completionSnapshot = \{[\s\S]*?\n    \};",
        replacement_block,
        content
    )

    if new_content != content:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {html_path} with latest local snapshot ({now_iso}).")
        return True
    else:
        print("No changes needed in repository-status.html.")
        return False


def main():
    parser = argparse.ArgumentParser(description="Sync GitHub issues and local exercise status.")
    parser.add_argument("--issues", action="store_true", help="Fetch and display open issues from GitHub")
    parser.add_argument("--status", action="store_true", help="Display local exercise completion table")
    parser.add_argument("--update-html", action="store_true", help="Update repository-status.html with local status")
    parser.add_argument("--all", action="store_true", help="Run both issues report, local status, and update HTML")

    args = parser.parse_args()
    if not (args.issues or args.status or args.update_html or args.all):
        args.all = True

    local_comp = scan_local_completion()

    if args.status or args.all:
        print("\n" + "=" * 70)
        print(" Local Exercise Completion Status")
        print("=" * 70)
        total_comp = sum(c[1] for c in local_comp)
        total_incomp = sum(c[2] for c in local_comp)
        total_all = total_comp + total_incomp

        for sec, comp, incomp in local_comp:
            total_sec = comp + incomp
            pct = int(comp / total_sec * 100) if total_sec else 0
            bar = "█" * (pct // 5) + "░" * (20 - (pct // 5))
            print(f"  {sec:<45} {comp:2d}/{total_sec:2d} [{bar}] {pct:3d}%")
        print("-" * 70)
        pct_total = int(total_comp / total_all * 100) if total_all else 0
        print(f"  {'Total Completed':<45} {total_comp:2d}/{total_all} ({pct_total}%)")

    if args.issues or args.all:
        issues = fetch_open_issues()
        print_issues_report(issues)

    if args.update_html or args.all:
        update_repository_status_html(local_comp)


if __name__ == "__main__":
    main()

