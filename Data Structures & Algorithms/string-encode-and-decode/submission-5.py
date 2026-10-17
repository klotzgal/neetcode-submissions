class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}|{s}'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            i = s.find('|')
            if i == -1:
                break
            length = int(s[:i])
            res.append(s[i + 1:i + 1 + length])
            s = s[i + 1 + length:]
        return res