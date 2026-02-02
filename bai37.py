class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        words_list = re.findall(r'\w+', paragraph.lower())
        word_dict = defaultdict(int)
        for i in words_list:
            if i in word_dict:
                word_dict[i] += 1
            else:
                word_dict[i] = 1
        sorted_dict = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
        for word, fre in sorted_dict:
            if word not in banned:
                return word
        

        