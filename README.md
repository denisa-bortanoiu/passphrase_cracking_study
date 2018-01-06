# passphrase_cracking_study
## Introduction

Nowadays, most of user data is password protected, in an effort to preserve the privacy of this information, but the security of most accounts is left at the latitude of the user, which has the choice of his passwords. Indeed, most recommendations suggest using long and random passwords, but, as they are usually hard to remember, the user forgoes one of these key suggestions, more specifically the random criteria. Usually, humans decide on using passphrases – sequences of words or other text. 

The main objective of this study is comparing methods for cracking passphrases with lengths of up to 10 characters. We consider that the passphrases are linguistically correct and contain only lowercase letters (the punctuation and white spaces are completely removed). The three approaches presented are: brute-force attacks, dictionary attacks, and, finally, attacks using Markov Chains [1]. 

## Theory 

### Brute-force approach 

A brute-force search, also known as an exhaustive search, is a very simple attack which consists of calculating all possible combinations that could make up a password and testing it to verify it is the correct solution. It is a cryptanalytic attack that might be used when no other weaknesses in an encryption system may be taken advantage of.  

This approach is easy to implement and always guarantees finding the solution, but it is a very time-consuming attack. The resources needed for such an attack grow exponentially as the password’s length increases and most brute-force tools can perform decently for lengths of up to 10 characters. Given that passphrases are usually longer than 10 characters, this approach does not produce good results. 

### Dictionary attack 

A dictionary attack is generally an improvement of the aforementioned method. It implies trying likely possibilities instead of any random string. It checks all the words in an exhaustive, pre-arranged list, typically derived from listing such as dictionaries. 

Comparative to brute-force attacks, this type of attack only tries possibilities with are more likely to succeed, as many people choose short, common passwords that usually consist of ordinary words. Both single word and multiple word passphrases are highly susceptible to be cracked by this type of attack [2]. 

### Markov Chains Approach 

This approach described next was proposed by Peder Sparell and Mikael Simovits in their paper, Linguistic Cracking of Passphrases using Markov chains. They set out to improve the former attack methods, starting with the idea that the probability of certain sequences' occurrences is higher than others in human language. They worked with sequences consisting of characters and words and they based their implementation on 2 fundamental concepts: Markov chains and N-grams. 

#### Markov chains  

A Markov chain is “a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event” [3]. A Markov process is a “memoryless” process, and if satisfies the Markov property. This property requires that a future state of the process is not dependent upon the sequence of events that were before the present state, which is the only one which influences the future state. 

#### N-grams 

An N-gram is a contiguous sequence of N items from a given sequence. An item might reference either a character or a word. A (n-1)-order Markov model can be used for representing a n-gram model, as it is a type of probabilistically predicting the next item in a sequence.  

It can become apparent why using n-grams can be a step forward into passphrase cracking, as trying more probably frequent sequences first is an improvement comparative to the brute-force attack. 

### Implementation 

The three methods were implemented for comparison and made available to the public [4]. All approaches use an Oracle, a class which contains a secret passphrase and provides a method for checking is a guess is correct or not. All types of attacks were wrapped into classes with an attack(oracle) method. 

The BruteForce and Dictionary classes are very similar and implement their attack methods the same: a list of all possible combinations (guesses) is generated and each guess is verified by the oracle until we either run out of guesses or we crack the password held by the oracle. They can receive the length range for their guesses (number of characters and respectively number of words). The difference between them consists of the space out of which we form the combination:

 * for BruteForce, the alphabet consists of the 26 lowercase English-alphabet letters.  
 * for Dictionary, we initialise the guess list by reading a very large file [5] and extracting the most frequent words used. 

As Sparell and Simovits proposed in their work, the Markov Chains approach to cracking passphrases is implemented in two scripts: ngram_extraction, which uses a large file [5] consisting of several books to extract the frequency of word n-grams and markov_chains_attack, which uses the output of the first script to generate passphrases. The current implementation only considers word n-grams, in contrast to Sparell et al.'s work which also takes into account character n-grams. 

When extracting the n-grams, in the ExtractNgrams class, all punctuation is replaced by white spaces, exception making the following characters (',', '.', '!', '?', ';', ':') which usually mark breaks in speech. Any of these characters (or sequence of characters) is replaced by a single dot. The resulting n-grams are written to a file, each on a line and followed by the number of occurrences they had in the file. 

The main algorithm for the Markov chains attack is explained in the proposing paper and it follows the same steps: 

 

This implementation considers all n-grams as possible initial states and iterates through them following the generation algorithm above. The n-grams are filtered to match a higher occurrence rate as the threshold (by default, we require at least 10 occurrences). As before, when a likely phrase is found, we test it with the given oracle. 

## References

[1] P. Sparell and M. Simovits. "Linguistic Cracking of Passphrases using Markov chains." 

[2] J. Bonneau and E. Shutove, "Linguistic properties of multi-word passphrases" 

[3] Markov chain | Definition of Markov chain in US English by Oxford Dictionaries. Oxford Dictionaries | English. 
