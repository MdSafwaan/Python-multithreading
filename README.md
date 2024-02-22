# Message Processing System

This is a message processing system implemented in Python. It allows users to add messages with priorities, peek at the top message in the priority queue, and stop the program.

## Requirements

 Python 3.11.2


## Usage

1. Run the program:
  python main.py

2. Follow the on-screen instructions to interact with the message processing system:
- Choose option 1 to add a message.
- Choose option 2 to peek at the top message in the priority queue.
- Choose option 3 to stop the program.

## Test Cases

### Adding a Message

- **Description**: User adds a message with high priority.
- **Steps**:
1. Choose option 1 to add a message.
2. Enter priority as 0 (high).
3. Enter message content.
- **Expected Outcome**: Message is added to the priority queue and processed immediately.

### Peeking at the Top Message

- **Description**: User peeks at the top message in the priority queue.
- **Steps**:
1. Choose option 2 to peek at the top message.
- **Expected Outcome**: Details of the top message (if any) are displayed to the user.

### Stopping the Program

- **Description**: User chooses to stop the program.
- **Steps**:
1. Choose option 3 to stop the program.
- **Expected Outcome**: Program terminates gracefully.

## Additional Information

- The system utilizes threads and a priority queue for efficient message processing.
- User input is handled through the command line interface.
- Message processing occurs in the background, allowing users to interact with the system seamlessly.




