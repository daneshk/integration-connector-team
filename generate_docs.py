#!/usr/bin/env python3
import json
import os
from pathlib import Path

def generate_module_page(area, module, issues, output_dir):
    """Generate a markdown page for a module"""
    filename = f"{area.replace('/', '_')}_{module.replace('/', '_')}.md"
    filepath = output_dir / filename

    content = f"# {area} - {module}\n\n"
    content += f"Total Issues: {len(issues)}\n\n"

    # Group by priority
    by_priority = {}
    for issue in issues:
        priority = issue['priority']
        if priority not in by_priority:
            by_priority[priority] = []
        by_priority[priority].append(issue)

    # Generate content for each priority (in order)
    priority_order = ['Highest', 'High', 'Medium', 'Low', 'None']
    for priority in priority_order:
        if priority not in by_priority:
            continue
        if by_priority[priority]:
            content += f"## Priority: {priority}\n\n"
            for issue in by_priority[priority]:
                content += f"### [#{issue['number']}]({issue['url']}) {issue['title']}\n"
                content += f"**Labels:** {', '.join([f'`{l}`' for l in issue['labels']])}\n\n"

    with open(filepath, 'w') as f:
        f.write(content)

    return filename

def generate_readme(organized, module_files):
    """Generate README with summary and links"""
    from datetime import datetime
    readme = "# Ballerina Library Issues Analysis\n\n"
    readme += "This repository contains an organized breakdown of open issues from the "
    readme += "[ballerina-library](https://github.com/ballerina-platform/ballerina-library) repository.\n\n"
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    readme += f"**Last Updated:** {last_updated}\n\n"

    for area in sorted(organized.keys()):
        readme += f"## {area}\n\n"

        modules = organized[area]
        total_issues = sum(len(issues) for issues in modules.values())
        readme += f"**Total Issues:** {total_issues}\n\n"

        # Create table
        readme += "| Module | Issues | Priority High | Priority Medium | Priority Low | No Priority |\n"
        readme += "|--------|--------|---------------|-----------------|--------------|-------------|\n"

        for module in sorted(modules.keys()):
            issues = modules[module]
            highest = len([i for i in issues if i['priority'] == 'Highest'])
            high = len([i for i in issues if i['priority'] == 'High'])
            medium = len([i for i in issues if i['priority'] == 'Medium'])
            low = len([i for i in issues if i['priority'] == 'Low'])
            none = len([i for i in issues if i['priority'] == 'None'])

            module_file = module_files[area][module]
            total_priority = highest + high + medium
            readme += f"| [{module}]({module_file}) | {len(issues)} | {high} | {medium} | {low} | {none} |\n"

        readme += "\n"

    readme += "## Issue Distribution by Priority\n\n"
    for area in sorted(organized.keys()):
        all_issues = [issue for issues in organized[area].values() for issue in issues]
        highest = len([i for i in all_issues if i['priority'] == 'Highest'])
        high = len([i for i in all_issues if i['priority'] == 'High'])
        medium = len([i for i in all_issues if i['priority'] == 'Medium'])
        low = len([i for i in all_issues if i['priority'] == 'Low'])
        none = len([i for i in all_issues if i['priority'] == 'None'])

        readme += f"### {area}\n"
        if highest > 0:
            readme += f"- **Highest Priority:** {highest}\n"
        readme += f"- **High Priority:** {high}\n"
        readme += f"- **Medium Priority:** {medium}\n"
        readme += f"- **Low Priority:** {low}\n"
        readme += f"- **No Priority:** {none}\n"
        readme += f"- **Total:** {len(all_issues)}\n\n"

    return readme

def main():
    # Load organized data
    with open('organized_issues.json', 'r') as f:
        organized = json.load(f)

    # Create issues directory
    issues_dir = Path('issues')
    issues_dir.mkdir(exist_ok=True)

    # Generate module pages
    module_files = {}
    print("Generating module pages...")
    for area in organized:
        module_files[area] = {}
        for module in organized[area]:
            issues = organized[area][module]
            filename = generate_module_page(area, module, issues, issues_dir)
            module_files[area][module] = f"issues/{filename}"
            print(f"  Created {filename} ({len(issues)} issues)")

    # Generate README
    print("\nGenerating README...")
    readme_content = generate_readme(organized, module_files)

    with open('README.md', 'w') as f:
        f.write(readme_content)

    print("README.md updated successfully")
    print(f"\nTotal files created: {len([f for files in module_files.values() for f in files.values()])} module pages + 1 README")

if __name__ == '__main__':
    main()
