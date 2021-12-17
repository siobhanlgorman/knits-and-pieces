Manual Testing
User Stories Testing
Features Testing
Browser Compatibility
Responsiveness
Bugs and Fixes
1. Toast success message doesn't display if same item is added again to basket. Error in if statement in bag/views.py
2. Image media url not working. FIx - add media context processor in settings.py
3. Can-custom design - displaying text by default - FIX incorrect format of if statement
4. Zip code error - indefinite number of numbers and error message pointing to order - error in views.py keys had values which were strings not variables ('' around the variables) - FIX '' removed
5. checkout_success no reverse match found although payment in stripe succeeded. Discovered order number not being generated. Fix: Narrowed issue down to order generation in models.py update total function and found indentation errors.
![#](documentation/screenshots/##.png)
Code Validation
Lighthouse Scores
Accessibility