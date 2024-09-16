class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam_maps = {}
        for log in logs:
            uam_maps[log[0]] = uam_maps.get(log[0], )
            