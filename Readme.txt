Github - Open issue tracker
---------------------------

input format : https://github.com/{username}/{repo}/issues

Technology Used : 
-----------------
	* Python 3.4 
	* JSON
	* urllib requets
	* GITHUB APIs
	
Approach : 
----------
	I have used urllib request to make a API request to Github. The result is then processed using Python and then output is displayed.
	* Step - 1 :
		* Input the URL from the User
		* Validate the URL(regex is used)
                
	* Step - 2 :
		* Then a API request is made with the given url
		* Response is got as JSON and it is processed to get the created date of all the open issues.
	* Step - 3 :
		* Calculate the difference between the current time stamp and open issues time stamp and classify them as one of the 3 categories ( 1. Less than 24Hrs, 2. Greater than 24Hrs but less than 7days, 3. Greater than 7days ) and increment the corresponding count.
	* Step - 4 :
		* The final output is then printed.
		
Improvements that can be made with more time :
----------------------------------------------
	* The URL validation can be done more effectively.
	* The UI could have been been added and made attractive.
	* Other errors that can occur could have beeen managed.
	* Could have been able to more clearly understand the working of the APIs
        * could have hosted in any other server for Python.
	