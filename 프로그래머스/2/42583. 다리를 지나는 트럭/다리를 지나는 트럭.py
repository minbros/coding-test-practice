def solution(bridge_length, weight, truck_weights):
    from collections import deque

    time = 0
    bridge = deque()
    times = deque()

    while len(truck_weights) or len(bridge):
        if len(times) and times[0] <= time:
            bridge.popleft()
            times.popleft()

        if len(truck_weights) and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
            times.append(time + bridge_length)

        time += 1

    return time