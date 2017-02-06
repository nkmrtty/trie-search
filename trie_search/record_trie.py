from marisa_trie import RecordTrie
from .trie import TrieSearch


class RecordTrieSearch(RecordTrie, TrieSearch):
    def __init__(self, record_format, records=None, filepath=None):
        super(RecordTrieSearch, self).__init__(record_format, records)
        if filepath:
            self.load(filepath)

    def search_all_patterns(self, text, splitter=u' ', min_weight=0.0):
        for pattern, start_idx in super(
                RecordTrie, self).search_all_patterns(text, splitter):
            weight = self[pattern][0][0]
            if weight < min_weight:
                continue
            yield pattern, start_idx, weight

    def search_longest_patterns(self, text, splitter=u' ', min_weight=0.0):
        all_patterns = self.search_all_patterns(text, splitter, min_weight)
        check_field = [0] * len(text)
        for pattern, start_idx, weight in sorted(
                all_patterns,
                key=lambda x: len(x[0].split(splitter)),
                reverse=True):
            target_field = check_field[start_idx:start_idx + len(pattern)]
            check_sum = sum(target_field)
            if check_sum != len(target_field):
                for i in range(len(pattern)):
                    check_field[start_idx + i] = 1
                yield pattern, start_idx, weight
