def solution(w,h):
    number = max(w, h)
    devisor = min(w, h)
    while number % devisor != 0:
        remainder = number % devisor
        number = devisor
        devisor = remainder
    total = w * h
    blockW = w / devisor
    blockH = h / devisor
    unusable = devisor * (blockW + blockH - 1)
    return int(total - unusable)
