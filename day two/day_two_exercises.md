Exercise 1: One of the first known examples of encryption was used by Julius Caesar. Caesar needed to provide written instructions to his generals, but he didn’t want his enemies to learn his plans if the message slipped into their hands. As result, he developed what later became known as the Caesar Cipher. The idea behind this cipher is simple (and as a result, it provides no protection against modern code breaking techniques). Each letter in the original message is shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc. The last three letters in the alphabet are wrapped around to the beginning: X becomes A, Y becomes B and Z becomes C. Non-letter characters are not modified by the cipher. Write a program that implements a Caesar cipher. Allow the user to supply the message and the shift amount, and then display the shifted message. Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift values so that it can be used both to encode messages and decode messages. Hints: ord(), chr()

    https://learncryptography.com/classical-encryption/caesar-cipher
    
Exercise 2: Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase “i” should be replaced with an uppercase “I” if it is both preceded and followed by a space. The first character in the string should also be capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the function is provided with the string “what time do i have to be there? what’s the address?” then it should return the string “What time do I have to be there? What’s the address?”. Include a main program that reads a string from the user, capitalizes it using your function, and displays the result.


Exercise 3: Two words are anagrams if they contain all of the same letters, but in a different order. For example, “evil” and “live” are anagrams because each contains one e, one i, one l, and one v. Create a program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.


Exercise 4: The Sieve of Eratosthenes is a technique that was developed more than 2,000 years ago to easily find all of the prime numbers between 2 and some limit, say 100. A description of the algorithm follows: Write down all of the numbers from 0 to the limit Cross out 0 and 1 because they are not prime Set p equal to 2 While p is less than the limit do Cross out all multiples of p (but not p itself) Set p equal to the next number in the list that is not crossed out Report all of the numbers that have not been crossed out as prime The key to this algorithm is that it is relatively easy to cross out every nth number on a piece of paper. This is also an easy task for a computer—a for loop can simulate this behavior when a third parameter is provided to the range function. When a number is crossed out, we know that it is no longer prime, but it still occupies space on the piece of paper, and must still be considered when computing later prime numbers. As a result, you should not simulate crossing out a number by removing it from the list. Instead, you should simulate crossing out a number by replacing it with 0. Then, once the algorithm completes, all of the non-zero values in the list are prime. Create a Python program that uses this algorithm to display all of the prime numbers between 2 and a limit entered by the user. If you implement the algorithm correctly you should be able to display all of the prime numbers less than 1,000,000 in a few seconds.

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


Exercise 5: Did you know our numeral system - the symbols we use to represent numbers are called Arabic numerals? Fun fact, because now it gets serious. You're going to be translating Arabic to Italian.
Have the input form accept a number from the user. When the form is submitted, have the function to_roman take an integer as an argument and return a roman numerals string. For example:

60 >> LX  

78 >> LXXVIII  

99 >> XCIX  

3000 >>> MMM  

Look up Roman Numerals to get a complete list and jog your memory on its ancient conventions. This is an easy challenge to code, but can be a difficult mental exercise. Don't overcomplicate it! Hints: divmod(a, b)
https://en.wikipedia.org/wiki/Roman_numerals


Exercise 6:
Write a function named reverseLookup that finds all of the keys in a dictionary that map to a specific value. The function will take the dictionary and the value to search for as its only parameters. It will return a (possibly empty) list of keys from the dictionary that map to the provided value. Include a main program that demonstrates the reverseLookup function as part of your solution to this exercise. Your program should create a dictionary and then show that the reverseLookup function works correctly when it returns multiple keys, a single key, and no keys. Ensure that your main program only runs when the file containing your solution to this exercise has not been imported into another program. Use french words as keys to english words. Example: "le":"the", "chat":"cat", "livre":"book", "pomme":"apple"
