# Task Management using Stack and Queue

from collections import deque

# ---------- STACK ----------
stack = []

print("===== STACK: TASK MANAGEMENT =====")

# Push tasks
stack.append("Complete Assignment")
stack.append("Study Python")
stack.append("Prepare PPT")

print("Tasks in Stack:", stack)

# Peek
print("Top Task:", stack[-1])

# Pop
completed_task = stack.pop()
print("Completed Task:", completed_task)
print("Stack after completion:", stack)


# ---------- QUEUE ----------
queue = deque()

print("\n===== QUEUE: TASK MANAGEMENT =====")

# Add tasks
queue.append("Attend Lecture")
queue.append("Submit Assignment")
queue.append("Practice Coding")

print("Tasks in Queue:", list(queue))

# Peek
print("First Task:", queue[0])

# Remove task
completed_task = queue.popleft()
print("Completed Task:", completed_task)

print("Queue after completion:", list(queue))