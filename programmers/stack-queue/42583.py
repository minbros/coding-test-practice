# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    from collections import deque

    time = 0
    bridge = deque(maxlen=bridge_length)
    times = deque(maxlen=bridge_length)

    while len(truck_weights) or len(bridge):
        if len(times) and times[0] <= time:
            bridge.popleft()
            times.popleft()

        if len(truck_weights) and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
            times.append(time + bridge_length)

        time += 1

    return time
