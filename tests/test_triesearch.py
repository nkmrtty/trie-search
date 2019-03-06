from unittest import TestCase
from trie_search.trie import TrieSearch


class TestTrieSearch(TestCase):
    def test_search_all_patterns(self):
        patterns = ['new york', 'york city', 'new york city']
        text = 'new york city'
        answers = {'new york': 0, 'york city': 4, 'new york city': 0}
        trie = TrieSearch(patterns=patterns)

        for ptn, idx in trie.search_all_patterns(text):
            self.assertIn(ptn, answers)
            self.assertEqual(idx, answers[ptn])

    def test_search_longest_patterns(self):
        patterns = ['new york', 'york city', 'new york city']
        text = 'new york city'
        answers = {'new york city': 0}
        trie = TrieSearch(patterns=patterns)

        for ptn, idx in trie.search_longest_patterns(text):
            self.assertIn(ptn, answers)
            self.assertEqual(idx, answers[ptn])

    def test_search_all_patterns_jp(self):
        patterns = ['ニューヨーク', 'ヨークシティ', 'ニューヨークシティ']
        text = 'ニューヨークシティ'
        answers = {'ニューヨーク': 0, 'ヨークシティ': 3, 'ニューヨークシティ': 0}
        trie = TrieSearch(patterns=patterns, splitter='')

        for ptn, idx in trie.search_all_patterns(text):
            self.assertIn(ptn, answers)
            self.assertEqual(idx, answers[ptn])

    def test_search_longest_patterns_jp(self):
        patterns = ['ニューヨーク', 'ヨークシティ', 'ニューヨークシティ']
        text = 'ニューヨークシティ'
        answers = {'ニューヨークシティ': 0}
        trie = TrieSearch(patterns=patterns, splitter='')

        for ptn, idx in trie.search_longest_patterns(text):
            self.assertIn(ptn, answers)
            self.assertEqual(idx, answers[ptn])
