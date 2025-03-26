import cvxpy

t = 1/4
x = cvxpy.Variable()

# פונקציית מטרה: במקום x*(1 - t*x), נעבור ל-log(x) + log(1 - t*x)
objective = cvxpy.Maximize(cvxpy.log(x) + cvxpy.log(1 - t * x))

# x > 0, 1 - t*x > 0  ⇒ x < 1/t : הגבלות כדי להבטיח ש-log חוקי
constraints = [x >= 0, x <= 1]

prob = cvxpy.Problem(objective, constraints)
prob.solve()

# הדפסת ערכים ברורה לעמי ותמי
print("status:", prob.status)
print("עמי מקבל פלדה בשווי:", x.value)
print("תמי מקבלת פלדה:", 1 - x.value, "ונפט בשווי 1")
print("שווי עבור תמי:", t * (1 - x.value) + (1 - t))





