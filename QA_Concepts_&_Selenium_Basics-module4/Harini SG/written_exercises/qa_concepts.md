# Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Testing Types

### 1. Test Cases for Different Testing Levels

**Unit Testing**
- Test: Verify that the function to create a course stores the course correctly.
- Type: Functional Testing

**Integration Testing**
- Test: Verify that the API endpoint correctly stores course data in the database.
- Type: Functional Testing

**System Testing**
- Test: Verify that a user can create a course through the API and retrieve it successfully.
- Type: Functional Testing

**User Acceptance Testing (UAT)**
- Test: Verify that a college administrator can create a new course without errors.
- Type: Functional Testing

### Non-Functional Test Example

- Performance Testing: Verify that the API responds within 2 seconds when 100 users access it simultaneously.

### Black-Box vs White-Box Testing

**Black-Box Testing**
- Tests the application without knowing the internal code.
- Usually performed by QA Testers.

**White-Box Testing**
- Tests the internal code, logic, and structure.
- Usually performed by Developers.
## 2. Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC001 | Create course with valid data | API is running | Send POST request with valid course details | Course created successfully with HTTP 201 | | |
| TC002 | Create course with missing course name | API is running | Send POST request without course name | HTTP 400 Bad Request | | |
| TC003 | Create duplicate course | Course already exists | Send POST request with existing course details | Duplicate course error returned | | |


## Task 2: Defect Lifecycle

### Defect Lifecycle

New → Assigned → Open → Fixed → Retest → Verified → Closed

**Rejected:** Bug is not valid.

**Deferred:** Bug fix is postponed to a future release.


### Severity and Priority

**a) POST /api/courses/ returns 500 Internal Server Error**
- Severity: Critical
- Priority: P1

**b) Course name longer than 150 characters is truncated**
- Severity: Medium
- Priority: P2

**c) Typo in Swagger documentation**
- Severity: Low
- Priority: P4

**d) Login occasionally returns 401**
- Severity: High
- Priority: P1
### Defect Report

- **Defect ID:** DEF001
- **Title:** POST /api/courses/ returns 500 Internal Server Error
- **Environment:** Windows 11, Python 3.12, Flask API
- **Build Version:** 1.0
- **Severity:** Critical
- **Priority:** P1
- **Steps to Reproduce:**
  1. Start the API.
  2. Send a POST request to `/api/courses/`.
  3. Observe the response.
- **Expected Result:** Course should be created successfully with HTTP 201.
- **Actual Result:** API returns HTTP 500 Internal Server Error.
- **Attachments:** Screenshot of 500 error.

---

## Severity vs Priority

**Severity** is the impact of the bug on the application.

**Priority** is how quickly the bug should be fixed.

### Example

A spelling mistake on the CEO's dashboard:
- Severity: Low (does not affect functionality)
- Priority: High (must be fixed quickly because it is visible to the CEO).

---

## Conclusion

This hands-on covered:
- Testing levels
- Functional and Non-Functional Testing
- Black-Box and White-Box Testing
- Formal Test Cases
- Defect Lifecycle
- Severity and Priority
- Defect Report