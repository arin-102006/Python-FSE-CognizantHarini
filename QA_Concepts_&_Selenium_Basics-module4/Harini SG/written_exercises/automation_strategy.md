# Hands-On 3: Test Automation Process, Lifecycle & Framework Types

## Task 1: Automation Decision and Test Case Selection

### 1. Criteria for Automation

1. Repetitive test cases
2. Regression testing
3. Stable functionality
4. Data-driven testing
5. Time-consuming manual tests

**Example:** The POST `/api/courses/` endpoint is a good candidate for automation because it is repetitive, stable, and frequently tested.

---

### 2. Automate or Manual

| Test Case | Decision | Reason |
|-----------|----------|--------|
| Regression test for CRUD APIs | Automate | Executed frequently |
| Exploratory testing | Manual | Requires human observation |
| Performance test | Automate | Tool-based execution |
| Login UI test | Automate | Repeated often |
| Swagger documentation check | Manual | Visual verification |
| Smoke test after deployment | Automate | Quick verification |

---

### 3. Test Automation ROI

- Automation Time = 4 hours = 240 minutes
- Manual Execution = 30 minutes

Break-even:

240 ÷ 30 = **8 runs**

After the 10th run, maintenance takes additional effort, but automation still saves time over repeated manual execution.

---

### 4. Flaky Test

A flaky test is a test that sometimes passes and sometimes fails without any code changes.

Example:
- Clicking a button before it becomes clickable.

Ways to prevent flaky tests:
1. Use Explicit Waits.
2. Avoid `time.sleep()`.
3. Use stable locators (ID or CSS).
## Task 2: Automation Framework Types

### Linear Framework
**Description:** Test steps are written in a single script from start to finish.

**Advantage:** Easy to develop.

**Disadvantage:** Difficult to maintain.

**Example:** Simple login automation.

---

### Modular Framework
**Description:** The application is divided into separate modules.

**Advantage:** Reusable code.

**Disadvantage:** Initial setup takes time.

**Example:** Separate modules for Login, Courses, and Students.

---

### Data-Driven Framework
**Description:** Test data is stored in external files such as Excel or CSV.

**Advantage:** Same test runs with multiple inputs.

**Disadvantage:** Managing data files can be complex.

**Example:** Testing login with multiple usernames and passwords.

---

### Keyword-Driven Framework
**Description:** Tests are executed using predefined keywords.

**Advantage:** Non-programmers can create tests.

**Disadvantage:** Framework setup is complex.

**Example:** Keywords like Click, EnterText, Verify.

---

### Hybrid Framework
**Description:** Combines Modular, Data-Driven, and Keyword-Driven approaches.

**Advantage:** Flexible and highly reusable.

**Disadvantage:** More complex to design.

**Example:** Enterprise Selenium automation projects.

---

## Recommended Framework

A **Hybrid Framework** is recommended because:
- Supports multiple login test data.
- Reuses common modules.
- Easy to maintain.
- Suitable for both technical and non-technical team members.

---

## Hybrid Framework Folder Structure

```
Hybrid_Framework/
│
├── tests/
├── pages/
├── test_data/
├── utilities/
├── config/
├── reports/
└── screenshots/
```

---

## Conclusion

This hands-on covered:
- Automation decision criteria
- Test Automation ROI
- Flaky tests
- Automation framework types
- Hybrid framework recommendation