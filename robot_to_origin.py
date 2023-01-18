"""There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves,
judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move.
Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once,
'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each
move.

 """

"(0,0) origin"


def robot_to_origin(string):
    left_Right_check = 0
    Up_down_check = 0
    for i in string:
        if i == "U":
            Up_down_check += 1
        elif i == "D":
            Up_down_check -= 1
        elif i == "L":
            left_Right_check += 1
        elif i == "R":
            left_Right_check -= 1

    if left_Right_check == Up_down_check:
        return True
    return False


print(robot_to_origin("LL"))
