# 🔴 Highest Priority Issues

**Total Issues:** 24

## Area/Library

### 📦 module/http (7 issues)

#### ✨ Improvement

- **[#5799](https://github.com/ballerina-platform/ballerina-library/issues/5799)** [HTTP Client] Support for resolving round-robin DNS
- **[#4329](https://github.com/ballerina-platform/ballerina-library/issues/4329)** Interceptor support for client side
- **[#3630](https://github.com/ballerina-platform/ballerina-library/issues/3630)** Improve `Connection between remote client and host is closed` error message

#### 🚀 NewFeature

- **[#7460](https://github.com/ballerina-platform/ballerina-library/issues/7460)** Allow configuring TCP Keep-Alive related properties in the Ballerina HTTP Client
- **[#6547](https://github.com/ballerina-platform/ballerina-library/issues/6547)** Add HTTP compression support for `brotli` format

#### 📋 Task

- **[#7330](https://github.com/ballerina-platform/ballerina-library/issues/7330)** Disabled tests due to the Jsondata module fixes
- **[#4213](https://github.com/ballerina-platform/ballerina-library/issues/4213)** Make HTTP module FIPS compliant

### 📦 module/persist (5 issues)

#### 🐛 Bug

- **[#7920](https://github.com/ballerina-platform/ballerina-library/issues/7920)** Query Expressions with Persist Clients do not push down 'where' conditions to the database, leading to inefficient in-memory filtering
- **[#4745](https://github.com/ballerina-platform/ballerina-library/issues/4745)** Compiler crash in persist for model with few records
- **[#4081](https://github.com/ballerina-platform/ballerina-library/issues/4081)** [Persist] `time:Utc` type values mismatch on retrieval

#### ✨ Improvement

- **[#5736](https://github.com/ballerina-platform/ballerina-library/issues/5736)** Allow passing config parameters to the generated persist client and set default values to configurable variables
- **[#4812](https://github.com/ballerina-platform/ballerina-library/issues/4812)** Ballerina Persist module not support association(1:N) that can have nilable values

### 📦 module/sql (3 issues)

#### 🐛 Bug

- **[#5097](https://github.com/ballerina-platform/ballerina-library/issues/5097)** [Bug]: Unable use map<anydata> instead of record {} 
- **[#4081](https://github.com/ballerina-platform/ballerina-library/issues/4081)** [Persist] `time:Utc` type values mismatch on retrieval

#### ✨ Improvement

- **[#3842](https://github.com/ballerina-platform/ballerina-library/issues/3842)** Add support to enable logs to detect connection leaks in DB connectors

### 📦 module/jwt (2 issues)

#### ✨ Improvement

- **[#8185](https://github.com/ballerina-platform/ballerina-library/issues/8185)** Ballerina JWT library does not support PS 256 and ES 256 algorithms
- **[#7510](https://github.com/ballerina-platform/ballerina-library/issues/7510)** JWT Validation - Support for RFC 8725

### 📦 module/grpc (2 issues)

#### 🐛 Bug

- **[#4762](https://github.com/ballerina-platform/ballerina-library/issues/4762)** [Bug]: gRPC runtime error with `readonly` parameter in isolated function
- **[#3274](https://github.com/ballerina-platform/ballerina-library/issues/3274)** Client error is not received in server when `grpc:Caller` is used to send values inside the client stream

### 📦 module/crypto (1 issues)

#### 📋 Task

- **[#4212](https://github.com/ballerina-platform/ballerina-library/issues/4212)** Make Crypto module FIPS compliant

### 📦 module/time (1 issues)

#### ✨ Improvement

- **[#1841](https://github.com/ballerina-platform/ballerina-library/issues/1841)** Ballerina should be able to parse strings in custom time formats

## Area/Connector/Handwritten Connectors

### 📦 module/All (1 issues)

#### 📋 Task

- **[#7816](https://github.com/ballerina-platform/ballerina-library/issues/7816)** Finalize the Ballerina Connectors release progress with breaking changes

### 📦 module/salesforce (1 issues)

#### 📚 Docs

- **[#8209](https://github.com/ballerina-platform/ballerina-library/issues/8209)** Update Ballerina Use Case Page with Salesforce Event Listener

### 📦 module/mysql (1 issues)

#### 🐛 Bug

- **[#3511](https://github.com/ballerina-platform/ballerina-library/issues/3511)** Database parameter is not validated in MySQL connector

