# integration-connector-team
This is a management repository which maintains the status of the issues. This includes standard libraries, connectors and integration toolings.

**Last Updated:** 2025-10-06 12:13:55 UTC

**Total Open Issues:** 15

## Area/Library (5 issues)

| # | Title | State | Labels | Assignee |
|---|-------|-------|--------|----------|
| [#8302](https://github.com/ballerina-platform/ballerina-library/issues/8302) | Implement static analysis rule "Avoid directly using database entity records as parameters in HTTP resource methods" in HTTP module | open | Type/Task, module/http... | nureka-rodrigo |
| [#8301](https://github.com/ballerina-platform/ballerina-library/issues/8301) | Implement static analysis rule "Deserialization should not be vulnerable to injection attacks" in HTTP module | open | Type/Task, module/http... | nureka-rodrigo |
| [#8292](https://github.com/ballerina-platform/ballerina-library/issues/8292) | Add support for RSASSA-PSS (PS256) algorithm | open | Type/Improvement, module/crypto | randilt |
| [#8277](https://github.com/ballerina-platform/ballerina-library/issues/8277) | [Low Priority] Review Library/Connector API docs in BI editor | open | Type/Task, Area/Connector | daneshk |
| [#8276](https://github.com/ballerina-platform/ballerina-library/issues/8276) | [Medium Priority] Review Library/Connector API docs in BI editor | open | Type/Task, Area/Connector | daneshk |

[View all Area/Library issues →](https://github.com/ballerina-platform/ballerina-library/issues?q=is%3Aissue+is%3Aopen+label%3AArea%2FLibrary)

## Area/Connector (5 issues)

| # | Title | State | Labels | Assignee |
|---|-------|-------|--------|----------|
| [#8312](https://github.com/ballerina-platform/ballerina-library/issues/8312) | Prioritize Library and Connector current issues | open | Type/Task | daneshk |
| [#8277](https://github.com/ballerina-platform/ballerina-library/issues/8277) | [Low Priority] Review Library/Connector API docs in BI editor | open | Type/Task, Area/Library | daneshk |
| [#8276](https://github.com/ballerina-platform/ballerina-library/issues/8276) | [Medium Priority] Review Library/Connector API docs in BI editor | open | Type/Task, Area/Library | daneshk |
| [#8275](https://github.com/ballerina-platform/ballerina-library/issues/8275) | [High Priority] Review Library/Connector API docs in BI editor | open | Type/Task, module/All... | daneshk |
| [#8246](https://github.com/ballerina-platform/ballerina-library/issues/8246) | Salesforce connection issue error is static | open | Type/Bug, module/salesforce | - |

[View all Area/Connector issues →](https://github.com/ballerina-platform/ballerina-library/issues?q=is%3Aissue+is%3Aopen+label%3AArea%2FConnector)

## Area/Tooling (5 issues)

| # | Title | State | Labels | Assignee |
|---|-------|-------|--------|----------|
| [#8315](https://github.com/ballerina-platform/ballerina-library/issues/8315) | Support OpenAPI 3.1.0 client generations | open | Type/Improvement, module/openapi-tools | - |
| [#8244](https://github.com/ballerina-platform/ballerina-library/issues/8244) | Restructure OpenAPI tool repository to a multi-repository | open | Type/Task, module/openapi-tools | TharmiganK |
| [#8242](https://github.com/ballerina-platform/ballerina-library/issues/8242) | Enable the Disabled Tests in Persist Tools | open | Type/Task, module/persist-tools | daneshk |
| [#8229](https://github.com/ballerina-platform/ballerina-library/issues/8229) | NullPointerException in Ballerina GraphQL client code generation during formatting (CLASS_DEFINITION | open | Type/Bug, module/graphql-tool | - |
| [#8217](https://github.com/ballerina-platform/ballerina-library/issues/8217) | Unaligned type name with spaces | open | Type/Bug, module/openapi-tools | - |

[View all Area/Tooling issues →](https://github.com/ballerina-platform/ballerina-library/issues?q=is%3Aissue+is%3Aopen+label%3AArea%2FTooling)

---

## How to Update This List

To fetch and update the issue list with the latest data, run:

```bash
python3 update_issues.py
```

**Requirements:**
- Python 3.6+
- GitHub Personal Access Token (to avoid API rate limits)

```bash
export GITHUB_TOKEN=your_github_token
python3 update_issues.py
```

The script will fetch the latest issues from the [ballerina-library repository](https://github.com/ballerina-platform/ballerina-library) and update this README with a detailed table.
