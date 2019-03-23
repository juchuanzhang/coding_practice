class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for item in emails:
            at_index = item.find("@")
            local = item[0: at_index]
            domain = item[at_index: len(item)]
            for i in range(0, at_index):
                if local[i] == '+':
                    local = local[0: i]
                    break
            local = local.replace('.', '')
            item_final = local + domain
            result.add(item_final)
        return len(result)


solution = Solution()
input = ["test.email+alex@leetcode.com",
         "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
output = solution.numUniqueEmails(input)
print(output)
