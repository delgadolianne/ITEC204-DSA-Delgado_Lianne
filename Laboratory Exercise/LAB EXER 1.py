# ==========================================
#       INCIDENT TICKET MANAGEMENT SYSTEM
# ==========================================

incidents = [
    ["INC1392939", "BOT-Inventory", "Failed to generate the daily report"],
    ["INC1392940", "BOT-Email", "Failed to send the scheduled notification"],
    ["INC1392941", "BOT-DataSync", "Encountered an error during data transfer"],
    ["INC1392942", "BOT-Invoice", "Failed to process an invoice"],
    ["INC1392943", "BOT-Report", "Failed to generate the weekly report"],
    ["INC1392944", "BOT-FileTransfer", "Failed to upload the required file"],
    ["INC1392945", "BOT-DataEntry", "Encountered an error while entering records"],
    ["INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"],
    ["INC1392947", "BOT-Validation", "Failed to validate the submitted records"],
    ["INC1392948", "BOT-Notification", "Failed to send the system alert"]
]


# ==========================================
# 1. ADD INCIDENT TICKET
# ==========================================

def add_ticket():
    print("\n===== ADD INCIDENT TICKET =====")

    incident_id = input("Enter Incident ID: ").strip()

    if incident_id == "":
        print("ERROR: Incident ID cannot be empty.")
        return

    # Check if ID already exists
    for ticket in incidents:
        if ticket[0] == incident_id:
            print("ERROR: Incident ID already exists.")
            return

    bot = input("Enter Bot: ").strip()

    if bot == "":
        print("ERROR: Bot cannot be empty.")
        return

    description = input("Enter Short Description: ").strip()

    if description == "":
        print("ERROR: Short Description cannot be empty.")
        return

    incidents.append([incident_id, bot, description])

    print("SUCCESS: Incident ticket added.")


# ==========================================
# 2. DISPLAY ALL ACTIVE TICKETS
# ==========================================

def display_tickets():
    print("\n===== ACTIVE INCIDENT TICKETS =====")

    if len(incidents) == 0:
        print("ERROR: There are no active incident tickets.")
        return

    print("-" * 80)
    print(f"{'Incident ID':<15} {'Bot':<20} {'Short Description'}")
    print("-" * 80)

    for ticket in incidents:
        print(f"{ticket[0]:<15} {ticket[1]:<20} {ticket[2]}")

    print("-" * 80)
    print(f"Total Active Tickets: {len(incidents)}")


# ==========================================
# 3. SEARCH INCIDENT TICKET
# ==========================================

def search_ticket():
    print("\n===== SEARCH INCIDENT TICKET =====")

    incident_id = input("Enter Incident ID: ").strip()

    if incident_id == "":
        print("ERROR: Incident ID cannot be empty.")
        return

    for ticket in incidents:
        if ticket[0] == incident_id:
            print("\nSUCCESS: Incident ticket found!")
            print("Incident ID:", ticket[0])
            print("Bot:", ticket[1])
            print("Short Description:", ticket[2])
            return

    print("ERROR: Incident ID does not exist.")


# ==========================================
# 4. REMOVE RESOLVED INCIDENT
# ==========================================

def remove_ticket():
    print("\n===== REMOVE RESOLVED INCIDENT =====")

    incident_id = input("Enter Incident ID to remove: ").strip()

    if incident_id == "":
        print("ERROR: Incident ID cannot be empty.")
        return

    for ticket in incidents:
        if ticket[0] == incident_id:
            incidents.remove(ticket)
            print("SUCCESS: Resolved incident ticket removed.")
            return

    print("ERROR: Incident ID does not exist.")


# ==========================================
# 5. COUNT ACTIVE INCIDENTS
# ==========================================

def count_tickets():
    print("\n===== ACTIVE INCIDENT COUNT =====")
    print("Total active incident tickets:", len(incidents))


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n==========================================")
    print("       INCIDENT TICKET SYSTEM")
    print("==========================================")
    print("1. Add Incident Ticket")
    print("2. Display All Active Tickets")
    print("3. Search Incident Ticket")
    print("4. Remove Resolved Ticket")
    print("5. Count Active Tickets")
    print("6. Exit")
    print("==========================================")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_ticket()

    elif choice == "2":
        display_tickets()

    elif choice == "3":
        search_ticket()

    elif choice == "4":
        remove_ticket()

    elif choice == "5":
        count_tickets()

    elif choice == "6":
        print("\nProgram terminated.")
        break

    else:
        print("ERROR: Invalid choice. Please enter a number from 1 to 6.")