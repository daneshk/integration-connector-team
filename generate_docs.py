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
    content += f"**Total Issues:** {len(issues)}\n\n"

    # Count by type
    type_counts = {}
    for issue in issues:
        issue_type = issue.get('type', 'Unknown')
        type_counts[issue_type] = type_counts.get(issue_type, 0) + 1

    # Type emoji indicators
    type_emojis = {
        'Bug': '🐛',
        'Improvement': '✨',
        'Task': '📋',
        'NewFeature': '🚀',
        'Docs': '📚',
        'Proposal': '💡',
        'Unknown': '❓'
    }

    content += "## 📊 Issue Types\n\n"
    for issue_type in sorted(type_counts.keys()):
        emoji = type_emojis.get(issue_type, '▪️')
        content += f"- {emoji} **{issue_type}:** {type_counts[issue_type]}\n"
    content += "\n---\n\n"

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

    # Priority emoji indicators
    priority_emojis = {
        'Highest': '🔴',
        'High': '🟠',
        'Normal': '🟡',
        'Low': '🔵',
        'None': '⚪'
    }

    for priority in priority_order:
        if priority not in by_priority:
            continue
        if by_priority[priority]:
            priority_emoji = priority_emojis.get(priority, '')
            content += f"## {priority_emoji} Priority: {priority}\n\n"

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

                type_emoji = type_emojis.get(issue_type, '▪️')
                content += f"### {type_emoji} {issue_type}\n\n"
                for issue in by_type[issue_type]:
                    content += f"**[#{issue['number']}]({issue['url']})** {issue['title']}\n\n"
                    content += f"Labels: {', '.join([f'`{l}`' for l in issue['labels']])}\n\n"

    with open(filepath, 'w') as f:
        f.write(content)

    return filename

def get_priority_score(issues):
    """Calculate priority score for sorting (higher score = higher priority)"""
    score = 0
    for issue in issues:
        priority = issue['priority']
        if priority == 'Highest':
            score += 1000
        elif priority == 'High':
            score += 100
        elif priority == 'Normal':
            score += 10
        elif priority == 'Low':
            score += 1
    return score

def format_priority_cell(count, priority_type):
    """Format a priority cell with emoji indicators if count > 0"""
    if count == 0:
        return "0"

    indicators = {
        'Highest': '🔴',  # Red circle
        'High': '🟠',     # Orange circle
        'Normal': '🟡',   # Yellow circle
        'Low': '🔵',      # Blue circle
        'None': '⚪'      # White circle
    }

    indicator = indicators.get(priority_type, '')
    return f'{indicator} **{count}**'

def format_priority_cell_with_breakdown(issues, priority_type):
    """Format a priority cell with type breakdown"""
    priority_issues = [i for i in issues if i['priority'] == priority_type]

    if len(priority_issues) == 0:
        return "0"

    # Count by type
    type_counts = {}
    type_emojis = {
        'Bug': '🐛',
        'Improvement': '✨',
        'Task': '📋',
        'NewFeature': '🚀',
        'Docs': '📚',
        'Proposal': '💡',
        'Unknown': '❓'
    }

    for issue in priority_issues:
        issue_type = issue.get('type', 'Unknown')
        type_counts[issue_type] = type_counts.get(issue_type, 0) + 1

    # Priority indicator
    priority_indicators = {
        'Highest': '🔴',
        'High': '🟠',
        'Normal': '🟡',
        'Low': '🔵',
        'None': '⚪'
    }

    indicator = priority_indicators.get(priority_type, '')

    # Build breakdown string
    breakdown_parts = []
    for issue_type in sorted(type_counts.keys()):
        emoji = type_emojis.get(issue_type, '▪️')
        breakdown_parts.append(f"{emoji}{type_counts[issue_type]}")

    breakdown = " ".join(breakdown_parts)
    total = len(priority_issues)

    return f'{indicator} **{total}**<br/><sub>{breakdown}</sub>'

def generate_priority_page(issues, priority_name, priority_dir):
    """Generate a page for priority issues grouped by module"""
    from collections import defaultdict

    # Group issues by area and module
    grouped = defaultdict(lambda: defaultdict(list))

    for issue in issues:
        area_key = issue['area']
        if issue['category']:
            area_key = f"{issue['area']}/{issue['category']}"
        module_key = issue['module']
        grouped[area_key][module_key].append(issue)

    # Type emojis
    type_emojis = {
        'Bug': '🐛',
        'Improvement': '✨',
        'Task': '📋',
        'NewFeature': '🚀',
        'Docs': '📚',
        'Proposal': '💡',
        'Unknown': '❓'
    }

    # Priority emojis
    priority_emojis = {
        'Highest': '🔴',
        'High': '🟠'
    }

    content = f"# {priority_emojis.get(priority_name, '')} {priority_name} Priority Issues\n\n"
    content += f"**Total Issues:** {len(issues)}\n\n"

    # Define area order
    area_order = ['Area/Library', 'Area/Connector/Handwritten Connectors', 'Area/Connector/Generated Connectors', 'Area/Tooling']

    for area in area_order:
        if area not in grouped:
            continue

        content += f"## {area}\n\n"

        # Sort modules by number of issues (descending)
        sorted_modules = sorted(grouped[area].keys(), key=lambda m: len(grouped[area][m]), reverse=True)

        for module in sorted_modules:
            module_issues = grouped[area][module]
            content += f"### 📦 {module} ({len(module_issues)} issues)\n\n"

            # Group by type
            by_type = defaultdict(list)
            for issue in module_issues:
                issue_type = issue.get('type', 'Unknown')
                by_type[issue_type].append(issue)

            # Output issues grouped by type
            for issue_type in sorted(by_type.keys()):
                type_emoji = type_emojis.get(issue_type, '❓')
                content += f"#### {type_emoji} {issue_type}\n\n"

                for issue in by_type[issue_type]:
                    content += f"- **[#{issue['number']}]({issue['url']})** {issue['title']}\n"

                content += "\n"

    filepath = priority_dir / f"{priority_name.upper().replace(' ', '_')}_PRIORITY.md"
    with open(filepath, 'w') as f:
        f.write(content)

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

    # Count priority issues
    highest_count = 0
    high_count = 0

    for area in organized:
        if area == 'Area/Connector':
            for category in organized[area]:
                for module in organized[area][category]:
                    for issue in organized[area][category][module]:
                        if issue['priority'] == 'Highest':
                            highest_count += 1
                        elif issue['priority'] == 'High':
                            high_count += 1
        else:
            for module in organized[area]:
                for issue in organized[area][module]:
                    if issue['priority'] == 'Highest':
                        highest_count += 1
                    elif issue['priority'] == 'High':
                        high_count += 1

    # Generate priority issues pages links
    if highest_count > 0:
        readme += f"## 🔴 Highest Priority Issues ({highest_count})\n\n"
        readme += "Critical issues that require immediate attention.\n\n"
        readme += f"[View all Highest Priority Issues →](priority/HIGHEST_PRIORITY.md)\n\n"

    if high_count > 0:
        readme += f"## 🟠 High Priority Issues ({high_count})\n\n"
        readme += "Important issues that should be addressed soon.\n\n"
        readme += f"[View all High Priority Issues →](priority/HIGH_PRIORITY.md)\n\n"

    readme += "---\n\n"

    # Define area order
    area_order = ['Area/Library', 'Area/Connector', 'Area/Tooling']

    for area in area_order:
        if area not in organized:
            continue
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

                # Sort modules by priority score (highest first)
                sorted_modules = sorted(modules.keys(), key=lambda m: get_priority_score(modules[m]), reverse=True)

                for module in sorted_modules:
                    issues = modules[module]

                    module_file = module_files[area][category][module]
                    readme += f"| [{module}]({module_file}) | {len(issues)} | "
                    readme += f"{format_priority_cell_with_breakdown(issues, 'Highest')} | "
                    readme += f"{format_priority_cell_with_breakdown(issues, 'High')} | "
                    readme += f"{format_priority_cell_with_breakdown(issues, 'Normal')} | "
                    readme += f"{format_priority_cell_with_breakdown(issues, 'Low')} | "
                    readme += f"{format_priority_cell_with_breakdown(issues, 'None')} |\n"

                readme += "\n"
        else:
            modules = organized[area]
            total_issues = sum(len(issues) for issues in modules.values())
            readme += f"**Total Issues:** {total_issues}\n\n"

            # Create table
            readme += "| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |\n"
            readme += "|--------|--------|------------------|---------------|-----------------|--------------|-------------|\n"

            # Sort modules by priority score (highest first)
            sorted_modules = sorted(modules.keys(), key=lambda m: get_priority_score(modules[m]), reverse=True)

            for module in sorted_modules:
                issues = modules[module]

                module_file = module_files[area][module]
                readme += f"| [{module}]({module_file}) | {len(issues)} | "
                readme += f"{format_priority_cell_with_breakdown(issues, 'Highest')} | "
                readme += f"{format_priority_cell_with_breakdown(issues, 'High')} | "
                readme += f"{format_priority_cell_with_breakdown(issues, 'Normal')} | "
                readme += f"{format_priority_cell_with_breakdown(issues, 'Low')} | "
                readme += f"{format_priority_cell_with_breakdown(issues, 'None')} |\n"

            readme += "\n"

    readme += "## Issue Distribution by Priority\n\n"
    for area in area_order:
        if area not in organized:
            continue
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
    for area in area_order:
        if area not in organized:
            continue
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

    # Create issues and priority directories
    issues_dir = Path('issues')
    issues_dir.mkdir(exist_ok=True)

    priority_dir = Path('priority')
    priority_dir.mkdir(exist_ok=True)

    # Collect all Highest and High priority issues
    high_priority_issues = []
    highest_priority_issues = []

    for area in organized:
        if area == 'Area/Connector':
            for category in organized[area]:
                for module in organized[area][category]:
                    for issue in organized[area][category][module]:
                        if issue['priority'] == 'Highest':
                            issue['area'] = area
                            issue['category'] = category
                            issue['module'] = module
                            highest_priority_issues.append(issue)
                        elif issue['priority'] == 'High':
                            issue['area'] = area
                            issue['category'] = category
                            issue['module'] = module
                            high_priority_issues.append(issue)
        else:
            for module in organized[area]:
                for issue in organized[area][module]:
                    if issue['priority'] == 'Highest':
                        issue['area'] = area
                        issue['category'] = None
                        issue['module'] = module
                        highest_priority_issues.append(issue)
                    elif issue['priority'] == 'High':
                        issue['area'] = area
                        issue['category'] = None
                        issue['module'] = module
                        high_priority_issues.append(issue)

    # Generate priority pages
    print("Generating priority pages...")
    if highest_priority_issues:
        generate_priority_page(highest_priority_issues, "Highest", priority_dir)
        print(f"  Created HIGHEST_PRIORITY.md ({len(highest_priority_issues)} issues)")

    if high_priority_issues:
        generate_priority_page(high_priority_issues, "High", priority_dir)
        print(f"  Created HIGH_PRIORITY.md ({len(high_priority_issues)} issues)")

    # Generate module pages
    module_files = {}
    print("\nGenerating module pages...")
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
    priority_count = len([f for f in priority_dir.iterdir() if f.is_file()])
    module_count = len([f for files in module_files.values() for f in (files.values() if isinstance(files, dict) and all(isinstance(v, str) for v in files.values()) else [])])
    print(f"\nTotal files created: {priority_count} priority pages + {module_count} module pages + 1 README")

if __name__ == '__main__':
    main()
