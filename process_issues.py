#!/usr/bin/env python3
import json
import subprocess
import sys
from collections import defaultdict

def fetch_issues(label):
    """Fetch issues for a given label"""
    cmd = [
        'gh', 'issue', 'list',
        '--repo', 'ballerina-platform/ballerina-library',
        '--state', 'open',
        '--label', label,
        '--limit', '1000',
        '--json', 'number,title,labels,url'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return json.loads(result.stdout)
    return []

def get_priority(labels):
    """Extract priority from labels"""
    for label in labels:
        if label['name'].startswith('Priority/'):
            return label['name'].split('/')[-1]
    return 'None'

def get_module_labels(labels):
    """Extract module labels"""
    modules = []
    for label in labels:
        if label['name'].startswith('module/') or label['name'].startswith('Module/'):
            modules.append(label['name'])
    return modules if modules else ['No Module']

def priority_sort_key(priority):
    """Sort key for priority"""
    priority_order = {'High': 0, 'Medium': 1, 'Low': 2, 'None': 3}
    return priority_order.get(priority, 4)

def main():
    print("Fetching issues...")

    # Fetch issues for each area
    areas = ['Area/Library', 'Area/Connectors', 'Area/Tooling']
    all_issues = {}

    for area in areas:
        print(f"Fetching {area}...")
        issues = fetch_issues(area)
        all_issues[area] = issues
        print(f"  Found {len(issues)} issues")

    # Organize by area and module
    organized = {}
    for area, issues in all_issues.items():
        organized[area] = defaultdict(list)
        for issue in issues:
            priority = get_priority(issue['labels'])
            modules = get_module_labels(issue['labels'])

            for module in modules:
                organized[area][module].append({
                    'number': issue['number'],
                    'title': issue['title'],
                    'priority': priority,
                    'url': issue['url'],
                    'labels': [l['name'] for l in issue['labels']]
                })

        # Sort each module's issues by priority
        for module in organized[area]:
            organized[area][module].sort(key=lambda x: priority_sort_key(x['priority']))

    # Save organized data
    with open('organized_issues.json', 'w') as f:
        json.dump(organized, f, indent=2)

    print("\nIssue Summary:")
    for area in organized:
        print(f"\n{area}:")
        total = sum(len(issues) for issues in organized[area].values())
        print(f"  Total: {total} issues")
        for module in sorted(organized[area].keys()):
            print(f"    {module}: {len(organized[area][module])} issues")

    print("\nData saved to organized_issues.json")

if __name__ == '__main__':
    main()
