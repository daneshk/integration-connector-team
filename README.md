# Ballerina Library Issues Analysis

This repository contains an organized breakdown of open issues from the [ballerina-library](https://github.com/ballerina-platform/ballerina-library) repository.

**Last Updated:** 2025-10-23 13:47:46

## Overall Summary

**Total Issues Across All Areas:** 543

## 🔴 Highest Priority Issues (22)

Critical issues that require immediate attention.

- 🐛 **[#7920](https://github.com/ballerina-platform/ballerina-library/issues/7920)** Query Expressions with Persist Clients do not push down 'where' conditions to the database, leading to inefficient in-memory filtering
  - 📍 Module: `module/persist` (Area/Library)

- 🐛 **[#4745](https://github.com/ballerina-platform/ballerina-library/issues/4745)** Compiler crash in persist for model with few records
  - 📍 Module: `module/persist` (Area/Library)

- 🐛 **[#4081](https://github.com/ballerina-platform/ballerina-library/issues/4081)** [Persist] `time:Utc` type values mismatch on retrieval
  - 📍 Module: `module/persist` (Area/Library)

- ✨ **[#5736](https://github.com/ballerina-platform/ballerina-library/issues/5736)** Allow passing config parameters to the generated persist client and set default values to configurable variables
  - 📍 Module: `module/persist` (Area/Library)

- ✨ **[#4812](https://github.com/ballerina-platform/ballerina-library/issues/4812)** Ballerina Persist module not support association(1:N) that can have nilable values
  - 📍 Module: `module/persist` (Area/Library)

- ✨ **[#5799](https://github.com/ballerina-platform/ballerina-library/issues/5799)** [HTTP Client] Support for resolving round-robin DNS
  - 📍 Module: `module/http` (Area/Library)

- ✨ **[#4329](https://github.com/ballerina-platform/ballerina-library/issues/4329)** Interceptor support for client side
  - 📍 Module: `module/http` (Area/Library)

- ✨ **[#3630](https://github.com/ballerina-platform/ballerina-library/issues/3630)** Improve `Connection between remote client and host is closed` error message
  - 📍 Module: `module/http` (Area/Library)

- 🚀 **[#7460](https://github.com/ballerina-platform/ballerina-library/issues/7460)** Allow configuring TCP Keep-Alive related properties in the Ballerina HTTP Client
  - 📍 Module: `module/http` (Area/Library)

- 🚀 **[#6547](https://github.com/ballerina-platform/ballerina-library/issues/6547)** Add HTTP compression support for `brotli` format
  - 📍 Module: `module/http` (Area/Library)

- 📋 **[#7330](https://github.com/ballerina-platform/ballerina-library/issues/7330)** Disabled tests due to the Jsondata module fixes
  - 📍 Module: `module/http` (Area/Library)

- 📋 **[#4213](https://github.com/ballerina-platform/ballerina-library/issues/4213)** Make HTTP module FIPS compliant
  - 📍 Module: `module/http` (Area/Library)

- 📋 **[#8312](https://github.com/ballerina-platform/ballerina-library/issues/8312)** Prioritize Library and Connector current issues
  - 📍 Module: `module/All` (Area/Library)

- 📋 **[#4212](https://github.com/ballerina-platform/ballerina-library/issues/4212)** Make Crypto module FIPS compliant
  - 📍 Module: `module/crypto` (Area/Library)

- ✨ **[#8185](https://github.com/ballerina-platform/ballerina-library/issues/8185)** Ballerina JWT library does not support PS 256 and ES 256 algorithms
  - 📍 Module: `module/jwt` (Area/Library)

- 🐛 **[#5097](https://github.com/ballerina-platform/ballerina-library/issues/5097)** [Bug]: Unable use map<anydata> instead of record {} 
  - 📍 Module: `module/sql` (Area/Library)

- 🐛 **[#4081](https://github.com/ballerina-platform/ballerina-library/issues/4081)** [Persist] `time:Utc` type values mismatch on retrieval
  - 📍 Module: `module/sql` (Area/Library)

- ✨ **[#3842](https://github.com/ballerina-platform/ballerina-library/issues/3842)** Add support to enable logs to detect connection leaks in DB connectors
  - 📍 Module: `module/sql` (Area/Library)

- 📋 **[#8312](https://github.com/ballerina-platform/ballerina-library/issues/8312)** Prioritize Library and Connector current issues
  - 📍 Module: `module/All` (Area/Connector/Handwritten Connectors)

- 📋 **[#7816](https://github.com/ballerina-platform/ballerina-library/issues/7816)** Finalize the Ballerina Connectors release progress with breaking changes
  - 📍 Module: `module/All` (Area/Connector/Handwritten Connectors)

- 📚 **[#8209](https://github.com/ballerina-platform/ballerina-library/issues/8209)** Update Ballerina Use Case Page with Salesforce Event Listener
  - 📍 Module: `module/salesforce` (Area/Connector/Handwritten Connectors)

- 🐛 **[#3511](https://github.com/ballerina-platform/ballerina-library/issues/3511)** Database parameter is not validated in MySQL connector
  - 📍 Module: `module/mysql` (Area/Connector/Handwritten Connectors)

## 🟠 High Priority Issues (168)

Important issues that should be addressed soon.

- 🐛 **[#6128](https://github.com/ballerina-platform/ballerina-library/issues/6128)** [Bug]: bal persist generate gives an error when trying to generate the files again
  - 📍 Module: `module/persist` (Area/Library)

- ✨ **[#4943](https://github.com/ballerina-platform/ballerina-library/issues/4943)** Improve persist query optimisation to include non global variable
  - 📍 Module: `module/persist` (Area/Library)

- 🐛 **[#8339](https://github.com/ballerina-platform/ballerina-library/issues/8339)** Investigate possible thread blocked issues in SSE services
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#7893](https://github.com/ballerina-platform/ballerina-library/issues/7893)** HTTP compile error when referring a listener in different file in a service
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#7727](https://github.com/ballerina-platform/ballerina-library/issues/7727)** Getting a compilation error when using `http:ServiceContract`
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#7512](https://github.com/ballerina-platform/ballerina-library/issues/7512)** Http POST resource functions can define more than one payload parameters
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#7298](https://github.com/ballerina-platform/ballerina-library/issues/7298)** Error when use getJsonPayload method and Client.forward() over https
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#7292](https://github.com/ballerina-platform/ballerina-library/issues/7292)** Error in data binding with the URL encoded content-type with charset directive
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#6663](https://github.com/ballerina-platform/ballerina-library/issues/6663)** h2-h2 load test with h1 client hanging after sometime
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#5962](https://github.com/ballerina-platform/ballerina-library/issues/5962)** HTTP compiler failed when we have a default value for payload parameter
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#5894](https://github.com/ballerina-platform/ballerina-library/issues/5894)** Defaultable header parameters in the HTTP resource is not considered as optional
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#5085](https://github.com/ballerina-platform/ballerina-library/issues/5085)** HTTP compiler validations are not working for isolated service
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#4915](https://github.com/ballerina-platform/ballerina-library/issues/4915)** Intermittent test failure: `testRequestInterceptorCtxNext`
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#4461](https://github.com/ballerina-platform/ballerina-library/issues/4461)** Enable testHttp2InvalidHeaderLength testcase.
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#4671](https://github.com/ballerina-platform/ballerina-library/issues/4671)** [Bug] Reading a byte stream from a backend hangs in the passthrough
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#3318](https://github.com/ballerina-platform/ballerina-library/issues/3318)** [Windows] Test failure : testAuthnError
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#3250](https://github.com/ballerina-platform/ballerina-library/issues/3250)** [Windows] Test failure `testSslClientFallbackFromH2ToH1`
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#3138](https://github.com/ballerina-platform/ballerina-library/issues/3138)** H2ConnectionPoolWithPriorKnowledge intermittent test failure
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#2886](https://github.com/ballerina-platform/ballerina-library/issues/2886)** Issue when sending a curl request to the WebSocket service
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#317](https://github.com/ballerina-platform/ballerina-library/issues/317)** [Windows] Intermittent transport test failures
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#501](https://github.com/ballerina-platform/ballerina-library/issues/501)** [HTTP][CORS] Exact value origin match fails
  - 📍 Module: `module/http` (Area/Library)

- 📚 **[#2710](https://github.com/ballerina-platform/ballerina-library/issues/2710)** [http] Documentation for the `http:Payload` annotation is inadequate
  - 📍 Module: `module/http` (Area/Library)

- 📚 **[#2521](https://github.com/ballerina-platform/ballerina-library/issues/2521)** Lack of Documentation for enabling/configuring `Trace logs` and `Access logs` in the API Docs
  - 📍 Module: `module/http` (Area/Library)

- ✨ **[#6110](https://github.com/ballerina-platform/ballerina-library/issues/6110)** [WIP] Review the `nil` return from interceptors via `RequestContext:next()`
  - 📍 Module: `module/http` (Area/Library)

- ✨ **[#5885](https://github.com/ballerina-platform/ballerina-library/issues/5885)** Http Client error does not contain the full stacktrace.
  - 📍 Module: `module/http` (Area/Library)

- ✨ **[#4092](https://github.com/ballerina-platform/ballerina-library/issues/4092)** Ability to configure resource level `ResponseErrorInterceptor` 
  - 📍 Module: `module/http` (Area/Library)

- ✨ **[#3939](https://github.com/ballerina-platform/ballerina-library/issues/3939)** Client side compression should be improved
  - 📍 Module: `module/http` (Area/Library)

- ✨ **[#2420](https://github.com/ballerina-platform/ballerina-library/issues/2420)** Maintain the consistent of generated OpenAPI specification with  Ballerina to OAS CLI command and OpenAPI built-in plugin
  - 📍 Module: `module/http` (Area/Library)

- ✨ **[#1687](https://github.com/ballerina-platform/ballerina-library/issues/1687)** Validate StatusCodeRecords at compile time for extra fields
  - 📍 Module: `module/http` (Area/Library)

- ✨ **[#1646](https://github.com/ballerina-platform/ballerina-library/issues/1646)** Remove deprecated runtime APIs `getParamNames()` & `getParamDefaultability()` for resource methods
  - 📍 Module: `module/http` (Area/Library)

- 🚀 **[#5992](https://github.com/ballerina-platform/ballerina-library/issues/5992)** Need to implement `maxHeaderSize` validation in http2 client
  - 📍 Module: `module/http` (Area/Library)

- 🚀 **[#897](https://github.com/ballerina-platform/ballerina-library/issues/897)** Add 417,406 validation to @http:Payload annotation
  - 📍 Module: `module/http` (Area/Library)

- 📋 **[#6987](https://github.com/ballerina-platform/ballerina-library/issues/6987)** Update the HTTP spec with the data binding annotations details 
  - 📍 Module: `module/http` (Area/Library)

- 📋 **[#5988](https://github.com/ballerina-platform/ballerina-library/issues/5988)** [HTTP] The HTTP status code error feature is missing in the spec
  - 📍 Module: `module/http` (Area/Library)

- 📋 **[#4414](https://github.com/ballerina-platform/ballerina-library/issues/4414)** Error percentage has increased in the load-tests 
  - 📍 Module: `module/http` (Area/Library)

- 📋 **[#4267](https://github.com/ballerina-platform/ballerina-library/issues/4267)** [HTTP] Update module spec with the new error structure
  - 📍 Module: `module/http` (Area/Library)

- 📋 **[#4222](https://github.com/ballerina-platform/ballerina-library/issues/4222)** ssl_wellknown_cert_test.bal fails intermittently
  - 📍 Module: `module/http` (Area/Library)

- 📋 **[#3747](https://github.com/ballerina-platform/ballerina-library/issues/3747)** Refactor the listener gracefulstop and immediate stop test cases
  - 📍 Module: `module/http` (Area/Library)

- 🐛 **[#7241](https://github.com/ballerina-platform/ballerina-library/issues/7241)** IO file write as stream does not support streams with generic error as a completion type
  - 📍 Module: `module/io` (Area/Library)

- 🐛 **[#4273](https://github.com/ballerina-platform/ballerina-library/issues/4273)** Program crashes with NPE
  - 📍 Module: `module/io` (Area/Library)

- 🐛 **[#3353](https://github.com/ballerina-platform/ballerina-library/issues/3353)** io:fileReadBytes function consumes significant memory.
  - 📍 Module: `module/io` (Area/Library)

- 📋 **[#4414](https://github.com/ballerina-platform/ballerina-library/issues/4414)** Error percentage has increased in the load-tests 
  - 📍 Module: `module/io` (Area/Library)

- 🚀 **[#7917](https://github.com/ballerina-platform/ballerina-library/issues/7917)** Create a ballerina module for working with PDFs
  - 📍 Module: `No Module` (Area/Library)

- 🐛 **[#6106](https://github.com/ballerina-platform/ballerina-library/issues/6106)** Migrating gradle plugin from v2.0.1 to v2.2.2 requires additional configuration
  - 📍 Module: `module/All` (Area/Library)

- ✨ **[#3867](https://github.com/ballerina-platform/ballerina-library/issues/3867)** Improve the trivy security scan location for std libs
  - 📍 Module: `module/All` (Area/Library)

- 🚀 **[#7866](https://github.com/ballerina-platform/ballerina-library/issues/7866)** Expose Native Logs via Configurable Options for Easier Debugging
  - 📍 Module: `module/All` (Area/Library)

- 📋 **[#8275](https://github.com/ballerina-platform/ballerina-library/issues/8275)** [High Priority] Review Library/Connector API docs in BI editor
  - 📍 Module: `module/All` (Area/Library)

- ✨ **[#8292](https://github.com/ballerina-platform/ballerina-library/issues/8292)** Add support for RSASSA-PSS (PS256) algorithm
  - 📍 Module: `module/crypto` (Area/Library)

- ✨ **[#7831](https://github.com/ballerina-platform/ballerina-library/issues/7831)** Increase default iterations value for `PBKDF2` to meet OWASP security standards
  - 📍 Module: `module/crypto` (Area/Library)

- 🚀 **[#8182](https://github.com/ballerina-platform/ballerina-library/issues/8182)** Support NIST-Approved Post-Quantum Algorithms
  - 📍 Module: `module/crypto` (Area/Library)

- ✨ **[#7929](https://github.com/ballerina-platform/ballerina-library/issues/7929)** Add Support for Cryptographically Secure Random Number Generation (CSPRNG)
  - 📍 Module: `module/random` (Area/Library)

- 🐛 **[#8247](https://github.com/ballerina-platform/ballerina-library/issues/8247)** http client with password grant type to salesforce endpoint is failing with 400
  - 📍 Module: `module/oauth2` (Area/Library)

- ✨ **[#6192](https://github.com/ballerina-platform/ballerina-library/issues/6192)** Improve error message for failed token endpoint call
  - 📍 Module: `module/oauth2` (Area/Library)

- 🚀 **[#6081](https://github.com/ballerina-platform/ballerina-library/issues/6081)** Add support for OAuth2 SAML Bearer Assertion in ballerina/oauth2
  - 📍 Module: `module/oauth2` (Area/Library)

- 📋 **[#6968](https://github.com/ballerina-platform/ballerina-library/issues/6968)** Create a new WSO2 IS container to use in OAuth2 tests
  - 📍 Module: `module/oauth2` (Area/Library)

- ✨ **[#7510](https://github.com/ballerina-platform/ballerina-library/issues/7510)** JWT Validation - Support for RFC 8725
  - 📍 Module: `module/jwt` (Area/Library)

- 📋 **[#4414](https://github.com/ballerina-platform/ballerina-library/issues/4414)** Error percentage has increased in the load-tests 
  - 📍 Module: `module/jwt` (Area/Library)

- ✨ **[#7908](https://github.com/ballerina-platform/ballerina-library/issues/7908)** Support listener termination after all active jobs are completed
  - 📍 Module: `module/task` (Area/Library)

- ✨ **[#3830](https://github.com/ballerina-platform/ballerina-library/issues/3830)** Improve documentation for `scheduleJobRecurByFrequency()` function and `ErrorPolicy` in task package
  - 📍 Module: `module/task` (Area/Library)

- 📋 **[#8105](https://github.com/ballerina-platform/ballerina-library/issues/8105)** Update the spec with the task coordination support
  - 📍 Module: `module/task` (Area/Library)

- 📋 **[#5847](https://github.com/ballerina-platform/ballerina-library/issues/5847)** Upgrade quartz dependency
  - 📍 Module: `module/task` (Area/Library)

- 🐛 **[#7800](https://github.com/ballerina-platform/ballerina-library/issues/7800)** java.jdbc hangs in native image after a few requests
  - 📍 Module: `module/sql` (Area/Library)

- 🐛 **[#4427](https://github.com/ballerina-platform/ballerina-library/issues/4427)** Remove `io.ballerina.runtime.internal` imports in standard libraries
  - 📍 Module: `module/sql` (Area/Library)

- 🐛 **[#4283](https://github.com/ballerina-platform/ballerina-library/issues/4283)** Intersection Types Cannot Be Used to Database Operations
  - 📍 Module: `module/sql` (Area/Library)

- 🐛 **[#2056](https://github.com/ballerina-platform/ballerina-library/issues/2056)** Spec Deviation in sql:ParameterizedQuery and sql:ParameterizedCallQuery
  - 📍 Module: `module/sql` (Area/Library)

- 📚 **[#3807](https://github.com/ballerina-platform/ballerina-library/issues/3807)** Improve docs regarding client and stream lifecycle
  - 📍 Module: `module/sql` (Area/Library)

- ✨ **[#7763](https://github.com/ballerina-platform/ballerina-library/issues/7763)** Expose SQL connection pool metrics for observability and tuning
  - 📍 Module: `module/sql` (Area/Library)

- ✨ **[#727](https://github.com/ballerina-platform/ballerina-library/issues/727)** Supporting retryable transaction with SQL transactions
  - 📍 Module: `module/sql` (Area/Library)

- ✨ **[#611](https://github.com/ballerina-platform/ballerina-library/issues/611)** Streaming out large data set is not supported in Swan lake data clients
  - 📍 Module: `module/sql` (Area/Library)

- 📋 **[#6139](https://github.com/ballerina-platform/ballerina-library/issues/6139)** Add example to demonstrate how to use `arrayFlattenQuery` to construct IN clause
  - 📍 Module: `module/sql` (Area/Library)

- 🐛 **[#7296](https://github.com/ballerina-platform/ballerina-library/issues/7296)** Running `wget` using `os:exec` hangs
  - 📍 Module: `module/os` (Area/Library)

- 🐛 **[#3971](https://github.com/ballerina-platform/ballerina-library/issues/3971)** NoSuchMethodError thrown from the mime module for `io.ballerina.runtime.api.types.ObjectType`
  - 📍 Module: `module/mime` (Area/Library)

- 🐛 **[#7436](https://github.com/ballerina-platform/ballerina-library/issues/7436)** The `testInvokeUnavailableService` is failing intermittently
  - 📍 Module: `module/grpc` (Area/Library)

- 🐛 **[#4762](https://github.com/ballerina-platform/ballerina-library/issues/4762)** [Bug]: gRPC runtime error with `readonly` parameter in isolated function
  - 📍 Module: `module/grpc` (Area/Library)

- 🐛 **[#4316](https://github.com/ballerina-platform/ballerina-library/issues/4316)** gRPC `testClientStreamingSendError` is failing intermittently
  - 📍 Module: `module/grpc` (Area/Library)

- 🐛 **[#3274](https://github.com/ballerina-platform/ballerina-library/issues/3274)** Client error is not received in server when `grpc:Caller` is used to send values inside the client stream
  - 📍 Module: `module/grpc` (Area/Library)

- ✨ **[#3051](https://github.com/ballerina-platform/ballerina-library/issues/3051)** Error message is not descriptive enough when the client side and server side protos mismatch
  - 📍 Module: `module/grpc` (Area/Library)

- ✨ **[#1916](https://github.com/ballerina-platform/ballerina-library/issues/1916)** module-ballerina-grpc: generate an `service object` type for each protobuf service
  - 📍 Module: `module/grpc` (Area/Library)

- ✨ **[#389](https://github.com/ballerina-platform/ballerina-library/issues/389)** Generating records generated using ballerina grpc command automatically
  - 📍 Module: `module/grpc` (Area/Library)

- 📋 **[#7033](https://github.com/ballerina-platform/ballerina-library/issues/7033)** [Example 3] Write a Real World Example for Auth
  - 📍 Module: `module/auth` (Area/Library)

- 🐛 **[#3897](https://github.com/ballerina-platform/ballerina-library/issues/3897)** Email complier plugin doesn't work as expected 
  - 📍 Module: `module/email` (Area/Library)

- ✨ **[#6470](https://github.com/ballerina-platform/ballerina-library/issues/6470)** [Improvement]:  Non-descriptive error message when SMTP connection fails
  - 📍 Module: `module/email` (Area/Library)

- ✨ **[#1137](https://github.com/ballerina-platform/ballerina-library/issues/1137)** Email listener start reading old emails 
  - 📍 Module: `module/email` (Area/Library)

- 🚀 **[#2150](https://github.com/ballerina-platform/ballerina-library/issues/2150)** TCP listener to conveniently contact the message using custom logic
  - 📍 Module: `module/tcp` (Area/Library)

- ✨ **[#174](https://github.com/ballerina-platform/ballerina-library/issues/174)** Restrict cache value to the user-specified value type
  - 📍 Module: `module/cache` (Area/Library)

- 📋 **[#4414](https://github.com/ballerina-platform/ballerina-library/issues/4414)** Error percentage has increased in the load-tests 
  - 📍 Module: `module/cache` (Area/Library)

- 🐛 **[#2886](https://github.com/ballerina-platform/ballerina-library/issues/2886)** Issue when sending a curl request to the WebSocket service
  - 📍 Module: `module/websocket` (Area/Library)

- ✨ **[#1841](https://github.com/ballerina-platform/ballerina-library/issues/1841)** Ballerina should be able to parse strings in custom time formats
  - 📍 Module: `module/time` (Area/Library)

- ✨ **[#1582](https://github.com/ballerina-platform/ballerina-library/issues/1582)** Add functionality to compare two dates 
  - 📍 Module: `module/time` (Area/Library)

- 🐛 **[#6676](https://github.com/ballerina-platform/ballerina-library/issues/6676)** Connector build is not working on windows
  - 📍 Module: `module/All` (Area/Connector/Handwritten Connectors)

- 📋 **[#8275](https://github.com/ballerina-platform/ballerina-library/issues/8275)** [High Priority] Review Library/Connector API docs in BI editor
  - 📍 Module: `module/All` (Area/Connector/Handwritten Connectors)

- 🐛 **[#8246](https://github.com/ballerina-platform/ballerina-library/issues/8246)** Salesforce connection issue error is static
  - 📍 Module: `module/salesforce` (Area/Connector/Handwritten Connectors)

- 🐛 **[#7349](https://github.com/ballerina-platform/ballerina-library/issues/7349)** salesforce upsert does not handle the upsert response
  - 📍 Module: `module/salesforce` (Area/Connector/Handwritten Connectors)

- 📚 **[#4984](https://github.com/ballerina-platform/ballerina-library/issues/4984)** [Docs]: Salesforce connector test README mentions `ballerina.conf`
  - 📍 Module: `module/salesforce` (Area/Connector/Handwritten Connectors)

- ✨ **[#7396](https://github.com/ballerina-platform/ballerina-library/issues/7396)** Improve Error Message for Client Initialization in Salesforce connector
  - 📍 Module: `module/salesforce` (Area/Connector/Handwritten Connectors)

- ✨ **[#6560](https://github.com/ballerina-platform/ballerina-library/issues/6560)** Actual issue may not be properly conveyed when SF `createQueryJobAndWait` fails
  - 📍 Module: `module/salesforce` (Area/Connector/Handwritten Connectors)

- ✨ **[#4994](https://github.com/ballerina-platform/ballerina-library/issues/4994)** [Improvement]: Include the option to perform PK chunking for Bulk Query in Salesforce connector
  - 📍 Module: `module/salesforce` (Area/Connector/Handwritten Connectors)

- 🚀 **[#6733](https://github.com/ballerina-platform/ballerina-library/issues/6733)** Implement S/4HANA PP connectors
  - 📍 Module: `module/sap` (Area/Connector/Handwritten Connectors)

- 🚀 **[#6732](https://github.com/ballerina-platform/ballerina-library/issues/6732)** Implement S/4HANA MM connectors
  - 📍 Module: `module/sap` (Area/Connector/Handwritten Connectors)

- 🐛 **[#4993](https://github.com/ballerina-platform/ballerina-library/issues/4993)** [Question]: Aren't the parameters of `aws.s3:Client` methods inconsistent?
  - 📍 Module: `module/aws-s3` (Area/Connector/Handwritten Connectors)

- 🚀 **[#6175](https://github.com/ballerina-platform/ballerina-library/issues/6175)** Missing Copy Object Functionality in ballerinax/aws.s3 Library
  - 📍 Module: `module/aws-s3` (Area/Connector/Handwritten Connectors)

- 📋 **[#7409](https://github.com/ballerina-platform/ballerina-library/issues/7409)** Re-enable tests disabled in persist.redis module during Java 21 Migration
  - 📍 Module: `module/persist.redis` (Area/Connector/Handwritten Connectors)

- 🐛 **[#7359](https://github.com/ballerina-platform/ballerina-library/issues/7359)** Invalid stream value created by the MySQL client
  - 📍 Module: `module/mysql` (Area/Connector/Handwritten Connectors)

- 🐛 **[#7297](https://github.com/ballerina-platform/ballerina-library/issues/7297)** MySQL boolean type does not match with ballerina boolean type
  - 📍 Module: `module/mysql` (Area/Connector/Handwritten Connectors)

- 🐛 **[#6309](https://github.com/ballerina-platform/ballerina-library/issues/6309)** [Bug]: Mysql JSON attribute cannot be mapped to Ballerina JSON type 
  - 📍 Module: `module/mysql` (Area/Connector/Handwritten Connectors)

- ✨ **[#4703](https://github.com/ballerina-platform/ballerina-library/issues/4703)** Support inserting JSON types in MySQL connector using a ParameterizedQuery
  - 📍 Module: `module/mysql` (Area/Connector/Handwritten Connectors)

- ✨ **[#4141](https://github.com/ballerina-platform/ballerina-library/issues/4141)** Proposal: Introduce a new API to execute batch queries into multiple batches
  - 📍 Module: `module/mysql` (Area/Connector/Handwritten Connectors)

- 📋 **[#3518](https://github.com/ballerina-platform/ballerina-library/issues/3518)** Test disabled MySQL tests with native-image
  - 📍 Module: `module/mysql` (Area/Connector/Handwritten Connectors)

- 🐛 **[#7060](https://github.com/ballerina-platform/ballerina-library/issues/7060)** Conversion error when accessing array of primitives in MongoDB using Ballerina
  - 📍 Module: `module/mongodb` (Area/Connector/Handwritten Connectors)

- 📚 **[#4998](https://github.com/ballerina-platform/ballerina-library/issues/4998)** [Docs]: No docs on how to construct a query string for _id field
  - 📍 Module: `module/mongodb` (Area/Connector/Handwritten Connectors)

- ✨ **[#7258](https://github.com/ballerina-platform/ballerina-library/issues/7258)** MongoDB Connector: Outdated or Incompatible Examples with MongoDB Atlas
  - 📍 Module: `module/mongodb` (Area/Connector/Handwritten Connectors)

- ✨ **[#6377](https://github.com/ballerina-platform/ballerina-library/issues/6377)** MongoDB `find` API Should be able to Return an Array
  - 📍 Module: `module/mongodb` (Area/Connector/Handwritten Connectors)

- 🐛 **[#6819](https://github.com/ballerina-platform/ballerina-library/issues/6819)** Concurrent database calls timeout (with postgres)
  - 📍 Module: `module/postgresql` (Area/Connector/Handwritten Connectors)

- 🐛 **[#6132](https://github.com/ballerina-platform/ballerina-library/issues/6132)** [Bug]: Unable to identify error in PostgreSQL DB query results
  - 📍 Module: `module/postgresql` (Area/Connector/Handwritten Connectors)

- 🐛 **[#4170](https://github.com/ballerina-platform/ballerina-library/issues/4170)** Error retrieving JSON data as 'json?' type when entry is null
  - 📍 Module: `module/postgresql` (Area/Connector/Handwritten Connectors)

- ✨ **[#4141](https://github.com/ballerina-platform/ballerina-library/issues/4141)** Proposal: Introduce a new API to execute batch queries into multiple batches
  - 📍 Module: `module/postgresql` (Area/Connector/Handwritten Connectors)

- 🚀 **[#6733](https://github.com/ballerina-platform/ballerina-library/issues/6733)** Implement S/4HANA PP connectors
  - 📍 Module: `module/s4hana` (Area/Connector/Handwritten Connectors)

- 🚀 **[#6732](https://github.com/ballerina-platform/ballerina-library/issues/6732)** Implement S/4HANA MM connectors
  - 📍 Module: `module/s4hana` (Area/Connector/Handwritten Connectors)

- 🐛 **[#6562](https://github.com/ballerina-platform/ballerina-library/issues/6562)** Passing Null values to the float and date types fails in mssql connector
  - 📍 Module: `module/mssql` (Area/Connector/Handwritten Connectors)

- 🐛 **[#5954](https://github.com/ballerina-platform/ballerina-library/issues/5954)** Broken links in mssql documentation
  - 📍 Module: `module/mssql` (Area/Connector/Handwritten Connectors)

- ✨ **[#4141](https://github.com/ballerina-platform/ballerina-library/issues/4141)** Proposal: Introduce a new API to execute batch queries into multiple batches
  - 📍 Module: `module/mssql` (Area/Connector/Handwritten Connectors)

- 🐛 **[#5948](https://github.com/ballerina-platform/ballerina-library/issues/5948)** Azure storage service connector documentation issues in central
  - 📍 Module: `module/azure-storageservice` (Area/Connector/Handwritten Connectors)

- 📋 **[#4955](https://github.com/ballerina-platform/ballerina-library/issues/4955)** [Task]:  Implement a test suite for cdata connector 
  - 📍 Module: `module/cdata` (Area/Connector/Handwritten Connectors)

- ✨ **[#4141](https://github.com/ballerina-platform/ballerina-library/issues/4141)** Proposal: Introduce a new API to execute batch queries into multiple batches
  - 📍 Module: `module/oracledb` (Area/Connector/Handwritten Connectors)

- 🐛 **[#7970](https://github.com/ballerina-platform/ballerina-library/issues/7970)** Getting payload binding error in openai.chat connector
  - 📍 Module: `No Module` (Area/Connector/Generated Connectors)

- 🐛 **[#4991](https://github.com/ballerina-platform/ballerina-library/issues/4991)** [Bug]: `ballerinax/worldbank` doesn't work on Swan Lake Update 2 and later versions
  - 📍 Module: `No Module` (Area/Connector/Generated Connectors)

- 📋 **[#8148](https://github.com/ballerina-platform/ballerina-library/issues/8148)** Implement Ballerina Connector: SAP Concur/Shared APIs
  - 📍 Module: `module/sap` (Area/Connector/Generated Connectors)

- 📋 **[#8147](https://github.com/ballerina-platform/ballerina-library/issues/8147)** Implement Ballerina Connector: SAP SuccessFactors/Employee Central
  - 📍 Module: `module/sap` (Area/Connector/Generated Connectors)

- 📋 **[#6975](https://github.com/ballerina-platform/ballerina-library/issues/6975)** Implement SAP S4/HANA MM connectors under Procurement 
  - 📍 Module: `module/sap` (Area/Connector/Generated Connectors)

- 📋 **[#8148](https://github.com/ballerina-platform/ballerina-library/issues/8148)** Implement Ballerina Connector: SAP Concur/Shared APIs
  - 📍 Module: `module/sap.concur` (Area/Connector/Generated Connectors)

- 📋 **[#8147](https://github.com/ballerina-platform/ballerina-library/issues/8147)** Implement Ballerina Connector: SAP SuccessFactors/Employee Central
  - 📍 Module: `module/sap.sf` (Area/Connector/Generated Connectors)

- 🐛 **[#8024](https://github.com/ballerina-platform/ballerina-library/issues/8024)** Zoom Meetings - Compilation errors due to redeclared fields  in types.bal
  - 📍 Module: `module/zoom.meetings` (Area/Connector/Generated Connectors)

- 🐛 **[#8018](https://github.com/ballerina-platform/ballerina-library/issues/8018)** [Bug]: Github PullRequestReviewComment type issue
  - 📍 Module: `module/github` (Area/Connector/Generated Connectors)

- 📋 **[#7777](https://github.com/ballerina-platform/ballerina-library/issues/7777)** Fix GitHub connector test failures due to deprecated projects(classic)
  - 📍 Module: `module/github` (Area/Connector/Generated Connectors)

- 📋 **[#6917](https://github.com/ballerina-platform/ballerina-library/issues/6917)** Enable Project Creation and Deletion in Tests for GitHub Connector
  - 📍 Module: `module/github` (Area/Connector/Generated Connectors)

- ✨ **[#7820](https://github.com/ballerina-platform/ballerina-library/issues/7820)** Add API key authentication to googleapis.drive connector
  - 📍 Module: `module/googleapis.drive` (Area/Connector/Generated Connectors)

- 🐛 **[#7755](https://github.com/ballerina-platform/ballerina-library/issues/7755)** Payload binding failure for slack chat.postMessage.post endpoint.
  - 📍 Module: `module/slack` (Area/Connector/Generated Connectors)

- 📋 **[#7429](https://github.com/ballerina-platform/ballerina-library/issues/7429)** Check the dropbox connector test failure
  - 📍 Module: `module/dropbox` (Area/Connector/Generated Connectors)

- 🐛 **[#6647](https://github.com/ballerina-platform/ballerina-library/issues/6647)** Cannot resolve the Ballerina Gradle plugin dependency when building a ballerina library package on Windows
  - 📍 Module: `module/All` (Area/Connector/Generated Connectors)

- 🐛 **[#6569](https://github.com/ballerina-platform/ballerina-library/issues/6569)** Invalid parameters in the generated twilio:Client object in the diagram viewer in the Ballerina VS Code plugin
  - 📍 Module: `module/twilio` (Area/Connector/Generated Connectors)

- 🐛 **[#6472](https://github.com/ballerina-platform/ballerina-library/issues/6472)** Add Connector option of VSCode sequence diagram provides invalid names for the twitter module
  - 📍 Module: `module/twitter` (Area/Connector/Generated Connectors)

- 📋 **[#6342](https://github.com/ballerina-platform/ballerina-library/issues/6342)** Re-Enable temporarily disabled example builds on Candid Module
  - 📍 Module: `module/candid` (Area/Connector/Generated Connectors)

- ✨ **[#5046](https://github.com/ballerina-platform/ballerina-library/issues/5046)** [Improvement]: Improving Azure CosmosDB connector to support Managed Identities
  - 📍 Module: `module/cosmosdb` (Area/Connector/Generated Connectors)

- 🐛 **[#8387](https://github.com/ballerina-platform/ballerina-library/issues/8387)** Duplicate Parameter Name Generation in Types
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 🐛 **[#8217](https://github.com/ballerina-platform/ballerina-library/issues/8217)** Unaligned type name with spaces
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 🐛 **[#8205](https://github.com/ballerina-platform/ballerina-library/issues/8205)** OpenAPI generation incorrectly resolves additional properties, object when included in oneOf type
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 🐛 **[#7508](https://github.com/ballerina-platform/ballerina-library/issues/7508)** Invalid Ballerina.toml generation `openapi add` in Windows
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- ✨ **[#8132](https://github.com/ballerina-platform/ballerina-library/issues/8132)** Support OpenAPI CLI command options as tool options in Ballerina.toml
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- ✨ **[#6709](https://github.com/ballerina-platform/ballerina-library/issues/6709)** Add full support for OpenAPI specification version - `3.1.0`
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- ✨ **[#5118](https://github.com/ballerina-platform/ballerina-library/issues/5118)** Improve the error message given when client and service generation failed
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 📋 **[#8362](https://github.com/ballerina-platform/ballerina-library/issues/8362)** Check and re-enable windows tests which are failing in the workflow
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 📋 **[#8196](https://github.com/ballerina-platform/ballerina-library/issues/8196)** AI-Powered Automation for Ballerina Connector Generation
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 📋 **[#6785](https://github.com/ballerina-platform/ballerina-library/issues/6785)** Support server sent events in the openapi
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 📋 **[#6612](https://github.com/ballerina-platform/ballerina-library/issues/6612)** Add a changelog file into OpenAPI repository 
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 📋 **[#5127](https://github.com/ballerina-platform/ballerina-library/issues/5127)** OpenAPI to Ballerina Service spec writing
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 📋 **[#5128](https://github.com/ballerina-platform/ballerina-library/issues/5128)** OpenAPI to Ballerina Client spec writing
  - 📍 Module: `module/openapi-tools` (Area/Tooling)

- 🐛 **[#8323](https://github.com/ballerina-platform/ballerina-library/issues/8323)** Text Column Type Conversion Issue in Ballerina Persist Tool
  - 📍 Module: `module/persist-tools` (Area/Tooling)

- 🐛 **[#6931](https://github.com/ballerina-platform/ballerina-library/issues/6931)** [Ballerina Persist] Error when connecting to PostgreSQL on AWS
  - 📍 Module: `module/persist-tools` (Area/Tooling)

- 🐛 **[#6392](https://github.com/ballerina-platform/ballerina-library/issues/6392)** The ballerina project crashes without giving a proper error message for associated entities containing defaultable fields
  - 📍 Module: `module/persist-tools` (Area/Tooling)

- 📋 **[#8242](https://github.com/ballerina-platform/ballerina-library/issues/8242)** Enable the Disabled Tests in Persist Tools
  - 📍 Module: `module/persist-tools` (Area/Tooling)

- 📋 **[#7398](https://github.com/ballerina-platform/ballerina-library/issues/7398)** Re-enable tests disabled in persist-tools module during Java 21 Migration
  - 📍 Module: `module/persist-tools` (Area/Tooling)

- 📋 **[#6337](https://github.com/ballerina-platform/ballerina-library/issues/6337)** Improve the logic in cache of the persist code generation 
  - 📍 Module: `module/persist-tools` (Area/Tooling)

- 📋 **[#6434](https://github.com/ballerina-platform/ballerina-library/issues/6434)** Update `FunctionBodyGenerator` for `NodeFactory.createOnFailClauseNode` change
  - 📍 Module: `module/graphql-tool` (Area/Tooling)

- 🐛 **[#7772](https://github.com/ballerina-platform/ballerina-library/issues/7772)** Import statement absent in the ballerina file created using the xsd tool
  - 📍 Module: `module/xsd-tool` (Area/Tooling)

- 🐛 **[#7771](https://github.com/ballerina-platform/ballerina-library/issues/7771)** Xsd-tool module flag error
  - 📍 Module: `module/xsd-tool` (Area/Tooling)

- 🐛 **[#6837](https://github.com/ballerina-platform/ballerina-library/issues/6837)** GRPC client sample code generation is failing when protobuf schema contains cyclic dependent messages
  - 📍 Module: `module/grpc` (Area/Tooling)

- 🐛 **[#6837](https://github.com/ballerina-platform/ballerina-library/issues/6837)** GRPC client sample code generation is failing when protobuf schema contains cyclic dependent messages
  - 📍 Module: `module/protoc-tool` (Area/Tooling)

- 📋 **[#5748](https://github.com/ballerina-platform/ballerina-library/issues/5748)** Support code generation to Ballerina PreBuildRunner task within the Protoc tool
  - 📍 Module: `module/protoc-tool` (Area/Tooling)

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

