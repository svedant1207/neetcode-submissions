class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        # Use 'curr' to track where the user currently is
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        # Create new node, link it back to current, and move forward
        new_node = Node(url, prev=self.curr)
        self.curr.next = new_node
        self.curr = self.curr.next 

    def back(self, steps: int) -> str:
        # Move back up to 'steps' times, but stop if we hit the beginning
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
            
        # Return the string value of the page we landed on
        return self.curr.val

    def forward(self, steps: int) -> str:
        # Move forward up to 'steps' times, but stop if we hit the end
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
            
        # Return the string value of the page we landed on
        return self.curr.val