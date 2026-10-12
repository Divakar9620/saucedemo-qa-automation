# Bug Reports – SauceDemo

SauceDemo includes test accounts with intentional defects. The reports below
follow a standard defect-report format.

---

## BUG-001: Last Name field does not keep entered text for problem_user

| Field | Details |
|-------|---------|
| **Module** | Checkout – Your Information |
| **Environment** | https://www.saucedemo.com, Chrome (latest), Windows/Linux |
| **User** | problem_user / secret_sauce |
| **Severity** | High – checkout cannot be completed |
| **Priority** | High |
| **Status** | Open |
| **Linked test** | TC-29, `tests/test_checkout.py::test_problem_user_can_enter_last_name` |

**Steps to reproduce**
1. Log in as `problem_user`.
2. Add any product to the cart and open the cart.
3. Click **Checkout**.
4. Type a first name, then type a value into **Last Name**.

**Expected result:** The Last Name field shows the typed value.
**Actual result:** The Last Name field does not keep the typed value, so the user cannot complete checkout.

---

## BUG-002: All products show the same image for problem_user

| Field | Details |
|-------|---------|
| **Module** | Products page |
| **User** | problem_user / secret_sauce |
| **Severity** | Medium – wrong product information shown |
| **Priority** | Medium |
| **Status** | Open |
| **Linked test** | TC-30 (manual) |

**Steps to reproduce**
1. Log in as `problem_user`.
2. Look at the product images on the Products page.

**Expected result:** Each product shows its own image.
**Actual result:** Every product shows the same image, which does not match the product.

---

> **Note:** Before publishing, reproduce each bug yourself and attach a
> screenshot (drag the image into the GitHub editor). Update the "Actual
> result" if what you see differs.
