# Hands-On 2: SDLC vs TDLC – V-Model & Agile QA Integration

## Task 1: V-Model Mapping

### V-Model

Requirements           → Acceptance Testing

System Design          → System Testing

Architecture Design    → Integration Testing

Module Design          → Unit Testing

Coding (Bottom of V)

---

### Test Artifacts

| SDLC Phase | TDLC Phase | Test Artifact |
|------------|------------|---------------|
| Requirements | Acceptance Testing | Acceptance Test Plan |
| System Design | System Testing | System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan |
| Module Design | Unit Testing | Unit Test Cases |

---

### Entry and Exit Criteria

#### Unit Testing
- Entry: Module code completed.
- Exit: All unit tests passed.

#### Integration Testing
- Entry: Modules integrated.
- Exit: Interfaces work correctly.

#### System Testing
- Entry: Complete application available.
- Exit: System requirements satisfied.

#### Acceptance Testing
- Entry: System testing completed.
- Exit: Customer approves the application.

---

### QA Involvement

1. Requirement Review
2. Test Case Preparation before coding
## Task 2: Agile QA and Shift-Left Testing

### Problems in Waterfall Model

1. Bugs are found very late.
2. Fixing defects becomes expensive.
3. Project delivery gets delayed.

---

### QA Role in Agile

**Sprint Planning**
- Review requirements.
- Define acceptance criteria.

**Daily Stand-up**
- Discuss testing progress.
- Report blockers.

**Sprint Review**
- Verify completed features.
- Demonstrate testing results.

**Retrospective**
- Suggest process improvements.
- Discuss lessons learned.

---

### Shift-Left Practices

1. Review requirements before development.
2. Write test cases before coding.
3. Perform static code analysis.
4. Conduct API contract testing before integration.

---

### Acceptance Criteria (Given-When-Then)

#### Scenario 1: Valid Course Creation

**Given** the admin is on the course creation page

**When** valid course details are entered

**Then** the course should be created successfully.

---

#### Scenario 2: Duplicate Course Code

**Given** a course code already exists

**When** the admin submits the same course code

**Then** an error message should be displayed.

---

#### Scenario 3: Missing Required Fields

**Given** mandatory fields are empty

**When** the admin submits the form

**Then** validation errors should be shown.

---

## Conclusion

This hands-on covered:
- SDLC and TDLC
- V-Model
- Entry and Exit Criteria
- Agile QA
- Shift-Left Testing
- Gherkin Acceptance Criteria