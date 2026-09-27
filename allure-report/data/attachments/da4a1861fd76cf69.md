# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: smoke\login.spec.js >> login to new user
- Location: tests\smoke\login.spec.js:6:5

# Error details

```
Error: locator.click: Target page, context or browser has been closed
Call log:
  - waiting for getByText('Sign out', { exact: true })

```

```
Error: browserContext.close: Target page, context or browser has been closed
```