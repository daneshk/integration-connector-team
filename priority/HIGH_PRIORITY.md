# 🟠 High Priority Issues

**Total Issues:** 163

## Area/Library

### 📦 module/http (36 issues)

#### 🐛 Bug

- **[#8339](https://github.com/ballerina-platform/ballerina-library/issues/8339)** Investigate possible thread blocked issues in SSE services
- **[#7893](https://github.com/ballerina-platform/ballerina-library/issues/7893)** HTTP compile error when referring a listener in different file in a service
- **[#7727](https://github.com/ballerina-platform/ballerina-library/issues/7727)** Getting a compilation error when using `http:ServiceContract`
- **[#7512](https://github.com/ballerina-platform/ballerina-library/issues/7512)** Http POST resource functions can define more than one payload parameters
- **[#7298](https://github.com/ballerina-platform/ballerina-library/issues/7298)** Error when use getJsonPayload method and Client.forward() over https
- **[#7292](https://github.com/ballerina-platform/ballerina-library/issues/7292)** Error in data binding with the URL encoded content-type with charset directive
- **[#6663](https://github.com/ballerina-platform/ballerina-library/issues/6663)** h2-h2 load test with h1 client hanging after sometime
- **[#5962](https://github.com/ballerina-platform/ballerina-library/issues/5962)** HTTP compiler failed when we have a default value for payload parameter
- **[#5894](https://github.com/ballerina-platform/ballerina-library/issues/5894)** Defaultable header parameters in the HTTP resource is not considered as optional
- **[#5085](https://github.com/ballerina-platform/ballerina-library/issues/5085)** HTTP compiler validations are not working for isolated service
- **[#4915](https://github.com/ballerina-platform/ballerina-library/issues/4915)** Intermittent test failure: `testRequestInterceptorCtxNext`
- **[#4461](https://github.com/ballerina-platform/ballerina-library/issues/4461)** Enable testHttp2InvalidHeaderLength testcase.
- **[#4671](https://github.com/ballerina-platform/ballerina-library/issues/4671)** [Bug] Reading a byte stream from a backend hangs in the passthrough
- **[#3318](https://github.com/ballerina-platform/ballerina-library/issues/3318)** [Windows] Test failure : testAuthnError
- **[#3250](https://github.com/ballerina-platform/ballerina-library/issues/3250)** [Windows] Test failure `testSslClientFallbackFromH2ToH1`
- **[#3138](https://github.com/ballerina-platform/ballerina-library/issues/3138)** H2ConnectionPoolWithPriorKnowledge intermittent test failure
- **[#2886](https://github.com/ballerina-platform/ballerina-library/issues/2886)** Issue when sending a curl request to the WebSocket service
- **[#317](https://github.com/ballerina-platform/ballerina-library/issues/317)** [Windows] Intermittent transport test failures
- **[#501](https://github.com/ballerina-platform/ballerina-library/issues/501)** [HTTP][CORS] Exact value origin match fails

#### 📚 Docs

- **[#2710](https://github.com/ballerina-platform/ballerina-library/issues/2710)** [http] Documentation for the `http:Payload` annotation is inadequate
- **[#2521](https://github.com/ballerina-platform/ballerina-library/issues/2521)** Lack of Documentation for enabling/configuring `Trace logs` and `Access logs` in the API Docs

#### ✨ Improvement

- **[#6110](https://github.com/ballerina-platform/ballerina-library/issues/6110)** [WIP] Review the `nil` return from interceptors via `RequestContext:next()`
- **[#5885](https://github.com/ballerina-platform/ballerina-library/issues/5885)** Http Client error does not contain the full stacktrace.
- **[#4092](https://github.com/ballerina-platform/ballerina-library/issues/4092)** Ability to configure resource level `ResponseErrorInterceptor` 
- **[#3939](https://github.com/ballerina-platform/ballerina-library/issues/3939)** Client side compression should be improved
- **[#2420](https://github.com/ballerina-platform/ballerina-library/issues/2420)** Maintain the consistent of generated OpenAPI specification with  Ballerina to OAS CLI command and OpenAPI built-in plugin
- **[#1687](https://github.com/ballerina-platform/ballerina-library/issues/1687)** Validate StatusCodeRecords at compile time for extra fields
- **[#1646](https://github.com/ballerina-platform/ballerina-library/issues/1646)** Remove deprecated runtime APIs `getParamNames()` & `getParamDefaultability()` for resource methods

#### 🚀 NewFeature

- **[#5992](https://github.com/ballerina-platform/ballerina-library/issues/5992)** Need to implement `maxHeaderSize` validation in http2 client
- **[#897](https://github.com/ballerina-platform/ballerina-library/issues/897)** Add 417,406 validation to @http:Payload annotation

#### 📋 Task

- **[#6987](https://github.com/ballerina-platform/ballerina-library/issues/6987)** Update the HTTP spec with the data binding annotations details 
- **[#5988](https://github.com/ballerina-platform/ballerina-library/issues/5988)** [HTTP] The HTTP status code error feature is missing in the spec
- **[#4414](https://github.com/ballerina-platform/ballerina-library/issues/4414)** Error percentage has increased in the load-tests 
- **[#4267](https://github.com/ballerina-platform/ballerina-library/issues/4267)** [HTTP] Update module spec with the new error structure
- **[#4222](https://github.com/ballerina-platform/ballerina-library/issues/4222)** ssl_wellknown_cert_test.bal fails intermittently
- **[#3747](https://github.com/ballerina-platform/ballerina-library/issues/3747)** Refactor the listener gracefulstop and immediate stop test cases

### 📦 module/sql (9 issues)

#### 🐛 Bug

- **[#7800](https://github.com/ballerina-platform/ballerina-library/issues/7800)** java.jdbc hangs in native image after a few requests
- **[#4427](https://github.com/ballerina-platform/ballerina-library/issues/4427)** Remove `io.ballerina.runtime.internal` imports in standard libraries
- **[#4283](https://github.com/ballerina-platform/ballerina-library/issues/4283)** Intersection Types Cannot Be Used to Database Operations
- **[#2056](https://github.com/ballerina-platform/ballerina-library/issues/2056)** Spec Deviation in sql:ParameterizedQuery and sql:ParameterizedCallQuery

#### 📚 Docs

- **[#3807](https://github.com/ballerina-platform/ballerina-library/issues/3807)** Improve docs regarding client and stream lifecycle

#### ✨ Improvement

- **[#7763](https://github.com/ballerina-platform/ballerina-library/issues/7763)** Expose SQL connection pool metrics for observability and tuning
- **[#727](https://github.com/ballerina-platform/ballerina-library/issues/727)** Supporting retryable transaction with SQL transactions
- **[#611](https://github.com/ballerina-platform/ballerina-library/issues/611)** Streaming out large data set is not supported in Swan lake data clients

#### 📋 Task

- **[#6139](https://github.com/ballerina-platform/ballerina-library/issues/6139)** Add example to demonstrate how to use `arrayFlattenQuery` to construct IN clause

### 📦 module/grpc (5 issues)

#### 🐛 Bug

- **[#7436](https://github.com/ballerina-platform/ballerina-library/issues/7436)** The `testInvokeUnavailableService` is failing intermittently
- **[#4316](https://github.com/ballerina-platform/ballerina-library/issues/4316)** gRPC `testClientStreamingSendError` is failing intermittently

#### ✨ Improvement

- **[#3051](https://github.com/ballerina-platform/ballerina-library/issues/3051)** Error message is not descriptive enough when the client side and server side protos mismatch
- **[#1916](https://github.com/ballerina-platform/ballerina-library/issues/1916)** module-ballerina-grpc: generate an `service object` type for each protobuf service
- **[#389](https://github.com/ballerina-platform/ballerina-library/issues/389)** Generating records generated using ballerina grpc command automatically

### 📦 module/io (4 issues)

#### 🐛 Bug

- **[#7241](https://github.com/ballerina-platform/ballerina-library/issues/7241)** IO file write as stream does not support streams with generic error as a completion type
- **[#4273](https://github.com/ballerina-platform/ballerina-library/issues/4273)** Program crashes with NPE
- **[#3353](https://github.com/ballerina-platform/ballerina-library/issues/3353)** io:fileReadBytes function consumes significant memory.

#### 📋 Task

- **[#4414](https://github.com/ballerina-platform/ballerina-library/issues/4414)** Error percentage has increased in the load-tests 

### 📦 module/All (4 issues)

#### 🐛 Bug

- **[#6106](https://github.com/ballerina-platform/ballerina-library/issues/6106)** Migrating gradle plugin from v2.0.1 to v2.2.2 requires additional configuration

#### ✨ Improvement

- **[#3867](https://github.com/ballerina-platform/ballerina-library/issues/3867)** Improve the trivy security scan location for std libs

#### 🚀 NewFeature

- **[#7866](https://github.com/ballerina-platform/ballerina-library/issues/7866)** Expose Native Logs via Configurable Options for Easier Debugging

#### 📋 Task

- **[#8275](https://github.com/ballerina-platform/ballerina-library/issues/8275)** [High Priority] Review Library/Connector API docs in BI editor

### 📦 module/oauth2 (4 issues)

#### 🐛 Bug

- **[#8247](https://github.com/ballerina-platform/ballerina-library/issues/8247)** http client with password grant type to salesforce endpoint is failing with 400

#### ✨ Improvement

- **[#6192](https://github.com/ballerina-platform/ballerina-library/issues/6192)** Improve error message for failed token endpoint call

#### 🚀 NewFeature

- **[#6081](https://github.com/ballerina-platform/ballerina-library/issues/6081)** Add support for OAuth2 SAML Bearer Assertion in ballerina/oauth2

#### 📋 Task

- **[#6968](https://github.com/ballerina-platform/ballerina-library/issues/6968)** Create a new WSO2 IS container to use in OAuth2 tests

### 📦 module/task (4 issues)

#### ✨ Improvement

- **[#7908](https://github.com/ballerina-platform/ballerina-library/issues/7908)** Support listener termination after all active jobs are completed
- **[#3830](https://github.com/ballerina-platform/ballerina-library/issues/3830)** Improve documentation for `scheduleJobRecurByFrequency()` function and `ErrorPolicy` in task package

#### 📋 Task

- **[#8105](https://github.com/ballerina-platform/ballerina-library/issues/8105)** Update the spec with the task coordination support
- **[#5847](https://github.com/ballerina-platform/ballerina-library/issues/5847)** Upgrade quartz dependency

### 📦 module/crypto (3 issues)

#### ✨ Improvement

- **[#8292](https://github.com/ballerina-platform/ballerina-library/issues/8292)** Add support for RSASSA-PSS (PS256) algorithm
- **[#7831](https://github.com/ballerina-platform/ballerina-library/issues/7831)** Increase default iterations value for `PBKDF2` to meet OWASP security standards

#### 🚀 NewFeature

- **[#8182](https://github.com/ballerina-platform/ballerina-library/issues/8182)** Support NIST-Approved Post-Quantum Algorithms

### 📦 module/email (3 issues)

#### 🐛 Bug

- **[#3897](https://github.com/ballerina-platform/ballerina-library/issues/3897)** Email complier plugin doesn't work as expected 

#### ✨ Improvement

- **[#6470](https://github.com/ballerina-platform/ballerina-library/issues/6470)** [Improvement]:  Non-descriptive error message when SMTP connection fails
- **[#1137](https://github.com/ballerina-platform/ballerina-library/issues/1137)** Email listener start reading old emails 

### 📦 module/persist (2 issues)

#### 🐛 Bug

- **[#6128](https://github.com/ballerina-platform/ballerina-library/issues/6128)** [Bug]: bal persist generate gives an error when trying to generate the files again

#### ✨ Improvement

- **[#4943](https://github.com/ballerina-platform/ballerina-library/issues/4943)** Improve persist query optimisation to include non global variable

### 📦 module/cache (2 issues)

#### ✨ Improvement

- **[#174](https://github.com/ballerina-platform/ballerina-library/issues/174)** Restrict cache value to the user-specified value type

#### 📋 Task

- **[#4414](https://github.com/ballerina-platform/ballerina-library/issues/4414)** Error percentage has increased in the load-tests 

### 📦 No Module (1 issues)

#### 🚀 NewFeature

- **[#7917](https://github.com/ballerina-platform/ballerina-library/issues/7917)** Create a ballerina module for working with PDFs

### 📦 module/random (1 issues)

#### ✨ Improvement

- **[#7929](https://github.com/ballerina-platform/ballerina-library/issues/7929)** Add Support for Cryptographically Secure Random Number Generation (CSPRNG)

### 📦 module/jwt (1 issues)

#### 📋 Task

- **[#4414](https://github.com/ballerina-platform/ballerina-library/issues/4414)** Error percentage has increased in the load-tests 

### 📦 module/os (1 issues)

#### 🐛 Bug

- **[#7296](https://github.com/ballerina-platform/ballerina-library/issues/7296)** Running `wget` using `os:exec` hangs

### 📦 module/mime (1 issues)

#### 🐛 Bug

- **[#3971](https://github.com/ballerina-platform/ballerina-library/issues/3971)** NoSuchMethodError thrown from the mime module for `io.ballerina.runtime.api.types.ObjectType`

### 📦 module/auth (1 issues)

#### 📋 Task

- **[#7033](https://github.com/ballerina-platform/ballerina-library/issues/7033)** [Example 3] Write a Real World Example for Auth

### 📦 module/tcp (1 issues)

#### 🚀 NewFeature

- **[#2150](https://github.com/ballerina-platform/ballerina-library/issues/2150)** TCP listener to conveniently contact the message using custom logic

### 📦 module/websocket (1 issues)

#### 🐛 Bug

- **[#2886](https://github.com/ballerina-platform/ballerina-library/issues/2886)** Issue when sending a curl request to the WebSocket service

### 📦 module/time (1 issues)

#### ✨ Improvement

- **[#1582](https://github.com/ballerina-platform/ballerina-library/issues/1582)** Add functionality to compare two dates 

## Area/Connector/Handwritten Connectors

### 📦 module/salesforce (6 issues)

#### 🐛 Bug

- **[#8246](https://github.com/ballerina-platform/ballerina-library/issues/8246)** Salesforce connection issue error is static
- **[#7349](https://github.com/ballerina-platform/ballerina-library/issues/7349)** salesforce upsert does not handle the upsert response

#### 📚 Docs

- **[#4984](https://github.com/ballerina-platform/ballerina-library/issues/4984)** [Docs]: Salesforce connector test README mentions `ballerina.conf`

#### ✨ Improvement

- **[#7396](https://github.com/ballerina-platform/ballerina-library/issues/7396)** Improve Error Message for Client Initialization in Salesforce connector
- **[#6560](https://github.com/ballerina-platform/ballerina-library/issues/6560)** Actual issue may not be properly conveyed when SF `createQueryJobAndWait` fails
- **[#4994](https://github.com/ballerina-platform/ballerina-library/issues/4994)** [Improvement]: Include the option to perform PK chunking for Bulk Query in Salesforce connector

### 📦 module/mysql (6 issues)

#### 🐛 Bug

- **[#7359](https://github.com/ballerina-platform/ballerina-library/issues/7359)** Invalid stream value created by the MySQL client
- **[#7297](https://github.com/ballerina-platform/ballerina-library/issues/7297)** MySQL boolean type does not match with ballerina boolean type
- **[#6309](https://github.com/ballerina-platform/ballerina-library/issues/6309)** [Bug]: Mysql JSON attribute cannot be mapped to Ballerina JSON type 

#### ✨ Improvement

- **[#4703](https://github.com/ballerina-platform/ballerina-library/issues/4703)** Support inserting JSON types in MySQL connector using a ParameterizedQuery
- **[#4141](https://github.com/ballerina-platform/ballerina-library/issues/4141)** Proposal: Introduce a new API to execute batch queries into multiple batches

#### 📋 Task

- **[#3518](https://github.com/ballerina-platform/ballerina-library/issues/3518)** Test disabled MySQL tests with native-image

### 📦 module/mongodb (4 issues)

#### 🐛 Bug

- **[#7060](https://github.com/ballerina-platform/ballerina-library/issues/7060)** Conversion error when accessing array of primitives in MongoDB using Ballerina

#### 📚 Docs

- **[#4998](https://github.com/ballerina-platform/ballerina-library/issues/4998)** [Docs]: No docs on how to construct a query string for _id field

#### ✨ Improvement

- **[#7258](https://github.com/ballerina-platform/ballerina-library/issues/7258)** MongoDB Connector: Outdated or Incompatible Examples with MongoDB Atlas
- **[#6377](https://github.com/ballerina-platform/ballerina-library/issues/6377)** MongoDB `find` API Should be able to Return an Array

### 📦 module/postgresql (4 issues)

#### 🐛 Bug

- **[#6819](https://github.com/ballerina-platform/ballerina-library/issues/6819)** Concurrent database calls timeout (with postgres)
- **[#6132](https://github.com/ballerina-platform/ballerina-library/issues/6132)** [Bug]: Unable to identify error in PostgreSQL DB query results
- **[#4170](https://github.com/ballerina-platform/ballerina-library/issues/4170)** Error retrieving JSON data as 'json?' type when entry is null

#### ✨ Improvement

- **[#4141](https://github.com/ballerina-platform/ballerina-library/issues/4141)** Proposal: Introduce a new API to execute batch queries into multiple batches

### 📦 module/mssql (3 issues)

#### 🐛 Bug

- **[#6562](https://github.com/ballerina-platform/ballerina-library/issues/6562)** Passing Null values to the float and date types fails in mssql connector
- **[#5954](https://github.com/ballerina-platform/ballerina-library/issues/5954)** Broken links in mssql documentation

#### ✨ Improvement

- **[#4141](https://github.com/ballerina-platform/ballerina-library/issues/4141)** Proposal: Introduce a new API to execute batch queries into multiple batches

### 📦 module/All (2 issues)

#### 🐛 Bug

- **[#6676](https://github.com/ballerina-platform/ballerina-library/issues/6676)** Connector build is not working on windows

#### 📋 Task

- **[#8275](https://github.com/ballerina-platform/ballerina-library/issues/8275)** [High Priority] Review Library/Connector API docs in BI editor

### 📦 module/sap (2 issues)

#### 🚀 NewFeature

- **[#6733](https://github.com/ballerina-platform/ballerina-library/issues/6733)** Implement S/4HANA PP connectors
- **[#6732](https://github.com/ballerina-platform/ballerina-library/issues/6732)** Implement S/4HANA MM connectors

### 📦 module/aws-s3 (2 issues)

#### 🐛 Bug

- **[#4993](https://github.com/ballerina-platform/ballerina-library/issues/4993)** [Question]: Aren't the parameters of `aws.s3:Client` methods inconsistent?

#### 🚀 NewFeature

- **[#6175](https://github.com/ballerina-platform/ballerina-library/issues/6175)** Missing Copy Object Functionality in ballerinax/aws.s3 Library

### 📦 module/s4hana (2 issues)

#### 🚀 NewFeature

- **[#6733](https://github.com/ballerina-platform/ballerina-library/issues/6733)** Implement S/4HANA PP connectors
- **[#6732](https://github.com/ballerina-platform/ballerina-library/issues/6732)** Implement S/4HANA MM connectors

### 📦 module/persist.redis (1 issues)

#### 📋 Task

- **[#7409](https://github.com/ballerina-platform/ballerina-library/issues/7409)** Re-enable tests disabled in persist.redis module during Java 21 Migration

### 📦 module/azure-storageservice (1 issues)

#### 🐛 Bug

- **[#5948](https://github.com/ballerina-platform/ballerina-library/issues/5948)** Azure storage service connector documentation issues in central

### 📦 module/cdata (1 issues)

#### 📋 Task

- **[#4955](https://github.com/ballerina-platform/ballerina-library/issues/4955)** [Task]:  Implement a test suite for cdata connector 

### 📦 module/oracledb (1 issues)

#### ✨ Improvement

- **[#4141](https://github.com/ballerina-platform/ballerina-library/issues/4141)** Proposal: Introduce a new API to execute batch queries into multiple batches

## Area/Connector/Generated Connectors

### 📦 module/sap (3 issues)

#### 📋 Task

- **[#8148](https://github.com/ballerina-platform/ballerina-library/issues/8148)** Implement Ballerina Connector: SAP Concur/Shared APIs
- **[#8147](https://github.com/ballerina-platform/ballerina-library/issues/8147)** Implement Ballerina Connector: SAP SuccessFactors/Employee Central
- **[#6975](https://github.com/ballerina-platform/ballerina-library/issues/6975)** Implement SAP S4/HANA MM connectors under Procurement 

### 📦 module/github (3 issues)

#### 🐛 Bug

- **[#8018](https://github.com/ballerina-platform/ballerina-library/issues/8018)** [Bug]: Github PullRequestReviewComment type issue

#### 📋 Task

- **[#7777](https://github.com/ballerina-platform/ballerina-library/issues/7777)** Fix GitHub connector test failures due to deprecated projects(classic)
- **[#6917](https://github.com/ballerina-platform/ballerina-library/issues/6917)** Enable Project Creation and Deletion in Tests for GitHub Connector

### 📦 No Module (2 issues)

#### 🐛 Bug

- **[#7970](https://github.com/ballerina-platform/ballerina-library/issues/7970)** Getting payload binding error in openai.chat connector
- **[#4991](https://github.com/ballerina-platform/ballerina-library/issues/4991)** [Bug]: `ballerinax/worldbank` doesn't work on Swan Lake Update 2 and later versions

### 📦 module/sap.concur (1 issues)

#### 📋 Task

- **[#8148](https://github.com/ballerina-platform/ballerina-library/issues/8148)** Implement Ballerina Connector: SAP Concur/Shared APIs

### 📦 module/sap.sf (1 issues)

#### 📋 Task

- **[#8147](https://github.com/ballerina-platform/ballerina-library/issues/8147)** Implement Ballerina Connector: SAP SuccessFactors/Employee Central

### 📦 module/zoom.meetings (1 issues)

#### 🐛 Bug

- **[#8024](https://github.com/ballerina-platform/ballerina-library/issues/8024)** Zoom Meetings - Compilation errors due to redeclared fields  in types.bal

### 📦 module/googleapis.drive (1 issues)

#### ✨ Improvement

- **[#7820](https://github.com/ballerina-platform/ballerina-library/issues/7820)** Add API key authentication to googleapis.drive connector

### 📦 module/slack (1 issues)

#### 🐛 Bug

- **[#7755](https://github.com/ballerina-platform/ballerina-library/issues/7755)** Payload binding failure for slack chat.postMessage.post endpoint.

### 📦 module/dropbox (1 issues)

#### 📋 Task

- **[#7429](https://github.com/ballerina-platform/ballerina-library/issues/7429)** Check the dropbox connector test failure

### 📦 module/All (1 issues)

#### 🐛 Bug

- **[#6647](https://github.com/ballerina-platform/ballerina-library/issues/6647)** Cannot resolve the Ballerina Gradle plugin dependency when building a ballerina library package on Windows

### 📦 module/twilio (1 issues)

#### 🐛 Bug

- **[#6569](https://github.com/ballerina-platform/ballerina-library/issues/6569)** Invalid parameters in the generated twilio:Client object in the diagram viewer in the Ballerina VS Code plugin

### 📦 module/twitter (1 issues)

#### 🐛 Bug

- **[#6472](https://github.com/ballerina-platform/ballerina-library/issues/6472)** Add Connector option of VSCode sequence diagram provides invalid names for the twitter module

### 📦 module/candid (1 issues)

#### 📋 Task

- **[#6342](https://github.com/ballerina-platform/ballerina-library/issues/6342)** Re-Enable temporarily disabled example builds on Candid Module

### 📦 module/cosmosdb (1 issues)

#### ✨ Improvement

- **[#5046](https://github.com/ballerina-platform/ballerina-library/issues/5046)** [Improvement]: Improving Azure CosmosDB connector to support Managed Identities

## Area/Tooling

### 📦 module/openapi-tools (12 issues)

#### 🐛 Bug

- **[#8217](https://github.com/ballerina-platform/ballerina-library/issues/8217)** Unaligned type name with spaces
- **[#8205](https://github.com/ballerina-platform/ballerina-library/issues/8205)** OpenAPI generation incorrectly resolves additional properties, object when included in oneOf type
- **[#7508](https://github.com/ballerina-platform/ballerina-library/issues/7508)** Invalid Ballerina.toml generation `openapi add` in Windows

#### ✨ Improvement

- **[#8132](https://github.com/ballerina-platform/ballerina-library/issues/8132)** Support OpenAPI CLI command options as tool options in Ballerina.toml
- **[#6709](https://github.com/ballerina-platform/ballerina-library/issues/6709)** Add full support for OpenAPI specification version - `3.1.0`
- **[#5118](https://github.com/ballerina-platform/ballerina-library/issues/5118)** Improve the error message given when client and service generation failed

#### 📋 Task

- **[#8362](https://github.com/ballerina-platform/ballerina-library/issues/8362)** Check and re-enable windows tests which are failing in the workflow
- **[#8196](https://github.com/ballerina-platform/ballerina-library/issues/8196)** AI-Powered Automation for Ballerina Connector Generation
- **[#6785](https://github.com/ballerina-platform/ballerina-library/issues/6785)** Support server sent events in the openapi
- **[#6612](https://github.com/ballerina-platform/ballerina-library/issues/6612)** Add a changelog file into OpenAPI repository 
- **[#5127](https://github.com/ballerina-platform/ballerina-library/issues/5127)** OpenAPI to Ballerina Service spec writing
- **[#5128](https://github.com/ballerina-platform/ballerina-library/issues/5128)** OpenAPI to Ballerina Client spec writing

### 📦 module/persist-tools (6 issues)

#### 🐛 Bug

- **[#8323](https://github.com/ballerina-platform/ballerina-library/issues/8323)** Text Column Type Conversion Issue in Ballerina Persist Tool
- **[#6931](https://github.com/ballerina-platform/ballerina-library/issues/6931)** [Ballerina Persist] Error when connecting to PostgreSQL on AWS
- **[#6392](https://github.com/ballerina-platform/ballerina-library/issues/6392)** The ballerina project crashes without giving a proper error message for associated entities containing defaultable fields

#### 📋 Task

- **[#8242](https://github.com/ballerina-platform/ballerina-library/issues/8242)** Enable the Disabled Tests in Persist Tools
- **[#7398](https://github.com/ballerina-platform/ballerina-library/issues/7398)** Re-enable tests disabled in persist-tools module during Java 21 Migration
- **[#6337](https://github.com/ballerina-platform/ballerina-library/issues/6337)** Improve the logic in cache of the persist code generation 

### 📦 module/xsd-tool (2 issues)

#### 🐛 Bug

- **[#7772](https://github.com/ballerina-platform/ballerina-library/issues/7772)** Import statement absent in the ballerina file created using the xsd tool
- **[#7771](https://github.com/ballerina-platform/ballerina-library/issues/7771)** Xsd-tool module flag error

### 📦 module/protoc-tool (2 issues)

#### 🐛 Bug

- **[#6837](https://github.com/ballerina-platform/ballerina-library/issues/6837)** GRPC client sample code generation is failing when protobuf schema contains cyclic dependent messages

#### 📋 Task

- **[#5748](https://github.com/ballerina-platform/ballerina-library/issues/5748)** Support code generation to Ballerina PreBuildRunner task within the Protoc tool

### 📦 module/graphql-tool (1 issues)

#### 📋 Task

- **[#6434](https://github.com/ballerina-platform/ballerina-library/issues/6434)** Update `FunctionBodyGenerator` for `NodeFactory.createOnFailClauseNode` change

### 📦 module/grpc (1 issues)

#### 🐛 Bug

- **[#6837](https://github.com/ballerina-platform/ballerina-library/issues/6837)** GRPC client sample code generation is failing when protobuf schema contains cyclic dependent messages

