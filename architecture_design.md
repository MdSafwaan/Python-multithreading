# Message Processing System Documentation

## Overview

The message processing system implemented in this assignment allows users to add messages with priorities, peek at the top message in the priority queue, and stop the program. The system consists of two main components: `UserInputThread` and `ProcessThread`, which interact with each other to handle user input and process messages.

## Implemented Solution

The implemented solution utilizes threads and a priority queue to manage message processing. The `UserInputThread` is responsible for handling user input and interacting with the `ProcessThread` to perform actions such as adding messages, peeking at messages, and stopping the program. On the other hand, the `ProcessThread` continuously processes messages from the priority queue based on their priority.

## Data Structures and Algorithms Used

### Data Structures:
- `Message`: Represents a message with content, priority, and a unique identifier.
- `PriorityQueue`: Utilized for storing messages based on their priority.

### Algorithms:
- Enqueuing: Messages are added to the priority queue based on their priority.
- Processing: Messages are processed in the order of their priority, with higher priority messages being processed first.
- Peeking: Allows users to view the top message in the priority queue without removing it.

## Building and Running the Program

### Requirements:
- Python 3.11.2

## Test Cases and Expected Outcomes

### Test Case 1: Adding a Message
- Description: User adds a message with high priority.
- Steps:
1. Choose option 1 to add a message.
2. Enter priority as 0 (high).
3. Enter message content.
- Expected Outcome: Message is added to the priority queue and processed immediately.

### Test Case 2: Peeking at the Top Message
- Description: User peeks at the top message in the priority queue.
- Steps:
1. Choose option 2 to peek at the top message.
- Expected Outcome: Details of the top message (if any) are displayed to the user.

### Test Case 3: Stopping the Program
- Description: User chooses to stop the program.
- Steps:
1. Choose option 3 to stop the program.
- Expected Outcome: Program terminates gracefully.

## Conclusion

The message processing system provides a convenient way to manage messages with different priorities. By utilizing threads and a priority queue, the system ensures efficient processing of messages while allowing users to interact with it seamlessly.



