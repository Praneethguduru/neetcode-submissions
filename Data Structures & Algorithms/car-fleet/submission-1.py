class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions = sorted(zip(position, speed), reverse = True)
        times = [(target - p)/s for p, s in sorted_positions]
        prev_time = 0
        fleet = 0 
        for time in times:
            if time > prev_time:
                fleet += 1
                prev_time = time
        return fleet