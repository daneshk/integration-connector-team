# Ballerina Library Issues Analysis

This repository contains an organized breakdown of open issues from the [ballerina-library](https://github.com/ballerina-platform/ballerina-library) repository.

**Last Updated:** 2025-10-23 15:56:05

## Overall Summary

**Total Issues Across All Areas:** 543

## 🔴 Highest Priority Issues (22)

Critical issues that require immediate attention.

[View all Highest Priority Issues →](priority/HIGHEST_PRIORITY.md)

## 🟠 High Priority Issues (168)

Important issues that should be addressed soon.

[View all High Priority Issues →](priority/HIGH_PRIORITY.md)

---

## Area/Library

**Total Issues:** 336

| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |
|--------|--------|------------------|---------------|-----------------|--------------|-------------|
| [module/http](issues/Area_Library_module_http.md) | 127 | 🔴 **7**<br/><sub>✨3 🚀2 📋2</sub> | 🟠 **36**<br/><sub>🐛19 📚2 ✨7 🚀2 📋6</sub> | 🟡 **9**<br/><sub>🐛3 ✨2 📋4</sub> | 🔵 **74**<br/><sub>🐛7 📚1 ✨58 🚀4 📋4</sub> | ⚪ **1**<br/><sub>📋1</sub> |
| [module/persist](issues/Area_Library_module_persist.md) | 12 | 🔴 **5**<br/><sub>🐛3 ✨2</sub> | 🟠 **2**<br/><sub>🐛1 ✨1</sub> | 0 | 🔵 **4**<br/><sub>✨2 📋2</sub> | ⚪ **1**<br/><sub>📋1</sub> |
| [module/sql](issues/Area_Library_module_sql.md) | 17 | 🔴 **3**<br/><sub>🐛2 ✨1</sub> | 🟠 **9**<br/><sub>🐛4 📚1 ✨3 📋1</sub> | 🟡 **1**<br/><sub>✨1</sub> | 🔵 **4**<br/><sub>✨4</sub> | 0 |
| [module/All](issues/Area_Library_module_All.md) | 12 | 🔴 **1**<br/><sub>📋1</sub> | 🟠 **4**<br/><sub>🐛1 ✨1 🚀1 📋1</sub> | 🟡 **2**<br/><sub>✨1 📋1</sub> | 🔵 **5**<br/><sub>📋5</sub> | 0 |
| [module/crypto](issues/Area_Library_module_crypto.md) | 9 | 🔴 **1**<br/><sub>📋1</sub> | 🟠 **3**<br/><sub>✨2 🚀1</sub> | 0 | 🔵 **5**<br/><sub>✨2 🚀1 📋2</sub> | 0 |
| [module/jwt](issues/Area_Library_module_jwt.md) | 4 | 🔴 **1**<br/><sub>✨1</sub> | 🟠 **2**<br/><sub>✨1 📋1</sub> | 0 | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/grpc](issues/Area_Library_module_grpc.md) | 13 | 0 | 🟠 **7**<br/><sub>🐛4 ✨3</sub> | 🟡 **2**<br/><sub>🚀2</sub> | 🔵 **4**<br/><sub>✨2 🚀1 📋1</sub> | 0 |
| [module/oauth2](issues/Area_Library_module_oauth2.md) | 10 | 0 | 🟠 **4**<br/><sub>🐛1 ✨1 🚀1 📋1</sub> | 🟡 **1**<br/><sub>🚀1</sub> | 🔵 **5**<br/><sub>🐛1 ✨4</sub> | 0 |
| [module/task](issues/Area_Library_module_task.md) | 6 | 0 | 🟠 **4**<br/><sub>✨2 📋2</sub> | 🟡 **1**<br/><sub>🐛1</sub> | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/io](issues/Area_Library_module_io.md) | 7 | 0 | 🟠 **4**<br/><sub>🐛3 📋1</sub> | 0 | 🔵 **3**<br/><sub>✨3</sub> | 0 |
| [module/email](issues/Area_Library_module_email.md) | 3 | 0 | 🟠 **3**<br/><sub>🐛1 ✨2</sub> | 0 | 0 | 0 |
| [module/cache](issues/Area_Library_module_cache.md) | 3 | 0 | 🟠 **2**<br/><sub>✨1 📋1</sub> | 0 | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/time](issues/Area_Library_module_time.md) | 2 | 0 | 🟠 **2**<br/><sub>✨2</sub> | 0 | 0 | 0 |
| [No Module](issues/Area_Library_No_Module.md) | 11 | 0 | 🟠 **1**<br/><sub>🚀1</sub> | 🟡 **4**<br/><sub>✨1 🚀2 ❓1</sub> | 🔵 **6**<br/><sub>🐛1 ✨3 🚀2</sub> | 0 |
| [module/tcp](issues/Area_Library_module_tcp.md) | 4 | 0 | 🟠 **1**<br/><sub>🚀1</sub> | 🟡 **2**<br/><sub>✨2</sub> | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/os](issues/Area_Library_module_os.md) | 3 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 🟡 **2**<br/><sub>✨1 🚀1</sub> | 0 | 0 |
| [module/random](issues/Area_Library_module_random.md) | 3 | 0 | 🟠 **1**<br/><sub>✨1</sub> | 0 | 🔵 **2**<br/><sub>✨1 📋1</sub> | 0 |
| [module/websocket](issues/Area_Library_module_websocket.md) | 3 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 🔵 **2**<br/><sub>✨1 🚀1</sub> | 0 |
| [module/mime](issues/Area_Library_module_mime.md) | 2 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/auth](issues/Area_Library_module_auth.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/constraint](issues/Area_Library_module_constraint.md) | 2 | 0 | 0 | 🟡 **2**<br/><sub>🐛1 ✨1</sub> | 0 | 0 |
| [module/log](issues/Area_Library_module_log.md) | 4 | 0 | 0 | 🟡 **1**<br/><sub>🐛1</sub> | 🔵 **3**<br/><sub>✨1 🚀1 📋1</sub> | 0 |
| [module/ldap](issues/Area_Library_module_ldap.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>🐛1</sub> | 0 | 0 |
| [module/url](issues/Area_Library_module_url.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/graphql](issues/Area_Library_module_graphql.md) | 73 | 0 | 0 | 0 | 🔵 **2**<br/><sub>🚀1 📋1</sub> | ⚪ **71**<br/><sub>🐛9 ✨41 🚀11 📋10</sub> |
| [module/udp](issues/Area_Library_module_udp.md) | 2 | 0 | 0 | 0 | 🔵 **2**<br/><sub>✨2</sub> | 0 |
| [module/websubhub](issues/Area_Library_module_websubhub.md) | 1 | 0 | 0 | 0 | 🔵 **1**<br/><sub>🚀1</sub> | 0 |

## Area/Connector

**Total Issues:** 111

### Handwritten Connectors (67 issues)

| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |
|--------|--------|------------------|---------------|-----------------|--------------|-------------|
| [module/All](issues/Area_Connector_Handwritten_Connectors_module_All.md) | 10 | 🔴 **2**<br/><sub>📋2</sub> | 🟠 **2**<br/><sub>🐛1 📋1</sub> | 🟡 **4**<br/><sub>🐛1 ✨2 📋1</sub> | 🔵 **2**<br/><sub>📋2</sub> | 0 |
| [module/salesforce](issues/Area_Connector_Handwritten_Connectors_module_salesforce.md) | 11 | 🔴 **1**<br/><sub>📚1</sub> | 🟠 **6**<br/><sub>🐛2 📚1 ✨3</sub> | 🟡 **2**<br/><sub>✨2</sub> | 🔵 **2**<br/><sub>✨1 🚀1</sub> | 0 |
| [module/mysql](issues/Area_Connector_Handwritten_Connectors_module_mysql.md) | 8 | 🔴 **1**<br/><sub>🐛1</sub> | 🟠 **6**<br/><sub>🐛3 ✨2 📋1</sub> | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/mongodb](issues/Area_Connector_Handwritten_Connectors_module_mongodb.md) | 4 | 0 | 🟠 **4**<br/><sub>🐛1 📚1 ✨2</sub> | 0 | 0 | 0 |
| [module/postgresql](issues/Area_Connector_Handwritten_Connectors_module_postgresql.md) | 4 | 0 | 🟠 **4**<br/><sub>🐛3 ✨1</sub> | 0 | 0 | 0 |
| [module/mssql](issues/Area_Connector_Handwritten_Connectors_module_mssql.md) | 3 | 0 | 🟠 **3**<br/><sub>🐛2 ✨1</sub> | 0 | 0 | 0 |
| [module/aws-s3](issues/Area_Connector_Handwritten_Connectors_module_aws-s3.md) | 5 | 0 | 🟠 **2**<br/><sub>🐛1 🚀1</sub> | 🟡 **3**<br/><sub>✨3</sub> | 0 | 0 |
| [module/sap](issues/Area_Connector_Handwritten_Connectors_module_sap.md) | 3 | 0 | 🟠 **2**<br/><sub>🚀2</sub> | 0 | 🔵 **1**<br/><sub>💡1</sub> | 0 |
| [module/s4hana](issues/Area_Connector_Handwritten_Connectors_module_s4hana.md) | 2 | 0 | 🟠 **2**<br/><sub>🚀2</sub> | 0 | 0 | 0 |
| [module/oracledb](issues/Area_Connector_Handwritten_Connectors_module_oracledb.md) | 2 | 0 | 🟠 **1**<br/><sub>✨1</sub> | 0 | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/persist.redis](issues/Area_Connector_Handwritten_Connectors_module_persist.redis.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/azure-storageservice](issues/Area_Connector_Handwritten_Connectors_module_azure-storageservice.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/cdata](issues/Area_Connector_Handwritten_Connectors_module_cdata.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/redis](issues/Area_Connector_Handwritten_Connectors_module_redis.md) | 4 | 0 | 0 | 🟡 **3**<br/><sub>✨1 🚀2</sub> | 🔵 **1**<br/><sub>🚀1</sub> | 0 |
| [module/aws.secretmanager](issues/Area_Connector_Handwritten_Connectors_module_aws.secretmanager.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [No Module](issues/Area_Connector_Handwritten_Connectors_No_Module.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>🚀1</sub> | 0 | 0 |
| [module/cosmosdb](issues/Area_Connector_Handwritten_Connectors_module_cosmosdb.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/sap.jco](issues/Area_Connector_Handwritten_Connectors_module_sap.jco.md) | 2 | 0 | 0 | 0 | 🔵 **2**<br/><sub>✨1 💡1</sub> | 0 |
| [module/java.jdbc](issues/Area_Connector_Handwritten_Connectors_module_java.jdbc.md) | 2 | 0 | 0 | 0 | 🔵 **2**<br/><sub>🐛1 ✨1</sub> | 0 |
| [module/aws.marketplace.mpm](issues/Area_Connector_Handwritten_Connectors_module_aws.marketplace.mpm.md) | 1 | 0 | 0 | 0 | 🔵 **1**<br/><sub>✨1</sub> | 0 |

### Generated Connectors (44 issues)

| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |
|--------|--------|------------------|---------------|-----------------|--------------|-------------|
| [No Module](issues/Area_Connector_Generated_Connectors_No_Module.md) | 16 | 0 | 🟠 **2**<br/><sub>🐛2</sub> | 🟡 **14**<br/><sub>✨1 🚀13</sub> | 0 | 0 |
| [module/sap](issues/Area_Connector_Generated_Connectors_module_sap.md) | 3 | 0 | 🟠 **3**<br/><sub>📋3</sub> | 0 | 0 | 0 |
| [module/github](issues/Area_Connector_Generated_Connectors_module_github.md) | 3 | 0 | 🟠 **3**<br/><sub>🐛1 📋2</sub> | 0 | 0 | 0 |
| [module/All](issues/Area_Connector_Generated_Connectors_module_All.md) | 2 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/twilio](issues/Area_Connector_Generated_Connectors_module_twilio.md) | 2 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 🟡 **1**<br/><sub>📋1</sub> | 0 | 0 |
| [module/sap.concur](issues/Area_Connector_Generated_Connectors_module_sap.concur.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/sap.sf](issues/Area_Connector_Generated_Connectors_module_sap.sf.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/zoom.meetings](issues/Area_Connector_Generated_Connectors_module_zoom.meetings.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/googleapis.drive](issues/Area_Connector_Generated_Connectors_module_googleapis.drive.md) | 1 | 0 | 🟠 **1**<br/><sub>✨1</sub> | 0 | 0 | 0 |
| [module/slack](issues/Area_Connector_Generated_Connectors_module_slack.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/dropbox](issues/Area_Connector_Generated_Connectors_module_dropbox.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/twitter](issues/Area_Connector_Generated_Connectors_module_twitter.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/candid](issues/Area_Connector_Generated_Connectors_module_candid.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/cosmosdb](issues/Area_Connector_Generated_Connectors_module_cosmosdb.md) | 1 | 0 | 🟠 **1**<br/><sub>✨1</sub> | 0 | 0 | 0 |
| [module/googleapis.sheets](issues/Area_Connector_Generated_Connectors_module_googleapis.sheets.md) | 3 | 0 | 0 | 🟡 **3**<br/><sub>🐛1 ✨2</sub> | 0 | 0 |
| [module/discord](issues/Area_Connector_Generated_Connectors_module_discord.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/servicenow](issues/Area_Connector_Generated_Connectors_module_servicenow.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/googleapis.gmail](issues/Area_Connector_Generated_Connectors_module_googleapis.gmail.md) | 3 | 0 | 0 | 0 | 🔵 **3**<br/><sub>✨3</sub> | 0 |
| [module/microsoft.dynamics365](issues/Area_Connector_Generated_Connectors_module_microsoft.dynamics365.md) | 1 | 0 | 0 | 0 | 🔵 **1**<br/><sub>🚀1</sub> | 0 |

## Area/Tooling

**Total Issues:** 96

| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |
|--------|--------|------------------|---------------|-----------------|--------------|-------------|
| [module/openapi-tools](issues/Area_Tooling_module_openapi-tools.md) | 51 | 0 | 🟠 **13**<br/><sub>🐛4 ✨3 📋6</sub> | 🟡 **15**<br/><sub>🐛4 ✨9 📋2</sub> | 🔵 **22**<br/><sub>🐛1 ✨16 🚀1 📋4</sub> | ⚪ **1**<br/><sub>✨1</sub> |
| [module/persist-tools](issues/Area_Tooling_module_persist-tools.md) | 8 | 0 | 🟠 **6**<br/><sub>🐛3 📋3</sub> | 🟡 **1**<br/><sub>✨1</sub> | 🔵 **1**<br/><sub>🚀1</sub> | 0 |
| [module/protoc-tool](issues/Area_Tooling_module_protoc-tool.md) | 4 | 0 | 🟠 **2**<br/><sub>🐛1 📋1</sub> | 🟡 **1**<br/><sub>🐛1</sub> | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/xsd-tool](issues/Area_Tooling_module_xsd-tool.md) | 2 | 0 | 🟠 **2**<br/><sub>🐛2</sub> | 0 | 0 | 0 |
| [module/graphql-tool](issues/Area_Tooling_module_graphql-tool.md) | 24 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 🟡 **2**<br/><sub>✨2</sub> | 🔵 **1**<br/><sub>✨1</sub> | ⚪ **20**<br/><sub>🐛3 📚1 ✨12 🚀2 📋2</sub> |
| [module/grpc](issues/Area_Tooling_module_grpc.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/wsdl-tools](issues/Area_Tooling_module_wsdl-tools.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>🚀1</sub> | 0 | 0 |
| [module/asyncapi-tools](issues/Area_Tooling_module_asyncapi-tools.md) | 2 | 0 | 0 | 0 | 0 | ⚪ **2**<br/><sub>🐛1 📋1</sub> |
| [module/copybook](issues/Area_Tooling_module_copybook.md) | 3 | 0 | 0 | 0 | 0 | ⚪ **3**<br/><sub>✨1 🚀1 📋1</sub> |

## Issue Distribution by Priority

### Area/Library
- **Highest Priority:** 18
- **High Priority:** 89
- **Normal Priority:** 29
- **Low Priority:** 127
- **No Priority:** 73
- **Total:** 336

### Area/Connector
- **Highest Priority:** 4
- **High Priority:** 54
- **Normal Priority:** 37
- **Low Priority:** 16
- **Total:** 111

### Area/Tooling
- **High Priority:** 25
- **Normal Priority:** 20
- **Low Priority:** 25
- **No Priority:** 26
- **Total:** 96

## Issue Distribution by Type

### Area/Library
- **Bug:** 67
- **Docs:** 4
- **Improvement:** 173
- **NewFeature:** 38
- **Task:** 53
- **Unknown:** 1
- **Total:** 336

### Area/Connector
- **Bug:** 26
- **Docs:** 3
- **Improvement:** 37
- **NewFeature:** 24
- **Proposal:** 2
- **Task:** 19
- **Total:** 111

### Area/Tooling
- **Bug:** 21
- **Docs:** 1
- **Improvement:** 47
- **NewFeature:** 6
- **Task:** 21
- **Total:** 96

