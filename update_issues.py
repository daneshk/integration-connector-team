#!/usr/bin/env python3
"""
Script to fetch issues from ballerina-platform/ballerina-library
and update the README with a list of issues labeled with Area/Library, Area/Connector, and Area/Tooling
"""

import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from typing import List, Dict
import os

GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "ballerina-platform"
REPO_NAME = "ballerina-library"
LABELS = ["Area/Library", "Area/Connector", "Area/Tooling"]


def fetch_issues_by_label(label: str) -> List[Dict]:
    """Fetch issues from GitHub API for a specific label"""
    issues = []
    page = 1
    per_page = 100
    
    # Get GitHub token from environment if available
    github_token = os.environ.get('GITHUB_TOKEN', '')
    
    while True:
        url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
        params = f"?labels={label}&state=open&page={page}&per_page={per_page}"
        
        try:
            req = urllib.request.Request(url + params)
            req.add_header('Accept', 'application/vnd.github.v3+json')
            if github_token:
                req.add_header('Authorization', f'token {github_token}')
            
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                
                if not data:
                    break
                    
                # Filter out pull requests (they appear in issues endpoint too)
                for item in data:
                    if 'pull_request' not in item:
                        issues.append(item)
                
                if len(data) < per_page:
                    break
                    
                page += 1
                
        except urllib.error.HTTPError as e:
            print(f"Error fetching issues for label {label}: {e}")
            break
            
    return issues


def generate_markdown_table(issues_by_label: Dict[str, List[Dict]]) -> str:
    """Generate markdown content from issues"""
    markdown = "# integration-connector-team\n"
    markdown += "This is a management repository which maintains the status of the issues. This includes standard libraries, connectors and integration toolings.\n\n"
    
    # Add last updated timestamp
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    markdown += f"**Last Updated:** {now}\n\n"
    
    # Add summary
    total_issues = sum(len(issues) for issues in issues_by_label.values())
    markdown += f"**Total Open Issues:** {total_issues}\n\n"
    
    for label in LABELS:
        issues = issues_by_label.get(label, [])
        
        markdown += f"## {label} ({len(issues)} issues)\n\n"
        
        if not issues:
            markdown += "_No open issues found._\n\n"
            continue
        
        # Special handling for Area/Library - categorize by module
        if label == "Area/Library":
            # Group issues by module
            issues_by_module = {}
            for issue in issues:
                # Find module label
                module_label = None
                for lbl in issue.get('labels', []):
                    if lbl['name'].startswith('module/'):
                        module_label = lbl['name']
                        break
                
                # Use "Other" for issues without module label
                if not module_label:
                    module_label = "Other"
                
                if module_label not in issues_by_module:
                    issues_by_module[module_label] = []
                issues_by_module[module_label].append(issue)
            
            # Sort modules alphabetically, but keep "Other" at the end
            sorted_modules = sorted([m for m in issues_by_module.keys() if m != "Other"])
            if "Other" in issues_by_module:
                sorted_modules.append("Other")
            
            # Display each module as a subsection
            for module in sorted_modules:
                module_issues = issues_by_module[module]
                markdown += f"### {module} ({len(module_issues)} issues)\n\n"
                
                # Add module-specific filter link
                if module != "Other":
                    module_filter_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/issues?q=is%3Aissue+is%3Aopen+label%3A{label.replace('/', '%2F')}+label%3A{module.replace('/', '%2F')}"
                    markdown += f"[View {module} issues →]({module_filter_url})\n\n"
                else:
                    # For "Other", create a filter that excludes all module labels
                    # Get all module labels from issues_by_module
                    all_modules = [m for m in issues_by_module.keys() if m != "Other"]
                    if all_modules:
                        # Build exclusion query
                        exclusions = '+'.join([f"-label%3A{m.replace('/', '%2F')}" for m in all_modules])
                        other_filter_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/issues?q=is%3Aissue+is%3Aopen+label%3A{label.replace('/', '%2F')}+{exclusions}"
                        markdown += f"[View Other issues →]({other_filter_url})\n\n"
                
                markdown += "| # | Title | State | Labels | Assignee |\n"
                markdown += "|---|-------|-------|--------|----------|\n"
                
                for issue in sorted(module_issues, key=lambda x: x['number'], reverse=True):
                    number = issue['number']
                    title = issue['title'].replace('|', '\\|')  # Escape pipe characters
                    state = issue['state']
                    
                    # Get all label names except the current area label and module label
                    labels = [l['name'] for l in issue.get('labels', []) 
                             if l['name'] != label and not l['name'].startswith('module/')]
                    labels_str = ', '.join(labels[:3]) if labels else '-'  # Limit to 3 labels for readability
                    if len(labels) > 3:
                        labels_str += '...'
                    
                    # Get assignee
                    assignee = issue.get('assignee', {}).get('login', '-') if issue.get('assignee') else '-'
                    
                    # Create issue link
                    issue_link = f"[#{number}](https://github.com/{REPO_OWNER}/{REPO_NAME}/issues/{number})"
                    
                    markdown += f"| {issue_link} | {title} | {state} | {labels_str} | {assignee} |\n"
                
                markdown += "\n"
            
            markdown += f"[View all {label} issues →](https://github.com/{REPO_OWNER}/{REPO_NAME}/issues?q=is%3Aissue+is%3Aopen+label%3A{label.replace('/', '%2F')})\n\n"
        else:
            # For other labels, keep the original format
            markdown += "| # | Title | State | Labels | Assignee |\n"
            markdown += "|---|-------|-------|--------|----------|\n"
            
            for issue in sorted(issues, key=lambda x: x['number'], reverse=True):
                number = issue['number']
                title = issue['title'].replace('|', '\\|')  # Escape pipe characters
                state = issue['state']
                
                # Get all label names except the current area label
                labels = [l['name'] for l in issue.get('labels', []) if l['name'] != label]
                labels_str = ', '.join(labels[:3]) if labels else '-'  # Limit to 3 labels for readability
                if len(labels) > 3:
                    labels_str += '...'
                
                # Get assignee
                assignee = issue.get('assignee', {}).get('login', '-') if issue.get('assignee') else '-'
                
                # Create issue link
                issue_link = f"[#{number}](https://github.com/{REPO_OWNER}/{REPO_NAME}/issues/{number})"
                
                markdown += f"| {issue_link} | {title} | {state} | {labels_str} | {assignee} |\n"
            
            markdown += f"\n[View all {label} issues →](https://github.com/{REPO_OWNER}/{REPO_NAME}/issues?q=is%3Aissue+is%3Aopen+label%3A{label.replace('/', '%2F')})\n\n"
    
    # Add instructions
    markdown += "---\n\n"
    markdown += "## How to Update This List\n\n"
    markdown += "To update the issue list, run:\n\n"
    markdown += "```bash\n"
    markdown += "python3 update_issues.py\n"
    markdown += "```\n\n"
    markdown += "**Note:** Set the `GITHUB_TOKEN` environment variable to avoid API rate limits:\n\n"
    markdown += "```bash\n"
    markdown += "export GITHUB_TOKEN=your_github_token\n"
    markdown += "python3 update_issues.py\n"
    markdown += "```\n"
    
    return markdown


def main():
    """Main function to fetch issues and update README"""
    print("Fetching issues from ballerina-platform/ballerina-library...")
    
    issues_by_label = {}
    
    for label in LABELS:
        print(f"Fetching issues for label: {label}")
        issues = fetch_issues_by_label(label)
        issues_by_label[label] = issues
        print(f"  Found {len(issues)} issues")
    
    print("\nGenerating markdown...")
    markdown_content = generate_markdown_table(issues_by_label)
    
    # Write to README.md
    readme_path = "/home/runner/work/integration-connector-team/integration-connector-team/README.md"
    with open(readme_path, 'w') as f:
        f.write(markdown_content)
    
    print(f"README.md updated successfully!")
    print(f"Total issues: {sum(len(issues) for issues in issues_by_label.values())}")


if __name__ == "__main__":
    main()
