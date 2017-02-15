from marisa_trie import Trie
import re


class TrieSearch(Trie):
    def __init__(self, patterns=None, filepath=None):
        super(TrieSearch, self).__init__(patterns)
        if filepath:
            self.load(filepath)

    def search_all_patterns(self, text, splitter=u' '):
        text_idx = 0
        for line in re.split(ur'[\n\r]', text):
            if splitter:
                words = re.split(splitter, line)
            else:
                words = line
            line_idx = 0
            for i, w in enumerate(words):
                for pattern in self.__search_prefix_patterns(w, words[i + 1:],
                                                             splitter):
                    yield pattern, text_idx + line_idx
                line_idx += len(w) + len(splitter)
            text_idx += line_idx

    def search_longest_patterns(self, text, splitter=u' '):
        all_patterns = self.search_all_patterns(text, splitter)
        check_field = [0] * len(text)
        for pattern, start_idx in sorted(
                all_patterns, key=lambda x: len(x[0]), reverse=True):
            target_field = check_field[start_idx:start_idx + len(pattern)]
            check_sum = sum(target_field)
            if check_sum != len(target_field):
                for i in range(len(pattern)):
                    check_field[start_idx + i] = 1
                yield pattern, start_idx

    def __search_prefix_patterns(self, query, remaining_words, splitter=u' '):
        if query in self:
            yield query
        # generate next query
        if len(remaining_words):
            next_query = splitter.join((query, remaining_words[0]))
            if self.has_keys_with_prefix(next_query):
                for ptn in self.__search_prefix_patterns(
                        next_query, remaining_words[1:], splitter):
                    yield ptn
