# cs5213s20-project-g4
Corona virus desease model to find count of infected patients.

Input:

{Number of rows = rows 

Number of columns = cols.

Start date= start date in the term time frame 

End date= end date in the term time frame 

Infected patients’ locations = provided the infected patients locations as input.}

In a given matrix, each cell can have one of three values:

•	the value 0 representing an empty healthy person.

•	the value 1 representing a fresh infected person.

•	the value ‘A’ representing an antibody.

Presumptions: 

1.	Consistently, any healthy individual that is neighboring (8-directionally) to a tainted individual gets contaminated with infection.
2.	Here we are expecting that solitary 2 out of 8 adjacent individuals gets tainted randomly every day. So, we will take any 2 of the directions.

Output:

We have to locate the contaminated patients in between start date and end date.

Following is the step by step procedure for developing the application :

Step 1:
Firstly, we create the matrix with the provided row size and column size and fill the entire matrix with zeroes.

Step 2:
Secondly, we take 10 random locations and represent them as antibodies.

Step 3:
Thirdly, based on the infected locations provided, the matrix is filled with 1’s

Step 4:
Finally, we apply our graph algorithm for finding the infected patients 

1.	Also, to execute this model, we developed two rest web services, one is the post web service for providing the data sources like row size of a matrix, column size of a matrix, tainted patients area, start date and end date.
The input format is similar to the following:
{ 
	"rows":"10",
	"cols":"10",
	"start":"1",
	"end":"7",
	"points":"[]"
}

2.	The second web service is the get service through which we get the resultant grid after the end date. Furthermore, we get data with respect to number of patients tainted during the span.
