## Basic Terms in Excel

1. **Formulas**
In Excel, a formula is an expression that operates on values in a range of cells or a cell.

2. **Functions**
Functions are predefined formulas in Excel.

Example:

=SUM(B1:C1) – A simple selection that sums the values of a row.

=SUM(A1:A10) – A simple selection that sums the values of a column.

=SUM(A3:A7, A9, A12:A15) – A sophisticated collection that sums values from range A2 to A7, skips A8, adds A9, jumps A10 and A11, then finally adds from A12 to A15.

=SUM(A1:A10)/20 – Shows you can also turn your function into a formula.


#### Functions:

**TRIM**

The TRIM function makes sure your functions do not return errors due to unruly spaces. It ensures that all empty spaces are eliminated.

**MAX & MIN**
The MAX and MIN functions help in finding the maximum number and the minimum number in a pull of values.

**LEN**
If you want to count the number of characters in a single cell, including white spaces.

**CONCATENATE**

Concatenate gives a way to combine a list of text items from multiple cells.

Example:
=CONCATEBATE(B2, "", A1, "lives in", C2 ".") 
Output==> Name Surname lives in City.

To avoid extra empty spaces use TRIM with CONCATENATE:
=trim(CONCATEBATE(B2, "", A1, "lives in", C2 "."))

**PROPER** 

To ensure that names and places are properly capitylized.

**UPPER**

UPPER makes all letters upper case.

**LOWER**

Makes all letters lower case.

#### Math Functions:

There are two kinds of arithmetic operations in spreadsheets those done with arithmetic operators and those that use functions.

Arithmetic operators:
- addition: =add()
- substraction: =substruct()
- multiplication: =multiply()
- division: =divide()

**Statistical Functions**:

A couple of very useful statistical functions:
=sum()
=average()

#### Duplicate Rows

Tabel level data operations are useful for cleaning manipulating lists of data.
When clean data, we're trying to rid it of corrupt and inaccurate data items.

**Google Sheets Instructions**

If you are using Google Sheets as your spreadsheet application, there is an add-on named      [Remove Duplicates](https://chrome.google.com/webstore/detail/remove-duplicates/bckmhokpcdnhhjldhhfpebhdfipmlbog?hl=en) that makes this a very easy operation. Once you install the add-on, remove duplicates by highlighting the columns and selecting.
`Add-ons->Remove Duplicates`

#### Split Columns
To split column se text to columns tool. 

If work with larger data sets, its can be helpful to "freeze" the header row or far left column as you scroll through data. To do this, use the View->Freeze Panes operation in Excel or View->Freeze in Google Sheets to select the rows or columns you want to always be visible.


#### Filter Data 

Fiktering data is a way to group data by selecting characteristics from our data columns and not looking at the other data.