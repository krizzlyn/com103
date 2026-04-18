def intramurals_tracker():
    # Step 1: Ask for class section and coordinator's name
    section_name = input("Enter the class section name: ")
    coordinator_name = input("Enter the sports coordinator's name: ")

    # Step 2: Display sports events
    sports = [
        ("Basketball", "Team"),
        ("Volleyball", "Team"),
        ("Badminton", "Individual"),
        ("Chess", "Individual"),
        ("Table Tennis", "Individual")
    ]
    
    print("\n==========================================")
    print("   INTRAMURALS -- SPORTS EVENTS")
    print("==========================================")
    for i, (sport, category) in enumerate(sports, start=1):
        print(f" {i}. {sport}    [{category}]")
    print("==========================================\n")
    
    # Step 3: Initialize variables
    total_points = 0
    game_results = []

    # Step 4: Accept 4 game entries
    for game_num in range(1, 5):
        print(f"\n--- GAME {game_num} ---")
        sport_num = int(input("Sport number (0 to skip): "))
        
        if sport_num == 0:
            continue  # Skip this game if user inputs 0
        
        if 1 <= sport_num <= 5:
            sport, category = sports[sport_num - 1]
            opponent = input("Opposing section: ")
            result = input("Result (W/L): ").upper()

            # Assign points based on result
            points = 3 if result == "W" else 0
            
            # Save the game result
            game_results.append((game_num, sport, category, opponent, result, points))
            total_points += points
        else:
            print("Invalid sport number! Please enter a number between 1 and 5.")
    
    # Step 5: Determine standing
    if total_points >= 9:
        standing = "GOLD CONTENDER"
    elif total_points >= 6:
        standing = "SILVER PUSH"
    else:
        standing = "KEEP FIGHTING!"
    
    # Step 6: Print game results board
    print("\n=============================================")
    print(f"     {section_name} -- GAME RESULTS BOARD")
    print("=============================================")
    print(f"Coordinator : {coordinator_name}")
    print("---------------------------------------------")
    
    for idx, (game_num, sport, category, opponent, result, points) in enumerate(game_results, start=1):
        print(f"[{idx}] {sport}  [{category}]")
        print(f"    vs {opponent}  |  Result: {result}   |  Points: {points}")
        print()
    
    print("---------------------------------------------")
    print(f"Total Points   : {total_points}")
    print(f"Standing       : {standing}")
    print("=============================================")

# Call the function to run the program
intramurals_tracker()
