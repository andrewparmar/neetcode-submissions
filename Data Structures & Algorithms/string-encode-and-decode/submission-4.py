class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        list to string
        question doesn't say what encoding to use
        """
        res = ""
        for s in strs:
            res = f"{res}#{len(s)}#{s}"
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        # return s.split(".")
        res = []
        l = 0
        # counter = 0
        while l < len(s):
            if s[l] == "#":
                r = l + 1
                # print(l, r) 
                # counter = 0
                while s[r] != "#":
                    r += 1
                    # print(r)
                    # counter += 1
                    # if counter == 5:
                    #     break
                # print(s[l:r])
                count = int(s[l+1:r])
                res.append(s[r+1:r+1+count])
                l = r + 1 + count
                # print(res, l)
                # counter += 1
                # if counter == 5:
                #     break
                
        return res
            
