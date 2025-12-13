class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        import re

        def is_alnum_underscore(s):
            return bool(re.fullmatch(r"[A-Za-z0-9_]+", s))

        res = [
            (code[i], i)
            for i in range(len(code))
            if isActive[i]  and businessLine[i] != "invalid"
        ]
        # print(res)
        res.sort(key=lambda x: (businessLine[x[1]], x[0]))
        return [x[0] for x in res if is_alnum_underscore(x[0])]
