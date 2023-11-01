# [DONE] Home Page
Buttons with vertical layout
- unGSTfy Label
- Calculate Taxable Value
- Calculate GST Percent
- Currency Converter


# [DONE] Calculating Taxable Value
import re  
pattern = re.compile(r'[0-9.]+')  

amount_with_gst_input_str = str(input())    # Get user input for Total Amount with GST.  
rate_of_gst_input_str = str(input())        # Get user input for GST percent.  

amount_with_gst = amount_with_gst_input_str if amount_with_gst_input_str and re.fullmatch(pattern, amount_with_gst_input_str) else '0.0'    # Validating user input is digits.  
rate_of_gst = rate_of_gst_input_str if rate_of_gst_input_str and re.fullmatch(pattern, rate_of_gst_input_str) else '0.0'                    # Validating user input is digits.  

amount_with_gst = amount_with_gst if amount_with_gst[0] != '.' else '0'+amount_with_gst    # If use input starts with a dot(.) then add 0 in prefix.  
rate_of_gst = rate_of_gst if rate_of_gst[0] != '.' else '0'+rate_of_gst                    # If use input starts with a dot(.) then add 0 in prefix.  

amount_without_gst = (100 * float(amount_with_gst)) / (100 + float(rate_of_gst))  
result = str(round(amount_without_gst, 10))  


# [DONE] Calculating GST percent
import re  
pattern = re.compile(r'[0-9.]+')  

amount_with_gst_input_str = str(input())        # Get user input for Total Amount with GST.  
amount_without_gst_input_str = str(input())     # Get user input for Taxable Value  

amount_with_gst = amount_with_gst_input_str if amount_with_gst_input_str and re.fullmatch(pattern, amount_with_gst_input_str) else '0.0'                # Validating user input is digits.  
amount_without_gst = amount_without_gst_input_str if amount_without_gst_input_str and re.fullmatch(pattern, amount_without_gst_input_str) else '0.0'    # Validating user input is digits.  

amount_with_gst = amount_with_gst if amount_with_gst[0] != '.' else '0'+amount_with_gst                # If use input starts with a dot(.) then add 0 in prefix.  
amount_without_gst = amount_without_gst if amount_without_gst[0] != '.' else '0'+amount_without_gst    # If use input starts with a dot(.) then add 0 in prefix.  

rate_of_gst = ((float(amount_with_gst) / float(amount_without_gst)) - 1) * 100 if float(amount_with_gst) != 0.0 and float(amount_without_gst) != 0.0 else 0.0  
result = str(round(rate_of_gst, 10))  


# [TODO] Currency Converter
Same as google currency converter, auto calculates when inserted data, two integer box side by side, and just below it are the currency convertion drop downs.  
With non-negative float value validation.
```
                                    Convert From Value
Value of Convert From     =     ------------------------------    x    EUR exchange of 1 Convert To     =     Value of Convert To
                                EUR exchange of 1 Convert From
```

List of all Currencies: http://api.exchangeratesapi.io/v1/symbols?access_key=012432093fd9fd5a4f33393fee22c95b  
1 value Exchange Rates of all currencies: http://api.exchangeratesapi.io/v1/latest?access_key=012432093fd9fd5a4f33393fee22c95b&base=EUR  

If data not found for today in the sqlite3 database whenever the page loads, then hit the API, save in the DB, if no internet (show user the status of it).


# [TODO] Search for TODO comments and do it.


# [TODO] Converting Py to executable
https://coderslegacy.com/pyinstaller-spec-file-tutorial/    # PyInstaller spec file tutorial  
https://coderslegacy.com/cx_freeze-vs-pyinstaller-comparison/    # cx_freeze vs pyinstaller  
https://coderslegacy.com/nuitka-vs-pyinstaller/    # nuitka vs pyinstaller  
https://coderslegacy.com/better-alternatives-to-pyinstaller/    # pyinstaller alternatives  
https://coderslegacy.com/python-cx_freeze-tutorial/    # cx_freeze tutorial  
https://www.youtube.com/watch?v=UFz5kNTRk3g    # py_compile  
