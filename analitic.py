def calculate_goals_scored_average(games):
    individual_totals = [game["individual_total"] for game in games]
    total_sum = sum(individual_totals)
    total_coeffs = sum(1 if game["total"] > 2 else 0 for game in games)
    return total_sum / total_coeffs if total_coeffs != 0 else 0

def calculate_goals_conceded_average(games):
    individual_totals = [game["opponent_individual_total"] for game in games]
    total_sum = sum(individual_totals)
    total_coeffs = sum(1 if game["total"] > 2 else 0 for game in games)
    return total_sum / total_coeffs if total_coeffs != 0 else 0

def calculate_ay124(games_player1, games_player2):
    at118 = calculate_goals_scored_average(games_player1)
    au120 = calculate_goals_conceded_average(games_player2)
    ay117 = (at118 + au120) / 2
    return (at118 * au120) / ay117 if ay117 != 0 else 0

def get_prediction(ay124):
    bd131 = 0 if ay124 < 0.68 else 0
    be131 = 1 if ay124 >= 0.95 else bd131
    bf131 = 2 if ay124 >= 0.6 else be131
    bg131 = 3 if ay124 >= 2.38 else bf131
    bh131 = 4 if ay124 >= 3.38 else bg131
    bi131 = 5 if ay124 >= 4.38 else bh131
    bj131 = 6 if ay124 >= 5.38 else bi131
    return max([bd131, be131, bf131, bg131, bh131, bi131, bj131])
