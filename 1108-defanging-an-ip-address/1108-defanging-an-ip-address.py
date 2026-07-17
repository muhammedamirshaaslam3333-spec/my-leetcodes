class Solution:
    def defangIPaddr(self, address: str) -> str:
        for i in address:
            if i ==".":
                h=  address.replace(".","[.]")
        return h

