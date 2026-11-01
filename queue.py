event_queue = []

def add_event(event):
    event_queue.append(event)
    print(f"{event} added to the queue successfully.")

def process_next_event():
    if event_queue:
        event = event_queue.pop(0)
        print(f"{event} is processed successfully.")

    else:
        print("No event is processed.")

def display_pending_event():
    if event_queue:
        print("Pending Events.")
        for i, event in enumerate(event_queue,1):
            print(f"{i}.{event}")
    else:
        print("No pending event or event is already processed.")

def cancel_event(event_name):
    if event_name in event_queue :
        event_queue.remove(event_name)
        print(f"{event_name} is cancelled.")
    else:
        print("event not found or already cancelled")

def menu():
    while True:
        print("\n ---Menu---")
        print("1.add event")
        print("2.process next event")
        print("3.display pending event")
        print("4.cancel event")
        print("5.exit")

        choice = int(input("Enter the choice:"))

        if choice==1:
            event = input("enter the event to add:")
            add_event(event)
        elif choice==2:
            process_next_event()
        elif choice==3:
            display_pending_event()
        elif choice==4:
            event_name = input("Enter the event name:")
            cancel_event(event_name)
        elif choice==5:
            print("Exiting....")
            break
        else:
            print("Invalid choice")

menu()


    




