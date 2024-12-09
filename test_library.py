def main():
    testaddbooks()
    testsearchword()
      #testing out valid book titles :)
def testaddbooks():
    try:
        assert ("BFG".lower())=="bfg".lower()
    except AssertionError:
        print("Your output is inncorrect. 'Please try again until you get 'BFG'.")
    try:
        assert ("Shatter me".lower())=="shatter me".lower()
    except AssertionError:
        print("Your output is inncorrect. Please try again until you get 'Shatter me'.")
    try:
        assert ("The plauge".lower())=="the plague".lower()
    except AssertionError:
        print("Your output is inncorrect. Please try again until you get 'The plauge'.")
    try:
        assert ("Wuthering heights".lower())=="wuthering heights".lower()
    except AssertionError:
        print("Your output is inncorrect. Please try again until you get 'Weathering heights'.")
    try:
        assert ("Jane Eyre".lower())=="jane eyre".lower()
    except AssertionError:
     print("Your output is inncorrect. Please try again until you get 'Jane Eyre'.")
     # testing out invalid book tites :(
    try:
        assert  ("A2345664")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
    try:
        assert ("asdrgfkgjd")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
    try:
        assert ("lime")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
    try:
        assert ("d0009")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")

 #testing out valid author names :(
    try:
        assert ("Albert Camus".lower())=="albert camus"
    except AssertionError:
        print("Your output is inncorrect. 'Please try again until you get 'Albert Camus'.")
    try:
        assert ("Jane Austen".lower())=="jane austen"
    except AssertionError:
        print("Your output is inncorrect. Please try again until you get 'Jane Austen'.")
    try:
        assert ("Mary Shelley".lower())=="mary shelley".lower()
    except AssertionError:
        print("Your output is inncorrect. Please try again until you get ' Mary Shelley'.")
    try:
        assert ("Bram Stoker".lower())=="bram stoker".lower()
    except AssertionError:
        print("Your output is inncorrect. Please try again until you get 'Bram Stoker'.")
    try:
        assert ("Rebecca F. Kuang")=="rebecca f. kuang".lower()
    except AssertionError:
     print("Your output is inncorrect. Please try again until you get 'Rebecca F. Kuang'.")

     #testing out invlaid author names :(
    try:
        assert  ("X Æ A-12")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
    try:
        assert ("fghyte")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
    try:
        assert ("4r56fg")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
    try:
        assert ("S5555")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
 
def testsearchword():
    try:
        assert ("Picture".lower())=="picture"
    except AssertionError:
        print("Your output is inncorrect. 'Please try again until you get 'Picture'.")
    try:
        assert ("Life".lower())=="life".lower()
    except AssertionError:
        print("Your output is inncorrect. Please try again until you get 'Life'.")
    try:
        assert ("Brother".lower())=="brother".lower()
    except AssertionError:
        print("Your output is inncorrect. Please try again until you get 'Brother'.")
    try:
        assert ("Heights".lower())=="heights".lower()
    except AssertionError:
        print("Your output is inncorrect. Please try again until you get 'heights'.")
    try:
        assert ("Count".lower())=="count".lower()
    except AssertionError:
     print("Your output is inncorrect. Please try again until you get 'Count'.")
     # testing out invalid book tites :(
    try:
        assert  ("Lidl")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
    try:
        assert ("apple")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
    try:
        assert ("3d5g")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")
    try:
        assert ("b")=="Your input is incorrect. Please try again"
    except AssertionError:
        print("Your output is inncorrect.")