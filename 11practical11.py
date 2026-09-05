# Binary Tree for Folder/File Structure

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


# Create folder/file structure
root = Node("Root")

root.left = Node("Documents")
root.right = Node("Pictures")

root.left.left = Node("Resume.pdf")
root.left.right = Node("Assignment.docx")

root.right.left = Node("Photo1.jpg")
root.right.right = Node("Photo2.jpg")


# Display tree structure
def display(node, level=0):
    if node is not None:
        print("  " * level + "|-- " + node.name)

        display(node.left, level + 1)
        display(node.right, level + 1)


print("===== FOLDER / FILE STRUCTURE =====")
display(root)