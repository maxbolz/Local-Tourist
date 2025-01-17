def bubble_sort_attractions(attractions, user_preferences):
    # TODO: CHANGE TO MERGE SORT
    n = len(attractions)
    swapped = False

    for i in range(n-1):
        for j in range(0, n - i - 1):
            score_j = sum(user_preferences[k] * attractions[j][k] for k in range(0, len(user_preferences) - 1))
            score_j1 = sum(user_preferences[k] * attractions[j + 1][k] for k in range(0, len(user_preferences) - 1))

            if score_j < score_j1:
                swapped = True
                attractions[j], attractions[j + 1] = attractions[j + 1], attractions[j]

        if not swapped:
            return attractions
    return attractions


def tsp_attractions(distances):
    n = len(distances)
    all_points_set = set(range(n))
    memo = {}

    def tsp_attractions_helper(curr, remaining):
        if not remaining:
            return distances[curr][0], [0]  # Return distance and path

        if (curr, remaining) in memo:
            return memo[(curr, remaining)]

        min_distance = float('inf')
        optimal_path = []

        for next_city in remaining:
            new_remaining = tuple(point for point in remaining if point != next_city)
            distance, path = tsp_attractions_helper(next_city, new_remaining)
            total_distance = distances[curr][next_city] + distance

            if total_distance < min_distance:
                min_distance = total_distance
                optimal_path = [next_city] + path

        memo[(curr, remaining)] = min_distance, optimal_path
        return min_distance, optimal_path

    optimal_distance, optimal_path = tsp_attractions_helper(0, tuple(all_points_set - {0}))
    optimal_path.insert(0, 0)  # Add the starting point to complete the loop

    return optimal_distance, optimal_path


#     def merge_sort_attraction_ranking(side, attractions, attraction):
#         # given side go into that half of attractions, give user choice of left or right of mid-index attraction
#         #if half they choose is empty, return list page, and place attraction at ranked spot
# # if list not empty return form page again with new comparison

