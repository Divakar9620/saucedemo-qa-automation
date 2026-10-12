# Test Cases – SauceDemo

**Application:** https://www.saucedemo.com
**Prepared by:** Divakar S
**Techniques used:** Positive/negative testing, Equivalence Partitioning, Boundary checks, End-to-end flow testing

| ID | Module | Scenario | Steps | Test Data | Expected Result | Priority | Automated |
|----|--------|----------|-------|-----------|-----------------|----------|-----------|
| TC-01 | Login | Valid login | Enter valid username and password, click Login | standard_user / secret_sauce | Products page opens | High | Yes |
| TC-02 | Login | Locked-out user | Enter locked user credentials, click Login | locked_out_user / secret_sauce | Error: user has been locked out | High | Yes |
| TC-03 | Login | Wrong password | Enter valid username with wrong password | standard_user / wrong_password | Error: username and password do not match | High | Yes |
| TC-04 | Login | Unregistered user | Enter unknown username | unknown_user / secret_sauce | Error: username and password do not match | Medium | Yes |
| TC-05 | Login | Empty username | Leave username blank, click Login | "" / secret_sauce | Error: Username is required | Medium | Yes |
| TC-06 | Login | Empty password | Leave password blank, click Login | standard_user / "" | Error: Password is required | Medium | Yes |
| TC-07 | Login | Both fields empty | Click Login with no input | "" / "" | Error: Username is required | Low | Yes |
| TC-08 | Login | Password case sensitivity | Enter password in uppercase | standard_user / SECRET_SAUCE | Login fails with error | Medium | Yes |
| TC-09 | Security | Direct URL access without login | Open /inventory.html without logging in | – | Redirected to login with error | High | Yes |
| TC-10 | Login | Logout | Open menu, click Logout | – | Login page is displayed | High | Yes |
| TC-11 | Security | Back button after logout | Log out, press browser Back, refresh | – | User stays logged out | High | Yes |
| TC-12 | Products | Product count | Log in and view products | – | 6 products displayed | Medium | Yes |
| TC-13 | Products | Valid prices | Check every product price | – | All prices greater than 0 | Medium | Yes |
| TC-14 | Products | Sort A to Z | Select "Name (A to Z)" | – | Names in ascending order | Medium | Yes |
| TC-15 | Products | Sort Z to A | Select "Name (Z to A)" | – | Names in descending order | Medium | Yes |
| TC-16 | Products | Sort price low to high | Select "Price (low to high)" | – | Prices in ascending order | Medium | Yes |
| TC-17 | Products | Sort price high to low | Select "Price (high to low)" | – | Prices in descending order | Medium | Yes |
| TC-18 | Cart | Add to cart | Click "Add to cart" on a product | Sauce Labs Backpack | Badge shows 1, button changes to "Remove" | High | Yes |
| TC-19 | Cart | Remove from products page | Add then click "Remove" | Sauce Labs Backpack | Badge disappears, button reverts | High | Yes |
| TC-20 | Cart | Cart persists after refresh | Add 2 items, refresh page | Backpack, Bike Light | Badge still shows 2 | Medium | Yes |
| TC-21 | Cart | Items shown in cart | Add 2 items, open cart | Backpack, Onesie | Both items listed | High | Yes |
| TC-22 | Cart | Remove from cart page | Add item, open cart, click Remove | Sauce Labs Backpack | Cart is empty | Medium | Yes |
| TC-23 | Cart | Continue shopping | Open cart, click "Continue Shopping" | – | Products page opens, cart count unchanged | Low | Yes |
| TC-24 | Checkout | End-to-end purchase | Add items, checkout, fill details, finish | Divakar / S / 560001 | "Thank you for your order!" shown | High | Yes |
| TC-25 | Checkout | Total calculation | Proceed to overview | 2 items | Subtotal = sum of prices; Total = Subtotal + Tax | High | Yes |
| TC-26 | Checkout | Missing first name | Leave first name blank, click Continue | "" / S / 560001 | Error: First Name is required | Medium | Yes |
| TC-27 | Checkout | Missing last name | Leave last name blank, click Continue | Divakar / "" / 560001 | Error: Last Name is required | Medium | Yes |
| TC-28 | Checkout | Missing postal code | Leave postal code blank, click Continue | Divakar / S / "" | Error: Postal Code is required | Medium | Yes |
| TC-29 | Checkout | problem_user enters last name | Log in as problem_user, go to checkout, type last name | problem_user | Last name field keeps typed value | High | Yes (xfail – BUG-001) |
| TC-30 | UI | Product images for problem_user | Log in as problem_user, view products | problem_user | Each product shows its own image | Medium | No (manual) |
| TC-31 | Performance | Login response time | Log in as performance_glitch_user | performance_glitch_user | Products page loads within acceptable time | Low | No (manual) |
