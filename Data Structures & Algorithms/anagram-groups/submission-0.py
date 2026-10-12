class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# чтобы проверить две строки, можно сделать каунтер/словарь с буквами
# как хранить {"шаблон группы" : индекс элемента в изначальном массиве}, 
# если шаблон это словарь

# бля, словарь из 26 букв это кринге, ну ладно

        result_map = {}
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - 97] += 1

            counter = tuple(counter)
            if counter not in result_map:
                result_map[counter] = []
            result_map[counter].append(s)
        
        return list(result_map.values())