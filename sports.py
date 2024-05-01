class Team:
    def __init__(self, name, points, position, goal_diff):
        self.name = name
        self.points = points
        self.position = position
        self.goal_diff = goal_diff

    def update_points(self, result):
        if result == 'win':
            self.points += 3
        elif result == 'tie':
            self.points += 1
        elif result == 'lose':
            pass  # No points added for losing

def generate_code(team):
    return f"{team.name.replace(' ', '')}_{team.points}pts_{team.position}Place_{team.goal_diff}GD"

def main():
    teams = [
        Team("Real Madrid", 69, 1, 44),
        Team("Barcelona", 61, 2, 26),
        Team("Girona", 59, 3, 25)
    ]

    num_codes = int(input("Enter the number of codes to generate: "))

    print("Generated Codes:")
    for _ in range(num_codes):
        for team in teams:
            print(generate_code(team))

    # Update points based on match results
    match_results = {
        "Real Madrid": "win",
        "Barcelona": "lose",
        "Girona": "tie"
    }

    for team in teams:
        if team.name in match_results:
            team.update_points(match_results[team.name])

    print("\nPoints after match results update:")
    for team in teams:
        print(f"{team.name}: {team.points} points")

if __name__ == "__main__":
    main()
