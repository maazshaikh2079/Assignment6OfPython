# Info:-
# Name   : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-6
# Topic  :-
# 1)Create a function named ds with parameters roll_no and name.
# 2)Add those parameters in the following data structures:
# list, tuple, sets and dictionaries
# 3) After adding values
# change the values during runtime
# 4)Delete these data structures
# Date   : 20-06-2023

# Program:-
def ds(roll_no,name=''):
    yield roll_no
    yield name;

infoList=list(ds(109,"Maaz"));
print("Information  'List'      :",infoList);
print();

infoTuple=tuple(ds(108,"Rafe"));
print("Information  'Tuple'     :",infoTuple);
print();

infoSet=set(ds(117,"Shrikant"));
print("Information  'Set'       :",infoSet);
print();

dsReturn=ds(75,"Lucky");
infoDict={ "Roll no.": next(dsReturn), "Name": next(dsReturn) }
print("Information 'Dictionary' :",infoDict);
print();

rn=int(input("Enter roll no.: "));
nm=input("Enter name    : ");
print();

infoList=list(ds(rn,nm));
print("Information 'List' :",infoList);
print();

rn=int(input("Enter roll no.: "));
nm=input("Enter name    : ");
print();

infoTuple=tuple(ds(rn,nm));
print("Information 'Tuple' :",infoTuple);
print();

rn=int(input("Enter roll no.: "));
nm=input("Enter name    : ");
print();

infoSet=set(ds(rn,nm));
print("Information 'Set' :",infoSet);
print();

rn=int(input("Enter roll no.: "));
nm=input("Enter name    : ");
print();

dsReturn=ds(rn,nm);
infoDict={ "Roll no.": next(dsReturn), "Name": next(dsReturn) }
print("Information 'Dictionary' :",infoDict);

# Output:-
# Information  'List'      : [109, 'Maaz']

# Information  'Tuple'     : (108, 'Rafe')

# Information  'Set'       : {'Shrikant', 117}

# Information 'Dictionary' : {'Roll no.': 75, 'Name': 'Lucky'}

# Enter roll no.: 47
# Enter name    : Mario

# Information 'List' : [47, 'Mario']

# Enter roll no.: 65
# Enter name    : Wahaj

# Information 'Tuple' : (65, 'Wahaj')

# Enter roll no.: 51
# Enter name    : Amaan

# Information 'Set' : {'Amaan', 51}

# Enter roll no.: 116
# Enter name    : Vishal 

# Information 'Dictionary' : {'Roll no.': 116, 'Name': 'Vishal'}