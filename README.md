# A Message from your Local Representative
Querying Homework Assignment for ENGN1931Z

When working with online resources and web services, we will often want to combine several Application Programming Interfaces (APIs) to construct a new tool. In this homework, you will need combine the Census.Gov Geocoding Service with the OpenStates.org API to learn about the recent work of local state senators. 

Note that the [Census Geocoding API](http://www.census.gov/data/developers/data-sets/Geocoding-services.html) is an open public tool that can provide a wealth of information, but therefore can be somewhat slow to respond (sometimes even fail to respond). Therefore, one challenge will be to define your API calls as much as possible (e.g. by only requesting the appropriate layer).

In constrast, the [OpenStates.org API](http://sunlightlabs.github.io/openstates-api/index.html) is a private tool which is optimized for specific purposes. Speed will probably not be an issue, but you will need to register for an API key and then map out the necessary requests to use both the [Legislator Search](http://sunlightlabs.github.io/openstates-api/legislators.html#methods/legislator-search) and [Bill Search](http://sunlightlabs.github.io/openstates-api/bills.html#methods/bill-search) methods.

Your goal is to determine most recent bill sponsored by the state senator who represents a randomly choosen address in the United States. To achieve this goal, you should:
  - First parse the state's two-letter abbreviation from the address string using regular expressions;
  - Then use the Census.gov Geocoding API onelineaddress geographies search to find the 2016 Upper State Legislative District.
  - Next use the OpenStates.org API legislator method to determine the full name of the senator in this district.
  - Finally use the OpenStates.org API bills method to find the title of the last bill sponsored by this senator. (If none, then return 'nothing'.)

`hwQuerying.py` is a template code for the assignment. **Please review the comments at the top of that file.**  `submit.py` is the script that will submit your code to the autograder.

Please note you are welcome to try this assignment as many times as you would like. (There is no penalty for failed attempts, because I wanted to encourage you to practice, test, and debug.) **However, please make sure to obey the class collaboration policy --- do not share your code with others; please write and debug on your own!**
