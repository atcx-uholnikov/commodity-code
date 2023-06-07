# commodity-code
Django Web App project for searching samples of customs clearance of goods in the database. (Django + SQL)

### ADDITIONAL EXTANTIONS AND PACKAGES:
-  django-bootstrap-icons==0.8.2
-  fuzzywuzzy==0.18.0
-  Levenshtein==0.20.8


### 1. Start interface for searching
![1 start search](https://github.com/atcx-uholnikov/commodity_code/assets/10896191/1cb2e059-4bfa-4fc1-b6dd-036601fec86b)

The user can enter a search request in two formats:
- by the numerical code of the product (full or short code) 
- by a text description of the product

!!! The searching process logic assumes that the more detailed the entered query is, the smaller the sample will be provided to the user as a result.

### 2. Searching results

2.1 If there is no information on the user's request, then a message about this will be displayed:
![2 nothing was found](https://github.com/atcx-uholnikov/commodity_code/assets/10896191/f888ea66-5629-4504-9e24-8a589ef769c1)

2.2 If at the request of the user information is found, the following form will be displayed:
![3 result](https://github.com/atcx-uholnikov/commodity_code/assets/10896191/a7768c9b-438d-4ff0-8870-6c655b0772f9)

The user can operate the following data:
+ The query that was entered (**"printer"**)
+ Number of items in the search result (**2**)
+ And directly by information blocks with search results, in which the main parameters are specified: (**request compiliance, HS code, customs fee, commodity description, source, date**)


