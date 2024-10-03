# non_word_count.py
# Vamshikrishna Pandilla, DOB: January 25, 2000

from mrjob.job import MRJob
import re
from spellchecker import SpellChecker

class MRNonEnglishWordCount(MRJob):

    # Regex pattern to match words
    WORD_RE = re.compile(r"[\w']+")
    
    def mapper_init(self):
        # Initialize spellchecker
        self.spell = SpellChecker()

    def mapper(self, _, line):
        # Check for non-English words in the line
        for word in self.WORD_RE.findall(line):
            word_lower = word.lower()
            if word_lower not in self.spell:
                yield (word_lower, 1)

    def reducer(self, word, counts):
        # Sum the counts for each non-English word
        yield (word, sum(counts))

if __name__ == '__main__':
    MRNonEnglishWordCount.run()