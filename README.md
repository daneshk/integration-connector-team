# integration-connector-team
This is a management repository which maintains the status of the issues. This includes standard libraries, connectors and integration toolings.

**Last Updated:** 2025-10-06 12:33:59 UTC

**Total Open Issues:** 9

## Area/Library (6 issues)

### module/crypto (1 issues)

| # | Title | State | Labels | Assignee |
|---|-------|-------|--------|----------|
| [#8292](https://github.com/ballerina-platform/ballerina-library/issues/8292) | Add support for RSASSA-PSS (PS256) algorithm | open | Type/Improvement | randilt |

### module/http (2 issues)

| # | Title | State | Labels | Assignee |
|---|-------|-------|--------|----------|
| [#8302](https://github.com/ballerina-platform/ballerina-library/issues/8302) | Implement static analysis rule "Avoid directly using database entity records as parameters in HTTP resource methods" in HTTP module | open | Type/Task | nureka-rodrigo |
| [#8301](https://github.com/ballerina-platform/ballerina-library/issues/8301) | Implement static analysis rule "Deserialization should not be vulnerable to injection attacks" in HTTP module | open | Type/Task | nureka-rodrigo |

### Other (3 issues)

| # | Title | State | Labels | Assignee |
|---|-------|-------|--------|----------|
| [#8277](https://github.com/ballerina-platform/ballerina-library/issues/8277) | [Low Priority] Review Library/Connector API docs in BI editor | open | Type/Task, Area/Connector | daneshk |
| [#8276](https://github.com/ballerina-platform/ballerina-library/issues/8276) | [Medium Priority] Review Library/Connector API docs in BI editor | open | Type/Task, Area/Connector | daneshk |
| [#8100](https://github.com/ballerina-platform/ballerina-library/issues/8100) | Some issue without module label | open | Type/Bug | - |

[View all Area/Library issues →](https://github.com/ballerina-platform/ballerina-library/issues?q=is%3Aissue+is%3Aopen+label%3AArea%2FLibrary)

## Area/Connector (2 issues)

| # | Title | State | Labels | Assignee |
|---|-------|-------|--------|----------|
| [#8312](https://github.com/ballerina-platform/ballerina-library/issues/8312) | Prioritize Library and Connector current issues | open | Type/Task | daneshk |
| [#8246](https://github.com/ballerina-platform/ballerina-library/issues/8246) | Salesforce connection issue error is static | open | Type/Bug, module/salesforce | - |

[View all Area/Connector issues →](https://github.com/ballerina-platform/ballerina-library/issues?q=is%3Aissue+is%3Aopen+label%3AArea%2FConnector)

## Area/Tooling (1 issues)

| # | Title | State | Labels | Assignee |
|---|-------|-------|--------|----------|
| [#8315](https://github.com/ballerina-platform/ballerina-library/issues/8315) | Support OpenAPI 3.1.0 client generations | open | Type/Improvement, module/openapi-tools | - |

[View all Area/Tooling issues →](https://github.com/ballerina-platform/ballerina-library/issues?q=is%3Aissue+is%3Aopen+label%3AArea%2FTooling)

---

## How to Update This List

To update the issue list, run:

```bash
python3 update_issues.py
```

**Note:** Set the `GITHUB_TOKEN` environment variable to avoid API rate limits:

```bash
export GITHUB_TOKEN=your_github_token
python3 update_issues.py
```
