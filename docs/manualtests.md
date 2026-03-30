### Manual Testing

#### Authentication Testing

| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 1 | User Registration with valid data | Account created successfully, user logged in | pass |
![1](media/1-1.png)
![1](media/1-2.png)
![1](media/1-3.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 2 | User Registration with invalid email | Error message displayed, registration fails | pass |
![2](media/2-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 3 | User Registration with weak password | Error message displayed, registration fails | pass |
![3](media/3-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 4 | User Login with valid credentials | User logged in successfully, redirected to home | pass |
![4](media/4-1.png)
![4](media/4-2.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 5 | User Login with invalid credentials | Error message displayed, login fails | pass |
![5](media/5-1.png)
![5](media/5-2.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 6 | User Logout | User logged out successfully, session ended | pass |
![6](media/6-1.png)
![6](media/6-2.png)

#### Product Browsing Testing

| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 7 | View All Products | All products displayed in grid layout | pass |
![7](media/7-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 8 | Product Detail View | Detailed product information displayed | pass |
![8](media/8-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 9 | Filter by Category | Only products from selected category shown | pass |
![9](media/9-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 11 | Sort by Price (Low to High) | Products sorted in ascending price order | pass |
![11](media/11-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 12 | Sort by Price (High to Low) | Products sorted in descending price order | pass |
![12](media/12-1.png)

#### Shopping Cart Testing

| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 13 | Add Product to Bag | Product added successfully | pass |
![13](media/13-1.png)
![13](media/13-2.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 14 | Add Same Product Multiple Times | Quantity increases, not duplicate entries | pass |
![14](media/14-1.png)
![14](media/14-2.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 15 | View Cart Contents | All cart items displayed with correct details | pass |
![15](media/15-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 16 | Update Item Quantity | Quantity updated, totals recalculated | pass |
![16](media/16-1.png)
![16](media/16-2.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 17 | Remove Item from Cart | Item removed, totals recalculated | pass |
![17](media/17-1.png)
![17](media/17-2.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 18 | Empty Cart Display | Appropriate message shown for empty cart | pass |
![18](media/18-1.png)


#### Checkout Testing

| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 19 | Checkout with Valid Payment | Order processed successfully, confirmation shown | pass |
![19](media/19-1.png)
![19](media/19-2.png)
![19](media/19-3.png)
![19](media/19-4.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 20 | Checkout with Invalid Card | Error message displayed, order not processed | pass |
![20](media/20-1.png)
![20](media/20-2.png)

#### Responsive Design Testing

| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 21 | Mobile View (320px-767px) | All elements display correctly on mobile | pass |
![21](media/21-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 22 | Tablet View (768px-1199px) | All elements display correctly on tablet | pass |
![22](media/22-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 23 | Desktop View (1200px+) | All elements display correctly on desktop | pass |
![23](media/23-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|
| 24 | Navigation Menu Mobile | Hamburger menu works correctly | pass |
![24](media/24-1.png)
| Test | Test Description | Expected Result | Status |
|-----------|------------------|-----------------|---------|