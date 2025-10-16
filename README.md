# Ballerina Library Issues Analysis

This repository contains an organized breakdown of open issues from the [ballerina-library](https://github.com/ballerina-platform/ballerina-library) repository.

**Last Updated:** 2025-10-16 15:53:23

## Overall Summary

**Total Issues Across All Areas:** 706

## Area/Library

**Total Issues:** 443

| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |
|--------|--------|------------------|---------------|-----------------|--------------|-------------|
| [module/http](issues/Area_Library_module_http.md) | 166 | 🔴 **2**<br/><sub>📋2</sub> | 🟠 **51**<br/><sub>🐛18 📚2 ✨10 🚀3 📋18</sub> | 🟡 **12**<br/><sub>🐛3 ✨1 📋8</sub> | 🔵 **101**<br/><sub>🐛7 ✨72 🚀8 📋14</sub> | 0 |
| [module/persist](issues/Area_Library_module_persist.md) | 17 | 🔴 **2**<br/><sub>🐛1 ✨1</sub> | 🟠 **6**<br/><sub>🐛4 ✨2</sub> | 0 | 🔵 **9**<br/><sub>✨2 🚀3 📋4</sub> | 0 |
| [module/crypto](issues/Area_Library_module_crypto.md) | 12 | 🔴 **2**<br/><sub>📋2</sub> | 🟠 **4**<br/><sub>✨2 🚀1 📋1</sub> | 0 | 🔵 **6**<br/><sub>✨2 🚀2 📋2</sub> | 0 |
| [module/sql](issues/Area_Library_module_sql.md) | 23 | 🔴 **1**<br/><sub>✨1</sub> | 🟠 **13**<br/><sub>🐛7 📚1 ✨3 📋2</sub> | 🟡 **1**<br/><sub>✨1</sub> | 🔵 **7**<br/><sub>✨7</sub> | ⚪ **1**<br/><sub>✨1</sub> |
| [module/grpc](issues/Area_Library_module_grpc.md) | 30 | 🔴 **1**<br/><sub>📋1</sub> | 🟠 **11**<br/><sub>🐛4 ✨3 📋4</sub> | 🟡 **2**<br/><sub>🚀2</sub> | 🔵 **16**<br/><sub>✨8 🚀2 📋6</sub> | 0 |
| [module/All](issues/Area_Library_module_All.md) | 17 | 🔴 **1**<br/><sub>📋1</sub> | 🟠 **5**<br/><sub>🐛1 ✨1 🚀1 📋2</sub> | 🟡 **2**<br/><sub>✨1 📋1</sub> | 🔵 **9**<br/><sub>📋9</sub> | 0 |
| [module/jwt](issues/Area_Library_module_jwt.md) | 5 | 🔴 **1**<br/><sub>✨1</sub> | 🟠 **2**<br/><sub>✨1 📋1</sub> | 0 | 🔵 **2**<br/><sub>✨2</sub> | 0 |
| [module/email](issues/Area_Library_module_email.md) | 8 | 0 | 🟠 **5**<br/><sub>🐛1 ✨4</sub> | 0 | 🔵 **3**<br/><sub>✨1 🚀1 📋1</sub> | 0 |
| [module/oauth2](issues/Area_Library_module_oauth2.md) | 12 | 0 | 🟠 **4**<br/><sub>🐛1 ✨1 🚀1 📋1</sub> | 🟡 **1**<br/><sub>🚀1</sub> | 🔵 **7**<br/><sub>🐛1 ✨5 📋1</sub> | 0 |
| [module/task](issues/Area_Library_module_task.md) | 6 | 0 | 🟠 **4**<br/><sub>✨2 📋2</sub> | 🟡 **1**<br/><sub>🐛1</sub> | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/io](issues/Area_Library_module_io.md) | 8 | 0 | 🟠 **3**<br/><sub>🐛2 📋1</sub> | 0 | 🔵 **5**<br/><sub>✨4 🚀1</sub> | 0 |
| [module/os](issues/Area_Library_module_os.md) | 6 | 0 | 🟠 **2**<br/><sub>🐛1 ✨1</sub> | 🟡 **2**<br/><sub>✨1 🚀1</sub> | 🔵 **2**<br/><sub>✨1 📋1</sub> | 0 |
| [module/log](issues/Area_Library_module_log.md) | 8 | 0 | 🟠 **2**<br/><sub>🐛2</sub> | 🟡 **1**<br/><sub>🐛1</sub> | 🔵 **5**<br/><sub>✨2 🚀2 📋1</sub> | 0 |
| [module/cache](issues/Area_Library_module_cache.md) | 3 | 0 | 🟠 **2**<br/><sub>✨1 📋1</sub> | 0 | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/time](issues/Area_Library_module_time.md) | 2 | 0 | 🟠 **2**<br/><sub>✨2</sub> | 0 | 0 | 0 |
| [No Module](issues/Area_Library_No_Module.md) | 14 | 0 | 🟠 **1**<br/><sub>🚀1</sub> | 🟡 **3**<br/><sub>✨1 🚀1 ❓1</sub> | 🔵 **9**<br/><sub>🐛1 📚1 ✨3 🚀4</sub> | ⚪ **1**<br/><sub>🚀1</sub> |
| [module/tcp](issues/Area_Library_module_tcp.md) | 7 | 0 | 🟠 **1**<br/><sub>🚀1</sub> | 🟡 **3**<br/><sub>✨2 🚀1</sub> | 🔵 **3**<br/><sub>✨2 📋1</sub> | 0 |
| [module/udp](issues/Area_Library_module_udp.md) | 4 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 🔵 **3**<br/><sub>✨2 🚀1</sub> | 0 |
| [module/random](issues/Area_Library_module_random.md) | 3 | 0 | 🟠 **1**<br/><sub>✨1</sub> | 0 | 🔵 **2**<br/><sub>✨2</sub> | 0 |
| [module/websocket](issues/Area_Library_module_websocket.md) | 3 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 🔵 **2**<br/><sub>✨1 🚀1</sub> | 0 |
| [module/mime](issues/Area_Library_module_mime.md) | 2 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/auth](issues/Area_Library_module_auth.md) | 2 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 🔵 **1**<br/><sub>🚀1</sub> | 0 |
| [module/constraint](issues/Area_Library_module_constraint.md) | 4 | 0 | 0 | 🟡 **2**<br/><sub>🐛1 ✨1</sub> | 🔵 **2**<br/><sub>✨1 📋1</sub> | 0 |
| [module/ldap](issues/Area_Library_module_ldap.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>🐛1</sub> | 0 | 0 |
| [module/url](issues/Area_Library_module_url.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/xslt](issues/Area_Library_module_xslt.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>📋1</sub> | 0 | 0 |
| [module/graphql](issues/Area_Library_module_graphql.md) | 76 | 0 | 0 | 0 | 🔵 **3**<br/><sub>🚀1 📋2</sub> | ⚪ **73**<br/><sub>🐛9 ✨42 🚀11 📋11</sub> |
| [module/websubhub](issues/Area_Library_module_websubhub.md) | 1 | 0 | 0 | 0 | 🔵 **1**<br/><sub>🚀1</sub> | 0 |
| [module/protobuf](issues/Area_Library_module_protobuf.md) | 1 | 0 | 0 | 0 | 🔵 **1**<br/><sub>✨1</sub> | 0 |

## Area/Connector

**Total Issues:** 159

### Handwritten Connectors (105 issues)

| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |
|--------|--------|------------------|---------------|-----------------|--------------|-------------|
| [module/All](issues/Area_Connector_Handwritten_Connectors_module_All.md) | 13 | 🔴 **2**<br/><sub>📋2</sub> | 🟠 **2**<br/><sub>🐛1 📋1</sub> | 🟡 **4**<br/><sub>🐛1 ✨2 📋1</sub> | 🔵 **5**<br/><sub>📋5</sub> | 0 |
| [module/salesforce](issues/Area_Connector_Handwritten_Connectors_module_salesforce.md) | 12 | 🔴 **1**<br/><sub>📚1</sub> | 🟠 **6**<br/><sub>🐛2 📚1 ✨3</sub> | 🟡 **3**<br/><sub>✨2 📋1</sub> | 🔵 **2**<br/><sub>✨1 🚀1</sub> | 0 |
| [module/mysql](issues/Area_Connector_Handwritten_Connectors_module_mysql.md) | 11 | 🔴 **1**<br/><sub>🐛1</sub> | 🟠 **6**<br/><sub>🐛3 ✨2 📋1</sub> | 🟡 **1**<br/><sub>✨1</sub> | 🔵 **3**<br/><sub>📋3</sub> | 0 |
| [module/sap](issues/Area_Connector_Handwritten_Connectors_module_sap.md) | 7 | 0 | 🟠 **6**<br/><sub>🚀3 📋3</sub> | 0 | 🔵 **1**<br/><sub>💡1</sub> | 0 |
| [module/postgresql](issues/Area_Connector_Handwritten_Connectors_module_postgresql.md) | 7 | 0 | 🟠 **4**<br/><sub>🐛3 ✨1</sub> | 0 | 🔵 **3**<br/><sub>📋3</sub> | 0 |
| [module/mongodb](issues/Area_Connector_Handwritten_Connectors_module_mongodb.md) | 4 | 0 | 🟠 **4**<br/><sub>🐛1 📚1 ✨2</sub> | 0 | 0 | 0 |
| [module/s4hana](issues/Area_Connector_Handwritten_Connectors_module_s4hana.md) | 4 | 0 | 🟠 **4**<br/><sub>🚀3 📋1</sub> | 0 | 0 | 0 |
| [module/mssql](issues/Area_Connector_Handwritten_Connectors_module_mssql.md) | 6 | 0 | 🟠 **3**<br/><sub>🐛2 ✨1</sub> | 0 | 🔵 **3**<br/><sub>🚀1 📋2</sub> | 0 |
| [module/aws-s3](issues/Area_Connector_Handwritten_Connectors_module_aws-s3.md) | 5 | 0 | 🟠 **2**<br/><sub>🐛1 🚀1</sub> | 🟡 **3**<br/><sub>✨3</sub> | 0 | 0 |
| [module/oracledb](issues/Area_Connector_Handwritten_Connectors_module_oracledb.md) | 8 | 0 | 🟠 **1**<br/><sub>✨1</sub> | 0 | 🔵 **7**<br/><sub>✨1 🚀3 📋3</sub> | 0 |
| [module/persist.redis](issues/Area_Connector_Handwritten_Connectors_module_persist.redis.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/azure-storageservice](issues/Area_Connector_Handwritten_Connectors_module_azure-storageservice.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/cdata](issues/Area_Connector_Handwritten_Connectors_module_cdata.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [No Module](issues/Area_Connector_Handwritten_Connectors_No_Module.md) | 6 | 0 | 0 | 🟡 **5**<br/><sub>🚀5</sub> | 🔵 **1**<br/><sub>🚀1</sub> | 0 |
| [module/redis](issues/Area_Connector_Handwritten_Connectors_module_redis.md) | 6 | 0 | 0 | 🟡 **3**<br/><sub>✨1 🚀2</sub> | 🔵 **3**<br/><sub>🚀3</sub> | 0 |
| [module/cosmosdb](issues/Area_Connector_Handwritten_Connectors_module_cosmosdb.md) | 3 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 🔵 **1**<br/><sub>📚1</sub> | ⚪ **1**<br/><sub>📋1</sub> |
| [module/aws.secretmanager](issues/Area_Connector_Handwritten_Connectors_module_aws.secretmanager.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/netsuite](issues/Area_Connector_Handwritten_Connectors_module_netsuite.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/java.jdbc](issues/Area_Connector_Handwritten_Connectors_module_java.jdbc.md) | 4 | 0 | 0 | 0 | 🔵 **4**<br/><sub>🐛1 ✨1 📋2</sub> | 0 |
| [module/sap.jco](issues/Area_Connector_Handwritten_Connectors_module_sap.jco.md) | 2 | 0 | 0 | 0 | 🔵 **2**<br/><sub>✨1 💡1</sub> | 0 |
| [module/aws.marketplace.mpm](issues/Area_Connector_Handwritten_Connectors_module_aws.marketplace.mpm.md) | 1 | 0 | 0 | 0 | 🔵 **1**<br/><sub>✨1</sub> | 0 |
| [module/business-central](issues/Area_Connector_Handwritten_Connectors_module_business-central.md) | 1 | 0 | 0 | 0 | 🔵 **1**<br/><sub>📋1</sub> | 0 |

### Generated Connectors (54 issues)

| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |
|--------|--------|------------------|---------------|-----------------|--------------|-------------|
| [No Module](issues/Area_Connector_Generated_Connectors_No_Module.md) | 18 | 0 | 🟠 **2**<br/><sub>🐛2</sub> | 🟡 **16**<br/><sub>✨1 🚀15</sub> | 0 | 0 |
| [module/sap](issues/Area_Connector_Generated_Connectors_module_sap.md) | 3 | 0 | 🟠 **3**<br/><sub>📋3</sub> | 0 | 0 | 0 |
| [module/github](issues/Area_Connector_Generated_Connectors_module_github.md) | 3 | 0 | 🟠 **3**<br/><sub>🐛1 📋2</sub> | 0 | 0 | 0 |
| [module/googleapis.drive](issues/Area_Connector_Generated_Connectors_module_googleapis.drive.md) | 2 | 0 | 🟠 **2**<br/><sub>✨1 📋1</sub> | 0 | 0 | 0 |
| [module/zuora](issues/Area_Connector_Generated_Connectors_module_zuora.md) | 2 | 0 | 🟠 **2**<br/><sub>📋2</sub> | 0 | 0 | 0 |
| [module/All](issues/Area_Connector_Generated_Connectors_module_All.md) | 2 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 🟡 **1**<br/><sub>📋1</sub> | 0 | 0 |
| [module/twilio](issues/Area_Connector_Generated_Connectors_module_twilio.md) | 2 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 🟡 **1**<br/><sub>📋1</sub> | 0 | 0 |
| [module/microsoft-excel](issues/Area_Connector_Generated_Connectors_module_microsoft-excel.md) | 3 | 0 | 🟠 **1**<br/><sub>✨1</sub> | 0 | 🔵 **2**<br/><sub>📋2</sub> | 0 |
| [module/sap.concur](issues/Area_Connector_Generated_Connectors_module_sap.concur.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/sap.sf](issues/Area_Connector_Generated_Connectors_module_sap.sf.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/zoom.meetings](issues/Area_Connector_Generated_Connectors_module_zoom.meetings.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/slack](issues/Area_Connector_Generated_Connectors_module_slack.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/dropbox](issues/Area_Connector_Generated_Connectors_module_dropbox.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/twitter](issues/Area_Connector_Generated_Connectors_module_twitter.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/candid](issues/Area_Connector_Generated_Connectors_module_candid.md) | 1 | 0 | 🟠 **1**<br/><sub>📋1</sub> | 0 | 0 | 0 |
| [module/cosmosdb](issues/Area_Connector_Generated_Connectors_module_cosmosdb.md) | 1 | 0 | 🟠 **1**<br/><sub>✨1</sub> | 0 | 0 | 0 |
| [module/googleapis.sheets](issues/Area_Connector_Generated_Connectors_module_googleapis.sheets.md) | 4 | 0 | 0 | 🟡 **4**<br/><sub>🐛1 ✨2 📋1</sub> | 0 | 0 |
| [module/discord](issues/Area_Connector_Generated_Connectors_module_discord.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/servicenow](issues/Area_Connector_Generated_Connectors_module_servicenow.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>✨1</sub> | 0 | 0 |
| [module/googleapis.gmail](issues/Area_Connector_Generated_Connectors_module_googleapis.gmail.md) | 3 | 0 | 0 | 0 | 🔵 **3**<br/><sub>✨3</sub> | 0 |
| [module/microsoft.dynamics365](issues/Area_Connector_Generated_Connectors_module_microsoft.dynamics365.md) | 1 | 0 | 0 | 0 | 🔵 **1**<br/><sub>🚀1</sub> | 0 |
| [module/microsoft-onedrive](issues/Area_Connector_Generated_Connectors_module_microsoft-onedrive.md) | 1 | 0 | 0 | 0 | 🔵 **1**<br/><sub>📋1</sub> | 0 |

## Area/Tooling

**Total Issues:** 104

| Module | Issues | Priority Highest | Priority High | Priority Normal | Priority Low | No Priority |
|--------|--------|------------------|---------------|-----------------|--------------|-------------|
| [module/openapi-tools](issues/Area_Tooling_module_openapi-tools.md) | 52 | 0 | 🟠 **12**<br/><sub>🐛3 ✨3 📋6</sub> | 🟡 **17**<br/><sub>🐛4 ✨10 📋3</sub> | 🔵 **22**<br/><sub>🐛1 ✨16 🚀1 📋4</sub> | ⚪ **1**<br/><sub>✨1</sub> |
| [module/persist-tools](issues/Area_Tooling_module_persist-tools.md) | 9 | 0 | 🟠 **6**<br/><sub>🐛3 📋3</sub> | 🟡 **2**<br/><sub>✨1 📋1</sub> | 🔵 **1**<br/><sub>🚀1</sub> | 0 |
| [module/protoc-tool](issues/Area_Tooling_module_protoc-tool.md) | 7 | 0 | 🟠 **3**<br/><sub>🐛1 ✨1 📋1</sub> | 🟡 **1**<br/><sub>🐛1</sub> | 🔵 **2**<br/><sub>✨2</sub> | ⚪ **1**<br/><sub>📋1</sub> |
| [module/graphql-tool](issues/Area_Tooling_module_graphql-tool.md) | 28 | 0 | 🟠 **2**<br/><sub>📋2</sub> | 🟡 **3**<br/><sub>✨2 📋1</sub> | 🔵 **1**<br/><sub>✨1</sub> | ⚪ **22**<br/><sub>🐛3 📚1 ✨12 🚀2 📋4</sub> |
| [module/xsd-tool](issues/Area_Tooling_module_xsd-tool.md) | 2 | 0 | 🟠 **2**<br/><sub>🐛2</sub> | 0 | 0 | 0 |
| [module/grpc](issues/Area_Tooling_module_grpc.md) | 1 | 0 | 🟠 **1**<br/><sub>🐛1</sub> | 0 | 0 | 0 |
| [module/wsdl-tools](issues/Area_Tooling_module_wsdl-tools.md) | 1 | 0 | 0 | 🟡 **1**<br/><sub>🚀1</sub> | 0 | 0 |
| [module/copybook](issues/Area_Tooling_module_copybook.md) | 4 | 0 | 0 | 0 | 0 | ⚪ **4**<br/><sub>✨1 🚀1 📋2</sub> |

## Issue Distribution by Priority

### Area/Library
- **Highest Priority:** 10
- **High Priority:** 123
- **Normal Priority:** 33
- **Low Priority:** 202
- **No Priority:** 75
- **Total:** 443

### Area/Connector
- **Highest Priority:** 4
- **High Priority:** 64
- **Normal Priority:** 46
- **Low Priority:** 44
- **No Priority:** 1
- **Total:** 159

### Area/Tooling
- **High Priority:** 26
- **Normal Priority:** 24
- **Low Priority:** 26
- **No Priority:** 28
- **Total:** 104

## Issue Distribution by Type

### Area/Library
- **Bug:** 68
- **Docs:** 4
- **Improvement:** 210
- **NewFeature:** 54
- **Task:** 106
- **Unknown:** 1
- **Total:** 443

### Area/Connector
- **Bug:** 26
- **Docs:** 4
- **Improvement:** 38
- **NewFeature:** 39
- **Proposal:** 2
- **Task:** 50
- **Total:** 159

### Area/Tooling
- **Bug:** 19
- **Docs:** 1
- **Improvement:** 50
- **NewFeature:** 6
- **Task:** 28
- **Total:** 104

