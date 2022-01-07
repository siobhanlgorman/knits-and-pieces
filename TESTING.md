# Knits and Pieces Testing
## Manual Testing
Thorough testing was conducted by the developer and multiple users among friends and family especially with order creation, updating totals, editing line items. Bugs were found and fixed as detailed below in Bugs section. Testing steps and results are detailed as follows.

## User Stories Testing
## Features Testing
## Browser Compatibility
## Responsiveness
## Bugs and Fixes
1. Toast success message doesn't display if same item is added again to basket. Fix: Error in if statement in bag/views.py
2. Image media url not working. FIx - add media context processor in settings.py
3. Can-custom design - displaying text by default - FIX incorrect format of if statement
4. Zip code error - indefinite number of numbers and error message pointing to order - error in views.py keys had values which were strings not variables ('' around the variables) - FIX '' removed
5. Checkout_success no reverse match found although payment in stripe succeeded. Discovered order number not being generated. Fix: Narrowed issue down to order generation in models.py update total function and found indentation errors.
6. Error after adding countryfield - could not migrate. Folder still looking for max value of 2. Eventually deleted all orders in the database as they were created wth countries longer than 2 letters. Then the migration worked.
7. After creating profile and linking to order history two orders being created in db with two different numbers. Fix - corrected stripe billing and shipping name fields. Due to subsequent ongoing issues with duplicate orders being created and non-recognition of two name fields in billing and shipping information, the order model field was reverted to full name and first and last name fields removed as they can be accessed from using the full name method
8. Remove button bug with W3C validator - two ids as element on mobile and desktop views at same time (hidden on one). Fix: Id changed to data-id

![#](documentation/screenshots/##.png)
## Code Validation
### HTML Validation
HTML was validated by [The WEC Markup Validation Service](https://validator.w3.org/)

No errors or warnings were found:

Home Page: 

![](documentation/screenshots/home_valid.png)

About Page:

![](documentation/screenshots/about_valid.png)

Custom Order Page

![](documentation/screenshots/custom_valid.png)

Contact Page

![](documentation/screenshots/contact_valid.png)

Register Page

![](documentation/screenshots/register_valid.png)

Sign In Page

![](documentation/screenshots/signin_valid.png)

Sign Out Page
![](documentation/screenshots/signout_valid.png)


### CSS Validation

![](documentation/screenshots/css_valid1.png)
![](documentation/screenshots/css_valid2.png)
![](documentation/screenshots/css_valid.png)

### PEP 8 Validation

The following files were checked:

* **#/views.py**

![](documentation/screenshots/pep8_views2.png)


* **#/views.py**

![](documentation/screenshots/pep8_views.png)

* **models.py**

![](documentation/screenshots/pep8_models.png)

* **forms.py**

![](documentation/screenshots/pep8_forms.png)

* **urls.py**

![](documentation/screenshots/pep8_urls.png)

* **admin.py**

![](documentation/screenshots/pep8_admin.png)

## Lighthouse Scores
## Accessibility