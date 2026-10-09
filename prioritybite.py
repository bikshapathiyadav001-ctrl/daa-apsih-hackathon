 url=http://127.0.0.1:5501/index1.html
 def RecommendCourses(courses, credits, benefit, W):
    n = len(courses)
    dp = [[0 for c in range(W + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(W + 1):
            dp[i][c] = dp[i - 1][c]
            if credits[i - 1] <= c:
                dp[i][c] = max(
                    dp[i][c],
                    dp[i - 1][c - credits[i - 1]]
                    + benefit[i - 1]
                )
    chosen = []
    c = W
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            chosen.append(courses[i - 1])
            c = c - credits[i - 1]
    chosen.reverse()
    return dp[n][W], chosen
courses = [
    "Python Programming",
    "Data Structures",
    "Database Systems",
    "Computer Networks",
    "Artificial Intelligence"
]
credits = [3, 4, 3, 2, 4]
benefit = [8, 10, 7, 6, 12]
W = 10
max_benefit, chosen_courses = RecommendCourses(
    courses,
    credits,
    benefit,
    W
)
print("Maximum Benefit:", max_benefit)
print("Recommended Courses:")
for course in chosen_courses:
    print("-", course)