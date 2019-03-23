class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        station_num = len(gas)
        # start station
        for i in range(0, station_num):
            station = i
            total_gas = 0
            flag = True
            while 1:
                if total_gas + gas[station] < cost[station]:
                    flag = False
                    # print(station)
                    break
                else:
                    total_gas = total_gas + gas[station] - cost[station]
                    # print(station, total_gas)
                    station = (station + 1) % station_num
                if station == (i + station_num) % station_num:
                    break
            if flag:
                # print(station)
                return i
        return -1


solution = Solution()
# input_gas = [2, 3, 4]
# input_cost = [3, 4, 3]
# input_gas = [1, 2, 3, 4, 5]
# input_cost = [3, 4, 5, 1, 2]
input_gas = [5, 8, 2, 8]
input_cost = [6, 5, 6, 6]
output = solution.canCompleteCircuit(input_gas, input_cost)
print(output)
