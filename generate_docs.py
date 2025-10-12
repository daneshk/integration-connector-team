#!/usr/bin/env python3
import json
import os
from pathlib import Path

def generate_module_page(area, module, issues, output_dir):
    """Generate a markdown page for a module"""
    # Sanitize filename by replacing spaces and slashes with underscores
    filename = f"{area.replace('/', '_').replace(' ', '_')}_{module.replace('/', '_').replace(' ', '_')}.md"
    filepath = output_dir / filename

    content = f"# {area} - {module}\n\n"
    content += f"Total Issues: {len(issues)}\n\n"

    # Count by type
    type_counts = {}
    for issue in issues:
        issue_type = issue.get('type', 'Unknown')
        type_counts[issue_type] = type_counts.get(issue_type, 0) + 1

    content += "## Issue Types\n\n"
    for issue_type in sorted(type_counts.keys()):
        content += f"- **{issue_type}:** {type_counts[issue_type]}\n"
    content += "\n"

    # Group by priority
    by_priority = {}
    for issue in issues:
        priority = issue['priority']
        if priority not in by_priority:
            by_priority[priority] = []
        by_priority[priority].append(issue)

    # Generate content for each priority (in order)
    priority_order = ['Highest', 'High', 'Normal', 'Low', 'None']
    type_order = ['Bug', 'Improvement', 'Task', 'NewFeature', 'Docs', 'Proposal', 'Unknown']

    for priority in priority_order:
        if priority not in by_priority:
            continue
        if by_priority[priority]:
            content += f"## Priority: {priority}\n\n"

            # Group by type within this priority
            by_type = {}
            for issue in by_priority[priority]:
                issue_type = issue.get('type', 'Unknown')
                if issue_type not in by_type:
                    by_type[issue_type] = []
                by_type[issue_type].append(issue)

            # Output issues grouped by type
            for issue_type in type_order:
                if issue_type not in by_type:
                    continue

                content += f"### {issue_type}\n\n"
                for issue in by_type[issue_type]:
                    content += f"**[#{issue['number']}]({issue['url']})** {issue['title']}\n\n"
                    content += f"Labels: {', '.join([f'`{l}`' for l in issue['labels']])}\n\n"

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

    # Calculate total issues across all areas
    total_issues = 0
    for area in organized:
        if area == 'Area/Connector':
            for category in organized[area]:
                total_issues += sum(len(issues) for issues in organized[area][category].values())
        else:
            total_issues += sum(len(issues) for issues in organized[area].values())

    readme += f"## Overall Summary\n\n"
    readme += f"**Total Issues Across All Areas:** {total_issues}\n\n"

    for area in sorted(organized.keys()):
        readme += f"## {area}\n\n"

        if area == 'Area/Connector':
            # Handle connector categories
            total_issues = 0
            for category in ['Handwritten Connectors', 'Generated Connectors']:
                if category in organized[area]:
                    total_issues += sum(len(issues) for issues in organized[area][category].values())

            readme += f"**Total Issues:** {total_issues}\n\n"

            # Process each category
            for category in ['Handwritten Connectors', 'Generated Connectors']:
                if category not in organized[area]:
                    continue

                modules = organized[area][category]
                category_total = sum(len(issues) for issues in modules.values())
                readme += f"### {category} ({category_total} issues)\n\n"

                # Create table
                readme += "| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |\n"
                readme += "|--------|--------|------------------|---------------|-----------------|--------------|-------------|\n"

                for module in sorted(modules.keys()):
                    issues = modules[module]
                    highest = len([i for i in issues if i['priority'] == 'Highest'])
                    high = len([i for i in issues if i['priority'] == 'High'])
                    normal = len([i for i in issues if i['priority'] == 'Normal'])
                    low = len([i for i in issues if i['priority'] == 'Low'])
                    none = len([i for i in issues if i['priority'] == 'None'])

                    module_file = module_files[area][category][module]
                    readme += f"| [{module}]({module_file}) | {len(issues)} | {highest} | {high} | {normal} | {low} | {none} |\n"

                readme += "\n"
        else:
            modules = organized[area]
            total_issues = sum(len(issues) for issues in modules.values())
            readme += f"**Total Issues:** {total_issues}\n\n"

            # Create table
            readme += "| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |\n"
            readme += "|--------|--------|------------------|---------------|-----------------|--------------|-------------|\n"

            for module in sorted(modules.keys()):
                issues = modules[module]
                highest = len([i for i in issues if i['priority'] == 'Highest'])
                high = len([i for i in issues if i['priority'] == 'High'])
                normal = len([i for i in issues if i['priority'] == 'Normal'])
                low = len([i for i in issues if i['priority'] == 'Low'])
                none = len([i for i in issues if i['priority'] == 'None'])

                module_file = module_files[area][module]
                readme += f"| [{module}]({module_file}) | {len(issues)} | {highest} | {high} | {normal} | {low} | {none} |\n"

            readme += "\n"

    readme += "## Issue Distribution by Priority\n\n"
    for area in sorted(organized.keys()):
        # Get all issues for this area
        if area == 'Area/Connector':
            all_issues = []
            for category in organized[area]:
                for issues in organized[area][category].values():
                    all_issues.extend(issues)
        else:
            all_issues = [issue for issues in organized[area].values() for issue in issues]

        highest = len([i for i in all_issues if i['priority'] == 'Highest'])
        high = len([i for i in all_issues if i['priority'] == 'High'])
        normal = len([i for i in all_issues if i['priority'] == 'Normal'])
        low = len([i for i in all_issues if i['priority'] == 'Low'])
        none = len([i for i in all_issues if i['priority'] == 'None'])

        readme += f"### {area}\n"
        if highest > 0:
            readme += f"- **Highest Priority:** {highest}\n"
        if high > 0:
            readme += f"- **High Priority:** {high}\n"
        if normal > 0:
            readme += f"- **Normal Priority:** {normal}\n"
        if low > 0:
            readme += f"- **Low Priority:** {low}\n"
        if none > 0:
            readme += f"- **No Priority:** {none}\n"
        readme += f"- **Total:** {len(all_issues)}\n\n"

    readme += "## Issue Distribution by Type\n\n"
    for area in sorted(organized.keys()):
        # Get all issues for this area
        if area == 'Area/Connector':
            all_issues = []
            for category in organized[area]:
                for issues in organized[area][category].values():
                    all_issues.extend(issues)
        else:
            all_issues = [issue for issues in organized[area].values() for issue in issues]

        type_counts = {}
        for issue in all_issues:
            issue_type = issue.get('type', 'Unknown')
            type_counts[issue_type] = type_counts.get(issue_type, 0) + 1

        readme += f"### {area}\n"
        for issue_type in sorted(type_counts.keys()):
            readme += f"- **{issue_type}:** {type_counts[issue_type]}\n"
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
        if area == 'Area/Connector':
            module_files[area] = {}
            for category in organized[area]:
                module_files[area][category] = {}
                for module in organized[area][category]:
                    issues = organized[area][category][module]
                    filename = generate_module_page(f"{area}/{category}", module, issues, issues_dir)
                    module_files[area][category][module] = f"issues/{filename}"
                    print(f"  Created {filename} ({len(issues)} issues)")
        else:
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
